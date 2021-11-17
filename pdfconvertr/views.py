from django.shortcuts import render
from .models import product
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def show_product(request):
    products=product.objects.all()
    context={
        'products':products
    }
    return render(request,'home.html',context)
def pdf_report(request):
    products=product.objects.all()
    template_path = 'pdfreport.html'
    context = {'products': products}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

# Create your views here.
