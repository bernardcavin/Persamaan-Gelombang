#Copyright 2021 Made by bangber
import numpy as np
import matplotlib.pyplot as plot
import math


#UBAH YANG INI
Amplitudo = 1
Frekuensi = 1
Fasa = 0
Waktu = 5
plot.title('Gelombang A')
#UBAH YANG DIATAS


#kalau ada yang mau diubah, ganti aja namanya. kalau diatas tadi namanya kalian mau ganti, ganti juga yang dibawah. misalnya Amplitudo ganti ke Ampli, yang diatas ganti, yang dibawah ganti
y=[Amplitudo*np.sin((2*math.pi*Frekuensi*t) + Fasa) for t in np.arange(0,Waktu,0.01)] #ini persamaannya. kalau ganti nama, ganti disini juga
plot.plot(np.arange(0,Waktu,0.01),y)
plot.xlabel('Waktu(s)')
plot.ylabel('Amplitudo(m)')
plot.grid(True, which='both')
plot.axhline(y=0, color='k')
plot.show()


#yang ijo ijo ini bisa diapus. hapusnya sampe tanda pagar pojok kiri.