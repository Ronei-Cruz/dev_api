from models import Pessoas


def insere_pessoas():
    pessoa = Pessoas(nome='Ronei', idade=33)
    print(pessoa)
    pessoa.save()

def consulta_pessoas():
    pessoa = Pessoas.query.all()
    print(pessoa)
    pessoa = Pessoas.query.filter_by(nome='Ronei').first()
    print(pessoa.idade)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome="Ronei").first()
    pessoa.idade = 35
    pessoa.save()

def exluir_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Ronei').first()
    pessoa.delete()

if __name__ == '__main__':
    insere_pessoas()
    consulta_pessoas()
    altera_pessoa()
    exluir_pessoa()