from instruments.instrument import Instrument


class Bass:
    def __init__(self, key_base, track, channel, volume, beats_in_bar, midi_file, narcossity_level):
        midi_file.addProgramChange(track, channel, 0, Instrument.ElectricBass_pick)
        self.midi_file = midi_file
        self.key_base = 24 + key_base
        self.track = track
        self.channel = channel
        self.volume = volume
        self.beats_in_bar = beats_in_bar
        self.number_of_ticks_per_beat = beats_in_bar // 4
        self.narcossity_level = narcossity_level

    def generate_until_bar(self, bar_start_time, chord, stopien):
        time = bar_start_time
        for interval in chord:
            if self.narcossity_level == 1:
                self.midi_file.addNote(self.track, self.channel, self.key_base + stopien + interval,
                                       time, self.number_of_ticks_per_beat, self.volume)
            else:
                beat_count = self.number_of_ticks_per_beat // 2
                for i in range(0, self.number_of_ticks_per_beat):
                    if beat_count != 0 and i % beat_count == 0:
                        self.midi_file.addNote(self.track, self.channel, self.key_base + stopien + interval,
                                               time + i, beat_count, self.volume)
                    elif beat_count == 0:
                        self.midi_file.addNote(self.track, self.channel, self.key_base + stopien + interval,
                                               time + i, 1, self.volume)
            time += self.number_of_ticks_per_beat
