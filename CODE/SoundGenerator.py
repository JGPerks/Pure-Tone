import pygame

class BOBsHeart:
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.set_num_channels(35)

        self.sine3 = ['Sine Files/C#3.wav', 'Sine Files/D#3.wav', 'Sine Files/F#3.wav',
                      'Sine Files/G#3.wav', 'Sine Files/A#3_2.wav', 'Sine Files/C#4.wav',
                      'Sine Files/D#4.wav',

                      'Sine Files/C3.wav', 'Sine Files/D3.wav', 'Sine Files/E3.wav',
                      'Sine Files/F3.wav', 'Sine Files/G3.wav', 'Sine Files/A4.wav',
                      'Sine Files/B4.wav', 'Sine Files/C4.wav', 'Sine Files/D4.wav',
                      'Sine Files/E4.wav', ]


        self.currentPitch1 = 1

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

        self.keysounds = {'Key.DIGIT_1': 'BOB.wav',
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


    def getKeyNote(self, key):
        keyNote = self.keysounds[str(key)]
        return keyNote

    def getChannel(self, key):
        channel = self.channels[str(key)]
        return channel

    def changePitch(self):
        for key in self.keysounds:
            pass


    def changeWave(self, ):
        pass

    def play(self, sound, channel):
        channel.play(pygame.mixer.Sound(sound))

    def stop(self, channel):
        channel.fadeout(50)

    def play_file(self, file):
        pygame.mixer.Channel(34).play(file)