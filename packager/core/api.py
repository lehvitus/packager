# packager:core:api

from django.urls import include, path
from .viewsets.router import router


urlpatterns = [
   path('', include(router.urls)),
]
