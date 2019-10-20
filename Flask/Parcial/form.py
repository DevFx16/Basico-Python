from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, IntegerField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.widgets.html5 import NumberInput, EmailInput
from wtforms.validators import Email, DataRequired
import os
import app


class Form(FlaskForm):
    Id = StringField('Identificación:', validators=[DataRequired()])
    Tipo = StringField('Tipo:', validators=[DataRequired()])
    Nombres = StringField('Nombres:', validators=[DataRequired()])
    Apellidos = StringField('Apelldios:', validators=[
                            DataRequired()])
    Edad = IntegerField('Edad:', validators=[
                        DataRequired()], widget=NumberInput(min=18, max=80))
    Email = StringField('Email:', validators=[
                        Email(), DataRequired()], widget=EmailInput())
    Profesion = StringField('Profesion:', validators=[
                            DataRequired()])
    Telefono = StringField('Telefono:', validators=[
                           DataRequired()])
    Cargo = StringField('Cargo:', validators=[DataRequired()])
    Salario = FloatField('Salario:', validators=[
                         DataRequired()], widget=NumberInput())
    Image = FileField('Imagen del empleado: ')
    Sub = SubmitField('Enviar')


class FileUpload():

    def allowed_files(self, file_name):
        allowed_extensions = ['png', 'jpg', 'jpeg', 'gif']
        return '.' in file_name and file_name.rsplit('.', 1)[1].lower() in allowed_extensions

    def upload(self, file, path):
        file_name = file.filename
        if file_name == '':
            return 'NULL'

        elif file_name and self.allowed_files(file_name):
            file.save(os.path.join(os.path.dirname(os.path.realpath(__file__)), app.app.config["UPLOAD_FOLDER"], path+'.'+file_name.rsplit('.', 1)[1].lower()))

        return os.path.join(app.app.config["UPLOAD_FOLDER"], path+'.'+file_name.rsplit('.', 1)[1].lower())
