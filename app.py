from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Estado
from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
estado_tag = Tag(name="Estado", description="Adição, visualização e remoção de estado à base")



@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/estado', tags=[estado_tag],
          responses={"200": EstadoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_produto(form: EstadoSchema):
    """Adiciona um novo Estado à base de dados

    Retorna uma representação dos estado.
    """
    estado = Estado(
        nome=form.nome,
        quantidade=form.quantidade,
        valor=form.valor)
    logger.debug(f"Adicionando estado de nome: '{estado.nome}'")
    try:
        # criando conexão com a base
        session = Session()
        # adicionando produto
        session.add(estado)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado estado de nome: '{estado.nome}'")
        return apresenta_estado(estado), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Produto de mesmo nome já salvo na base :/"
        logger.warning(f"Erro ao adicionar produto '{estado.nome}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar produto '{estado.nome}', {error_msg}")
        return {"mesage": error_msg}, 400


@app.get('/estados', tags=[estado_tag],
         responses={"200": ListagemEstadosSchema, "404": ErrorSchema})
def get_estados():
    """Faz a busca por todos os Produto cadastrados

    Retorna uma representação da listagem de produtos.
    """
    logger.debug(f"Coletando estados ")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    estados = session.query(Estado).all()

    if not estados:
        # se não há produtos cadastrados
        return {"estados": []}, 200
    else:
        logger.debug(f"%d estados econtrados" % len(estados))
        # retorna a representação de produto
        print(estados)
        return apresenta_estados(estados), 200


@app.get('/estado', tags=[estado_tag],
         responses={"200": EstadoViewSchema, "404": ErrorSchema})
def get_produto(query: EstadoBuscaSchema):
    """Faz a busca por um Estados a partir do id do estado

    Retorna uma representação dos estados.
    """
    estado_id = query.id
    logger.debug(f"Coletando dados sobre produto #{estado_id}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    estado = session.query(Estado).filter(Estado.id == estado_id).first()

    if not estado:
        # se o produto não foi encontrado
        error_msg = "Produto não encontrado na base :/"
        logger.warning(f"Erro ao buscar produto '{estado_id}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"estado econtrado: '{estado.nome}'")
        # retorna a representação de estado
        return apresenta_estado(estado), 200


@app.delete('/estado', tags=[estado_tag],
            responses={"200": EstadoDelSchema, "404": ErrorSchema})
def del_estado(query: EstadoBuscaSchema):
    """Deleta um Estados a partir do nome de estado informado

    Retorna uma mensagem de confirmação da remoção.
    """
    estado_nome = unquote(unquote(query.nome))
    print(estado_nome)
    logger.debug(f"Deletando dados sobre estado #{estado_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Estado).filter(Estado.nome == estado_nome).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado produto #{estado_nome}")
        return {"mesage": "estado removido", "id": estado_nome}
    else:
        # se o estado não foi encontrado
        error_msg = "estado não encontrado na base :/"
        logger.warning(f"Erro ao deletar estado #'{estado_nome}', {error_msg}")
        return {"mesage": error_msg}, 404