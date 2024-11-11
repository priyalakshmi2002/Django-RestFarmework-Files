# from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import viewsets,mixins
from rest_framework import status


# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated

# class ProductsView(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    # def get(self, request):
    #     all_products = Products.objects.all()
    #     products_data =[]
    #     for product in all_products:
    #        single_product = {
    #            "id": product.id,
    #            "product_name": product.product_name,
    #            "code":product.code,
    #            "price": product.price,
    #            "category_reference_id":product.category_reference_id,
    #        }
           
    #        products_data.append(single_product)
            
    #     return Response(products_data)
    
    # def post(self, request):
    #     new_product = Products(product_name= request.data["product_name"], code=request.data["code"], price= request.data['price'],category_reference_id=request.data['category_reference_id'])
    #     new_product.save()
    #     return Response("Data Saved")
    
#     def get(self, request):
#         all_products = Products.objects.all()
#         serialized_products = Products_Serializers2(all_products, many=True).data
#         return Response(serialized_products)
    
#     def post(self, request):
#         new_category = Products_Serializers(data=request.data)
#         if new_category.is_valid():
#             new_category.save()
#             return Response("Data Saved")
        
#         else:
#             return Response(new_category.errors)

    
# class ProductsViewById(APIView):
    # def get(self,request,id):
    #     product = Products.objects.get(id=id)
        
    #     single_product = {
    #            "id": product.id,
    #            "product_name": product.product_name,
    #            "code":product.code,
    #            "price": product.price,
    #            "category_reference_id":product.category_reference_id
    #     }
        
    #     return Response(single_product)
    
#     def get(self,request,id):
#         product = Products.objects.get(id=id)
        
#         single_product = Products_Serializers(product).data
        
#         return Response(single_product)
    
#     def patch(self,request,id):
#         product = Products.objects.filter(id=id)
#         product.update(product_name = request.data["product_name"], code = request.data["code"], 
#                        price = request.data['price'],category_reference = request.data['category_reference'])
#         return Response("Updated")
    
#     def delete(self,request,id):
#           product = Products.objects.get(id=id)
          
#           product.delete()
          
#           return Response("Deleted")
      
# class CategoryView(APIView):
#     def get(self,request):       
#         all_category = Category_Serializer(Category.objects.all(), many=True).data
#         return Response(all_category)
    
#     def post(self,request):
#         new_category = Category_Serializer(data=request.data)
#         if new_category.is_valid():
#             new_category.save()
#             return Response("Data Saved")
        
#         else:
#             return Response(new_category.errors)
        
# class CategoryViewById(APIView):
#     def delete(self, request, id):
#         category = Category.objects.get(id=id)
#         category.delete()
#         return Response("Deleted")
    
# # Generic views
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# from .models import Products, Category
# from .serializers import Products_Serializers, Products_Serializers2, Category_Serializer

# # Products API Views
# class ProductsView(ListCreateAPIView):
#     queryset = Products.objects.all()
#     serializer_class = Products_Serializers  # Using the serializer that handles all products

# class ProductsViewById(RetrieveUpdateDestroyAPIView):
#     queryset = Products.objects.all()
#     serializer_class = Products_Serializers  # For single product operations
#     lookup_field = 'id'

    #   def destroy(self, request, *args, **kwargs):
    #       product = self.get_object()
    #       if product.is_featured:
    #           return Response(
    #               {"error": "Cannot delete a featured product."},
    #               status=status.HTTP_400_BAD_REQUEST
    #           )
    #        return super().destroy(request,*args,**kwargs)
    
# # Category API Views
# class CategoryView(ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = Category_Serializer  # Serializer for the Category model

# class CategoryViewById(RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = Category_Serializer
#     lookup_field = 'id'
    #   def destroy(self, request, *args,**kwargs):
    #       category = self.get_object()
    #       if Products.objects.filter(category_reference=category).exists():
    #           return Response(
    #               {"error": "Cannot delete a category with associated products."},
    #               status=status.HTTP_400_BAD_REQUEST
    #           )
    #       return super().destroy(request,*args, **kwargs)
    

#mixins and genericviewsets
# class ProductsViewSet(
#     mixins.CreateModelMixin,
#     mixins.ListModelMixin,
#     mixins.RetrieveModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
#     viewsets.GenericViewSet
# ):
#     queryset = Products.objects.all()
#     serializer_class = Products_Serializers

# class CategoryViewSet(
#     mixins.CreateModelMixin,
#     mixins.ListModelMixin,
#     mixins.RetrieveModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
#     viewsets.GenericViewSet
# ):
#     queryset = Category.objects.all()
#     serializer_class = Category_Serializer
    
    
#viewsets in django rest framework

# Category ViewSet
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = Category_Serializer

    # Overriding create method for custom response
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response({"message": "Data Saved"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Overriding destroy method for custom delete response
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Deleted"})
    
#Product viewset  
class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = Products_Serializers

    # Overriding create method for custom response
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response({"message": "Data Saved"})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    # Overriding update method for PATCH functionality
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response({"message": "Updated"})
        return Response(serializer.errors)


    
