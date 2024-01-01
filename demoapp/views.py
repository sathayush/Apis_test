# views.py
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework import generics
from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from django .http import HttpResponse

##############################temple get calls#################################

class TempleCategoryView(APIView):
    def get(self, request):
        categories = Temple_category.objects.values()
        return JsonResponse(list(categories), safe=False)
    

class TempleView(APIView):
    def get(self, request,temple_category_code):
        temples = Temple.objects.filter(Temple_Category_Code=temple_category_code).values()
        return JsonResponse(list(temples), safe=False)
    
# class TempleView(APIView):
#     def get(self, request, input_value):
#         # Get all field names from the model
#         fields = [field.name for field in Temple._meta.get_fields()]
#         print(fields,"###################")
#         # Create a filter condition using Q objects
#         filter_condition = Q()

#         for field in fields:
#             filter_condition |= Q(**{f'{field}__icontains': input_value})
#             print(filter_condition,"@@@@@@@@@@@@@@@@@@@@@@@@@@@@")


#         # Apply the filter condition to the queryset
#         queryset = Temple.objects.filter(filter_condition)
#         print(queryset,"1111111111111111111111111111")

#         # Convert the queryset to a list of dictionaries
#         result_list = list(queryset.values())
#         print(result_list,"222222222222222222222222222222")

#         # Return the list as a JSON response
#         return JsonResponse(result_list, safe=False)

    
class TempleViewAll(APIView):
    def get(self, request,):
        temples = Temple.objects.values()
        return JsonResponse(list(temples), safe=False)
    


    

   

class TemplePriorityView(APIView):
    def get(self,request):
        templepriority=Temple_priority.objects.values() 
        return JsonResponse(list(templepriority),safe=False)   


########################################temple post calls CRUD################################################



class TempleViewPost(generics.GenericAPIView):
    serializer_class = TempleSerializer

    def post(self, request):
        try:
            serializer = TempleSerializer(data=request.data)

            if serializer.is_valid():
                v = serializer.save()
                return Response({
                    "message": "success",
                    "data": TempleSerializer(v).data,
                    "status": status.HTTP_200_OK
                })

            return JsonResponse({
                "message": "error",
                "errors": serializer.errors,
                "status": status.HTTP_400_BAD_REQUEST
            })

        except Temple.DoesNotExist:
            return JsonResponse({"error": "error"}, status=404)    


class TempleViewPut(generics.GenericAPIView):
    serializer_class = TempleSerializer

    def put(self, request, Temple_code):
        try:
            # Get the existing Temple instance
            a = Temple.objects.get(pk=Temple_code)
            print(a,"111111111111111111111111111111111111111")

            # Deserialize the request data and update the instance
            b = TempleSerializer(a, data=request.data, partial=True)
            print(b,"22222222222222222222222222222222222")

            # Validate and save the updated data
            if b.is_valid():
                c = b.save()
                return Response({
                    "message": "success",
                    "edit_data": b.data,  # Use the serializer to get the serialized data
                    "result": TempleSerializer(c).data,
                    "status": status.HTTP_200_OK
                })

            return Response({
                "message": "error",
                "errors": b.errors,
                "status": status.HTTP_400_BAD_REQUEST
            })

        except Temple.DoesNotExist:
            # Handle the case where Temple with the specified code does not exist
            return Response({
                "message": f"Temple with code {Temple_code} does not exist",
                "status": status.HTTP_404_NOT_FOUND
            })


class TempleViewDelete(generics.GenericAPIView):
    serializer_class = TempleSerializer

    def delete(self, request, pk):
        try:
            # Get the existing Temple instance
            temple_instance = Temple.objects.get(pk=pk)

            # Delete the instance
            temple_instance.delete()

            return Response({"message": "Temple deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

        except Temple.DoesNotExist:
            # Handle the case where Temple with the specified code does not exist
            return JsonResponse({"error": "Error"}, status=404)        
        








########################################## GOSHALA  ####################################################

#########get calls##################
        
class GoshalaCategoryView(APIView):
    def get(self, request):
        categories = Goshala_category.objects.values()
        return JsonResponse(list(categories), safe=False) 




class GoshalaView(generics.GenericAPIView):
    serializer_class = GoshalaSerializer

    def get(self, request, Goshala_Category_Code):  # Update parameter name
   
        filtered_goshalas = Goshala_Model.objects.filter(Goshala_Category_Code = Goshala_Category_Code)
        print(filtered_goshalas, "1111111111111111111111")

        # Serialize the single object
        serializer = GoshalaSerializer(filtered_goshalas,many = True)

        # Return the serialized data as a JSON response
        return Response(serializer.data)

    

class GoshalaViewAll(APIView):
    def get(self, request,):
        goshalas = Goshala_Model.objects.values()
        return JsonResponse(list(goshalas), safe=False)
    
##########################goshala post calls#####################



#post#
class GoshalaViewPost(generics.GenericAPIView):
    serializer_class = GoshalaSerializer

    def post(self, request):
        try:
            serializer = GoshalaSerializer(data=request.data)
            print(serializer,"!!!!!!!!!!!!!!!!!!!!!!!!!!!")

            if serializer.is_valid():
                v = serializer.save()
                print(v,"2222222222222222222222222222222")
                return Response({
                    "message": "success",
                    "data": GoshalaSerializer(v).data,
                    "status": status.HTTP_200_OK
                })

            return JsonResponse({
                "message": "error",
                "errors": serializer.errors,
                "status": status.HTTP_400_BAD_REQUEST
            })

        except Temple.DoesNotExist:
            return JsonResponse({"error": "error"}, status=404)
        


#put#



class GoshalaViewPut(generics.GenericAPIView):
    serializer_class = GoshalaSerializer

    def put(self, request, Goshala_Code):
        try:
            # Get the existing Temple instance
            a = Goshala_Model.objects.get(pk=Goshala_Code)
            print(a,"111111111111111111111111111111111111111")

            # Deserialize the request data and update the instance
            b = GoshalaSerializer(a, data=request.data, partial=True)
            print(b,"22222222222222222222222222222222222")

            # Validate and save the updated data
            if b.is_valid():
                c = b.save()
                return Response({
                    "message": "success",
                    "edit_data": b.data,  # Use the serializer to get the serialized data
                    "result": GoshalaSerializer(c).data,
                    "status": status.HTTP_200_OK
                })

            return Response({
                "message": "error",
                "errors": b.errors,
                "status": status.HTTP_400_BAD_REQUEST
            })

        except Goshala_Model.DoesNotExist:
            # Handle the case where Temple with the specified code does not exist
            return Response({
                "message": f"Goshala with code {Goshala_Code} does not exist",
                "status": status.HTTP_404_NOT_FOUND
            })
        


#Delete#
        

class GosdhalaViewDelete(generics.GenericAPIView):
    serializer_class = GoshalaSerializer

    def delete(self, request, pk):
        try:
            # Get the existing Temple instance
            goshala_instance = Temple.objects.get(pk=pk)
            

            # Delete the instance
            goshala_instance.delete()

            return Response({"message": "goashala deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

        except Temple.DoesNotExist:
            # Handle the case where Temple with the specified code does not exist
            return JsonResponse({"error": "Error"}, status=404)        
        

##########################Events##########################
##############get_calls#############    





class EventCategoryView(APIView):
    def get(self, request):
        categories = Event_Category.objects.values()
        return JsonResponse(list(categories), safe=False) 
    

# class EventView(generics.GenericAPIView):
#     serializer_class = EventSerializer

#     def get(self, request, Event_Category_Code):  # Update parameter name
   
#         events = Event.objects.filter(Event_Category_Code = Event_Category_Code).values()
#         print(events, "1111111111111111111111")

#         # Serialize the single object
#         serializer = EventSerializer(events,many = True)

#         # Return the serialized data as a JSON response
#         return JsonResponse(serializer.data,safe=False)    




class EventView(generics.GenericAPIView):
    serializer_class = EventSerializer

    def get(self, request, Event_Category_Code):
        # Filter queryset based on Event_Category_Code
        events = Event.objects.filter(Event_Category_Code=Event_Category_Code)

        # Serialize the queryset
        serializer = EventSerializer(events, many=True)

        # Return the serialized data as a JSON response
        return Response(serializer.data)





class EventViewAll(APIView):
    def get(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data) 

        




        
        
           
