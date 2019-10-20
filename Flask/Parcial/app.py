from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import config
from form import Form
import os

app = Flask(__name__)
app.config.from_object(config)
Bootstrap(app)
db = SQLAlchemy(app)


@app.route('/')
def inicio():
    from model import Empleado
    Empleados = Empleado.query.all()
    return render_template("templates/inicio.html", Empleados=Empleados)


@app.route('/Add')
def add():
    form = Form()
    return render_template("add.html", form=form)


@app.route('/new', methods=["POST"])
def new():
    from model import Empleado
    form = Form(request.form)
    if form.validate_on_submit():
        emple = Empleado(Id=form.Id.data, Nombres=form.Nombres.data,
                         Apellidos=form.Apellidos.data, Edad=form.Edad.data, Email=form.Email.data, Tipo=form.Tipo.data, Profesion=form.Profesion.data, Cargo=form.Cargo.data, Salario=form.Salario.data, Telefono=form.Telefono.data)
        db.session.add(emple)
        db.session.commit()
    return redirect(url_for("inicio"))


@app.errorhandler(404)
def page_not_found(error):
    return render_template("error.html", error="Página no encontrada..."), 404

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port, debug=True)