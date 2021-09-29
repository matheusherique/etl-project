from django.urls import path
from .views import LoadView

urlpatterns = [
    path("sorted_numbers", LoadView.as_view(), name='Load'),
]
