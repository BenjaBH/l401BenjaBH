from flask import Flask, render_template
import socket

app = Flask(__name__)

HOST = "192.168.1.15"  ## IP del celular
PORT = 12345             ## Puerto del servidor

def leer_sensor():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            data = s.recv(1024).decode().strip()
            print("RECIBIDO:", data)
            ejeX, ejeY = data.split(',')
            ejeX = float(ejeX.replace('X:', ''))
            ejeY = float(ejeY.replace('Y:', ''))
            return ejeX, ejeY
    except Exception as e:
        print("ERROR:", e)
        return 0, 0

def mapear(valor, min_val, max_val, min_out, max_out):
    return int((valor - min_val) / (max_val - min_val) * (max_out - min_out) + min_out)

@app.route('/')
def index():
    ejeY, ejeX = leer_sensor()
    colX = max(0, min(3, mapear(ejeX, -20, 20, 0, 3)))
    filY = max(0, min(3, mapear(ejeY, -20, 20, 3, 0)))
    return render_template('index.html', ejeX=ejeX, ejeY=ejeY, colX=colX, filY=filY)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
