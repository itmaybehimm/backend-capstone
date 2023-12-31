from django.shortcuts import render
from rest_framework import generics
from .serializers import MenuSerializer, BookingSerializer
from .models import Menu, Booking
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
# Create your views here.

from .models import MenuItem
from .serializers import MenuItemSerializer


def index(request):
    return render(request, 'index.html', {})


# class MenuItemsView(generics.ListCreateAPIView):
#     queryset = Menu.objects.all()
#     serializer_class = MenuSerializer
#     permission_classes = [IsAuthenticated]


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    # permission_classes = [permissions.IsAuthenticated]


class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
