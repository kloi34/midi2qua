# midi2qua
Converts MIDI into a text file whose contents can be copied into a .qua file. This helps make maps for [Quaver](https://github.com/Quaver), the ultimate community-driven and open-source competitive rhythm game.

This program was created primarily for converting MIDIs of live piano performances for 7 key maps. However, the program should still work with any kind of MIDI file. Also 4 key is supported (albeit poorly)

## How to use this program
* Get Python (3.6+?)
* Install [Mido](https://mido.readthedocs.io/en/latest/) wherever this program is downloaded to with `pip install mido`
* Run the program (somehow)

After using the program, you should get a .txt file in the same location as the program. Open the text file and copy the HitObject text into the desired .qua file

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

## Goals to improve this program
1. Implement option to discard extra notes
2. Implement mapping to different columns
3. Improve UI

