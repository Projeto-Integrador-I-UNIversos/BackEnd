from flask import Blueprint, request, jsonify
from models.chat import Chat
from models import mysql

chat_bp = Blueprint('chat', __name__)
chat_model = Chat(mysql)

@chat_bp.route('/chats', methods=['POST'])
def criar_chat():
    dados = request.json
    idChat = chat_model.criar_chat(dados)
    return jsonify({"idChat": idChat}), 201

@chat_bp.route('/chats/<int:idChat>', methods=['GET'])
def buscar_chat(idChat):
    chat = chat_model.buscar_chat_por_id(idChat)
    return jsonify(chat), 200
