from django.shortcuts import render, redirect


def index(request):
    return redirect('/dashboard')


def dashboard(request):
    return render(request, 'dashboard.html')


def videocall(request):
    return render(request, 'videocall.html')
