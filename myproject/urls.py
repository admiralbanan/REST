# myproject/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from accounts.views import CustomUserViewSet
from myapp.views import PersonViewSet, CarAccidentViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'persons', PersonViewSet)
router.register(r'accidents', CarAccidentViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', obtain_auth_token, name='api_token_auth'),
]