# Prueba técnica Macropay

El siguiente repositorio es el resultado de la prueba técnica de Macropay. El contexto de esta gira alrededor de un directorio de contactos como recurso del servidor y el que se busca exponer a través de una REST API. En la prueba se solicita la creación de 3 EP para acceder al recurso de contactos.

## Implementation

La implementación de la API se realizó utilizando Flask. Esta elección se hizo debido a la agilidad que brinda Flask para crear aplicaciones simples y confiables. A pesar de poder escalar bien a proyectos más grandes, en este caso recomendaría migrar a marcos más robustos como Django, Expressjs, entre otros.

### Cómo levantar el proyecto en local

La estructura del proyecto se muestra a continuación:

```
.
├── app
│   ├── contacts
│   │   └── routes.py
│   ├── database
│   │   ├── database.py
│   │   └── fakedatabase.json
│   └── __init__.py
│   ├── conftest.py
├── tests
│   ├── functional
│   │   └── test_get_contacts.py
│   └── unit
├── config.py
├── Procfile
├── README.md
├── requirements.txt
└── wsgi.py
```

### Servidor

Los paquetes utilizados para el proyecto se encuentran en el archivo `requirements.txt` que se puede instalar con el siguiente comando:

    pip install -r ./requirements.txt

Una vez instaladas las dependencias, el proyecto se puede levantar con el siguiente comando:

    flask run

### Testing

La estructura de la carpeta test se muestra a continuación

```
.
├── functional
│ └── test_get_contacts.py
└── unit
├── conftest.py
```

Debido al tiempo solo se implementaron 7 test funcionales relativamente sencillos que verifican que los EP respondan de manera correcta a los recursos solicitados.

Los test pueden ser ejecutados con el siguiente comando:

    python -m pytest

## Notas

La prueba me permitió refrescar varios conceptos que no uso con tanta frecuencia, lo que a su vez hizo que la pudiera disfrutar. De igual forma, se buscó realizar un poco más de lo pedido, con el fin de aprovechar el tiempo sobrante, sin embargo, irónicamente, al final el tiempo fue una limitante.

### DynamoDB table

A pesar de ser una aplicación sencilla, se encontró con el problema de manejar la _"base de datos"_. Por esta razón, debido a la sencillez de los datos, se optó por migrar los datos a una tabla de DynamoDB con el siguiente script mostrado a continuación. Para esto se generó un usuario IAM con políticas que le permiten acceder a la tabla creada y realizar acciones put.

```python
import json
import boto3

...

def main():
    client = boto3.client('dynamodb', region_name=region_name)
    contacts = get_all_contacts("./fakedatabase.json")
    for contact in contacts:
        contact = format_contact_to_ddb(contact)
        add_item_to_table(client, contact)


if __name__ == '__main__':
    main()
```

Se logró micrar el fakedatabase.json a una tabla de DynamoDB, ~~sin embargo, debido al tiempo, no se logró implementar este recurso con el servidor.~~. Y se logró implementar en el objeto Directory encargado de intermediar con DynamoDB (en la rama _mejoras_). Para poder utilizar estas caracteristicas de forma local, puede solicitar unas credeciales IAM con los permisos requeridos. De igual forma, se buscará asignar un rol a la instancia de EC2 con estos permisos, y utilizar el código actualizado.

### Despliegue

Se realizó un despliegue sencillo en una instancia de EC2, por lo que es posible llevar a cabo el análisis del proyecto sin tener que levantarlo como es mencionado en la sección de #Servidor. La dirección IP del servidor, fue mandada por correo a los evaluadores.

Una limitación de este paso, es que a pesar de que en local funcionan todos los EP, en el servidor corriendo en EC2, el método DELETE en el recurso contacts/<contact_id> termina en un error 500, sin embargo, por tiempo no me fue posible diagnosticar qué está generando el error.
