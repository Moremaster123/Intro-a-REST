# Introducción a REST con Django REST Framework

Primera API del e-commerce. Expone los productos en formato JSON con vistas basadas en `APIView`. Forma parte de la serie de tareas del proyecto e-commerce de la profesión Full Stack Python de EBAC. Cada repositorio guarda el proyecto como quedó al terminar ese tema; la versión final es [e-commerce-completo](https://github.com/Moremaster123/e-commerce-completo).

## Tecnologías

- Python y Django 6.1
- Django REST Framework 3.18
- SQLite

## Endpoints

| Método | Ruta | Descripción |
|---|---|---|
| GET | `/api/products/` | Lista de productos |
| POST | `/api/products/` | Crea un producto |
| GET | `/api/products/<id>/` | Detalle de un producto |
| PUT | `/api/products/<id>/` | Actualiza un producto |
| DELETE | `/api/products/<id>/` | Elimina un producto |

## Cómo ejecutarlo

```bash
python -m venv venv
venv\Scripts\activate        # en Linux o macOS: source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Abre `http://127.0.0.1:8000/api/products/` en el navegador para usar la interfaz de DRF.

Ejemplo con curl:

```bash
curl http://127.0.0.1:8000/api/products/
```

## Autor

Juan Carlos González Herrera · [LinkedIn](https://www.linkedin.com/in/juan-carlos-desarrollador-web) · [Portafolio](https://moremaster123.github.io)
