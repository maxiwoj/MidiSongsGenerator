from instruments.instrument import Instrument


class Choir:
    def __init__(self, key_base, track, channel, volume, beats_in_bar, midi_file):
        midi_file.addProgramChange(track, channel, 0, Instrument.ChoirAahs)
        self.midi_file = midi_file
        self.key_base = 36 + key_base
        self.track = track
        self.channel = channel
        self.volume = volume
        self.beats_in_bar = beats_in_bar
        self.first_note_duration = 3 * beats_in_bar // 4 - 1

    def generate_until_bar(self, bar_start_time, chord, relative_pitch):
        if relative_pitch > 7:
            relative_pitch -= 12
        for interval in chord:
            self.midi_file.addNote(self.track, self.channel, self.key_base + relative_pitch + interval,
                                   bar_start_time, self.first_note_duration, self.volume)
            self.midi_file.addNote(self.track, self.channel, self.key_base + relative_pitch + interval,
                                   bar_start_time + self.first_note_duration + 1, self.beats_in_bar / 4, self.volume)
