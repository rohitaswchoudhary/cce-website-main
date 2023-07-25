from django.shortcuts import render
from placements.models import *

from website.models import Gallery, Hero_Image, Recruiters

# Create your views here.

def placement_page(request,slug):
    context_temp = {
        'title': 'Placements',
        'hero_title': 'Placements',
        'hero_img': Hero_Image.objects.filter(page='placements').first(),
        'route': slug,
    }
    context={**context_temp}
    if slug=='index':
        # vission = PVissionANDMission.objects.filter(name='Vision').first()
        # mission = PVissionANDMission.objects.filter(name='Mission').first()
        # objectives = PVissionANDMission.objects.filter(name='objectives')
        testimonials = Testimonials.objects.all()
        recruiters = Recruiters.objects.all()
        recruiters3 = recruiters.order_by('?')
        recruiters2 = recruiters.order_by('?')
        side_updates = PlacementUpdates.objects.all().order_by('-date')
        gallery = Gallery.objects.all()
        context = {**context_temp,'testimonials':testimonials,"recruiters": recruiters, "recruiters2": recruiters2, "recruiters3": recruiters3,"side_updates":side_updates,"gallery":gallery}
        return render(request, 'Placements/index.html',context=context)
    elif slug=="placement_traning":
        context = {**context_temp,'data':PlacementTraning.objects.all()}
        return render(request, 'Placements/placement_traning.html',context=context)
    elif slug=="achivements":
        return render(request, 'Placements/achivements.html',context=context)
    elif slug=="faculty":
        return render(request, 'Placements/faculty.html',context=context)
    elif slug=="statistics":
        return render(request, 'Placements/statistics.html',context=context)
    elif slug=="activities":
        return render(request, 'Placements/activities.html',context=context)
    elif slug=="recruiters":
        return render(request, 'Placements/recruiters.html',context=context)

    