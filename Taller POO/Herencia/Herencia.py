class Vehiculo():
  def __init__(self, fmasa):
    self.masa = fmasa
  pass

class VehiculoTerrestre(Vehiculo):
  def __init__(self, frueda, fmasa):
    Vehiculo.__init__(self, fmasa)
    self.rueda = frueda 
  pass

  
class VehiculoAereo(Vehiculo):
  def __init__(self, faleron, fmasa):
    Vehiculo.__init__(self, fmasa)
    self.aleron = faleron
  pass


class Avion(VehiculoAereo):
  def __init__(self,ftipo_de_motor ,faleron):
    VehiculoAereo.__init__(self, faleron)
    self.tipo_de_motor = ftipo_de_motor
  pass


class Helicoptero(VehiculoAereo):
  def __init__(self,felice ,faleron):
    VehiculoAereo.__init__(self, faleron)
    self.elice = felice
  pass


class Dron(VehiculoAereo):
  def __init__(self,fcontrol ,faleron):
    VehiculoAereo.__init__(self, faleron)
    self.control = fcontrol
  pass


class Motocicleta(VehiculoTerrestre):
  def __init__(self,fcachos ,frueda):
    VehiculoTerrestre.__init__(self, frueda)
    self.cachos = fcachos
  pass


class Auto(VehiculoTerrestre):
  def __init__(self,fvolante ,frueda):
    VehiculoTerrestre.__init__(self, frueda)
    self.volante = fvolante
  pass


class Bicicleta(VehiculoTerrestre):
  def __init__(self,fpedal ,frueda):
    VehiculoTerrestre.__init__(self, frueda)
    self.pedal = fpedal
  pass