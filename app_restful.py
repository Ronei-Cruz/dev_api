import json
from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {'id':0,
    'nome':'Ronei',
    'habilidades': ['Python', 'Flask']},
    {'id':1,
    'nome':'Diego',
    'habilidades': ['CSharp', 'Dotnet']}
]

class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = f'Desenvolvedor de ID {id} não existe'
            response = {'status':'Erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desonhecido, procure o Administrador da API'
            response = {'status':'Erro', 'mensagem':mensagem}
        return (response)

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return (dados)
        
    def delete(self, id):
        desenvolvedores.pop(id)
        return ({'status':'SUCESSO', 'mensagem':'Dados excluidos'})

class List_dev(Resource):
    def get(self):
        return (desenvolvedores)
    
    def post(self):
        dados = json.loads(request.data)
        desenvolvedores.append(dados)
        return ({'status':'SUCESSO', 'mensagem':'Registro inserido'})


api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(List_dev, '/dev/')

if __name__ == '__main__':
    app.run(debug=True)
