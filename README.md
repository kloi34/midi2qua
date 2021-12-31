# midi2qua
Converts MIDI into a text file whose contents can be copied into a .qua file. This helps make maps for [Quaver](https://github.com/Quaver), the ultimate community-driven and open-source competitive rhythm game.

This program was created primarily for converting MIDIs of live piano performances for 7 key maps. However, the program should still work with any kind of MIDI file and also produce 4 key maps if desired.

## How to use this program
* Get Python (3.6+)
* Install [Mido](https://mido.readthedocs.io/en/latest/) wherever this program is downloaded to with `pip install mido`
* Run the program (somehow)

You should get a .txt file in the same location as the program after running it. Open the text file and copy + paste the HitObject text into the desired .qua file.

For now, you will still have to manually rearrange/shift notes to different columns using a Quaver plugin. Maybe a future version of this program can remedy this step and pre-arrange notes to make it easier. 

## Examples of Quaver maps made with this program
- [Glinka/Balakirev - The Lark](https://quavergame.com/mapset/9136)
- [Sergei Rachmaninoff - Etude-Tableau Op. 39 No. 6 in A Minor](https://quavergame.com/mapset/9377)
- [Frederic Chopin - Op. 10 No. 4 in C-sharp Minor](https://quavergame.com/mapset/11405)
- [Maurice Ravel - Jeux d'eau](https://quavergame.com/mapset/11945)
- [Joe Hisaishi/Kyle Landry - Howl's Moving Castle Theme 2.0](https://quavergame.com/mapset/12245)

## Good sources of live piano MIDIs
### Minnesota International Piano-e-Competition
MIDIs: https://piano-e-competition.com/
MP3s for most MIDIs: https://www.kaggle.com/jackvial/themaestrodatasetv2 (use the .csv or .json to find the mp3 that corresponds to a performance)
### Personal homepage of 小栗克裕 (Katsuhiro Oguri)
MIDIs + MP3s: (JP) http://www.bc9.jp/~oguri/index1.html or (EN) http://www.bc9.jp/~oguri/indexe.html
### kunstderfuge.com
MIDIs: https://www.kunstderfuge.com/
### SMD MIDI-Audio Piano Music dataset from International Audio Laboratories Erlangen
MIDIs + MP3s: https://www.audiolabs-erlangen.de/resources/MIR/SMD/midi
