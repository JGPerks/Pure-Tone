import pygame

class BOBsHeart:
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.set_num_channels(34)

        self.channels = {
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
                        'Key.DIGIT_2': 'Sound Files/Long Keys/C#5_2.wav',
                        'Key.DIGIT_3': 'Sound Files/Long Keys/D#5_2.wav',
                        'Key.DIGIT_5': 'Sound Files/Long Keys/F#5.wav',
                        'Key.DIGIT_6': 'Sound Files/Long Keys/G#5_3.wav',
                        'Key.DIGIT_7': 'Sound Files/Long Keys/A#5_2.wav',
                        'Key.DIGIT_9': 'Sound Files/Long Keys/C#6_2.wav',
                        'Key.DIGIT_0': 'Sound Files/Long Keys/D#6_2.wav',
                        'Key.Q': 'Sound Files/Long Keys/C5.wav',
                        'Key.W': 'Sound Files/Long Keys/D5.wav',
                        'Key.E': 'Sound Files/Long Keys/E5.wav',
                        'Key.R': 'Sound Files/Long Keys/F5.wav',
                        'Key.T': 'Sound Files/Long Keys/G5.wav',
                        'Key.Y': 'Sound Files/Long Keys/A5.wav',
                        'Key.U': 'Sound Files/Long Keys/B5.wav',
                        'Key.I': 'Sound Files/Long Keys/C6.wav',
                        'Key.O': 'Sound Files/Long Keys/D6.wav',
                        'Key.P': 'Sound Files/Long Keys/E6.wav',
                        'Key.S': 'Sound Files/Long Keys/C#4_2.wav',
                        'Key.D': 'Sound Files/Long Keys/D#4_2.wav',
                        'Key.G': 'Sound Files/Long Keys/F#4_2.wav',
                        'Key.H': 'Sound Files/Long Keys/G#4_2.wav',
                        'Key.J': 'Sound Files/Long Keys/A#4_2.wav',
                        'Key.L': 'Sound Files/Long Keys/C#5_2.wav',
                        'Key.SEMICOLON': 'Sound Files/Long Keys/D#5_2.wav',
                        'Key.Z': 'Sound Files/Long Keys/C4_2.wav',
                        'Key.X': 'Sound Files/Long Keys/D4_3.wav',
                        'Key.C': 'Sound Files/Long Keys/E4.wav',
                        'Key.V': 'Sound Files/Long Keys/F4_2.wav',
                        'Key.B': 'Sound Files/Long Keys/G4_3.wav',
                        'Key.N': 'Sound Files/Long Keys/A4.wav',
                        'Key.M': 'Sound Files/Long Keys/B4_2.wav',
                        'Key.COMMA': 'Sound Files/Long Keys/C5.wav',
                        'Key.PERIOD': 'Sound Files/Long Keys/D5.wav',
                        'Key.FORWARDSLASH': 'Sound Files/Long Keys/E5.wav'}





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

