from instruments.instrument import Instrument



class Bass:
    def __init__(self, key_base, track, channel, volume, beats_in_bar, midi_file, narcossity_level):
        midi_file.addProgramChange(track, channel, 0, Instrument.ElectricBass_pick)
        self.MidiFile = midi_file
        self.keyBase = 24 + key_base
        self.track = track
        self.channel = channel
        self.volume = volume
        self.beatsInBar = beats_in_bar
        self.numberOfTicksPerBeat = beats_in_bar // 4
        self.narcossity_level = narcossity_level

    def generate_until_bar(self, bar_start_time, chord, stopien):
        time = bar_start_time
        for interval in chord:
            if self.narcossity_level == 1:
                self.MidiFile.addNote(self.track, self.channel, self.keyBase + stopien + interval,
                                      time, self.numberOfTicksPerBeat, self.volume)
            else:
                beatCount = self.numberOfTicksPerBeat // 2
                for i in range(0, self.numberOfTicksPerBeat):
                    if beatCount != 0 and i % beatCount == 0:
                        self.MidiFile.addNote(self.track, self.channel, self.keyBase + stopien + interval,
                                              time + i, beatCount, self.volume)
                    elif beatCount == 0:
                        self.MidiFile.addNote(self.track, self.channel, self.keyBase + stopien + interval,
                                              time + i, 1, self.volume)
            time += self.numberOfTicksPerBeat
