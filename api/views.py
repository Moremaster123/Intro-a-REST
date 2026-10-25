from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import Product

from .serializers import ProductSerializer


class ProductListAPIView(APIView):
    def get(self, request):
        print('GET: listar productos')
        products = Product.objects.order_by('id')
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        print('POST: crear producto', request.data)
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailAPIView(APIView):
    def get(self, request, pk):
        print(f'GET: consultar producto {pk}')
        product = get_object_or_404(Product, pk=pk)
        return Response(ProductSerializer(product).data)

    def put(self, request, pk):
        print(f'PUT: actualizar producto {pk}', request.data)
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        print(f'DELETE: borrar producto {pk}')
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
