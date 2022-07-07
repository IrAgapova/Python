class Road:
    massa = 25
    tel_pol = 5
    def __init__(self, l ,w):
        self._length=l
        self._width = w
    def on_mass(self ):
      return (self._length * self._width * Road.massa * Road.tel_pol)//1000
ro_1 = Road (20, 5000)
print(f'Масса асфальта для покрытия дороги {ro_1.on_mass()} тонн')





