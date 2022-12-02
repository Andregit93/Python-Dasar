class people:
#membuat class people

  def __init__(self, name, age):
    self.name = name
    self.age = age
#membuat function class yg berisi name dan age

  def Intro(self):
    print("Hai namaku " + self.name)
#membuat function intro untuk memanggil function class self.name

p1 = people("andre sevtian", "19")
#membuat objek p1 untuk mengisi nilai functionclass name dan age

p1.Intro()
#menampilkan objek p1 dengan function intro 