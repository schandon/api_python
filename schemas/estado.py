from pydantic import BaseModel
from typing import List
from model.estado import Estado


class EstadoSchema(BaseModel):
  nome: str = "Rio de Janeiro"
  uf: str = 'RJ'

class EstadoBuscaSchema(BaseModel):
  nome: str = 'Teste'

class ListagemEstadoSchema(BaseModel):
  estados: List[EstadoSchema]
  
def apresenta_estados(estados: list[Estado]):
  result = []
  for estado in estados:
    result.append({ 
      "nome" : estado.nome,
      "uf" : estado.uf,
    })
    
  return { "Estados" : result }

class EstadoViewSchema(BaseModel):
    id : int = 1
    Nome : str = "Rio de Janeiro"
    uf: str = "RJ"

class EstadoDelSchema(BaseModel):
  mesage : str
  nome : str

def apresenta_estado(estado:Estado):
  return {
    "id" : estado.id,
    "Nome" : estado.nome,
    "uf": estado.uf
  }