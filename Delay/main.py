from Tkinter import *
import scipy.io.wavfile as wavfile
import pyaudio
import sys
import getopt
from Reproducir import Reproducir
#from Seno import Seno
import struct
import wave
import numpy as np

def counter_label(label):
      def count():
        global counter
        counter += 1
        label.config(text=str(counter))
        label.after(1000, count)
      count()

def main():

    root = Tk()
    root.title("Delay")

    label3 = Label(root, fg="blue")
    label3.pack()
    label3.grid(row=10,column=1)
    label3.config(text="Nombre o ruta del archivo a reproducir con delay")
    Nombre3 = "texto"
    Archivo3 = Reproducir(Nombre3)

    e3 = Entry(root)
    e3.grid(row=11,column=1)

    label4 = Label(root, fg="red")
    label4.pack()
    label4.grid(row=10,column=2)
    label4.config(text="Retraso en frames para el delay")
    Nombre4 = "texto"


    e4 = Entry(root)
    e4.grid(row=11,column=2)

    def init_audio3():

        n5=e3.get()
        n6=float(e4.get())

        NUMEROREPETICIONES = 10 #numero de repeticiones
        TIEMPODELAY = n6 #tiempo en milisegundos
        NumeroFramesDelay = 44100*(TIEMPODELAY/1000.0) #Numero de frames

        rate, data = wavfile.read(n5)  #Abrir Archivo usando la scipy.io.wavfile
        data1 = data
        data = np.append(data, np.zeros(NUMEROREPETICIONES*NumeroFramesDelay))


        delay = np.zeros([NUMEROREPETICIONES], dtype=object)

        for i in range(0, NUMEROREPETICIONES):
            delay[i] = np.zeros(NumeroFramesDelay*i)
            delay[i] = np.append(delay[i],data1)
            delay[i].resize(data.shape)

            if i == 0:
                data = data*0.5 + (delay[i]*(1/float(i+2)))*0.5 #sumatoria ajustada para evitar saturacion
            else:
                data = data + (delay[i]*(1/float(i+2)))*0.5 #sumatoria ajustada para evitar saturacion


        delay_output = wave.open('sumaa.wav', 'w')
        delay_output.setparams((1, 2, 44100, 0, 'NONE', 'not compressed'))

        values = []


        for i in range(0, len(data)):
                packed_value = struct.pack('<h', data[i])
                values.append(packed_value)


        value_str = ''.join(values)
        delay_output.writeframes(value_str)

        delay_output.close()

        Archivo6 = Reproducir('sumaa.wav')
        Archivo6.ruta = "sumaa.wav"
        Argumentos = Archivo6.abrir()
        Archivo6.inicio(Argumentos[0],Argumentos[1],Argumentos[2])


        Archivo6.rep()



    rep3=Button(root,text='Reproducir', command=init_audio3)
    rep3.grid(row=11,column=3)

    a = BooleanVar(root)
    a.set(False)

    root.mainloop()


if __name__ == '__main__':
    main()
