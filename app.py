from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Estado
from logger import logger
from schemas import estado
from flask_cors import CORS


info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
estado_tag = Tag(name="Produto", description="Adição, visualização e remoção de Estado à base")


@app.get('/', tags= [home_tag])
def home():
  return redirect('/openapi')


@app.get('/estado')
def estados():
  session = Session()
  estado = session.query(Estado).all()
  if not estado:
    error_msg = "Nenhum estado encontrado na base"
    return render_template("error.html", error_code = 404, error_msg = error_msg ), 404
  else:
    return render_template("estado.html", estado=estado), 200                         



app.post('/estado', tags= [estado_tag], 
         response = {"200" : EstadoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_estado(form: EstadoSchema):
  '''
  '''
  estado = Estado(
    nome = form.nome,
    uf = form.uf)
  logger.debug(f"Adicionando produto de nome: '{estado.nome}'")
  try:
    session = Session()
    
    session.add(estado)

    session.commit()
    
    logger.debug(f"Adicionando estado de nome: '{estado.nome}'")
    
    return estado.apresenta_estado(estado),200
  except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Estado de mesmo nome já salvo na base :/"
        logger.warning(f"Erro ao adicionar Estado '{estado.nome}', {error_msg}")
        return {"mesage": error_msg}, 409

  except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar Estado '{estado.nome}', {error_msg}")
        return {"mesage": error_msg}, 400