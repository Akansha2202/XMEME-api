from django.urls import path
from .views import MemeAPIView,MemeDetail

urlpatterns=[
    path('memes',MemeAPIView.as_view()),
    path('memes/<int:id>',MemeDetail.as_view()),
]