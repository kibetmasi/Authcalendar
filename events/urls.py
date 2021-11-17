from django.urls import path, include
from django.views.generic.base import View
from rest_framework import routers
from events import views
from events.serializers import App
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# for user in User.objects.all():
#     Token.objects.get_or_create(user=user)


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'appointments', views.AppointmentViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path(r'api/', include(router.urls)),
    path('apii', views.AppView.as_view()),
    path('update', views.AppView2.as_view()),
    path("register/", views.register, name="register"),  # <-- added
    path('update/<pk>', views.AppView2.as_view()),
    path('x', views.notes.as_view({'get': 'list'}))
]