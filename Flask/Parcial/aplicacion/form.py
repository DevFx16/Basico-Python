from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, IntegerField
from flask_wtf.file import FileField
from wtforms.validators import Required, Email

class Form(FlaskForm):
    Id = StringField('Id:', validators=[Required(),])
    Tipo = StringField('Tipo:', validators=[Required()])
    Nombres = StringField('Nombres:', validators=[Required()])
    Apellidos = StringField('Apelldios:', validators=[Required()])
    Edad = IntegerField('Edad:', validators=[Required(), min])
    Email = StringField('Email:', validators=[Required(), Email()])
    Profesion = StringField('Profesion:', validators=[Required()])
    Telefono = StringField('Telefono:', validators=[Required()])
    Cargo = StringField('Cargo:', validators=[Required()])
    Salario = FloatField('Salario:', validators=[Required()])
    Image = FileField('Imagen del empleado: ', validators=[Required()])
    Sub = SubmitField('Enviar')
