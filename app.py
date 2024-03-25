from flask import Flask, request,  render_template, send_from_directory
from sqlalchemy.exc import IntegrityError
from model import Session, Estado

app = Flask(__name__)

@app.get('/')
def hello_world():
  # session = Session()
  return render_template("app.html"), 200
if __name__ == '__main__':
  app.run(debug=True)

@app.get('/estados')
def estados():
  session = Session()
  estado = session.query(Estado).all()
  if not estado:
    error_msg = "Nenhum estado encontrado na base"
    return render_template("error.html", error_code = 404, error_msg = error_msg ), 404
  else:
    return render_template("estado.html", estado=estado), 200                         

@app.post('/add_estado')
def add_estado():
  session = Session()
  estado = Estado(
    id = request.form.get("id"),
    nome = request.form.get("nome"),
    uf = request.form.get("uf")
  )
  try:
    session.add(estado)
    session.commit()
    return "Estado Cadastrado com Sucesso", 200
  except IntegrityError as e:
    error_msg = "Estado de mesmo nome já salvo na base :/"
    return render_template("error.html", error_code=409, error_msg=error_msg), 409
  except Exception as e:
    error_msg = "Não foi possível salvar novo item :/"
    print(str(e))
    return render_template("error.html", error_code=400, error_msg=error_msg), 400
  
if __name__ == '__main__':
  app.run(debug=True)
