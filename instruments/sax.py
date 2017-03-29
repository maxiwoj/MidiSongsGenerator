import random

from instruments.instrument import Instrument


class Sax:
    def __init__(self, keyBase, track, channel, volume, beats_in_bar, midi_file, narcossity_level):
        midi_file.addProgramChange(track, channel, 0, Instrument.AltoSax)
        self.MidiFile = midi_file
        self.keyBase = 60 + keyBase
        self.track = track
        self.channel = channel
        self.volume = volume
        self.beatsInBar = beats_in_bar
        self.numberOfTicksPerBeat = beats_in_bar // 4
        self.currentPitch = 0
        self.allowedMelodicIntervals = [0, 1, -1, 2, -2, 3, -3, 4, -4, -8, 8, 9, -9]
        self.narcossity_level = narcossity_level

    def generate_until_bar(self, time, chord, relative_pitch):
        end_time = time + self.beatsInBar
        if self.currentPitch + self.keyBase > 75:
            self.allowedMelodicIntervals.sort()
        elif self.currentPitch + self.keyBase < 50:
            self.allowedMelodicIntervals.sort()
            self.allowedMelodicIntervals.reverse()
        else:
            random.shuffle(self.allowedMelodicIntervals)
        while time < end_time:
            found = False
            for i in range(0, 4):
                for interval in chord:
                    if (self.currentPitch + self.allowedMelodicIntervals[i]) % 12 == (relative_pitch + interval) % 12:
                        if end_time - time > 1:
                            if self.narcossity_level == 4:
                                duration = random.randint(1, (end_time - time) // 2)
                            else:
                                duration = random.randint(1, end_time - time)
                        else:
                            duration = 1

                        self.currentPitch += self.allowedMelodicIntervals[i]
                        self.MidiFile.addNote(self.track, self.channel, self.keyBase + self.currentPitch,
                                              time, duration, self.volume)
                        time += duration
                        found = True
                        break
                if found:
                    break
            else:
                duration = 1
                self.currentPitch += random.choice([-1, 1])
                self.MidiFile.addNote(self.track, self.channel, self.keyBase + self.currentPitch,
                                      time, duration, self.volume)
                time += duration
