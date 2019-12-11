import csv
from itertools import groupby

import djqscsv
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, Sum
from django.db.models.functions import Trunc, TruncDate
from django.http import HttpResponse
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView, TemplateView

from core.mixins import MessageMixin, TemplateDataMixin


# Create your views here.
from orders.models import Order
from users.models import UserProfile


class ReportView(LoginRequiredMixin, TemplateView):
    template_name = "reports/create.html"


class ReportCreateView(LoginRequiredMixin, TemplateView):
    template_name = "reports/create.html"

    def get(self, request, *args, **kwargs):
        type_report = kwargs.get("type")

        if type_report == 1:
            qs = Order.objects.all().annotate(date=TruncDate('date_payment')).values('date').annotate(**{'total': Count('date')})
            return djqscsv.render_to_csv_response(qs)

        if type_report == 2:
            invoices = Order.objects.only('date_payment', 'total').order_by('date_payment')
            month_totals = {
                k: sum(x.total for x in g)
                for k, g in groupby(invoices, key=lambda i: i.date_payment.year)
            }
            qs = [{"año": key, "cantidad": value} for key, value in month_totals.items()]
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="reporte.csv"'

            fieldnames = ['año', 'cantidad']
            writer = csv.DictWriter(response, fieldnames=fieldnames)
            writer.writeheader()
            for q in qs:
                writer.writerow(q)
            return response

        if type_report == 3:
            invoices = UserProfile.objects.only('date_joined', ).order_by('date_joined')
            month_totals = {
                k: sum(1 for x in g)
                for k, g in groupby(invoices, key=lambda i: i.date_joined.month)
            }
            qs = [{"mes": key, "cantidad": value} for key, value in month_totals.items()]
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="reporte.csv"'
            fieldnames = ['mes', 'cantidad']
            writer = csv.DictWriter(response, fieldnames=fieldnames)
            writer.writeheader()
            for q in qs:
                writer.writerow(q)
            return response

        if type_report == 4:
            invoices = Order.objects.only('date_payment', 'total').order_by('date_payment')
            month_totals = {
                k: sum(x.total for x in g)
                for k, g in groupby(invoices, key=lambda i: i.date_payment.month)
            }
            qs = [{"mes": key, "cantidad": value} for key, value in month_totals.items()]
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="reporte.csv"'

            fieldnames = ['mes', 'cantidad']
            writer = csv.DictWriter(response, fieldnames=fieldnames)
            writer.writeheader()
            for q in qs:
                writer.writerow(q)
            return response

        if type_report == 5:
            qs = Order.objects.select_related('client').all().values('client__email').annotate(Valor_compra_total=Sum('total'))
            return djqscsv.render_to_csv_response(qs)

        if type_report == 6:
            invoices = UserProfile.objects.only('date_joined', ).order_by('date_joined')
            month_totals = {
                k: sum(1 for x in g)
                for k, g in groupby(invoices, key=lambda i: i.date_joined.year)
            }
            qs = [{"año": key, "cantidad": value} for key, value in month_totals.items()]
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="reporte.csv"'
            fieldnames = ['año', 'cantidad']
            writer = csv.DictWriter(response, fieldnames=fieldnames)
            writer.writeheader()
            for q in qs:
                writer.writerow(q)
            return response

    def get_success_url(self):
        return reverse('products:list_ingredients')