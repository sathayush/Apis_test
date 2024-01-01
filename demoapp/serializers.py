# serializers.py
from rest_framework import serializers
from .models import *

class TempleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Temple_category
        fields = '__all__'

class TempleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temple
        fields = '__all__'

class TemplePrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model=templePriority
        fields='__all__'



###############goshala serializers######################
        

class GoshalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goshala_Model
        fields = '__all__'



###############event serializers######################        
        

class EventCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Event_Category
        fields = '__all__'      




class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'              


