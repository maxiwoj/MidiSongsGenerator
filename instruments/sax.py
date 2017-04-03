import random

from instruments.instrument import Instrument


class Sax:
    def __init__(self, keyBase, track, channel, volume, beats_in_bar, midi_file, narcossity_level):
        midi_file.addProgramChange(track, channel, 0, Instrument.AltoSax)
        self.midi_file = midi_file
        self.key_base = 60 + keyBase
        self.track = track
        self.channel = channel
        self.volume = volume
        self.beats_in_bar = beats_in_bar
        self.number_of_ticks_per_beat = beats_in_bar // 4
        self.current_pitch = 0
        self.allowed_melodic_intervals = [0, 1, -1, 2, -2, 3, -3, 4, -4, -8, 8, 9, -9]
        self.narcossity_level = narcossity_level

    def generate_until_bar(self, time, chord, relative_pitch):
        end_time = time + self.beats_in_bar
        if self.current_pitch + self.key_base > 80:
            self.allowed_melodic_intervals.sort()
        elif self.current_pitch + self.key_base < 40:
            self.allowed_melodic_intervals.sort()
            self.allowed_melodic_intervals.reverse()
        else:
            random.shuffle(self.allowed_melodic_intervals)
        while time < end_time:
            found = False
            for i in range(0, 4):
                for interval in chord:
                    if (self.current_pitch + self.allowed_melodic_intervals[i]) % 12 == (relative_pitch + interval) % 12:
                        if end_time - time > 1:
                            if self.narcossity_level == 4:
                                duration = random.randint(1, (end_time - time) // 2)
                            else:
                                duration = random.randint(1, end_time - time)
                        else:
                            duration = 1
                        self.current_pitch += self.allowed_melodic_intervals[i]
                        self.midi_file.addNote(self.track, self.channel, self.key_base + self.current_pitch,
                                               time, duration, self.volume)
                        found = True
                        break
                if found:
                    break
            else:
                duration = 1
                self.current_pitch += random.choice([-1, 1])
                self.midi_file.addNote(self.track, self.channel, self.key_base + self.current_pitch,
                                       time, duration, self.volume)
            time += duration
