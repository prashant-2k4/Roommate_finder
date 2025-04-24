from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.db.models import Q
from .models import Room
from .forms import RoomForm

def room_list(request):
    query = request.GET.get('q')
    rooms = Room.objects.all()
    if query:
        rooms = rooms.filter(
            Q(title__icontains=query) |
            Q(location__icontains=query)
        )
    return render(request, "rooms/room_list.html", {"rooms": rooms})

@login_required
def room_create(request):
    if request.method == "POST":
        form = RoomForm(request.POST, request.FILES)
        if form.is_valid():
            room = form.save(commit=False)
            room.provider = request.user
            room.save()
            return redirect("room_list")
    else:
        form = RoomForm()
    return render(request, "rooms/room_form.html", {"form": form})

def room_detail(request, pk):
    room = get_object_or_404(Room, pk=pk)
    return render(request, "rooms/room_details.html", {"room": room})

@login_required
def room_update(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if room.provider != request.user:
        return HttpResponseForbidden("You are not allowed to edit this room.")
    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect("room_list")
    else:
        form = RoomForm(instance=room)
    return render(request, "rooms/room_form.html", {"form": form})

@login_required
def room_delete(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if room.provider != request.user:
        return HttpResponseForbidden("You are not allowed to delete this room.")
    if request.method == "POST":
        room.delete()
        return redirect("room_list")
    return render(request, "rooms/room_confirm_delete.html", {"room": room})
