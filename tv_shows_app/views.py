from django.shortcuts import render,redirect, HttpResponse
from django.contrib import messages
from .models import *

def redirect_to_main_page(request):
    return redirect('/shows')

def display_main_page(request):
    context = {
    'tv_shows' : Show.objects.all(),
    }
    return render(request,'main_page.html',context)

def display_form_to_add_tv_show(request):
    return render(request,'add_show.html')

def add_form_data_to_database(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request,value)
        return redirect('/shows/new')
    else:
        title=request.POST['title']
        network=request.POST['network']
        release_date=request.POST['release_date']
        description=request.POST['description']
        Show.objects.create(title=title,network=network,release_date=release_date,description=description)
        show_id = Show.objects.get(title=title,network=network,release_date=release_date,description=description).id    
    return redirect('/shows/'+str(show_id))

def display_show_information(request,show_id):
    show=Show.objects.get(id=show_id)
    context = {
        'id':show.id,
        'title':show.title,
        'network':show.network,
        'release_date':show.release_date,
        'description':show.description,
        'updated_at':show.updated_at,

        'title_type':str(type(show.title)),
        'network_type':str(type(show.network)),
        'release_date_type':str(type(show.release_date)),
        'description_type':str(type(show.description)),
        'updated_at_type':str(type(show.updated_at)),
    }
    return render(request,'show_information.html',context)

def display_form_to_update_show_information(request,show_id):
    show=Show.objects.get(id=show_id)
    context = {
        'id':show.id,
        'title':show.title,
        'network':show.network,
        'release_date':str(show.release_date),
        'description':show.description,
    }
    return render(request,'edit_information.html',context)

def update_form_information_in_database(request,show_id):
    show=Show.objects.get(id=show_id)
    show.title=request.POST['title']
    show.network=request.POST['network']
    show.description=request.POST['description']
    # show.release_date=request.POST['release_date']
    show.save()
    return redirect('/shows/'+str(show_id))

def delete_show_information_from_database(request,show_id):
    Show.objects.get(id=show_id).delete()
    return redirect('/shows')

