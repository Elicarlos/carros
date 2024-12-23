from django.urls import path
from .views import car,CarView, CarListView, new_car, NewCarCreateView, CarDetailView, CarUpdateView, CarDeleteView


urlpatterns = [
    path('', CarListView.as_view(), name="list-cars"),
    path('new-car/', NewCarCreateView.as_view(), name="new-car"),
    path('new-detail/<int:pk>/', CarDetailView.as_view(), name="car-detail"),  
    path('car-update/<int:pk>/update/', CarUpdateView.as_view(), name="car-update"),
    path('car-delete/<int:pk>/delete/', CarDeleteView.as_view(), name="car-delete")
]