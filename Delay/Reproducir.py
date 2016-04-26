import wave
import pyaudio


class Reproducir:
    ruta = ""
    def __init__(self, CHUNK):
        self.CHUNK = CHUNK


    def abrir(self):
        print Reproducir.ruta
        self.wf = wave.open(self.ruta, 'rb')
        sampwidth = self.wf.getsampwidth()
        channels = self.wf.getnchannels()
        rate = self.wf.getframerate()
        print
        return (sampwidth, channels, rate)

    def inicio(self, sampwidth, channels, framerate):
        self.p = pyaudio.PyAudio()

        self.stream = self.p.open(format=self.p.get_format_from_width(sampwidth),
                        channels=channels,
                        rate=framerate,
                        output=True)

    def rep(self):
        data = self.wf.readframes(self.CHUNK)

        while data != '':
            self.stream.write(data)
            data = self.wf.readframes(self.CHUNK)


    def cerrar(self):

        self.wf.close()
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

    def imprimir(self):
        print self.ruta
