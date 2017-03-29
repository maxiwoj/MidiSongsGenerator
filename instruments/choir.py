from instrument import Instrument


class Choir:
    def __init__(self, key_base, track, channel, volume, beats_in_bar, midi_file):
        midi_file.addProgramChange(track, channel, 0, Instrument.ChoirAahs)
        self.MidiFile = midi_file
        self.keyBase = 36 + key_base
        self.track = track
        self.channel = channel
        self.volume = volume
        self.beatsInBar = beats_in_bar
        self.firstNoteDuration = 3 * beats_in_bar // 4 - 1

    def generate_until_bar(self, bar_start_time, chord, relative_pitch):
        if relative_pitch > 7:
            relative_pitch -= 12
        for interval in chord:
            self.MidiFile.addNote(self.track, self.channel, self.keyBase + relative_pitch + interval,
                                  bar_start_time, self.firstNoteDuration, self.volume)
            self.MidiFile.addNote(self.track, self.channel, self.keyBase + relative_pitch + interval,
                                  bar_start_time + self.firstNoteDuration + 1, self.beatsInBar / 4, self.volume)
