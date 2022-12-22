from django.urls import path
from .views import AOTListView,AOTDetailView,AOTCreateView,AOTUpdateView,AOTDeleteView,About
urlpatterns = [
    path('AOT/',AOTListView.as_view(),name='AOT'),
    path('AOT/<int:pk>/',AOTDetailView.as_view(),name='aot_detail'),
    path('AOT/create/',AOTCreateView.as_view(),name='aot_create'),
    path('AOT/<int:pk>/update/',AOTUpdateView.as_view(),name='aot_update'),
    path('AOT/<int:pk>/delete/',AOTDeleteView.as_view(),name='aot_delete'),
    path('AOT/about/',About.as_view(),name='about'),
]