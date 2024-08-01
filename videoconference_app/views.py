from django.shortcuts import render, redirect


def index(request):
    return redirect('/dashboard')


def dashboard(request):
    return render(request, 'dashboard.html')


def videocall(request):
    return render(request, 'videocall.html')


def join_room(request):
    if request.method == 'POST':
        roomID = request.POST['roomID']
        return redirect("/meeting?roomID=" + roomID)
    return render(request, 'joinroom.html')
