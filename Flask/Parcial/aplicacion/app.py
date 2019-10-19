from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from aplicacion import config
from aplicacion.form import Form

app = Flask(__name__)
app.config.from_object(config)
Bootstrap(app)
db = SQLAlchemy(app)


@app.route('/')
def inicio():
    from aplicacion.model import Empleado
    Empleados = Empleado.query.all()
    return render_template("inicio.html", Empleados=Empleados)


@app.route('/Add')
def add():
    form = Form()
    return render_template("add.html", form=form)


@app.route('/new', methods=["POST"])
def new():
    from aplicacion.model import Empleado
    form = Form(request.form)
    if form.validate_on_submit():
        emple = Empleado(Id=form.Id.data, Nombres=form.Nombres.data, )
        db.session.add(emple)
        db.session.commit()
    return redirect(url_for("inicio"))


@app.errorhandler(404)
def page_not_found(error):
    return render_template("error.html", error="Página no encontrada..."), 404
