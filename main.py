import openai
import whisper
import yt_dlp
import sys
import os

# Función para descargar un video de YouTube y obtener su nombre de archivo
def descargar_youtube(url):
    titulo = input("Ingresa el nuevo nombre de tu video a analizar: ")

    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{titulo}.%(ext)s',
        'noplaylist': True,
        'download': False
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    titulo = titulo + f".mp4"
    return titulo

# Preguntar al usuario qué tipo de video desea analizar
print("¿Qué tipo de video desea analizar?")
print("1. Video descargado")
print("2. Video de YouTube")
opcion = int(input("Elija una opción: "))

if opcion == 1:
    archivo_video = input("Ingrese el nombre del video: ")
elif opcion == 2:
    url = input("Ingrese la URL de YouTube: ")
    archivo_video = descargar_youtube(url)
else:
    print("Opción no válida")
    sys.exit()

# Obtener el nombre del archivo sin extensión y crear una carpeta con el mismo nombre
nombre_archivo = os.path.splitext(archivo_video)[0]
nombre_carpeta = nombre_archivo

if not os.path.exists(nombre_carpeta):
    os.makedirs(nombre_carpeta)

# Extraer el audio del video y guardarlo como archivo WAV
archivo_audio = f"{nombre_carpeta}/{nombre_archivo}.wav"
os.system(f'ffmpeg -i "{archivo_video}" -vn "{archivo_audio}"')

# Cargar el modelo de reconocimiento de voz
model = whisper.load_model("base")

# Transcribir el audio del video
result = model.transcribe(archivo_audio)

# Guardar la transcripción en un archivo de texto
archivo_texto = f"{nombre_carpeta}/{nombre_archivo}.txt"
with open(archivo_texto, 'w') as f:
    f.write(result["text"])

# Menú de opciones para el contenido a generar
opciones = {
    1: "Crea un resumen de este texto",
    2: "Crea un artículo original basado en este texto",
    3: "Crea un post para redes sociales basado en este texto",
    4: "Crea un correo basado en este texto",
    5: "Introduce un comando personalizado"
}

opcion = int(input("¿Qué desea hacer con la información del video?\n1. Crear un resumen\n2. Crear un artículo original\n3. Crear un post para redes sociales\n4. Crear un correo\n5. Introducir un comando personalizado\nElija una opción: "))

# Establecer la clave de API de OpenAI
openai.api_key = "TU API"

if opcion in opciones:
    if opcion == 5:
        prompt_personalizado = input("Introduzca el comando personalizado: ")
        prompt = prompt_personalizado + f"{result['text']}" 
    else:
        prompt = f"{opciones[opcion]}: '{result['text']}'" 

    # Configurar el modelo de lenguaje
    modelo = "gpt-3.5-turbo"
    mensaje = [
        {"role":"system","content":"Eres un experto en redacción, resúmenes y creación de títulos."},
        {"role":"user","content":prompt}
    ] 

    # Generar la respuesta utilizando la API de OpenAI
    response = openai.ChatCompletion.create(
        model=modelo,
        messages=mensaje,
        temperature=0.8,
        max_tokens=1024
    )

    respuesta = response["choices"][0]["message"]["content"]
else:
    print("Opción inválida.")
    sys.exit()

# Guardar la respuesta generada en un archivo de texto
with open(f"{nombre_carpeta}/{nombre_archivo}_articulo.txt", 'w') as f:
    f.write(respuesta)

# Mostrar el archivo generado y la respuesta por pantalla
print(f"Artículo generado guardado en {nombre_carpeta}/{nombre_archivo}_articulo.txt")
print(respuesta)
