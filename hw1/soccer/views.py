from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from soccer.models import Country, Club, Player
from soccer.serializers import CountrySerializer, ClubSerializer, PlayerSerializer


##country
@api_view(['GET','POST'])
##list and create function
def country_list(request):
    if request.method == 'GET':
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many= True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

##update or delete
@api_view(['GET','PUT','DELETE'])
def country_detail(request,pk):
    try:
        country = Country.objects.get(pk = pk)
    except Country.DoesNotExist:
        return Response (status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CountrySerializer(country)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CountrySerializer(country,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        country.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


##club
@api_view(['GET','POST'])
##list and create function
def club_list(request):
    if request.method == 'GET':
        clubs = Club.objects.all()
        serializer = ClubSerializer(clubs, many= True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ClubSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

##update or delete
@api_view(['GET','PUT','DELETE'])
def club_detail(request,pk):
    try:
        clubs = Club.objects.get(pk = pk)
    except Country.DoesNotExist:
        return Response (status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClubSerializer(clubs)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ClubSerializer(clubs,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        clubs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


##player
@api_view(['GET','POST'])
##list and create function
def player_list(request):
    if request.method == 'GET':
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many= True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

##update or delete
@api_view(['GET','PUT','DELETE'])
def player_detail(request,pk):
    try:
        players = Player.objects.get(pk = pk)
    except Country.DoesNotExist:
        return Response (status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PlayerSerializer(players)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PlayerSerializer(players,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        players.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




