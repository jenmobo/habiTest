# API de Consulta de Inmuebles

## Descripción

La API de Consulta de Inmuebles se ha creado con el objetivo de proporcionar a los usuarios la capacidad de consultar inmuebles en diferentes estados (preventa, venta y vendido), y filtrarlos por año de construcción, ciudad y estado. Esta API se ha desarrollado utilizando Python como lenguaje principal y el framework FastAPI.

## Tecnologías Utilizadas

- Python: Lenguaje de programación principal utilizado en el desarrollo de la API.
- FastAPI: Framework de Python utilizado para la construcción rápida y flexible de APIs.

## Ventajas de FastAPI

FastAPI ofrece diversas ventajas en el desarrollo de APIs, entre las cuales destacan:

- Alta velocidad de ejecución.
- Autovalidación y documentación interactiva de los endpoints.
- Generación automática de esquemas de datos.
- Soporte nativo para Python tipo  hinting y Pydantic para la validación de datos.
- Integración sencilla con bibliotecas de terceros.

## Pruebas Unitarias con pytest

En el desarrollo de esta API, se han utilizado pruebas unitarias para garantizar el correcto funcionamiento de los diferentes componentes. Para ello, se ha empleado la biblioteca pytest, que ofrece diversas ventajas en la escritura y ejecución de pruebas unitarias en Python. Algunas de las ventajas de pytest son:

- Sintaxis clara y concisa para escribir pruebas.
- Soporte para fixtures, que facilitan la creación y reutilización de objetos en las pruebas.
- Generación de informes detallados de resultados.
- Integración con otras bibliotecas de pruebas y herramientas de desarrollo.

## Dudas en el Desarrollo

Durante el desarrollo de la API, surgieron algunas dudas que se resolvieron de la siguiente manera:

1. Duda sobre la consulta a la base de datos: Para obtener la información de los inmuebles, se realizó una consulta en la base de datos que involucraba tres tablas diferentes. Se diseñó una consulta SQL que permitía obtener los datos necesarios de manera acoplada.

2. Arquitectura de la API: Se optó por utilizar una arquitectura hexagonal con verticales slicing. Esta arquitectura proporciona flexibilidad a nivel de módulos y responsabilidades separadas, lo cual facilita el mantenimiento y escalabilidad del sistema.

## Servicio de "Me gusta"

Se ha implementado un servicio de "Me gusta" en la API, que permite a los usuarios darle me gusta a un inmueble en particular. A continuación, se presenta un diagrama de entidad-relación que representa el diseño de este servicio:

[![](https://mermaid.ink/img/pako:eNqFUcFqwzAM_RWjc_sDuY3Fh7CtMc56CxQRa53ZYgfZYYS0_754CSxd2KaDQU_PT0_SCI03BBkQ5xbPjG3txBTHSupKXC77vR-F0qWS-rmQlchEDeVBnkp9eiq1rGGmrxjjjKSwLooi_85DZOvO4s4YphA2-L2Nw-1nxbahDS-n0LDtovVurl3Xnv_vf8B2K6owhA_P5kZxNdayisfi4fctzMU_DKT8GIh_Yop9RxyHNW4wksinZ3EEO2iJW7RmutZXjxriK02jQLJjkN-Sj8TDPvpqcA1kkXvaQd8lseW-kL3ge6DrJwSKkwY?type=png)](https://mermaid.live/edit#pako:eNqFUcFqwzAM_RWjc_sDuY3Fh7CtMc56CxQRa53ZYgfZYYS0_754CSxd2KaDQU_PT0_SCI03BBkQ5xbPjG3txBTHSupKXC77vR-F0qWS-rmQlchEDeVBnkp9eiq1rGGmrxjjjKSwLooi_85DZOvO4s4YphA2-L2Nw-1nxbahDS-n0LDtovVurl3Xnv_vf8B2K6owhA_P5kZxNdayisfi4fctzMU_DKT8GIh_Yop9RxyHNW4wksinZ3EEO2iJW7RmutZXjxriK02jQLJjkN-Sj8TDPvpqcA1kkXvaQd8lseW-kL3ge6DrJwSKkwY)

El código SQL necesario para extender el modelo y almacenar la información de los "Me gusta" se encuentra disponible en el archivo `script.sql`. Este código SQL se ha diseñado de manera adecuada para incluir esta información de manera eficiente en la base de datos.

El modelo propuesto con las tablas "Usuarios" y "MeGusta" es una forma simple y eficiente de implementar la funcionalidad de "Me gusta" en un sistema de inmuebles. Aquí hay algunas razones por las cuales este modelo sería adecuado:

* Simplicidad y claridad: El modelo es fácil de entender y mantener. Las tablas "Usuarios" y "MeGusta" tienen una estructura simple y directa, lo que facilita la comprensión de su funcionamiento.

* Relación uno a muchos: La relación entre "Usuarios" e "Inmuebles" se establece mediante la tabla "MeGusta". Esto permite que un usuario pueda dar "Me gusta" a varios inmuebles y que un inmueble pueda recibir "Me gusta" de varios usuarios.

* Registro de información relevante: La tabla "MeGusta" almacena información importante, como el ID del usuario, el ID del inmueble y la fecha en que se dio el "Me gusta". Estos datos son fundamentales para realizar consultas y análisis sobre los "Me gusta" y su historial.

## Contribuciones

Las contribuciones a esta API son bienvenidas. Si encuentras algún error, tienes alguna sugerencia de mejora o deseas añadir nuevas características, no dudes en abrir un pull request.

