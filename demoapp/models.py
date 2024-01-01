# models.py
from django.db import models
import uuid

class Temple_category(models.Model):
    Temple_Category_Code = models.CharField(max_length=10, primary_key=True)
    Temple_Category_Name = models.CharField(max_length=100)
    Temple_Category_Desc = models.TextField()

    class Meta:
        managed = False  # Set managed to False to prevent table creation/modification
        db_table='temple_category'


class templePriority(models.Model):
    Temple_priority_Code = models.CharField(max_length=10, primary_key=True)
    Temple_priority_Name = models.CharField(max_length=100)
    Temple_priority_Desc = models.TextField()

    class Meta:
        managed = False  # Set managed to False to prevent table creation/modification
        db_table = 'temple_priority'


      


class Temple(models.Model):
    STATIC_CHOICES = [
        ("None", "None"),
        ("Ganesha", "Ganesha"),
        ("Hanuman", "Hanuman"),
        ("Jyothi Lingas", "Jyothi Lingas"),
        ("Sakthi Peetas", "Sakthi Peetas"),
    ]
    PRIORITY_CHOICES = [
        ("None", "None"),
        ("High", "High"),
        ("Medium", "Medium"),
        ("Low", "Low"),
    ]
    STYLE_CHOICES = [
        ("_", "_"),
        ("N", "N"),
        ("D", "D"),
        ("V", "V"),
    ]

    Temple_Code = models.CharField(max_length=50,primary_key=True)
    
    Temple_Category_Code =  models.ForeignKey(Temple_category,related_name ="Temple_category", on_delete=models.CASCADE, db_column='Temple_Category_Code')
    Temple_Priority_Code = models.ForeignKey(templePriority,related_name ="templePriority", on_delete=models.CASCADE, db_column='Temple_priority_Code')
    Temple_Name = models.CharField(max_length=100)
    Yr_of_Con = models.IntegerField(null=True, blank=True)
    Era = models.CharField(max_length=50)
    Is_Temp_Dest = models.BooleanField()
    Temple_Anim_Sacri_Status = models.BooleanField()
    Temple_Diety = models.BooleanField()

    Temple_Style = models.CharField(max_length=50,choices=STYLE_CHOICES, default="_")
    Tagged_Geo_Site = models.CharField(max_length=100)
    Location_Code = models.CharField(max_length=10)
    Temple_Map_Location = models.CharField(max_length=100)
    Temple_Address = models.TextField()
    Temple_Image_FileName1 = models.FileField(upload_to='static/media/temple_images/')
    Temple_Image_FileName2 = models.FileField(upload_to='static/media/temple_images/')
    Temple_Image_FilePath1 = models.FileField(upload_to='static/media/temple_images/')
    Temple_Image_FilePath2 = models.FileField(upload_to='static/media/temple_images/')
    Temple_URL_Link1 = models.URLField()
    Temple_URL_Link2 = models.URLField()
    Temple_Contact_Name = models.CharField(max_length=100)
    Temple_Contact_Phone = models.CharField(max_length=15)
    Temple_Email = models.EmailField()
    Temple_Desc = models.TextField()

    class Meta:
        managed = False  # Set managed to False to prevent table creation/modification
        db_table = 'temple'




class Temple_priority(models.Model):
    Temple_priority_Code = models.CharField(max_length=10, primary_key=True)
    Temple_priority_Name = models.CharField(max_length=100)
    Temple_priority_Desc = models.TextField()

    class Meta:
        managed = False  # Set managed to False to prevent table creation/modification
        db_table='temple_priority'        


############Goshala models################
        



class Goshala_category(models.Model):
    Goshala_Category_Code = models.CharField(max_length=10, primary_key=True)
    Goshala_Category_Name = models.CharField(max_length=100)
    Goshala_Category_Desc = models.TextField()

    class Meta:
        managed = False  # Set managed to False to prevent table creation/modification
        db_table='goshala_category'    



class Goshala_Model(models.Model):
    STATIC_CHOICES = [
        ("None", "None"),
        ("GOVT", "GOVT"),
        ("PVT", "PVT"),
        ("TR", "TR"),
    ]
    Goshala_Code = models.CharField(max_length=50,primary_key = True)
    # Goshala_Category_Code = models.CharField(max_length=50, choices=STATIC_CHOICES, default="None")
    # Goshala_Category = models.ForeignKey(Goshala_category, on_delete=models.CASCADE)
    Goshala_Category_Code = models.ForeignKey(Goshala_category,related_name ="Goshala_category", on_delete=models.CASCADE, db_column='Goshala_Category_Code')
    Goshala_Name = models.CharField(max_length=255)
    Goshala_Regn_No = models.CharField(max_length=50)
    Goshala_Status = models.BooleanField()
    Tagged_Geo_Site = models.CharField(max_length=255)
    Location_Code = models.CharField(max_length=50)
    Goshala_Map_Location = models.CharField(max_length=255)
    Temple_Code = models.ForeignKey(Temple,on_delete=models.CASCADE,db_column='Temple_Code')
    # Temple_Code = models.CharField(max_length=200)
    Goshala_Image_FilePath1 = models.FileField(upload_to='static/media/goshala_images/', blank=True, null=True)
    Goshala_Image_FilePath2 = models.FileField(upload_to='static/media/goshala_images/', blank=True, null=True)
    Goshala_URL_Link1 = models.URLField(max_length=255, blank=True, null=True)
    Goshala_URL_Link2 = models.URLField(max_length=255, blank=True, null=True)
    
    Goshala_Contact_Name = models.CharField(max_length=255)
    Goshala_Contact_Phone = models.CharField(max_length=20)
    Goshala_Address = models.TextField()
    Goshala_Email = models.EmailField(max_length=255)
    Goshala_Desc = models.TextField()
    Goshal_Regn_Document = models.FileField(upload_to='static/media/goshala_documents/')

    class Meta:
        managed = False  # Set managed to False to prevent table creation/modification
        db_table='goshala'



############################# Events_Mosels ##############################        
        



class Event_Category(models.Model):
    Event_Category_Code = models.CharField(max_length=10, primary_key=True)
    Event_Category_Name = models.CharField(max_length=100)
    Event_Category_Desc = models.TextField()

    class Meta:
        managed = False  # Set managed to False to prevent table creation/modification
        db_table='event_category'





class Event(models.Model):

    STATIC_CHOICES = [
        ("T", "T"),
        ("G", "G"),
    ]

    Event_Code = models.CharField(max_length=50, primary_key=True)
    Event_Category_Code = models.ForeignKey('Event_Category', on_delete=models.CASCADE, db_column='Event_Category_Code')
    Event_Name = models.CharField(max_length=255)
    Event_Status = models.BooleanField()
    Event_Start = models.CharField(max_length=50,)
    Event_End = models.CharField(max_length=50,)
    Tagged_Temple_Goshala_Code = models.CharField(max_length=50, choices=STATIC_CHOICES, default="T")
    Tagged_Code = models.CharField(max_length=50)
    Tagged_Geo_Site = models.CharField(max_length=255)
    Location_Code = models.CharField(max_length=50)
    Event_Map_Location = models.CharField(max_length=255)
    Event_Contact_Name = models.CharField(max_length=255)
    Event_Contact_Phone = models.CharField(max_length=20)
    Event_Email = models.EmailField(max_length=255)
    Event_Image_FileName1 = models.FileField(upload_to='static/media/event_images/', blank=True)
    Event_Image_FileName2 = models.FileField(upload_to='static/media/event_images/', blank=True, null=True)
    Event_Image_FilePath1 = models.FileField(upload_to='static/media/event_images/', blank=True, null=True)
    Event_Image_FilePath2 = models.FileField(upload_to='static/media/event_images/', blank=True, null=True)
    Event_URL_Link1 = models.URLField(max_length=255, blank=True, null=True)
    Event_URL_Link2 = models.URLField(max_length=255, blank=True, null=True)
    Event_Desc = models.TextField()

    class Meta:
        managed = False  # Set managed to False to prevent table creation/modification
        db_table = 'event'
     