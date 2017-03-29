from instrument import Instrument


class Piano:
    def __init__(self, key_base, track, channel, volume, beats_in_bar, midi_file, narcossity_level):
        midi_file.addProgramChange(track, channel, 0, Instrument.AcousticGrandPiano)
        self.MidiFile = midi_file
        self.keyBase = 60 + key_base
        self.track = track
        self.channel = channel
        self.volume = volume
        self.beatsInBar = beats_in_bar
        self.numberOfTicksPerBeat = beats_in_bar // 4
        self.narcossity_level = narcossity_level

    def generate_until_bar(self, bar_start_time, chord, relative_pitch):
        time = bar_start_time
        if self.narcossity_level == 2:
            for interval in chord:
                self.MidiFile.addNote(self.track, self.channel, self.keyBase + relative_pitch + interval,
                                      time + self.numberOfTicksPerBeat // 2, self.numberOfTicksPerBeat, self.volume)
                self.MidiFile.addNote(self.track, self.channel, self.keyBase + relative_pitch + interval,
                                      time + self.numberOfTicksPerBeat + self.numberOfTicksPerBeat // 2,
                                      self.beatsInBar - (2 * self.numberOfTicksPerBeat), self.volume)
        elif self.narcossity_level == 4:
            for i in range(0, self.beatsInBar):
                for interval in chord:
                    if i % self.numberOfTicksPerBeat == self.numberOfTicksPerBeat - 1:
                        self.MidiFile.addNote(self.track, self.channel, self.keyBase + relative_pitch + interval,
                                              time + i, self.numberOfTicksPerBeat // 2, self.volume)
                    elif i % self.numberOfTicksPerBeat >= self.numberOfTicksPerBeat // 2:
                        self.MidiFile.addNote(self.track, self.channel, self.keyBase + relative_pitch + interval,
                                              time + i, 1, self.volume)
        else:
            if relative_pitch > 5:
                relative_pitch = relative_pitch - 12
            for i in range(0, self.beatsInBar):
                self.MidiFile.addNote(self.track, self.channel, self.keyBase + relative_pitch + chord[i % 4],
                                      time + i, 1, self.volume)
