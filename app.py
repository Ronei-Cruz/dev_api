import json
from flask import Flask, jsonify, request

app = Flask(__name__)

desenvolvedores = [
    {'nome':'Ronei',
    'habilidades': ['Python', 'Flask']},
    {'nome':'Diego',
    'habilidades': ['CSharp', 'Dotnet']}
]

@app.route('/<int:id>')
def pessoas(id):
    soma = id + 1
    return jsonify ({'id':id, 'nome': 'Ronei', 'profissao': 'Estudante'})

@app.route('/soma/<int:valor1>/<int:valor2>')
def soma(valor1, valor2):
    return jsonify({'soma':valor1 + valor2})

@app.route('/soma', methods=['POST'])
def soma():
    dados = json.loads(request.data)
    total = sum(dados['valores'])
    print(dados)
    return jsonify({'soma': total})

# Devolve, Deleta e Altera um desenvolvedor por ID.
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = f'Desenvolvedor de ID {id} não existe'
            response = {'status':'Erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desonhecido, procure o Administrador da API'
            response = {'status':'Erro', 'mensagem':mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status':'SUCESSO', 'mensagem':'Dados excluidos'})

#Lista e registra um novo desenvolvedor
@app.route('/dev/', methods=['POST', 'GET'])
def lista_dev():
    if request.method == 'POST':
        dados = json.loads(request.data)
        desenvolvedores.append(dados)
        return jsonify({'status':'SUCESSO', 'mensagem':'Registro inserido'})
    elif request.method == 'GET':
        return jsonify(desenvolvedores)

if __name__ == '__main__':
    app.run(debug=True)