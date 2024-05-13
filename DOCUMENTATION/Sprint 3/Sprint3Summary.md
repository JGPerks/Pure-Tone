# SPRINT 3

Sprint 3 (final sprint of this project for Software Engineering CYBR 404 at UNK), teammates did their best to prepare neccessary requirements for the Pure Tone BOB Keyboard.

Thus far we have an:

Oscilloscope GUI,
Keyboard GUI,
Music keysounds,
Recording feature.

John and Alexis worked on trying to integrate PySimpleGUI and tkinter into one common window. However, this involves some back-end work that may take too long between now and when the project is due.
Jonathan worked on the math and locating of files on one's computer for the recording feature.
Isaac mapped keys and documentation. Juan worked on documentation and the keyboard GUI. Bhavya worked on getting audio tasks done (wave files). 

The team communicates via dicord. 
Here are some of the updates that were shared:

Jonathan: I found a way to record audio played through the speakers of the computer rather than by the microphone . Now we can hit record, play keys, save audio.

Isaac: Pushing a change to KeyboardGUI that should make the keyboard not go crazy when holding a key, and also allow it to hold as many keys as there are sounds without any errors.  I have unmapped the keys so only the number keys have sounds right now.  I am having trouble getting everything mapped in a good way, and want some suggestions before I do too much.
Also, we may want audio files that last several seconds rather than just one second.  Not sure what causes it, but holding multiple keys for long enough that the sound files reach their end (~1 second right now) causes the program to only replay the sound of the last played key
Finally, there's a popping sound that comes when audio is cut before the end of the file.  Not sure how we can fix that one though. 

Isaac: Some testing, you can't hold however many keys you want.  Not sure what's causing it, but the keyboard only recognizes a handful of keys before it won't take more input.  Strangely seems to be tied to what keys are pressed, as I can press the 1,2,3,4 keys before it locks up, but only the 5,6 keys in other scenarios.  Also pushing another tiny change that helps with the popping to an extent.

Alexis: editing the demo oscilloscope file now with code markups

Bhavya: hey guys just pushed the key mapping diagram for refrence. its fl chart.gif

Jonathan: I updated the record button in KeyboardGUI.py to record from stereo mix instead of mic input. It might not work for you as stereo mix is disabled by default and its index on your computer might be different from mine. I’ll try to have it auto detect your index eventually.

Alexis: I am still having troubles getting PySimpleGUI onto a tkinter screen. I have some code I found and have played around some with on the Test.py document but the PySimpleGUI still does not seem to be integrating. Right now in the main screen, multiple windows get opened (not all within same window).  But I am having difficulties integrating all the features (PySimpleGUI oscilloscope, keyboard, recording button,) all into one common tkinter window. Do you guys have any ideas? One idea I have is just to create an executable now to see what the layout looks like.

Isaac: If needed, we could attempt to translate the PySimpleGUI code into TKinter code, though I don't know how feasible that is
Also, I found this website that generates pure tones, has all the wave forms we originally planned, and has a note tuning feature.  May be useful, though our tones don't line up with it's tones in terms of note value.
https://www.szynalski.com/tone-generator/

John: I think the current version of the oscilloscope for the uses the matplotlib back end. something with the figurecanvastkagg.
https://matplotlib.org/stable/gallery/user_interfaces/embedding_in_tk_sgskip.html

Jonathan: I pushed some code that should detect your (Stereo Mix) and auto assign its index so we don't have to bash our heads in as much. For testing purposes it'll print out the index. If there are any issues with it lmk.

Juan: Added some items in our documentation about the recording buttons and new libraries used this week
