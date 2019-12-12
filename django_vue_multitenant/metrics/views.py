from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from tenants.models import Pizzeria
from plans.models import Plan
from datetime import timedelta
from datetime import date
import datetime
# Create your views here.

class ShowMetricsView(LoginRequiredMixin, TemplateView):
    template_name = 'metrics/metrics_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(ShowMetricsView, self).get_context_data()

        period_current = datetime.date.today()
        last_period = date.today() - timedelta(days=period_current.day)

        new_clients_current = Pizzeria.objects.filter(created_at__year=period_current.year,
                                                      created_at__month=period_current.month,
                                                      date_expired_paid__gte=period_current
                                                      ).exclude(schema_name='public').count()

        counts_cancelled = Pizzeria.objects.filter(created_at__year=period_current.year,
                                                   created_at__month=period_current.month,
                                                   date_expired_paid__lte=period_current
                                                   ).exclude(schema_name='public').count()

        clients_current = Pizzeria.objects.filter(created_at__lte=period_current,
                                                  date_expired_paid__gte=period_current
                                                  ).exclude(schema_name='public').count()

        last_clients = Pizzeria.objects.filter(created_at__lte=last_period,
                                               ).exclude(schema_name='public').count()
        price_plan = Plan.objects.filter(is_basic=False).first()

        customer_lost = last_clients + new_clients_current - clients_current
        churn_rate = customer_lost / last_clients if last_clients else 0
        cmrr = (new_clients_current - counts_cancelled) * price_plan.price
        arpu = cmrr / clients_current if clients_current else 0
        context['customer_lost'] = customer_lost
        context['acl'] = str((1 / churn_rate) * 100) + "%" if churn_rate else "Estable"
        context['crr'] = 1 - churn_rate
        context['arpu'] = arpu
        context['ltv'] = (1 / churn_rate) * arpu if churn_rate else arpu
        context['cac'] = None
        context['rentabilidad'] = None
        context['fecha'] = period_current
        return context
