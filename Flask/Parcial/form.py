from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, IntegerField
from flask_wtf.file import FileField
from wtforms.validators import Required, Email, DataRequired

class Form(FlaskForm):
    Id = StringField('Id:', validators=[Required(), DataRequired()])
    Tipo = StringField('Tipo:', validators=[Required(), DataRequired()])
    Nombres = StringField('Nombres:', validators=[Required(), DataRequired()])
    Apellidos = StringField('Apelldios:', validators=[Required(), DataRequired()])
    Edad = IntegerField('Edad:', validators=[Required(),  DataRequired()])
    Email = StringField('Email:', validators=[Required(), Email(), DataRequired()])
    Profesion = StringField('Profesion:', validators=[Required(), DataRequired()])
    Telefono = StringField('Telefono:', validators=[Required(), DataRequired()])
    Cargo = StringField('Cargo:', validators=[Required(), DataRequired()])
    Salario = FloatField('Salario:', validators=[Required(), DataRequired()])
    Image = FileField('Imagen del empleado: ', validators=[Required(), DataRequired()])
    Sub = SubmitField('Enviar')
