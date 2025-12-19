# Talento-tech


## Propósito del proyecto Y Las tecnologías utilizadas

El propósito de este proyecto es implementar **AUTOMATIZACIÓN DE PRUEBAS PYTHON** utilizando **PYTEST**, **SELENIUM** y **WEBDRIVER**, generando **REPORTES DE RESULTADOS EN FORMATO HTML**.  
Este framework está orientado a **VALIDAR DE FORMA AUTOMÁTICA Y REPETIBLE** el comportamiento de la aplicación, facilitando su mantenimiento y la entrega de pruebas al equipo de desarrollo y al cliente.


**Estructura del proyecto**
El proyecto se organiza de la siguiente forma:


**assets/**
Contiene recursos auxiliares usados en las pruebas (imágenes, datos, archivos, etc.).


**pages/**
Implementa el patrón Page Object, encapsulando la lógica de interacción con las distintas páginas de la aplicación web (elementos, acciones, validaciones).


**reportess/**
Carpeta donde se generan los reportes HTML de ejecución de las pruebas automatizadas.


**test/**
Contiene los casos de prueba implementados con pytest, organizados según las funcionalidades a validar.


**conftest.py**
Archivo de configuración de pytest donde se definen fixtures comunes, configuración del WebDriver y parámetros compartidos entre pruebas.


**run_test.py**
Script principal para ejecutar la suite de pruebas, integrando pytest y la generación de reportes.


**__pycache__/, .pytest_cache/**
Directorios generados automáticamente por Python y pytest para caché de compilación y ejecución de pruebas (no contienen código fuente manual).

**README.md**
Documentación principal del proyecto, con descripción, propósito, instalación y uso.



**instalar las dependencias**

PYTHON:

Descargar Python desde la página oficial:
https://www.python.org/downloads/

Verificar la instalación en una terminal o consola:

python --version


----------------------------------------------

PYTEST:

Para instalar Pytest y el plugin para generar reportes HTML usando pip:

pip install pytest pytest-html

---------------------------------------------

Reporte HTML nativo:

pytest --html=report.html --self-contained-html

---------------------------------------------

SELENIUM: 

pip install selenium

Para verificar que se haya instalado

pip show selenium

---------------------------------------------

WebDriver:

Cada navegador necesita su propio "conductor" como en mi caso es Chrome use este

https://googlechromelabs.github.io/chrome-for-testing/

Para verificar la instalación 

chromedriver --version


------------------------------------------------
FAKER:

pip install faker


-------------------------------------------------


**Como ejecutar las pruebas?**
Ejecutar todas las pruebas con el script del proyecto
Desde la raíz del proyecto:

python run_test.py


Este script se encarga de:

#Lanzar pytest
#Ejecutar los tests ubicados en la carpeta test/
#Generar el reporte HTML dentro de la carpeta reports/



Alternativa Ejecutar pytest directamente :

pytest -v test/ --html=reports/reporte.html --self-contained-html

Ver reporte de resultados


Una vez finalizada la ejecución, abrir el archivo generado en reports/ (por ejemplo, reporte.html) con un navegador web para ver el detalle de las pruebas.


**¿Cómo interpretar los reportes generados?**

Interpretación de los reportes HTML
Después de ejecutar las pruebas, se genera un reporte HTML en la carpeta reports/ (por ejemplo: reports/reporte.html).

#Para visualizarlo:


Abrir el archivo HTML con un navegador web (Chrome, Edge, Firefox, etc.).

Revisar las siguientes secciones principales:

Resumen general (Summary)  


#Muestra el número total de pruebas ejecutadas.  

Indica cuántas pruebas pasaron (Passed), fallaron (Failed) o quedaron omitidas (Skipped).  

Permite ver rápidamente si la ejecución fue exitosa o si hay errores que revisar.


#Listado de casos de prueba (Test Results / Details)
Para cada caso de prueba se muestra:


#Nombre del test: normalmente el nombre de la función de prueba (test_nombre_funcionalidad).

#Estado:
Passed: la prueba se ejecutó correctamente.

Failed: la prueba falló; requiere análisis.

Skipped: la prueba se omitió por alguna condición o marca.


#Duración: tiempo que tardó en ejecutarse la prueba.

Mensaje de error / traza (si falló):  
Indica la causa del fallo, la línea de código donde ocurrió y el assert que no se cumplió.

#Esta información sirve para identificar rápidamente el problema (en la aplicación o en el propio test).



Logs, capturas y adjuntos (si están configurados)
Si el framework está configurado para adjuntar logs o capturas de pantalla:


En el reporte, junto a cada prueba, pueden aparecer enlaces a capturas (screenshots) tomadas al fallar la prueba.

También pueden mostrarse logs de la ejecución, útiles para depurar.



Cómo usar el reporte en la práctica
Si el reporte muestra todas las pruebas en verde (Passed), la ejecución fue exitosa para ese conjunto de casos.

Si hay pruebas en rojo (Failed):
Abrir el detalle de esa prueba en el reporte.

Leer el mensaje de error y la traza (stack trace).

Ver (si aplica) las capturas de pantalla asociadas.

Con esa información, decidir si:
El fallo está en la aplicación (bug funcional).

El fallo está en el test (selector incorrecto, aserción mal planteada, timing, etc.).
