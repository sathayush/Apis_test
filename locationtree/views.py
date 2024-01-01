from django.shortcuts import render
from .serializers import *
from rest_framework import generics
from rest_framework .response import Response
from rest_framework.views import APIView
from django .db import connections,DatabaseError,connection
from django .http import JsonResponse



class Get_all_countries(APIView):

    def get(self, request):
        try:
            # Specify the database alias defined in your Django settings
            database_alias = 'default'  # Update this if necessary

            # Query to get specific fields for all user details
            select_query = "SELECT * FROM country;"

            # Use Django's connection module to handle the database connection
            with connections[database_alias].cursor() as cursor:
                cursor.execute(select_query)
                countries = cursor.fetchall()

                # Get field names from the cursor description
                field_names = [desc[0] for desc in cursor.description]

            if countries:
                # Construct a list of dictionaries for all users
                country_list = [
                    {
                        "Country_Code": row[0],
                        "Country_Name": row[1],
                        "Country_ShortName": row[2] ,
                        'Country_AlternativeName':row[3] ,
                        'Country_Desc':row[4]

                    }
                    for row in countries
                ]
                return JsonResponse({"users": country_list})
            else:
                return JsonResponse({"message": "No country found"}, status=404)

        except DatabaseError as e:
            error_message = str(e)
            return JsonResponse({"message": error_message})
        





class Get_States_by_country_code(APIView):

    def get(self, request, country_code):
        try:
            # Specify the database alias defined in your Django settings
            database_alias = 'default'  # Update this if necessary

            # Query to get specific fields for states based on Country_Code
            select_query = "SELECT * FROM state WHERE Country_Code = %s;"

            # Use Django's connection module to handle the database connection
            with connections[database_alias].cursor() as cursor:
                cursor.execute(select_query, [country_code])
                all_state_details = cursor.fetchall()

                # Get field names from the cursor description
                field_names = [desc[0] for desc in cursor.description]

            if all_state_details:
                # Construct a list of dictionaries for states
                states_list = [
                    {
                        "State_Code": row[0],
                        "State_Name": row[1],
                        "State_ShortName": row[2],
                        "State_Desc": row[3],
                        "Country_Code": row[4]
                    }
                    for row in all_state_details
                ]
                return JsonResponse({"states": states_list})
            else:
                return JsonResponse({"message": f"No states found for Country_Code: {country_code}"}, status=404)

        except DatabaseError as e:
            error_message = str(e)
            return JsonResponse({"message": error_message})
        




class Get_Districts_by_state_code(APIView):

    def get(self, request, state_code):
        try:
            # Specify the database alias defined in your Django settings
            database_alias = 'default'  # Update this if necessary

            # Query to get specific fields for states based on Country_Code
            select_query = "SELECT * FROM District WHERE state_Code = %s;"

            # Use Django's connection module to handle the database connection
            with connections[database_alias].cursor() as cursor:
                cursor.execute(select_query, [state_code])
                districts = cursor.fetchall()

                # Get field names from the cursor description
                field_names = [desc[0] for desc in cursor.description]

            if districts:
                # Construct a list of dictionaries for states
                dst_list = [
                    {
                        "District_Code": row[0],
                        "District_Name": row[1],
                        "District_ShortName": row[2],
                        "District_Desc": row[3],
                        "State_code": row[4]
                    }
                    for row in districts
                ]
                return JsonResponse({"Districts": dst_list})
            else:
                return JsonResponse({"message": f"No dist found for state_Code: {state_code}"}, status=404)

        except DatabaseError as e:
            error_message = str(e)
            return JsonResponse({"message": error_message})
        

class Get_Blocks_by_dst_code(APIView):

    def get(self, request, district_code):
        try:
            # Specify the database alias defined in your Django settings
            database_alias = 'default'  # Update this if necessary

            # Query to get specific fields for states based on Country_Code
            select_query = "SELECT * FROM Block WHERE district_Code = %s;"

            # Use Django's connection module to handle the database connection
            with connections[database_alias].cursor() as cursor:
                cursor.execute(select_query, [district_code])
                all_blocks_details = cursor.fetchall()

                # Get field names from the cursor description
                field_names = [desc[0] for desc in cursor.description]

            if all_blocks_details:
                # Construct a list of dictionaries for states
                dst_list = [
                    {
                        "Block_Code": row[0],
                        "Block_Name": row[1],
                        
                        "Block_Desc": row[2],
                        "district_code": row[3]
                    }
                    for row in all_blocks_details
                ]
                return JsonResponse({"Blocks": dst_list})
            else:
                return JsonResponse({"message": f"No blocks found for dst_Code: {district_code}"}, status=404)

        except DatabaseError as e:
            error_message = str(e)
            return JsonResponse({"message": error_message})    




class Get_Village_by_block_code(APIView):

    def get(self, request, block_code):
        try:
            # Specify the database alias defined in your Django settings
            database_alias = 'default'  # Update this if necessary

            # Query to get specific fields for states based on Country_Code
            select_query = "SELECT * FROM Village WHERE block_Code = %s;"

            # Use Django's connection module to handle the database connection
            with connections[database_alias].cursor() as cursor:
                cursor.execute(select_query, [block_code])
                all_Village_details = cursor.fetchall()

                # Get field names from the cursor description
                field_names = [desc[0] for desc in cursor.description]

            if all_Village_details:
                # Construct a list of dictionaries for states
                dst_list = [
                    {
                        "Village_Code": row[0],
                        "Village_Name":row[1],
                        
                        "block_Code": row[2]
                    }
                    for row in  all_Village_details
                ]
                return JsonResponse({"Blocks": dst_list})
            else:
                return JsonResponse({"message": f"No villages found for dst_Code: {block_code}"}, status=404)

        except DatabaseError as e:
            error_message = str(e)
            return JsonResponse({"message": error_message})             































