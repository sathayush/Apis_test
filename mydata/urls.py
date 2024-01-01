# # api/urls.py
# from django.urls import path
# from .views import MyDataApiView

# urlpatterns = [
#     path('mydata/', MyDataApiView.as_view(), name='mydata-api'),
# ]



# mydata/urls.py
from django.urls import path
from .views import *

urlpatterns = [
  path('get_data/', get_data_view, name='get-data'),
  path('temple_data_view/', temple_data_view, name='temple_data_view'),
  path('Goshala_data_view/', Goshala_data_view, name='Goshala_data_view'),
  path('Goshala_view/', Goshala_view, name='Goshala_view'),
  path('event_data_view/',event_data_view, name='event_data_view'),
  path('Event_view/', Event_view, name='Event_view'),
]

