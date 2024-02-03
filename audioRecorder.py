import pyaudio
import wave
import threading

class AudioRecorder:
    def __init__(self):
        self.audio = pyaudio.PyAudio()
        self.frames = []
        self.is_recording = False
        self.stream = None

    def start_recording(self):
        if not self.is_recording:
            self.stream = self.audio.open(format=pyaudio.paInt16,
                                          channels=1,
                                          rate=44100,
                                          input=True,
                                          frames_per_buffer=1024)
            self.is_recording = True
            self.frames = []

            def record():
                while self.is_recording:
                    data = self.stream.read(1024)
                    self.frames.append(data)

           
            self.record_thread = threading.Thread(target=record)
            self.record_thread.start()

    def stop_recording(self):
        if self.is_recording:
            self.is_recording = False
            self.record_thread.join() 
            self.stream.stop_stream()
            self.stream.close()
            self.audio.terminate()

            sound_file = wave.open("record.wav", "wb")
            sound_file.setnchannels(1)
            sound_file.setsampwidth(self.audio.get_sample_size(pyaudio.paInt16))
            sound_file.setframerate(44100)
            sound_file.writeframes(b"".join(self.frames))
            sound_file.close()
