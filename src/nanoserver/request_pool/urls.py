from django.conf.urls import include, url
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import InferView

router = DefaultRouter()
urlpatterns = [
    path('', include(router.urls)),
    url(r"^(?P<endpoint_name>.+)/infer/$", InferView.as_view(), name="infer"),
]
