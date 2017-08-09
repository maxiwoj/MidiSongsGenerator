from instruments.instrument import Instrument


class Piano:
    def __init__(self, key_base, track, channel, volume, beats_in_bar, midi_file, narcossity_level):
        midi_file.addProgramChange(track, channel, 0, Instrument.AcousticGrandPiano)
        self.midi_file = midi_file
        self.key_base = 60 + key_base
        self.track = track
        self.channel = channel
        self.volume = volume
        self.beats_in_bar = beats_in_bar
        self.number_of_ticks_per_beat = beats_in_bar // 4
        self.narcossity_level = narcossity_level

    def generate_until_bar(self, bar_start_time, chord, relative_pitch):
        time = bar_start_time
        if self.narcossity_level == 2: #jazzy
            for interval in chord:
                self.midi_file.addNote(self.track, self.channel, self.key_base + relative_pitch + interval,
                                       time + self.number_of_ticks_per_beat // 2, self.number_of_ticks_per_beat, self.volume)
                self.midi_file.addNote(self.track, self.channel, self.key_base + relative_pitch + interval,
                                       time + self.number_of_ticks_per_beat + self.number_of_ticks_per_beat // 2,
                                       self.beats_in_bar - (2 * self.number_of_ticks_per_beat), self.volume)
        elif self.narcossity_level == 4: #samba
            for i in range(0, self.beats_in_bar):
                for interval in chord:
                    if i % self.number_of_ticks_per_beat == self.number_of_ticks_per_beat - 1:
                        self.midi_file.addNote(self.track, self.channel, self.key_base + relative_pitch + interval,
                                               time + i, self.number_of_ticks_per_beat // 2, self.volume)
                    elif i % self.number_of_ticks_per_beat >= self.number_of_ticks_per_beat // 2:
                        self.midi_file.addNote(self.track, self.channel, self.key_base + relative_pitch + interval,
                                               time + i, 1, self.volume)
        else: #simple arpeggio
            if relative_pitch > 5:
                relative_pitch = relative_pitch - 12
            for i in range(0, self.beats_in_bar):
                self.midi_file.addNote(self.track, self.channel, self.key_base + relative_pitch + chord[i % 4],
                                       time + i, 1, self.volume)
