from django.urls import path, include
from django.views.generic.base import View
from rest_framework import routers
from events import views

from events.serializers import App



router = routers.DefaultRouter(trailing_slash=False)
router.register(r'appointments', views.AppointmentViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path(r'api/', include(router.urls)),
    path('apii', views.AppView.as_view()),
    path('update/<pk>', views.AppView2.as_view())
]