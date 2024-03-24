from django.shortcuts import render,redirect
from . models import Room,Message
from django.http import HttpResponse,JsonResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def room(request,room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    context = {
        'username':username,
        "room":room,
        "room_details":room_details
    }
    return render(request, 'room.html',context)
  
def checkview(request):
   room = request.POST.get('room_name')
   username = request.POST.get('username')

   if Room.objects.filter(name=room).exists():#if the room name that was inputed exists
       return redirect("/"+room+"/?username="+username)#we wanna redirect to the room
   else:
       new_room = Room.objects.create(name=room)
       new_room.save()
       return redirect("/"+room+"/?username="+username)#we wanna redirect to the room

def send(request):
    message = request.POST.get('message')
    username = request.POST.get('username')
    room_id = request.POST.get('room_id')

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse("Hi, Message sent successfully")

def getMessage(request,room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})