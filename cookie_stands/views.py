from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import CookieStand
from .serializer import CookieStandSerializer
from .permissions import isOwnerOrReadOnly
# Create your views here.

class CookieStandList(ListCreateAPIView):
    queryset = CookieStand.objects.all()
    serializer_class = CookieStandSerializer

class CookieStandDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (isOwnerOrReadOnly,)
    queryset = CookieStand.objects.all()
    serializer_class = CookieStandSerializer
