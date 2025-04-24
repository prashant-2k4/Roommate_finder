from django.urls import path
from .views import room_list, room_detail, room_create, room_update, room_delete

urlpatterns = [
    path('', room_list, name='room_list'),  # this makes /rooms/ go to the list
    path('create/', room_create, name='room_create'),
    path('<int:pk>/', room_detail, name='room_detail'),
    path('<int:pk>/edit/', room_update, name='room_update'),
    path('<int:pk>/delete/', room_delete, name='room_delete'),
]
