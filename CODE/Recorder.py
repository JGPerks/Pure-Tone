import pyaudio
import wave


def startRecording():
    found = False
    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 1
    fs = 44100  # Record at 44100 samples per second
    dev_index = 0
    seconds = 5
    filename = "BOB.wav"

    p = pyaudio.PyAudio()  # Create an interface to PortAudio
    # Below finds your (Stereo Mix) index and auto assigns it, print statement is for testing purposes
    for i in range(p.get_device_count()):
        if "Stereo" in p.get_device_info_by_index(i).get("name") and found is False:
            dev_index = i
            found = True

    print("Your (Stereo Mix) index is: " + str(dev_index))
    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    input_device_index=dev_index,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for X seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    # Added to test early exit of recording
    def stopStream():
        # Stop and close the stream
        stream.stop_stream()
        stream.close()
        # Terminate the PortAudio interface
        p.terminate()

        print('Finished recording')

        # Save the recorded data as a WAV file
        wf = wave.open(filename, 'wb')
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(sample_format))
        wf.setframerate(fs)
        wf.writeframes(b''.join(frames))
        wf.close()

    stopStream()

