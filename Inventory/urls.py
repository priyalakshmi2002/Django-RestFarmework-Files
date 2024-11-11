# from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter
from .views import ProductsViewSet,CategoryViewSet

router= DefaultRouter()
router.register(r'products', ProductsViewSet,basename='products')
router.register(r'category',CategoryViewSet, basename='category')

urlpatterns = router.urls

# urlpatterns = [
#     path('products/',ProductsView.as_view()),
#     path('products/<int:id>/',ProductsViewById.as_view()),
#     path('category/', CategoryView.as_view()),
#     path('category/<int:id>/',CategoryViewById.as_view()),
# ]
