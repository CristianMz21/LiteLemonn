# Little Lemon API

## Descripción del Proyecto

Little Lemon es una API RESTful desarrollada con Django y Django REST Framework para gestionar un restaurante. La aplicación permite administrar el menú, reservas y autenticación de usuarios.

## Características

- Gestión de menú (crear, leer, actualizar y eliminar elementos del menú)
- Sistema de reservas de mesas
- Autenticación de usuarios mediante tokens
- API RESTful completa
- Soporte para bases de datos SQLite y PostgreSQL

## Requisitos

- Python 3.8 o superior
- Django 5.1 o superior
- Django REST Framework
- PostgreSQL (opcional, SQLite por defecto)

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/LiteLemonn.git
cd LiteLemonn
```

### 2. Crear y activar un entorno virtual

#### En Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

#### En macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar la base de datos

#### Opción 1: SQLite (por defecto)

No se requiere configuración adicional. Django utilizará SQLite por defecto.

#### Opción 2: PostgreSQL

1. Instalar PostgreSQL desde [el sitio oficial](https://www.postgresql.org/download/)
2. Crear una base de datos llamada 'littlelemon'
3. Crear un archivo `.env` en la raíz del proyecto con el siguiente contenido:

```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=littlelemon
DB_USER=postgres
DB_PASSWORD=tu_contraseña
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY=tu_clave_secreta
DEBUG=True
```

### 5. Aplicar migraciones

```bash
cd littlelemon
python manage.py makemigrations
python manage.py migrate
```

### 6. Crear un superusuario (opcional)

```bash
python manage.py createsuperuser
```

### 7. Iniciar el servidor de desarrollo

```bash
python manage.py runserver
```

El servidor estará disponible en http://127.0.0.1:8000/

## Estructura del Proyecto

```
littlelemon/
├── littlelemon/       # Configuración principal del proyecto
├── restaurant/        # Aplicación principal
│   ├── models.py      # Modelos de datos
│   ├── views.py       # Vistas y lógica de negocio
│   ├── urls.py        # Configuración de URLs
│   ├── serializers.py # Serializadores para la API
│   ├── static/        # Archivos estáticos
│   └── templates/     # Plantillas HTML
└── tests/             # Pruebas automatizadas
```

## API Endpoints

### Autenticación

- `POST /auth/token/login/` - Obtener token de autenticación
- `POST /auth/token/logout/` - Cerrar sesión (invalidar token)
- `POST /restaurant/api-token-auth/` - Obtener token (método alternativo)

### Menú

- `GET /restaurant/menu-items/` - Listar todos los elementos del menú
- `POST /restaurant/menu-items/` - Crear un nuevo elemento del menú
- `GET /restaurant/menu-items/{id}/` - Obtener detalles de un elemento del menú
- `PUT /restaurant/menu-items/{id}/` - Actualizar un elemento del menú
- `DELETE /restaurant/menu-items/{id}/` - Eliminar un elemento del menú

### Reservas

- `GET /restaurant/booking/tables/` - Listar todas las reservas (requiere autenticación)
- `POST /restaurant/booking/tables/` - Crear una nueva reserva (requiere autenticación)
- `GET /restaurant/booking/tables/{id}/` - Obtener detalles de una reserva (requiere autenticación)
- `PUT /restaurant/booking/tables/{id}/` - Actualizar una reserva (requiere autenticación)
- `DELETE /restaurant/booking/tables/{id}/` - Eliminar una reserva (requiere autenticación)

### Mensajes protegidos

- `GET /restaurant/message/` - Obtener mensaje protegido (requiere autenticación)

## Ejemplos de Uso

### Obtener token de autenticación

```bash
curl -X POST http://127.0.0.1:8000/auth/token/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"tu_usuario","password":"tu_contraseña"}'
```

### Listar elementos del menú

```bash
curl -X GET http://127.0.0.1:8000/restaurant/menu-items/
```

### Crear una reserva (con autenticación)

```bash
curl -X POST http://127.0.0.1:8000/restaurant/booking/tables/ \
  -H "Authorization: Token tu_token" \
  -H "Content-Type: application/json" \
  -d '{"name":"Juan Pérez","no_of_guests":4,"booking_date":"2023-12-25T19:30:00Z"}'
```

## Pruebas

Para ejecutar las pruebas automatizadas:

```bash
python manage.py test
```

## Contribuir

1. Haz un fork del repositorio
2. Crea una rama para tu característica (`git checkout -b feature/nueva-caracteristica`)
3. Haz commit de tus cambios (`git commit -am 'Añadir nueva característica'`)
4. Haz push a la rama (`git push origin feature/nueva-caracteristica`)
5. Crea un nuevo Pull Request

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo LICENSE para más detalles.