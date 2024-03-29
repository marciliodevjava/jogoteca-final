import os

from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField

from jogoteca import app


class FormularioJogo(FlaskForm):
    nome = StringField('Nome do jogo', [validators.DataRequired(), validators.length(min=2, max=50)])
    categoria = StringField('Categoria', [validators.DataRequired(), validators.length(min=2, max=40)])
    console = StringField('Console', [validators.DataRequired(), validators.length(min=2, max=20)])
    salvar = SubmitField('Salvar')


class FormularioUsuario(FlaskForm):
    nickname = StringField('Login do usuário', [validators.DataRequired(), validators.length(min=2, max=8)])
    senha = StringField('Senha do jogo', [validators.DataRequired(), validators.length(min=2, max=100)])
    login = SubmitField()


def recupera_imagem(id):
    for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']):
        if f'capa{id}' in nome_arquivo:
            return nome_arquivo

    return 'capa_padrao.jpg'


def deleta_arquivo(id):
    arquivo = recupera_imagem(id)
    if arquivo != 'capa_padrao.jpg':
        os.remove(os.path.join(app.config['UPLOAD_PATH']), arquivo)
