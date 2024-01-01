

# myapp/views.py
from django.db import connection
from django.http import JsonResponse
import json
from rest_framework  .response import Response
from rest_framework import generics
from .serializers import *



def get_data_view(request):
    # Write your raw SQL query to retrieve data
    sql_query = "SELECT Temple_Category_Code, Temple_Category_Name, Temple_Category_Desc FROM temple_category"

    with connection.cursor() as cursor:
        # Execute the SQL query
        cursor.execute(sql_query)

        # Fetch all rows from the result set
        rows = cursor.fetchall()
    data_list = [
        {
            'Temple_Category_Code': row[0],
            'Temple_Category_Name': row[1],
            'Temple_category_Desc': row[2],
        }
        for row in rows
    ]

    # Return the data as JSON response
    return JsonResponse(data_list, safe=False)







#######################################tempes ger api



def temple_data_view(request):
    # Write your raw SQL query to retrieve data
    sql_query = "SELECT * FROM temple"

    with connection.cursor() as cursor:
        # Execute the SQL query
        cursor.execute(sql_query)

        # Fetch all rows from the result set
        rows = cursor.fetchall()
    data_list = [
        {
            'Temple_Code': row[0],
            'Temple_Category_Code': row[1],
            'Temple_Priority_Code': row[2],
            'Temple_Name': row[3],
            'Yr_of_Con': row[4],
            'Era': row[5],
            'Is_Temp_Dest': row[6],
            'Temple_Anim_Sacri_Status': row[7],
            'Temple_Diety': row[8],
            'Temple_Style': row[9],
            'Tagged_Geo_Site': row[10],
            'Location_Code': row[11],
            'Temple_Map_Location': row[12],
            'Temple_Address': row[13],
            'Temple_Image_FileName1': row[14],
            'Temple_Image_FileName2': row[15],
            'Temple_Image_FilePath1': row[16],
            'Temple_Image_FilePath2': row[17],
            'Temple_URL_Link1': row[18],
            'Temple_URL_Link2': row[19],
            'Temple_Contact_Name': row[20],
            'Temple_Contact_Phone': row[21],
            'Temple_Email': row[22],
            'Temple_Desc': row[23]
        }
        for row in rows
    ]

    # Return the data as JSON response
    return JsonResponse(data_list, safe=False)


# class templeApiview(generics.GenericAPIView):
#     serializer_class = templeserializer

#     def post(self,request):
#         a = templeserializer(data=request.data)
#         if a.is_valid():
#             b = a.save()
#             return Response({
#                 "message":"success",
#                 "result":templeserializer(b).data,
#                 "status":200
#             })
#         else:
#             return Response({
#                 "message":"invalid data",
#                 "status":400
#             })


########################################################goshala_category


def Goshala_data_view(request):
    # Write your raw SQL query to retrieve data
    sql_query = "SELECT *  FROM goshala_category"

    with connection.cursor() as cursor:
        # Execute the SQL query
        cursor.execute(sql_query)

        # Fetch all rows from the result set
        rows = cursor.fetchall()
    data_list = [
        {
            'Goshala_Category_Code': row[0],
            'Goshala_Category_Name': row[1],
            'Goshala_Category_Desc': row[2],
        }
        for row in rows
    ]

    # Return the data as JSON response
    return JsonResponse(data_list, safe=False)


########################################################goshala

# Goshala_view
def Goshala_view(request):
    # Write your raw SQL query to retrieve data
    sql_query = "SELECT * FROM goshala"

    with connection.cursor() as cursor:
        # Execute the SQL query
        cursor.execute(sql_query)

        # Fetch all rows from the result set
        rows = cursor.fetchall()

    data_list = [
        {
            'Goshala_Code': row[0],
            'Goshala_Category_Code': row[1],
            'Goshala_Name': row[2],
            'Goshala_Regn_No': row[3],  # Assuming Goshala_Regn_No is present in the goshala table
            'Goshala_Status': row[4],
            'Tagged_Geo_Site': row[5],
            'Location_Code': row[6],
            'Goshala_Map_Location': row[7],
            'Temple_Code': row[8],
            'Goshala_Image_FileName1': row[9],
            'Goshala_Image_FileName2': row[10],
            'Goshala_Image_FilePath1': row[11],
            'Goshala_Image_FilePath2': row[12],
            'Goshala_URL_Link1': row[13],
            'Goshala_URL_Link2': row[14],
            'Goshala_Contact_Name': row[15],
            'Goshala_Contact_Phone': row[16],
            'Goshala_Address': row[17],
            'Goshala_Email': row[18],
            'Goshala_Desc': row[19],
            'Goshal_Regn_Document': row[20]
        }
        for row in rows
    ]

    # Return the data as JSON response
    return JsonResponse(data_list, safe=False)



########################################################event_category


def event_data_view(request):
    # Write your raw SQL query to retrieve data
    sql_query = "SELECT *  FROM event_category"

    with connection.cursor() as cursor:
        # Execute the SQL query
        cursor.execute(sql_query)

        # Fetch all rows from the result set
        rows = cursor.fetchall()
    data_list = [
        {
            'Event_Category_Code': row[0],
            'Event_Category_Name': row[1],
            'Event_Category_Desc': row[2],
        }
        for row in rows
    ]

    # Return the data as JSON response
    return JsonResponse(data_list, safe=False)


# Event_view##################################################


def Event_view(request):
    # Write your raw SQL query to retrieve data
    sql_query = "SELECT * FROM event"

    with connection.cursor() as cursor:
        # Execute the SQL query
        cursor.execute(sql_query)

        # Fetch all rows from the result set
        rows = cursor.fetchall()

    data_list = [
        {
            'Event_Code': row[0],
            'Event_Category_Code': row[1],
            'Event_Name': row[2],
            'Event_Status': row[3],
            'Event_Start': row[4],
            'Event_End': row[5],
            'Tagged_Temple_Goshala_Code': row[6],
            'Tagged_Code': row[7],
            'Tagged_Geo_Site': row[8],
            'Location_Code': row[9],
            'Event_Map_Location': row[10],
            'Event_Contact_Name': row[11],
            'Event_Contact_Phone': row[12],
            'Event_Email': row[13],
            'Event_Image_FileName1': row[14],
            'Event_Image_FileName2': row[15],
            'Event_Image_FilePath1': row[16],
            'Event_Image_FilePath2': row[17],
            'Event_URL_Link1': row[18],
            'Event_URL_Link2': row[19],
            'Event_Desc': row[20],
        }
        for row in rows
    ]

    # Return the data as JSON response
    return JsonResponse(data_list, safe=False)


