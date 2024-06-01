from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
from base.models import Room
from .serializers import RoomSerializer

@api_view(['GET'])
def getRoutes(request):

    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id',
        'GET /api/search/rooms?search=:search'
    ]

    return Response(routes)

@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getRoom(request, pk):
    room = Room.objects.get(id=pk)
    serializer = RoomSerializer(room, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def searchRooms(request):
    rooms = Room.objects.filter()

    if request.GET.get('search') != None:
        search = request.GET.get('search')
        rooms = Room.objects.filter(Q(name__icontains=search) | Q(topic__name__icontains=search) | Q(description__icontains=search) | Q(host__username__icontains=search))
    
    searializer = RoomSerializer(rooms, many=True)
    return Response(searializer.data)