from flask_restful import Resource, reqparse

hoteis = [
    {
        'hotel_id': '1',
        'nome': 'Hotel A',
        'estrelas': '4',
        'diaria': 100.92,
        'cidade': 'Nova York'
    },
    {
        'hotel_id': '2',
        'nome': 'Hotel B',
        'estrelas': '4.1',
        'diaria': 300.123,
        'cidade': 'Rio de Janeiro'
    },
    {
        'hotel_id': '3',
        'nome': 'Hotel C',
        'estrelas': '4.9',
        'diaria': 600.35,
        'cidade': 'São Paulo'
    },
]

class Hoteis(Resource):
    def get(self):
        return hoteis
    
class Hotel(Resource):
    def get(self, hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return {'erro': 'Hotel não encontrado'}, 404 # Not Found

    def post(self, hotel_id):
        argumentos = reqparse.RequestParser()
        argumentos.add_argument('nome')
        argumentos.add_argument('estrelas')
        argumentos.add_argument('diaria')
        argumentos.add_argument('cidade')
        dados = argumentos.parse_args()
        
        novo_hotel = {
            'hotel_id': hotel_id,
            'nome': dados['nome'],
            'estrelas': dados['estrelas'],
            'diaria': dados['diaria'],
            'cidade': dados['cidade'],
        }
        
        hoteis.append(novo_hotel)
    
    def put(self, hotel_id):
        pass
    
    def delete(self, hotel_id):
        pass
    