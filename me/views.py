from django.contrib import messages
from django.shortcuts import render

from contact_us.forms import contact_us_form
from contact_us.models import contact_us
from social_media.models import social_media
from .models import me, information, skills, Work, education, CV_file


# Create your views here.
def header(request):
    info = me.objects.first()
    social = social_media.objects.all()
    context = {
        'me': info,
        'socials': social,
    }
    return render(request, 'shared/_header.html', context)


def footer(request):
    info = me.objects.first()
    social = social_media.objects.all()
    context = {
        'me': info,
        'socials': social,
    }
    return render(request, 'shared/_footer.html', context)


def home_page(request):
    contact_form = contact_us_form(request.POST or None)
    if contact_form.is_valid():
        name = contact_form.cleaned_data.get('name')
        email = contact_form.cleaned_data.get('email')
        text = contact_form.cleaned_data.get('text')
        contact_us.objects.create(name=name, email=email, text=text, is_read=False)
        messages.success(request, '.پیام شما با موفقیت دریافت شد')

    general_info = me.objects.first()
    info = information.objects.all()
    main_skills = skills.objects.filter(others=False).all()
    other_skills = skills.objects.filter(others=True).all()
    work_experience = Work.objects.all()
    edu = education.objects.all()
    cv = CV_file.objects.first()

    context = {
        'me': general_info,
        'all_info': info,
        'skills': {'main_skills': main_skills, 'other_skills': other_skills},
        'jobs': work_experience,
        'education': edu,
        'contact_form': contact_form,
        'cv': cv,
    }
    return render(request, 'home_page.html', context)
