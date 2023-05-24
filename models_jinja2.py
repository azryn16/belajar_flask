# file : models.py
# contoh model untuk flask

class Lingkaran(object):
    def __init__(self):
        self.text = "Mahasiswa"
    
    def setRadius(self,radius):
        self.radius = radius
        
    def getRadius(self):
        return self.radius
    
    def hitungLuas(self):
        return pi * (self.radius ** 2)
    
    def hitungKeliling(self):
        return 2 * pi * self.radius
    