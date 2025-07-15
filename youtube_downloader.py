import yt_dlp

def descargar_video(url):
    try:
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
            'merge_output_format': 'mp4',  # Asegúrate de que el video se combine con el audio
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            print(f"Descargando video: {info_dict['title']}")
        print("Descarga completada.")
    except Exception as e:
        print(f"Error al descargar el video: {e}")

def descargar_audio(url):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
            'ignoreerrors': True,
            'no_abort_on_error': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',  # Establecer el formato de salida a MP3
                'preferredquality': '0',  # Calidad del MP3
            }],
            'postprocessor_args': [
                '-ar', '16000'  # Opcional: cambiar la tasa de muestreo
            ],
            'prefer_ffmpeg': True,  # Asegúrate de que FFmpeg se use para la conversión
            'noplaylist': False,
            'extractaudio': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            print(f"Descargando audio: {info_dict['title']}")
        print("Descarga completada.")
    except Exception as e:
        print(f"Error al descargar el audio: {e}")

def main():
    # Solicitar la URL del video
    url = input("Ingresa la URL del video de YouTube: ")

    # Solicitar al usuario que elija una opción
    print("Elige una opción:")
    print("1. Descargar el video")
    print("2. Descargar el audio")

    # Leer la opción del usuario
    opcion = input("Ingresa 1 o 2: ")

    # Verificar la opción y ejecutar la función correspondiente
    if opcion == "1":
        descargar_video(url)
    elif opcion == "2":
        descargar_audio(url)
    else:
        print("Opción no válida. Por favor, ingresa 1 o 2.")

if __name__ == "__main__":
    main()