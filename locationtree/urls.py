from django.urls import path

from .views import *

urlpatterns = [
    path("Get_all_countries/",Get_all_countries.as_view()),
    path("Get_States_by_country_code/<str:country_code>/",Get_States_by_country_code.as_view()),
    path("Get_Districts_by_state_code/<str:state_code>/",Get_Districts_by_state_code.as_view()),
    path("Get_Blocks_by_dst_code/<str:district_code>/",Get_Blocks_by_dst_code.as_view()),
    path("Get_Village_by_block_code/<str:block_code>/",Get_Village_by_block_code.as_view()),
    
]