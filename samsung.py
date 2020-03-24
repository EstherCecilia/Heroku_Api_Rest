# -*- coding: cp1252 -*-
from flask import Flask, request
from flask_restful import Resource, Api
import json
from models import *
from random import *

app = Flask(__name__)
api = Api(app)



class Sintoma(Resource):
    def get(self, nome):
        sintoma = Sintomas.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome' : sintoma.nome,
                'id' : sintoma.id

                }

        except AttributeError:
            response = {'status': False}
            
        return response
    def put(self, nome):
        sintoma = Sintomas.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            sintoma.nome = dados['nome']

        sintoma.save()

        response = {
            'id' : sintoma.id,
            'nome' : sintoma.nome
            }

        return response
    
    def delete(self, nome):
        sintoma = Sintomas.query.filter_by(nome=nome).first()
        sintoma.delete()

        return {'status': 'sucesso', 'mensagem': 'Registro excluido'}


class Lista_sintomas(Resource):
    def get(self):
        sintoma = Sintomas.query.all()
        response = [{'id':i.id, 'nome':i.nome} for i in sintoma]
        return response
    
    def post(self):
        dados = request.json
        sintoma = Sintomas(nome=dados['nome'])
        sintoma.save()
        response = {
            'id' : sintoma.id,
            'nome' : sintoma.nome
            }

        return response

class Transmicao(Resource):
    def get(self, nome):
        transmicao = Transmicaos.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome' : transmicao.nome,
                'id' : transmicao.id

                }

        except AttributeError:
            response = {'status': False}
            
        return response
    def put(self, nome):
        transmicao = Transmicaos.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            transmicao.nome = dados['nome']

        transmicao.save()

        response = {
            'id' : transmicao.id,
            'nome' : transmicao.nome
            }

        return response
    
    def delete(self, nome):
        transmicao = Transmicaos.query.filter_by(nome=nome).first()
        transmicao.delete()

        return {'status': 'sucesso', 'mensagem': 'Registro excluido'}


class Lista_transmicaos(Resource):
    def get(self):
        transmicao = Transmicaos.query.all()
        response = [{'id':i.id, 'nome':i.nome} for i in transmicao]
        return response
    
    def post(self):
        dados = request.json
        transmicao = Transmicaos(nome=dados['nome'])
        transmicao.save()
        response = {
            'id' : transmicao.id,
            'nome' : transmicao.nome
            }

        return response


class Prevencao(Resource):
    def get(self, nome):
        prevencao = Prevencoes.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome' : prevencao.nome,
                'id' : prevencao.id

                }

        except AttributeError:
            response = {'status': False}
            
        return response
    def put(self, nome):
        prevencao = Prevencoes.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            prevencao.nome = dados['nome']

        prevencao.save()

        response = {
            'id' : prevencao.id,
            'nome' : prevencao.nome
            }

        return response
    
    def delete(self, nome):
        prevencao = Prevencoes.query.filter_by(nome=nome).first()
        prevencao.delete()

        return {'status': 'sucesso', 'mensagem': 'Registro excluido'}


class Lista_prevencoes(Resource):
    def get(self):
        prevencao = Prevencoes.query.all()
        response = [{'id':i.id, 'nome':i.nome} for i in prevencao]
        return response
    
    def post(self):
        dados = request.json
        prevencao = Prevencoes(nome=dados['nome'])
        prevencao.save()
        response = {
            'id' : prevencao.id,
            'nome' : prevencao.nome
            }

        return response

class Sala(Resource):
    def get(self, nome):
        sala = Salas.query.filter_by(nome=nome).first()
        try:
            response = {
                'status': True,
                'nome' : sala.nome,
                'senha' : sala.senha,
                'id' : sala.id

                }

        except AttributeError:
            response = {'status': False}
            
        return response
    
    def put(self, nome):
        sala = Salas.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            sala.nome = dados['nome']
            
        if 'senha' in dados:
            sala.senha = dados['senha']

        sala.save()

        response = {
                'nome' : sala.nome,
                'senha' : sala.senha,
                'id' : sala.id

                }

        return response
    
    def delete(self, nome):
        sala = Salas.query.filter_by(nome=nome).first()
        sala.delete()

        return {'status': 'sucesso', 'mensagem': 'Registro excluido'}


class Lista_salas(Resource):
    def get(self):
        sala = Salas.query.all()
        response = [{'id':i.id, 'nome':i.nome, 'senha':i.senha} for i in sala]
        return response
    
    def post(self):
        dados = request.json
        salaCheck = Salas.query.filter_by(nome=dados['nome']).first()
        
        try:
            salaCheck.nome = dados['nome']
            response = {
                'status':False
                

            }

        except AttributeError:
            sala = Salas(nome=dados['nome'], senha=dados['senha'])
            sala.save()
            response = {
                    'status':True,
                    'nome' : sala.nome,
                    'senha' : sala.senha,
                    'id' : sala.id

                }

        return response



class Doenca(Resource):
    def get(self, nome):
        doenca = Doencas.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome' : doenca.nome,
                'tipo' : doenca.tipo,
                'agente' : doenca.agente,
                'id' : doenca.id

                }

        except AttributeError:
            response = {'status': 'Error', 'mensagem':'Nome n�o encontrado'}
            
        return response
    
    def put(self, nome):
        doenca = Doencas.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            doenca.nome = dados['nome']
            
        doenca.save()

        response = {
                'nome' : doenca.nome,
                'tipo' : doenca.tipo,
                'agente' : doenca.agente,
                'id' : doenca.id

                }

        return response
    
    def delete(self, nome):
        doenca = Doencas.query.filter_by(nome=nome).first()
        doenca.delete()

        return {'status': 'sucesso', 'mensagem': 'Registro excluido'}



class Lista_doencas(Resource):
    def get(self):
        doencas = Doencas.query.all()
        response = [{'id':i.id, 'nome':i.nome, 'tipo':i.tipo, 'agente':i.agente, 'sintomas':[{'nome':s.nome} for s in i.sintomas], 'transmicao':[{'nome':s.nome} for s in i.transmicao], 'prevencao':[{'nome':s.nome} for s in i.prevencao]} for i in doencas]
        return response
    

    def post(self):
        dados = request.json
        prevencao = Prevencoes.query.filter_by(nome=dados['prevencao']).first()
        doenca = Doencas(nome=dados['nome'], agente=dados['agente'], tipo=dados['tipo'])
        doenca.save()
        return "Doen�a inserida com sucesso!"
        


class Lista_sessoes(Resource):
    def get(self):
        doencas = Doencas.query.all()
        dados = request.json
        shuffle(doencas)
        doenca = doencas[:dados['doencas']]

        salaCheck = Salas.query.filter_by(nome=dados['nome']).first()
        
        responSala = {'id':salaCheck.id, 'nome':salaCheck.nome, 'senha':salaCheck.senha}
        responDoenca = [{'id':i.id, 'nome':i.nome, 'tipo':i.tipo, 'agente':i.agente,'sintomas':[{'nome':s.nome} for s in i.sintomas], 'transmicao':[{'nome':s.nome} for s in i.transmicao], 'prevencao':[{'nome':s.nome} for s in i.prevencao] } for i in doenca]
        items = randrange(1000, 99999)
        item = randrange(1000, 99999)
        id = items + item - salaCheck.id

        if salaCheck.senha == dados['senha']:
                response = {'status':True, 'id':id,'sala':responSala,'doencas':responDoenca}
        else:
                response = {'status':False}                
        return response


class Jogador(Resource):

    def delete(self, nome):
        jogador = Ranking.query.filter_by(nome=nome).first()
        jogador.delete()

        return {'status': 'sucesso', 'mensagem': 'Registro excluido'}



class Lista_jogadores(Resource):
    def get(self):
        dados = request.json
        jogador = Ranking.query.filter_by(id_sessao=dados['id_sessao']).filter_by(adivinhador=True).all()
        
        jogador_ordenado = sorted(jogador, key = Ranking.get_pontuacao, reverse=True)
        

        responseAdivinhador = [{'nome':i.nome, 'pontuacao':i.pontuacao} for i in jogador_ordenado]

        jogadorDica = Ranking.query.filter_by(id_sessao=dados['id_sessao']).filter_by(adivinhador=False).first()

        responseDicas = {'nome':jogadorDica.nome, 'pontuacao':jogadorDica.pontuacao}

        response = {'darDica':responseDicas, 'adivinhador':responseAdivinhador}
        return response


    def put(self):
        dados = request.json
        pontuac = Ranking.query.filter_by(nome=dados['nome']).filter_by(id_sessao=dados['id_sessao']).filter_by(adivinhador=True).first()
        adivinhador =Ranking.query.filter_by(id_sessao=dados['id_sessao']).filter_by(adivinhador=False).first()


        
        try:
            rodada = len(Ranking.query.filter_by(id_sessao=dados['id_sessao']).filter_by(rodada=dados['rodada']).all())
            pontuac.rodada = dados['rodada']
            pontuac.ordem = rodada + 1
            ponti = (1/(pontuac.ordem))*10
            ponto = pontuac.pontuacao + ponti
            pontuac.pontuacao = ponto
            pontuac.save()


            adivinhador.pontuacao = ponti*0.75
            adivinhador.save()

            response = {
                'status':True,
                'nome' : pontuac.nome,
                'id_sessao' : pontuac.id_sessao,
                'ordem': pontuac.ordem,
                'id' : pontuac.id,
                'pontuacao': pontuac.pontuacao
                

            }

            

        except AttributeError:
            response = {
                'status':False

            }

        x = len(Ranking.query.filter_by(rodada=dados['rodada']).filter_by(id_sessao=dados['id_sessao']).all())
        y = len(Ranking.query.filter_by(id_sessao=dados['id_sessao']).all()) - 1
        if y == x:
            adivinhador.adivinhador = True
            adivinhador.save()
            adivinhador.ordem = 300
            adivinhador.save()
            jogadorVelho = Ranking.query.filter_by(id_sessao=dados['id_sessao']).filter_by(ordem=1).first()
            jogadorVelho.adivinhador = False
            jogadorVelho.save()

        
        

        return response

        
    def post(self):
        dados = request.json
        pontuac = Ranking.query.filter_by(id_sessao=dados['id_sessao']).filter_by(nome=dados['nome']).first()

        
        try:
            pontuac.nome = dados['nome']
            response = {
                'status':False
                

            }

        except AttributeError:
            ponto = 0
            rodada = 0
            ordem = len(Ranking.query.filter_by(id_sessao=dados['id_sessao']).all()) + 1
            if ordem == 1 :
                adivinhador = False
            else:
                adivinhador = True
            jogador = Ranking(nome=dados['nome'],  rodada = rodada, id_sessao=dados['id_sessao'], pontuacao=ponto, ordem=ordem, adivinhador=adivinhador)
            jogador.save()

            response = {
                'status':True,
                'nome' : jogador.nome,
                'id_sessao' : jogador.id_sessao,
                'id' : jogador.id,
                'pontuacao': jogador.pontuacao,
                'adivinhador': jogador.adivinhador
                

            }

        
        

        return response


class Encerra_jogadores(Resource):
    def get(self):
        Ranking.finaliza()
        return "Sess�o encerrada"



class Home(Resource):
    def get(self):
        return "Bem vindo, Adiciona um endpoint para melhor navegar na api"


    

api.add_resource(Home, '/')

api.add_resource(Jogador, '/jogador/<string:nome>')
api.add_resource(Lista_jogadores, '/jogador')
api.add_resource(Encerra_jogadores, '/jogador/encerra')

api.add_resource(Sintoma, '/sintoma/<string:nome>')
api.add_resource(Lista_sintomas, '/sintoma')

api.add_resource(Transmicao, '/transmicao/<string:nome>')
api.add_resource(Lista_transmicaos, '/transmicao')

api.add_resource(Prevencao, '/prevencao/<string:nome>')
api.add_resource(Lista_prevencoes, '/prevencao')

api.add_resource(Sala, '/sala/<string:nome>')
api.add_resource(Lista_salas, '/sala')

api.add_resource(Doenca, '/doenca/<string:nome>')
api.add_resource(Lista_doencas, '/doenca')

api.add_resource(Lista_sessoes, '/sessao')

if __name__ == '__main__':
    app.run(debug=True)

    
#debug=true
