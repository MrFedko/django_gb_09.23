from django.urls import path
from randomizer import views


urlpatterns = [
    path('coin/', views.CoinView.as_view(), name='coin_page'),
    path('cube/', views.CubeView.as_view(), name='cube_page'),
    path('number/', views.NumberView.as_view(), name='number_page'),
]
