from flask import Flask, jsonify, request
from flask_cors import CORS
import subprocess
import yaml

app = Flask(__name__)
CORS(app)

@app.route('/ejecutar_playbook', methods=['POST'])
def ejecutar_playbook():
    try:
        data = request.json
        directorio = data.get('directorio')

        if not directorio:
            return jsonify({'status': 'error', 'message': 'No se proporcionó una ruta de directorio'}), 400

        # Leer el contenido del playbook
        with open('/etc/ansible/crear_ruta.yml', 'r') as file:
            playbook = yaml.safe_load(file)

        # Modificar el playbook con la nueva ruta
        playbook[0]['tasks'][0]['file']['path'] = directorio

        # Guardar el playbook modificado temporalmente
        with open('/etc/ansible/temp_crear_ruta.yml', 'w') as file:
            yaml.dump(playbook, file)

        # Ejecutar el playbook Ansible modificado
        resultado = subprocess.run(
            ['ansible-playbook', '/etc/ansible/temp_crear_ruta.yml'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )

        # Verificar si la ejecución fue exitosa
        if resultado.returncode == 0:
            return jsonify({'status': 'success', 'output': resultado.stdout})
        else:
            return jsonify({'status': 'error', 'output': resultado.stderr}), 500

    except Exception as e:
        app.logger.error(f'Error al ejecutar el playbook: {e}')
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/ejecutar_playbook_recursos', methods=['POST'])
def ejecutar_playbook_recursos():
    try:
        # Ejecutar el playbook recursos.yml
        resultado = subprocess.run(
            ['ansible-playbook', '/etc/ansible/recursos.yml'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )

        # Verificar si la ejecución fue exitosa
        if resultado.returncode == 0:
            return jsonify({'status': 'success', 'output': resultado.stdout})
        else:
            return jsonify({'status': 'error', 'output': resultado.stderr}), 500

    except Exception as e:
        app.logger.error(f'Error al ejecutar el playbook recursos.yml: {e}')
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

