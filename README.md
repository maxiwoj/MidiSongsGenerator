# Midi Songs Generator
MIDI music generator is a script for generating simple MIDI music using basic music rules

## Usage
To use the generator you will need python (tested with 3.x)
```
$ git clone https://github.com/maxiwoj/MidiSongsGenerator
$ cd MidiSongsGenerator
$ python MIDIGenerator.py
```

### Additional options:
```
  -h, --help            show this help message and exit
  --narcossity {1,2,3,4}, -n {1,2,3,4}
                        Change the level of narcossity.
  -p FILENAME, --path FILENAME
                        Sets the path of the generated midi file. Note, that
                        the name should end witch .mid. If only a name is
                        given the file is created inworking directory
  -k KEY, --key KEY     Set the base key for whole midi file. The KEY should
                        bebetween 0 and 12.
  -b BEATS_PER_BAR, --beats BEATS_PER_BAR
                        Set the number of beats per bar. BEATS_PER_BAR should
                        be between 4 and 64
  -B NUMBER_OF_BARS, --bars NUMBER_OF_BARS
                        Set the number of bars = length of the music
  -j, --jazz            Sets genre type to jazz. Setting flag -j is similar to
                        setting: -n 2 -b 20
  -s, --samba           Sets genre type to samba. Setting flag -s is similar
                        to setting: -n 4 -b 16
```
