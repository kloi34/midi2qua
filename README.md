# midi2qua
Noob Python program by Noob Python programmer

Convert MIDI files to text that you can copy and paste into a .qua file. This helps make maps for [Quaver](https://github.com/Quaver), the ultimate community-driven and open-source competitive rhythm game. 

This program works but is very primative and hacky (as of 16 Nov 2021). I think you need to [Install Mido](https://mido.readthedocs.io/en/latest/installing.html) in whatever environment you are using this program in order for it to run. Maybe also need to [Installl tkinter](https://tkdocs.com/tutorial/install.html) depending on the Python distrubution you use.

## Examples of Quaver maps made with this program
- [Glinka/Balakirev - The Lark](https://quavergame.com/mapset/9136)
- [Sergei Rachmaninoff - Etude-Tableau Op. 39 No. 6 in A Minor](https://quavergame.com/mapset/9377)
- [Frederic Chopin - Op. 10 No. 4 in C-sharp Minor](https://quavergame.com/mapset/11405)
- [Maurice Ravel - Jeux d'eau](https://quavergame.com/mapset/11945)
- [Joe Hisaishi/Kyle Landry - Howl's Moving Castle Theme 2.0](https://quavergame.com/mapset/12245)

## Good Sources of MIDIs (and mp3s sometimes) of Live Piano Performances
### Minnesota International Piano-e-Competition
MIDIs: https://piano-e-competition.com/
MP3s for most of the performances: https://www.kaggle.com/jackvial/themaestrodatasetv2 (use the .csv or .json to find the mp3 that corresponds to a performance
### Piano performances by 小栗克裕 (Katsuhiro Oguri)
MIDIs + MP3s: (JP) http://www.bc9.jp/~oguri/index1.html or (EN) http://www.bc9.jp/~oguri/indexe.html

## Future Goals to make this program less noob:
1. Refactor code; Create functions that encapsulate single actions for better readablility and better maintainability
2. Improve tkinter UI?
3. Add more options to conversion (ex. automatically leaving out low velocity (i.e. very quiet, inaudible notes) midi notes)
4. Explain better how to start using this program in this readme
