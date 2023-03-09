from django.urls import path
from inventory_api.views import *


urlpatterns = [
    path('locations/', LocationList.as_view()),
    path('locations/id/<int:pk>/', LocationDetail.as_view()),
    path('producers/', ProducerList.as_view()),
    path('producers/id/<int:pk>/', ProducerDetail.as_view()),
    path('categories/', CategoryList.as_view()),
    path('categories/id/<int:pk>/', CategoryDetail.as_view()),
    path('ean_devices/', EanDeviceList.as_view()),
    path('ean_devices/id/<int:pk>/', EanDeviceDetail.as_view()),

]