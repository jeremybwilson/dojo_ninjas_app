# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Dojo

# Create your views here.
def index(request):
    if 'dojo_id' not in request.session:
        # request.session['dojo_id'] = False
        return redirect('dojos:new')
    else:
        # print the dojo_id, "THIS IS THE DOJO_ID"
        print "THIS IS THE DOJO_ID", request.session['dojo_id']


    dojo_id = int(request.session['dojo_id'])
    # print "*" * 80
    # print "Here is the USER ID from session:", user_id
    dojo_list = Dojo.objects.all()
    specific_dojo = Dojo.objects.get(id=dojo_id)

    context = {
        'dojos': dojo_list,
        'specific_dojo_id': specific_dojo.id
    }

    print "*" * 80
    print context

    return render(request, 'first_app/index.html', context)

def create(request):
    if request.method == 'POST':

        valid, result = Dojo.objects.validate_and_create_dojo(request.POST)
        print "*" * 80
        print "Successfully entered the create route."
        print valid
        print result

        if valid:
            request.session['dojo_id'] = result
            return redirect('dojos:index')
        else:
            for error in result:
                messages.error(request, error)
            return redirect('dojos:new')
    else:
        return redirect('dojos:index')

def edit(request):
    pass

def new(request):
    return render(request, 'first_app/new.html')

def show(request, dojo_id):
    if 'dojo_id' not in request.session:
        return redirect('dojos:new')
    else:
        # print the dojo_id, "THIS IS THE DOJO_ID"
        print "THIS IS THE DOJO_ID", request.session['dojo_id']

        dojo_id = int(dojo_id)
        try:
            dojo = Dojo.objects.get(id=dojo_id)
            # print "Try statement block => user info: ", dojo
        except:
            return redirect('dojos:index')

        context = {
                "name": dojo.name,
                "city": dojo.city,
                "state": dojo.state,
                "desc": dojo.desc,
                "dojo_id": dojo_id
        }

    return render(request, 'first_app/show.html', context)

def update(request, dojo_id):
    errors = Dojo.objects.validate_and_create_dojo(request.POST)
    if len(errors):
       for tag, error in errors.iteritems():
          messages.error(request, error, extra_tags=tag)
       return redirect('/dojos/'+dojo_id+'/edit/')
    else:
        dojo = Dojo.objects.get(id=id)
        dojo.name = request.POST['name']
        dojo.city = request.POST['city']
        dojo.state = request.POST['state']
        dojo.desc = request.POST['desc']
        dojo.save()
        return redirect('dojos:index')

def delete(request, dojo_id):
    pass

def logout(request):
    request.session.clear()
    return redirect('dojos:index')