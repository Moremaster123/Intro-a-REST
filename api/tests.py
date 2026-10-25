from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from product.models import Product


class ProductAPITests(APITestCase):
    def setUp(self):
        self.product = Product.objects.create(name='Taza', description='Cerámica', price=120, stock=10)
        self.list_url = reverse('api:product-list')
        self.detail_url = reverse('api:product-detail', args=[self.product.pk])

    def test_get_lista(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Taza')

    def test_get_detalle(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.data['price'], '120.00')

    def test_get_no_existe(self):
        response = self.client.get(reverse('api:product-detail', args=[999]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_post_crea_producto(self):
        data = {'name': 'Gorra', 'description': 'Negra', 'price': '250.00', 'stock': 5}
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Product.objects.filter(name='Gorra', stock=5).exists())

    def test_post_precio_invalido(self):
        data = {'name': 'Gorra', 'description': 'Negra', 'price': '0'}
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('price', response.data)

    def test_put_actualiza_producto(self):
        data = {'name': 'Taza grande', 'description': 'Cerámica', 'price': '150.00', 'stock': 8}
        response = self.client.put(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, 'Taza grande')
        self.assertEqual(self.product.stock, 8)

    def test_delete_borra_producto(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Product.objects.filter(pk=self.product.pk).exists())
