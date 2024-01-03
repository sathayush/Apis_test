# myapp/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('TempleCategoryView/', TempleCategoryView.as_view(), name='TempleCategoryView'),
    path('TempleView/<str:temple_category_code>/', TempleView.as_view(), name='TempleView'),
    path('TempleViewAll/', TempleViewAll.as_view(), name='TempleViewAll'),
    path('TemplePriorityView/', TemplePriorityView.as_view(), name='TemplePriorityView'),
    path('TempleViewPost/', TempleViewPost.as_view(), name='TempleViewPost'),
    path('TempleViewPut/<str:Temple_code>/', TempleViewPut.as_view(), name='TempleViewPut'),
    path('TempleViewDelete/<str:pk>/', TempleViewDelete.as_view(), name='TempleViewDelete'),
    path('GoshalaCategoryView/', GoshalaCategoryView.as_view(), name='GoshalaCategoryView'),
    path('GoshalaView/<str:Goshala_Category_Code>/', GoshalaView.as_view(), name='GoshalaView'),
    path('GoshalaViewAll/', GoshalaViewAll.as_view(), name='GoshalaViewAll'),
    path('GoshalaViewPost/', GoshalaViewPost.as_view(), name='GoshalaViewPost'),
    path('GoshalaViewPut/<str:Goshala_Code>/', GoshalaViewPut.as_view(), name='GoshalaViewPut'),
    path('GosdhalaViewDelete/<str:pk>/', GosdhalaViewDelete.as_view(), name='GosdhalaViewDelete'),
    path('EventCategoryView/', EventCategoryView.as_view(), name='EventCategoryView'),
    path('EventView/<str:Event_Category_Code>/', EventView.as_view(), name='EventView'),
    path('EventViewAll/', EventViewAll.as_view(), name='EventViewAll'),
    path('EventViewPost/', EventViewPost.as_view(), name='EventViewPost'),
    path('EventViewPut/<str:Event_Code>/', EventViewPut.as_view(), name='EventViewPut'),
    path('EventViewDelete/<str:pk>/', EventViewDelete.as_view(), name='EventViewDelete'),


]
