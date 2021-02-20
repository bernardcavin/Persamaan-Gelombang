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

gelombang = persamaan_gelombang(100,'sin',1,0,5)
plot.plot(gelombang.waktu, gelombang.amplitudo_gelombang())
plot.title('Gelombang A')
plot.xlabel('Waktu(s)')
plot.ylabel('Amplitudo(m)')
plot.grid(True, which='both')
plot.axhline(y=0, color='k')
plot.show()