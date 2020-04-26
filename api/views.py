from django.shortcuts import render


from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

from api.serializers import CategoryS, SubcategoryS, ProductS
from api.models import Category, SubCategory, Product, Order

@api_view(['GET'])
def categories(request):
    return JsonResponse(CategoryS(Category.objects.all(), many=True).data, safe=False)

@api_view(['GET'])
def by_category(request, id):
    category = Category.objects.get(id=id)
    return JsonResponse(ProductS(category.product_set.all(), many=True).data, safe=False)

@api_view(['POST'])
def by_subcat(request):
    subcategory=SubCategory.objects.get(name=request.data.get('subcat'))
    return JsonResponse(ProductS(subcategory.product_set.all(), many=True).data, safe=False)


class OrderV(APIView):
    def post(self, request):
        Order.objects.create(
            user = request.data.get('name'),
            phoneNumber = request.data.get('phone'),
            address = request.data.get('address')
        )
        return JsonResponse({"asd": "asdas"}, safe=False)