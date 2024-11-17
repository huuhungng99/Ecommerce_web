from xhtml2pdf import pisa
from io import BytesIO
from django.template.loader import get_template
from django.http import HttpResponse

def generate_pdf(request):
    template = get_template('index.html')
    #noi dung can in 
    context = {'data': 'ABC123'}

    html = template.render(context)

    #tạo file pdf
    result_pdf = BytesIO()
    pdf = pisa.CreatePDF(BytesIO(html.encode('UTF-8')), desst = result_pdf)

    if not pdf.err:
        reponse = HttpResponse(content_type = 'pdf')
        reponse.write(result_pdf.getvalue())
        return reponse
    return HttpResponse("Error pdf")


