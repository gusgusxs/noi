from django.urls import path
from myapp.views import Showdata,Edit,Del

urlpatterns = [
    path("show/",Showdata.as_view(), name='Show'),
    path("update/<int:pk>",Edit.as_view(), name='update'),
    path("del/<int:pk>",Del.as_view(), name='delete'),
]