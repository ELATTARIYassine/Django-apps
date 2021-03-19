from django.shortcuts import render
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader


# Create your views here.

def index(request):
    if request.method == "POST":
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        phone = request.POST.get('phone', "")
        degree = request.POST.get('degree', "")
        school = request.POST.get('school', "")
        university = request.POST.get('university', "")
        previous_work = request.POST.get('previous_work', "")
        skills = request.POST.get('skills', "")
        summary = request.POST.get('summary', "")
        profile = Profile(summary=summary, name=name, email=email, phone=phone, degree=degree, school=school,
                          university=university, previous_work=previous_work, skills=skills)
        profile.save()
    return render(request, "generator/form_data.html")


def resume(request, id):
    resume = Profile.objects.get(id=id)
    template = loader.get_template('generator/resume.html')
    html = template.render({'resume': resume})
    options = {
        'page-size': 'Letter',
        'encoding': 'UTF-8'
    }
    pdf = pdfkit.from_string(html, False, options)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachement'
    filename = "resume.pdf"
    return response
