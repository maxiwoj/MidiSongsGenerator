import random

from midiutil import *

from arguments import get_arguments
from instruments.choir import Choir
from instruments.percussion import Percussion
from instruments.piano import Piano
from instruments.bass import Bass
from instruments.sax import Sax


# Read arguments
arguments = get_arguments()

key_base = arguments.key
number_of_bars = arguments.number_of_bars
file_name = arguments.fileName
narcossity_level = arguments.narcossity_level
beats_per_bar = arguments.beats_per_bar

# Set channels for each instrument
track = 0
choir_channel = 0
bass_channel = 1
piano_channel = 2
alt_sax_channel = 3
percussion_channel = 9

relative_pitch = 0

time = 0 # set start time
tempo = beats_per_bar // 4 * 120  # In Beats per minute
max_volume = 127  # setting max_volume, channel's volume will be relative to the max Volume

# simple graph for possible chord progressions - relative pitch to the key
chord_base_progression_map = {0: [0, 2, 4, 5, 7, 9, 11],
                              2: [7, 9],
                              4: [2, 5, 9],
                              5: [0, 11, 7],
                              7: [0, 9],
                              9: [2, 5, 7],
                              11: [0, 4]}

# simple map with possible chords per relative pitch to the key
pitch_chord_map = {
    0: [[0, 4, 7, 11], [0, 4, 11, 14], [0, 4, 9, 14], [0, 4, 7, 9]],
    2: [[0, 3, 7, 10], [0, 3, 10, 14], [3, 7, 10, 12]],
    4: [[0, 3, 7, 10], [0, 3, 10, 14], [0, 4, 7, 8]],
    5: [[0, 4, 7, 11], [0, 4, 11, 14], [0, 4, 9, 14], [0, 4, 7, 9], [-3, 0, 4, 7]],
    7: [[0, 4, 7, 10], [0, 4, 10, 14], [4, 7, 10, 13], [-2, 1, 4, 6]],
    9: [[0, 3, 7, 10], [0, 3, 10, 14], [3, 7, 10, 12]],
    11: [[0, 3, 6, 10], [0, 3, 6, 9], [3, 6, 10, 12]]
}

my_midi = MIDIFile(1, adjust_origin=True)  # One track, defaults to format 1
my_midi.addTempo(track, time, tempo) #add tempo to the track

# create channels:
choir = Choir(key_base, track, choir_channel, max_volume - 45, beats_per_bar, my_midi)
percussion = Percussion(track, percussion_channel, max_volume - 60, beats_per_bar, my_midi, narcossity_level)
bass = Bass(key_base, track, bass_channel, max_volume, beats_per_bar, my_midi, narcossity_level)
piano = Piano(key_base, track, piano_channel, max_volume - 35, beats_per_bar, my_midi, narcossity_level)

if narcossity_level != 1:
    alt_sax = Sax(key_base, track, alt_sax_channel, max_volume - 45, beats_per_bar, my_midi, narcossity_level)

# start with 1 bar percussion solo
percussion.generate_until_bar(time)
time = beats_per_bar

for i in range(0, number_of_bars):
    relative_pitch = random.choice(chord_base_progression_map[relative_pitch])
    chord = random.choice(pitch_chord_map[relative_pitch])

    bass.generate_until_bar(time, chord, relative_pitch)
    percussion.generate_until_bar(time)
    choir.generate_until_bar(time, chord, relative_pitch)
    piano.generate_until_bar(time, chord, relative_pitch)
    if narcossity_level != 1:
        alt_sax.generate_until_bar(time, chord, relative_pitch)
    time += beats_per_bar

with open(file_name, "wb") as output_file:
    my_midi.writeFile(output_file)
