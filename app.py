from flask import Flask
import socket
import os  # Added for port configuration

app = Flask(__name__)
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

@app.route('/')
def hello_cloud():
    return 'Welcome to Jabri Final Test API Server'
  
@app.route('/host')
def host_name():
    return hostname

@app.route('/ip')
def host_ip():
    return ip_address

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 80))  # Use port 80 by default
    app.run(host='0.0.0.0', port=port)
