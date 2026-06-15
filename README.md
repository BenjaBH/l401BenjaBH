# Visualización de Datos X-Y con Flask
### Benjamín Badilla — DCSH01, INACAP

## Descripción
Aplicación web desarrollada con Flask que recibe datos de los ejes X e Y desde una aplicación móvil via TCP, y los representa visualmente en 3 vistas diferentes en el navegador.

## ¿Cómo funciona?
La app móvil actúa como servidor TCP enviando los valores del acelerómetro del celular en formato `X:valor,Y:valor`. Flask se conecta, lee los datos y los representa en la vista seleccionada. La página se actualiza automáticamente cada 2 segundos.

## Vistas disponibles
- **Matriz 4x4** — La celda activa se ilumina en rojo según la posición del dispositivo
- **Texto** — Los valores X e Y se muestran en formato numérico grande en tiempo real
- **Barras** — Los valores X e Y se representan como barras horizontales según su magnitud

## Cambios realizados al repositorio base
- Se agregó título de la actividad y nombre del autor en el HTML
- Se añadió párrafo explicativo sobre el funcionamiento del sistema
- Se cambió la visualización de 4 cuadrantes (2x2) a una matriz de 4x4
- Se agregó la función `mapear()` en `app.py` para convertir los valores del acelerómetro a índices de la matriz
- Se aplicaron colores personalizados (rojo) para la celda activa y estructura visual
- Se agregaron 2 vistas adicionales (texto y barras) con navegación entre las 3 páginas

## Tecnologías usadas
- Python + Flask
- HTML + CSS + Jinja2
- Comunicación TCP con app móvil (APK)

## Cómo ejecutar
1. Conectar el celular y el PC a la misma red WiFi
2. Abrir la app móvil y activar el servidor TCP
3. Ejecutar `python3 app.py`
4. Abrir `http://localhost:5000` en el navegador
