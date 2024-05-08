import pyaudio
import wave


class Recorder(pyaudio.PyAudio):
    def __init__(self, filename):
        super().__init__()
        self.frames = None
        self.stream = None
        self.p = None
        self.found = False
        self.live = True
        self.chunk = 1024  # Record in chunks of 1024 samples
        self.sample_format = pyaudio.paInt16  # 16 bits per sample
        self.channels = 2
        self.fs = 44100  # Record at 44100 samples per second
        self.dev_index = 0
        self.seconds = 15
        self.filename = str(filename)

    def startRecording(self):
        # Create an interface to PortAudio
        self.p = pyaudio.PyAudio()
        self.live = True

        # Below finds your (Stereo Mix) index and auto assigns it, print statement is for testing purposes
        for i in range(self.p.get_device_count()):
            if "Stereo" in self.p.get_device_info_by_index(i).get("name") and self.found is False:
                self.dev_index = i
                self.found = True

        self.stream = self.p.open(format=self.sample_format,
                                  channels=self.channels,
                                  rate=self.fs,
                                  input_device_index=self.dev_index,
                                  frames_per_buffer=self.chunk,
                                  input=True)

        self.frames = []  # Initialize array to store frames

        print("Your (Stereo Mix) index is: " + str(self.dev_index))
        print('Recording')

        # Store data in chunks for X seconds
        while self.live is True:
            if self.live is True:
                data = self.stream.read(self.chunk)
                self.frames.append(data)
            else:
                Recorder.stopRecording(self)

        # Added to exit early from recording

    def stopRecording(self):
        self.live = False
        # Stop and close the stream
        self.stream.stop_stream()
        self.stream.close()
        # Terminate the PortAudio interface
        self.p.terminate()

        print('Finished recording')

        # Save the recorded data as a WAV file
        wf = wave.open(self.filename, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.p.get_sample_size(self.sample_format))
        wf.setframerate(self.fs)
        wf.writeframes(b''.join(self.frames))
        wf.close()
