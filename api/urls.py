from django.urls import path
from api import views

urlpatterns = [
    path('categories/', views.categories),

    path('products/subcategory/', views.by_subcat),    
    path('products/orders/', views.OrderV.as_view()),
    path('products/<int:id>/', views.by_category),

]