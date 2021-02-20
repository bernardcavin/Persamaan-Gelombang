#Copyright 2021 Made by bangber
import numpy as np
import matplotlib.pyplot as plot
import math

class persamaan_gelombang:
    def __init__(self, amplitudo,trigonometri,frekuensi,fasa=0,waktu=2):
        self.amplitudo = float(amplitudo)
        self.trigonometri = trigonometri
        self.frekuensi = float(frekuensi)
        self.fasa = float(fasa)
        self.waktu = np.arange(0,waktu,0.01)
        self.radian = [(2*math.pi*self.frekuensi*x)+self.fasa for x in self.waktu]
    def amplitudo_gelombang(self):
        if self.trigonometri=='sin':
            return [x*self.amplitudo for x in np.sin(self.radian)]
        else:
            return [x*self.amplitudo for x in np.cos(self.radian)]

#UBAH YANG INI. MISALNYA PERSAMAAN GELOMBANGMU Y = Asin(2*phi*f*t + k*x), masukkan A sebagai amplitudo, masukkan 'sin' sebagai trigonometri, masukkan f sebagai frekuensi, masukkan kx sebagai fasa(default=0), dan masukkan t sebagai waktu(default=2). Misal Y= 5cos(2*phi*2*t + 3), maka A nya 5, trigononya 'cos', frekuensinya 2, fase atau kx nya 3, waktunya terserah, misal dari 0 sampai 10, berarti tulis 10. Jadi kalau ditulis kaya gini: gelombang = persamaan_gelombang(5,'cos',2,3,10)
gelombang = persamaan_gelombang(100,'sin',1,0,5)

plot.plot(gelombang.waktu, gelombang.amplitudo_gelombang())
plot.title('Gelombang A')
plot.xlabel('Waktu(s)')
plot.ylabel('Amplitudo(m)')
plot.grid(True, which='both')
plot.axhline(y=0, color='k')
plot.show()