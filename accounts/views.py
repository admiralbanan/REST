# accounts/views.py
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from rest_framework import viewsets
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework import permissions
from .permissions import IsAdminOrOwner

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')  
    template_name = 'accounts/signup.html'

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAdminUser]

class IsAdminOrOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        # Админы могут всё, остальные — нет
        return request.user and request.user.is_staff

    def has_object_permission(self, request, view, obj):
        # Админ может всё, пользователь — только сам себя
        if request.user and request.user.is_staff:
            return True
        return obj == request.user