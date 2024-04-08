from pydantic import BaseModel
from typing import List
from model.estado import estado



class EstadoSchema(BaseModel):
  nome: str = "Rio de Janeiro"
  uf: str = 'RJ'

class EstadoBuscaSchema(BaseModel):
  nome: str = 'Teste'

class ListagemEstadosSchema(BaseModel):
  estados: List[EstadoSchema]
  
def apresenta_estado(estados: list[estado]):
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

def apresenta_estado(estado:estado):
  return {
    "id" : estado.id,
    "Nome" : estado.nome,
    "uf": estado.uf
  }