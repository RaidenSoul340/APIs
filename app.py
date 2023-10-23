from flask import Flask, jsonify, request

app = Flask(__name__)

pecas = [
    {
        'id': 1,
        'Peças': '',
        '': ''
    },
    {
        'id': 2,
        'Peças': '',
        '': ''
    },
    {
        'id': 3,
        'Peças': '',
        '': ''
    },
]

# Consultar(todos)
@app.route('/pecas',methods=['GET'])
def obter_pecas():
    return jsonify(pecas)

# Consultar(id)
@app.route('/pecas/<int:id>',methods=['GET'])
def obter_pecas_por_id(id):
    for peca in pecas:
        if peca.get('id') == id:
            return jsonify(peca)
# Editar
@app.route('/pecas/<int:id>',methods=['PUT'])
def editar_peca_por_id(id):
    peca_alterado = request.get_json()
    for indice,peca in enumerate(pecas):
        if pecas.get('id') == id:
            pecas[indice].update(peca_alterado)
            return jsonify(pecas[indice])
# Criar
@app.route('/pecas',methods=['POST'])
def incluir_novo_pecas():
    novo_peca = request.get_json()
    pecas.append(novo_peca)
    
    return jsonify(pecas)
# Excluir
@app.route('/pecas/<int:id>',methods=['DELETE'])
def excluir_peca(id):
    for indice, peca in enumerate(pecas):
        if peca.get('id') == id:
            del pecas[indice]

    return jsonify(pecas)

app.run(port=5000,host='localhost',debug=True)