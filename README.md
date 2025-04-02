# ¡Adivina mi nombre!

Una aplicación de chat interactiva desarrollada con Streamlit y modelos de lenguaje generativo.

## Descripción

Esta aplicación permite a los usuarios mantener una conversación con un asistente virtual que utiliza modelos de lenguaje generativo como Gemini. El objetivo es que el usuario adivine el nombre del asistente a través de la interacción.

## Características

- Interfaz de chat amigable
- Historial de conversación persistente
- Soporte para modelos de lenguaje Gemini
- Opción para limpiar el historial de chat

## Requisitos

- Python 3.11 o superior
- Dependencias listadas en el archivo `uv.lock`

## Instalación

1. Clona este repositorio
2. Instala las dependencias:
   ```bash
   uv sync
   ```
3. Configura tus claves API en Streamlit:
   - GEMINI_API_KEY

## Ejecución

Para ejecutar la aplicación:

```bash
streamlit run main.py
```

La aplicación se abrirá en tu navegador web predeterminado.

## Uso

Simplemente escribe tus mensajes en el campo de entrada de texto y presiona Enter para enviar. Puedes utilizar el botón "Limpiar" en la barra lateral para reiniciar la conversación.
