from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

# Create your views here.
@api_view(['GET','POST'])
def book(request):
    if request.method == 'GET':
        snippets = Book.objects.all()
        serilizer = BookSerializer(snippets, many=True)
        return Response(serilizer.data)

    elif request.method == 'POST':
        serilizer = BookSerializer(data = request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data, status=status.HTTP_201_CREATED)
        return Response(serilizer.errors, status = status.HTTP_400_BAD_REQUEST)
