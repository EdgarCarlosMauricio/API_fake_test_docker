from flask import Flask, jsonify, render_template, request
app = Flask(__name__)

from usuarios import usuarios

@app.route('/usuarios', methods=['GET'])
def getusuarios():
    return jsonify({"usuarios": usuarios, "test":"ok"})


@app.route('/usuarios/<int:id>', methods=['GET'])
def getusuario(id):
    userFound = [usuario for usuario in usuarios if usuario['id']==id]
    return jsonify({"usuario": userFound[0]})


@app.route('/usuarios', methods=['POST'])
def addusuario():
    new_user = {
        "id": request.json['id'],
        "nombre": request.json['nombre'],
        "apellido": request.json['apellido'],
        "permiso": request.json['permiso']
    }
    usuarios.append(new_user)
    return jsonify({"msn": "Usuario Agregado", "usuarios": usuarios})


@app.route('/')
def codesp():
    return render_template("index.html", title = 'Projects')


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
