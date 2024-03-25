from pydantic import BaseModel
from typing import List
from model.estado import Estado


class EstadoSchema(BaseModel):
  nome = str
  uf = str

class EstadoBucasSchema(BaseModel):
  nome = str
  uf = str

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

def apresenta_estado(estado: Estado):
  return {
    "id" : estado.id,
    "Nome" : estado.nome,
    "uf": estado.uf
  }