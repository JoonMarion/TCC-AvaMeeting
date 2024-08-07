from django.shortcuts import render, redirect


def index(request):
    return redirect('/meeting')


def videocall(request):
    return render(request, 'videocall.html')
