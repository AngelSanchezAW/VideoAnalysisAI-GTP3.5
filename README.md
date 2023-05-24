# VideoAnalysisAI-GTP3.5
![API de OpenAI con Python](https://github.com/AngelSanchezAW/VideoAnalysisAI-GTP3.5/assets/8365143/0e8a98bf-3436-4181-8eee-fe843d494cb9)

Analizar y Generar Contenido a partir de Videos con Python y la API de OpenAI

## Descripción
Este es un proyecto de Python que utiliza diversas herramientas y APIs para analizar y generar contenido a partir de videos. Permite descargar videos de YouTube, extraer su audio, transcribirlo y utilizar la API de OpenAI para generar resúmenes, artículos, posts para redes sociales o correos basados en la transcripción.

## El flujo de trabajo del programa es el siguiente:
1. El usuario elige el tipo de video a analizar: un video descargado o un video de YouTube.
2. Si se selecciona un video descargado, se ingresa el nombre del archivo. Si se selecciona un video de YouTube, se proporciona la URL y se descarga.
3. El programa extrae el audio del video y lo guarda en un archivo WAV.
4. Utilizando el modelo de reconocimiento de voz "base" de la librería Whisper, se transcribe el audio y se guarda en un archivo de texto.
5. Se presenta un menú de opciones para que el usuario elija qué tipo de contenido desea generar.
6. Se utiliza la API de OpenAI para generar el contenido deseado utilizando el texto transcrito y las opciones seleccionadas.
7. El contenido generado se guarda en un archivo de texto.

Este proyecto es ideal para aquellos interesados en analizar y aprovechar la información contenida en videos de forma automatizada, así como generar contenido escrito basado en esa información.

## Requisitos
Antes de ejecutar el programa, asegúrate de tener los siguientes requisitos:
- Python 3.7 o superior.
- Las siguientes librerías de Python instaladas:
- - openai
- - whisper
- - yt_dlp
- - ffmpeg (disponible en el sistema)
- Además, se requiere una clave de API de OpenAI para utilizar su servicio de generación de contenido. Puedes obtener una clave en el sitio web de OpenAI.

## Uso
Sigue estos pasos para utilizar el programa:
- Clona este repositorio o descarga el código fuente.
- Asegúrate de cumplir con los requisitos mencionados anteriormente.
- Ejecuta el archivo main.py desde tu entorno de desarrollo o utilizando el comando python main.py desde la terminal.
- Sigue las instrucciones en pantalla para seleccionar el video a analizar y elegir el tipo de contenido a generar.
- El contenido generado se guardará en archivos de texto en la carpeta correspondiente.

¡Disfruta analizando videos y generando contenido de manera automatizada!
