from django.urls import path
from .views import OwnerListView

urlpatterns = [
    path('', OwnerListView.as_view()),
]