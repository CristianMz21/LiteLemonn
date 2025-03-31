from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

class MenuViewTest(TestCase):
    def setUp(self):
        # Crear instancias de prueba del modelo Menu
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Pizza", price=120, inventory=50)
        Menu.objects.create(title="Burger", price=90, inventory=75)
    
    def test_getall(self):
        # Configurar el cliente API
        client = APIClient()
        
        # Usar la URL directa para la vista de lista de menús
        url = '/restaurant/menu-items/'
        
        # Realizar la solicitud GET
        response = client.get(url)
        
        # Verificar que la solicitud fue exitosa
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Obtener todos los objetos Menu de la base de datos
        menus = Menu.objects.all()
        
        # Serializar los objetos Menu
        serializer = MenuSerializer(menus, many=True)
        
        # Verificar que los datos serializados son iguales a la respuesta
        self.assertEqual(response.data, serializer.data)