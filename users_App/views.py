from django.shortcuts import render
from rest_framework import status,viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Profile,User_Attendance
from .serializers import ProfileSerializer,UserAttendanceSerializer

# Create your views here.

@api_view(['GET','POST'])
def profile_api_view(request):
    try:
        profile_objects = Profile.objects.all()
    except Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    #GET
    if request.method == "GET":
        serializer = ProfileSerializer(profile_objects,many=True)
        return Response(serializer.data)
    #POST
    elif request.method == "POST":
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def profile_api_update(request,id,format = None):
    try:
        profile = Profile.objects.get(id=id)
    except Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ProfileSerializer(profile,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


@api_view(['GET','POST'])
def mark_attendance(request,id,format=None):
    try:
        profile = Profile.objects.get(id=id)
    except Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = UserAttendanceSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def home(request):
    return render(request,'index.html')
