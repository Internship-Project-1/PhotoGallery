import random
import string
from datetime import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .forms import StudentForm, PhotoForm
from .models import Student, Photo


# Create your views here.
@login_required
def gallery(request):
    student = Student.objects.get(pk=request.user.id)
    photos = Photo.objects.filter(student=student)
    context = {'photos': photos}
    return render(request, 'myapp/gallery.html', context)


@login_required
def addPhoto(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES or None)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.student = Student.objects.get(pk=request.user.id)
            photo.save()
            form.save_m2m()
            context = {'response': 'Photo Uploaded'}
            return render(request, 'myapp/generic_response.html', context)
        else:
            context = {'response': 'Error occurred, trt again letter'}
            return render(request, 'myapp/generic_response.html', context)
    else:
        form = PhotoForm()
        context = {'form': form}
        return render(request, 'myapp/addPhoto.html', context)


def viewPhoto(request, pno):
    try:
        photo = Photo.objects.get(pk=pno)
        if request.method == 'POST':
            form = PhotoForm(request.POST, request.FILES or None, instance=photo)
            context = {'form': form, 'photo': photo}

            if form.is_valid():
                photo = form.save(commit=False)
                photo.student = Student.objects.get(pk=request.user.id)
                photo.save()
                form.save_m2m()
                context = {'response': 'Photo Updated'}
                return render(request, 'myapp/generic_response.html', context)
            else:
                context = {'response': 'Error occurred, trt again letter'}
                return render(request, 'myapp/generic_response.html', context)
        else:
            form = PhotoForm(instance=photo)
            context = {'form': form, 'photo':photo}
            return render(request, 'myapp/viewPhoto.html', context)

    except Photo.DoesNotExist:
        context = {'response': 'Page not found'}
        return render(request, 'myapp/generic_response.html', context)


def deletePhoto(request, pno):
    try:
        photo = Photo.objects.get(pk=pno)
        photo.delete()
        context = {'response': 'Photo Deleted'}
        return render(request, 'myapp/generic_response.html', context)
    except Photo.DoesNotExist:
        context = {'response': 'Page not found'}
        return render(request, 'myapp/generic_response.html', context)



def user_login(request):
    if request.user.is_authenticated:
        return redirect('myapp:part2_index')
    if request.method == 'POST':
        # if request.session.test_cookie_worked():
        #     request.session.delete_test_cookie()
        #     print("test cookie worked")
        # else:
        #     print("test cookie didn't work")
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                request.session['last_login'] = datetime.now().strftime("%H:%M:%S - %B %d, %Y")
                request.session.set_expiry(3600)
                if request.POST.get('next') != '':
                    return redirect(request.POST.get('next'))
                return HttpResponseRedirect(reverse('myapp:gallery'))
            else:
                return HttpResponse('Your account is disabled.')
        else:
            return HttpResponse('Invalid login details.')
    else:
        # request.session.set_test_cookie()
        return render(request, 'myapp/login.html')


@login_required
def user_logout(request):
    logout(request)
    # request.session.flush()
    # for key in list(request.session.keys()):
    #     del request.session[key]
    return HttpResponseRedirect(reverse('myapp:gallery'))



def register(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES or None)
        if form.is_valid():
            student = form.save(commit=False)
            student.set_password(student.password)
            student.save()
            form.save_m2m()

            msg = 'Congratulations, You are now registered as a student'
            return render(request, 'myapp/register_response.html', {'msg': msg})
    else:
        form = StudentForm()
    return render(request, 'myapp/register.html', {'form': form})

