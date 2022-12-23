from django.urls import path
from rest_framework import routers
from .views import *
from apps.products.api.v1.viewset import *
from . import views

 # Filters
    

router = routers.DefaultRouter()
router.register(r'Product', ProductViewSet, basename='Product')  

urlpatterns = router.urls


urlpatterns +=  [
    # products
    # path('ProductFilter/', ProductFilter),
    path('PRADUCT/<int:pk>/', ProductRetrieveAPIView.as_view()),
    path('product_api_view/', ProductListAPIView.as_view()),
    path('prproduct_api_viewoduct_api_view/create', ProductCreateAPIView.as_view()),
    path('product_api_view/<int:pk>/', Product_api_view),
    
    # Gallerys
    path('Gallery_api_view/', GalleryListAPIView.as_view()),
    path('Gallery_api_view/create', GalleryCreateAPIView.as_view()),
    path('Gallery_api_view/<int:pk>/', Gallery_api_view),
    
    # Sectionss
    path('Sections_api_view/', SectionsListAPIView.as_view()),
    path('Sections_api_view/create', SectionsCreateAPIView.as_view()),
    path('Sections_api_view/<int:pk>/', Sections_api_view),
    
    # ProductReview
    path('productReview_api_view/', ProductReviewListAPIView.as_view()),
    # path('productFilter/', ProductReviewaListAPIView.as_view()),
    path('productReview_api_view/create', ProductReviewCreateAPIView.as_view()),
    path('productReview_api_view/<int:pk>/', ProductReview_api_view),

    
    # SectionsCategory
    path('SectionsCategory_api_view/', SectionsCategoryListAPIView.as_view()),
    path('SectionsCategory_api_view/create', SectionsCategoryCreateAPIView.as_view()),
    path('SectionsCategory_api_view/<int:pk>/', SectionsCategory_api_view),

    path('Category_api_view/', CategoryListAPIView.as_view()),
    path('Category_api_view/create', CategoryCreateAPIView.as_view()),
]
   
    