import csv
from itertools import groupby
import djqscsv
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, Sum
from django.db.models.functions import TruncDate
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import  TemplateView
from orders.models import Order
from users.models import UserProfile
from django.db.models.functions import ExtractMonth


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


class GraphicsShowView(LoginRequiredMixin, TemplateView):
    template_name = 'reports/graphics.html'

    def get_context_data(self, **kwargs):
        monts = {'1':'enero', '2':'Febrero',
                 '3':'Marzo', '4':'Abril',
                 '5':'Mayo', '6':'Junio',
                 '7':'Julio', '8':'Agosto',
                 '9':'Septiembre', '10':'Octubre', '11':'Noviembre', '12':'Diciembre'}
        context = super(GraphicsShowView, self).get_context_data()
        invoices = Order.objects.only('date_payment', 'total').order_by('date_payment')
        month_totals = {
            k: sum(x.total for x in g)
            for k, g in groupby(invoices, key=lambda i: i.date_payment.month)
        }
        total_vendido_mes = [{"mes": key, "cantidad": value} for key, value in month_totals.items()]
        for q in total_vendido_mes:
            q['mes'] = monts[str(q['mes'])]

        invoices = UserProfile.objects.only('date_joined', ).order_by('date_joined')
        month_totals = {
            k: sum(1 for x in g)
            for k, g in groupby(invoices, key=lambda i: i.date_joined.month)
        }
        total_usuarios_mes = [{"mes": key, "cantidad": value} for key, value in month_totals.items()]
        for q in total_usuarios_mes:
            q['mes'] = monts[str(q['mes'])]

        usuarios_compras = Order.objects.select_related('client').all().values('client__email').annotate(
            Valor_compra_total=Sum('total'))

        context['ventas_mes'] = total_vendido_mes
        context['usuarios_mes'] = total_usuarios_mes
        context['usuarios_compras'] = usuarios_compras
        return context