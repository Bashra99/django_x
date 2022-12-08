from django.urls import path
from .views import AOTListView,AOTDetailView,AOTCreateView,AOTUpdateView,AOTDeleteView,About
urlpatterns = [
    path('',AOTListView.as_view(),name='AOT'),
    path('<int:pk>/',AOTDetailView.as_view(),name='AOT_detail'),
    path('create/',AOTCreateView.as_view(),name='AOT_create'),
    path('<int:pk>/update',AOTUpdateView.as_view(),name='AOT_update'),
    path('<int:pk>/delete',AOTDeleteView.as_view(),name='AOT_delete'),
    path('about/',About.as_view(),name='about'),
]