import pygame
print()
class BOBsHeart:
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.set_num_channels(35)

        self.pitches = [['C#3.wav', 'D#3.wav', 'F#3.wav', 'G#3.wav', 'A#3.wav', 'C#4.wav', 'D#4.wav',
                      'C3.wav', 'D3.wav', 'E3.wav', 'F3.wav', 'G3.wav', 'A3.wav', 'B3.wav', 'C4.wav', 'D4.wav', 'E4.wav'],
                        ['C#4.wav', 'D#4.wav', "F#4.wav", 'G#4.wav', 'A#4.wav', 'C#5.wav', 'D#5.wav',
                      'C4.wav', 'D4.wav', 'E4.wav', 'F4.wav', 'G4.wav', 'A4.wav', 'B4.wav', 'C5.wav', 'D5.wav', 'E5.wav'],
                        ['C#5.wav', 'D#5.wav', 'F#5.wav', 'G#5.wav', 'A#5.wav', 'C#6.wav', 'D#6.wav',
                      'C5.wav', 'D5.wav', 'E5.wav', 'F5.wav', 'G5.wav', 'A5.wav', 'B5.wav', 'C6.wav', 'D6.wav', 'E6.wav']]

        self.filepaths = ['Saw Files/', 'Sine Files/', 'Triangle wave files/', 'Square Files/']

        self.topKeys = ['Key.DIGIT_2',
                   'Key.DIGIT_3',
                   'Key.DIGIT_5',
                   'Key.DIGIT_6',
                   'Key.DIGIT_7',
                   'Key.DIGIT_9',
                   'Key.DIGIT_0',
                   'Key.Q',
                   'Key.W',
                   'Key.E',
                   'Key.R',
                   'Key.T',
                   'Key.Y',
                   'Key.U',
                   'Key.I',
                   'Key.O',
                   'Key.P']
        self.bottomKeys = ['Key.S',
                      'Key.D',
                      'Key.G',
                      'Key.H',
                      'Key.J',
                      'Key.L',
                      'Key.SEMICOLON',
                      'Key.Z',
                      'Key.X',
                      'Key.C',
                      'Key.V',
                      'Key.B',
                      'Key.N',
                      'Key.M',
                      'Key.COMMA',
                      'Key.PERIOD',
                      'Key.FORWARDSLASH']


        self.currentPitchTop = 1
        self.currentPitchBottom = 2
        self.currentPathTop = 1
        self.currentPathBottom = 1

        self.channels = {'Key.DIGIT_1': pygame.mixer.Channel(34),
                        'Key.DIGIT_2': pygame.mixer.Channel(27),
                        'Key.DIGIT_3': pygame.mixer.Channel(28),
                        'Key.DIGIT_5': pygame.mixer.Channel(29),
                        'Key.DIGIT_6': pygame.mixer.Channel(30),
                        'Key.DIGIT_7': pygame.mixer.Channel(31),
                        'Key.DIGIT_9': pygame.mixer.Channel(32),
                        'Key.DIGIT_0': pygame.mixer.Channel(33),
                        'Key.Q': pygame.mixer.Channel(0),
                        'Key.W': pygame.mixer.Channel(1),
                        'Key.E': pygame.mixer.Channel(2),
                        'Key.R': pygame.mixer.Channel(3),
                        'Key.T': pygame.mixer.Channel(4),
                        'Key.Y': pygame.mixer.Channel(5),
                        'Key.U': pygame.mixer.Channel(6),
                        'Key.I': pygame.mixer.Channel(7),
                        'Key.O': pygame.mixer.Channel(8),
                        'Key.P': pygame.mixer.Channel(9),
                        'Key.S': pygame.mixer.Channel(10),
                        'Key.D': pygame.mixer.Channel(11),
                        'Key.G': pygame.mixer.Channel(12),
                        'Key.H': pygame.mixer.Channel(13),
                        'Key.J': pygame.mixer.Channel(14),
                        'Key.L': pygame.mixer.Channel(15),
                        'Key.SEMICOLON': pygame.mixer.Channel(16),
                        'Key.Z': pygame.mixer.Channel(17),
                        'Key.X': pygame.mixer.Channel(18),
                        'Key.C': pygame.mixer.Channel(19),
                        'Key.V': pygame.mixer.Channel(20),
                        'Key.B': pygame.mixer.Channel(21),
                        'Key.N': pygame.mixer.Channel(22),
                        'Key.M': pygame.mixer.Channel(23),
                        'Key.COMMA': pygame.mixer.Channel(24),
                        'Key.PERIOD': pygame.mixer.Channel(25),
                        'Key.FORWARDSLASH': pygame.mixer.Channel(26)}

        self.keysounds = {
                        'Key.DIGIT_2': 'Sine Files/C#5.wav',
                        'Key.DIGIT_3': 'Sine Files/D#5.wav',
                        'Key.DIGIT_5': 'Sine Files/F#5.wav',
                        'Key.DIGIT_6': 'Sine Files/G#5.wav',
                        'Key.DIGIT_7': 'Sine Files/A#5.wav',
                        'Key.DIGIT_9': 'Sine Files/C#6.wav',
                        'Key.DIGIT_0': 'Sine Files/D#6.wav',
                        'Key.Q': 'Sine Files/C5.wav',
                        'Key.W': 'Sine Files/D5.wav',
                        'Key.E': 'Sine Files/E5.wav',
                        'Key.R': 'Sine Files/F5.wav',
                        'Key.T': 'Sine Files/G5.wav',
                        'Key.Y': 'Sine Files/A5.wav',
                        'Key.U': 'Sine Files/B5.wav',
                        'Key.I': 'Sine Files/C6.wav',
                        'Key.O': 'Sine Files/D6.wav',
                        'Key.P': 'Sine Files/E6.wav',
                        'Key.S': 'Sine Files/C#4.wav',
                        'Key.D': 'Sine Files/D#4.wav',
                        'Key.G': 'Sine Files/F#4.wav',
                        'Key.H': 'Sine Files/G#4.wav',
                        'Key.J': 'Sine Files/A#4.wav',
                        'Key.L': 'Sine Files/C#5.wav',
                        'Key.SEMICOLON': 'Sine Files/D#5.wav',
                        'Key.Z': 'Sine Files/C4.wav',
                        'Key.X': 'Sine Files/D4.wav',
                        'Key.C': 'Sine Files/E4.wav',
                        'Key.V': 'Sine Files/F4.wav',
                        'Key.B': 'Sine Files/G4.wav',
                        'Key.N': 'Sine Files/A4.wav',
                        'Key.M': 'Sine Files/B4.wav',
                        'Key.COMMA': 'Sine Files/C5.wav',
                        'Key.PERIOD': 'Sine Files/D5.wav',
                        'Key.FORWARDSLASH': 'Sine Files/E5.wav'}

    def checkKey(self, key):
        key = str(key)
        pitchShifters = ['Key.DIGIT_1', 'Key.LEFTBRACKET', 'Key.A', 'Key.F']
        waveShifters = ['Key.RIGHTBRACKET', 'Key.BACKSLASH', 'Key.SINGLEQUOTE', 'Key.RETURN']

        if key in pitchShifters:
            self.switchPitch(key)

        elif key in waveShifters:
            self.switchWave(key)

        else:
            try:
                keyNote = self.getKeyNote(key)
                channel = self.getChannel(key)
                if channel.get_busy() == False:
                    self.play(keyNote, channel)
            except KeyError:
                print()

    def switchPitch(self, key):
        keyCount = 0
        if key == 'Key.LEFTBRACKET':
            self.currentPitchTop += 1
            if self.currentPitchTop > 2:
                self.currentPitchTop = 0
            pitch = self.pitches[self.currentPitchTop]

            for i in self.topKeys:
                self.keysounds[i] = self.filepaths[self.currentPathTop] + pitch[keyCount]
                keyCount += 1

        elif key == 'Key.DIGIT_1':
            self.currentPitchTop -= 1
            if self.currentPitchTop < 0:
                self.currentPitchTop = 2
            pitch = self.pitches[self.currentPitchTop]
            for i in self.topKeys:
                self.keysounds[i] = self.filepaths[self.currentPathTop] + pitch[keyCount]
                keyCount += 1

        elif key == 'Key.A':
            self.currentPitchBottom -= 1
            if self.currentPitchBottom < 0:
                self.currentPitchBottom = 2
            pitch = self.pitches[self.currentPitchBottom]
            for i in self.bottomKeys:
                self.keysounds[i] = self.filepaths[self.currentPathBottom] + pitch[keyCount]
                keyCount += 1

        elif key == 'Key.F':
            self.currentPitchBottom += 1
            if self.currentPitchBottom > 2:
                self.currentPitchBottom = 0
            pitch = self.pitches[self.currentPitchBottom]
            for i in self.bottomKeys:
                self.keysounds[i] = self.filepaths[self.currentPathBottom] + pitch[keyCount]
                keyCount += 1

    def switchWave(self, key):
        keyCount = 0
        if key == 'Key.RIGHTBRACKET':
            self.currentPathTop -=1
            if self.currentPathTop < 0:
                self.currentPathTop = 3
            pitch = self.pitches[self.currentPitchTop]

            for i in self.topKeys:
                self.keysounds[i] = self.filepaths[self.currentPathTop] + pitch[keyCount]
                keyCount += 1


        elif key == 'Key.BACKSLASH':
            self.currentPathTop += 1
            if self.currentPathTop > 3:
                self.currentPathTop = 0
            pitch = self.pitches[self.currentPitchTop]

            for i in self.topKeys:
                self.keysounds[i] = self.filepaths[self.currentPathTop] + pitch[keyCount]
                keyCount += 1

        elif key == 'Key.SINGLEQUOTE':
            self.currentPathBottom -= 1
            if self.currentPathBottom < 0:
                self.currentPathBottom = 3
            pitch = self.pitches[self.currentPitchBottom]

            for i in self.bottomKeys:
                self.keysounds[i] = self.filepaths[self.currentPathBottom] + pitch[keyCount]
                keyCount += 1

        else:
            self.currentPathBottom += 1
            if self.currentPathBottom > 3:
                self.currentPathBottom = 0
            pitch = self.pitches[self.currentPitchBottom]

            for i in self.bottomKeys:
                self.keysounds[i] = self.filepaths[self.currentPathBottom] + pitch[keyCount]
                keyCount += 1

    def getKeyNote(self, key):
        keyNote = self.keysounds[str(key)]
        return keyNote

    def getChannel(self, key):
        channel = self.channels[str(key)]
        return channel

    def play(self, sound, channel):
        channel.play(pygame.mixer.Sound(sound))

    def stop(self, channel):
        channel.fadeout(50)

    def play_file(self, file):
        pygame.mixer.Channel(34).play(file)
