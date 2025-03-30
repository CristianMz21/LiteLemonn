# Configuración de PostgreSQL para Little Lemon

Este documento proporciona instrucciones para configurar PostgreSQL como base de datos para el proyecto Little Lemon.

## Requisitos previos

1. **Instalar PostgreSQL**
   - Descargue PostgreSQL desde [el sitio oficial](https://www.postgresql.org/download/windows/)
   - Durante la instalación, anote la contraseña que establezca para el usuario 'postgres'
   - Asegúrese de que el puerto predeterminado sea 5432 (o anote el puerto que elija)

2. **Instalar el adaptador psycopg2 (Ya instalado)**
   ```
   pip install psycopg2
   ```

## Configuración de la base de datos

1. **Crear la base de datos**
   - Abra pgAdmin (viene con la instalación de PostgreSQL)
   - Conéctese al servidor PostgreSQL con las credenciales que estableció durante la instalación
   - Cree una nueva base de datos llamada 'littlelemon'

2. **Configurar Django para usar PostgreSQL**
   - Abra el archivo `littlelemon/settings.py`
   - Busque la sección DATABASES
   - Descomente la configuración de PostgreSQL y comente la configuración de SQLite
   - Actualice los valores según su instalación:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'littlelemon',
           'USER': 'postgres',  # Cambie esto por su nombre de usuario de PostgreSQL
           'PASSWORD': 'su_contraseña',  # Cambie esto por su contraseña de PostgreSQL
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

3. **Migrar la base de datos**
   - Ejecute los siguientes comandos para aplicar las migraciones a la nueva base de datos PostgreSQL:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

## Verificación

Para verificar que la conexión a PostgreSQL funciona correctamente:

1. Ejecute el servidor de desarrollo:
   ```
   python manage.py runserver
   ```

2. Si el servidor se inicia sin errores relacionados con la base de datos, la configuración es correcta.

## Solución de problemas

- **Error de conexión**: Verifique que PostgreSQL esté en ejecución y que los datos de conexión sean correctos.
- **Error de autenticación**: Asegúrese de que el usuario y la contraseña sean correctos.
- **Base de datos no existe**: Verifique que haya creado la base de datos 'littlelemon' en PostgreSQL.

## Volver a SQLite

Si necesita volver a usar SQLite temporalmente, simplemente invierta los cambios en el archivo `settings.py`, comentando la configuración de PostgreSQL y descomentando la configuración de SQLite.