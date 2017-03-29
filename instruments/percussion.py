import random


class Percussion:
    BassDrum = 35
    LowTom = 41
    Maracas = 70

    def __init__(self, track, channel, volume, beats_in_bar, midi_file, narcossity_level):
        self.MidiFile = midi_file
        self.track = track
        self.channel = channel
        self.volume = volume
        self.beatsInBar = beats_in_bar
        self.numberOfTicksPerBeat = beats_in_bar // 4
        self.sambaBeat = -1
        self.narcossity_level = narcossity_level

    def _generate_samba_beat(self):
        samba_beat_list = list()
        for i in range(0, self.beatsInBar):
            samba_beat_list.insert(i, list())
            if i % self.numberOfTicksPerBeat == 0:
                samba_beat_list[i].append(61)
            else:
                samba_beat_list[i].append(60)
        for i in range(0, self.beatsInBar // 2):
            samba_beat_list[2 * i].append(54)
            samba_beat_list[2 * i + 1].append(44)
        for i in range(0, 25):
            samba_beat_list[random.randint(0, self.beatsInBar - 1)].append(random.randint(35, 81))
        return samba_beat_list

    def _add_samba_beat(self, time):
        for i in range(0, self.beatsInBar):
            for note in self.sambaBeat[i]:
                self.MidiFile.addNote(self.track, self.channel, note, time + i, 1, self.volume)

    def generate_until_bar(self, bar_start_time):
        if self.narcossity_level == 3:
            beat_count = self.numberOfTicksPerBeat // 2
            for i in range(0, self.beatsInBar):
                if beat_count != 0 and i % beat_count == 0:
                    if i // beat_count % 8 == 0 or i // beat_count % 8 == 3 or i // beat_count % 8 == 5 or i // beat_count % 8 == 7:
                        self.MidiFile.addNote(self.track, self.channel, Percussion.LowTom, bar_start_time + i,
                                              beat_count, self.volume)
                    else:
                        self.MidiFile.addNote(self.track, self.channel, Percussion.BassDrum, bar_start_time + i,
                                              beat_count, self.volume)
                elif beat_count == 0:
                    if i % 4 == 0:
                        self.MidiFile.addNote(self.track, self.channel, Percussion.LowTom, bar_start_time,
                                              1, self.volume)
                    else:
                        self.MidiFile.addNote(self.track, self.channel, Percussion.BassDrum, bar_start_time,
                                              1, self.volume)
        elif self.narcossity_level == 2:
            for i in range(0, self.beatsInBar):
                if i % self.numberOfTicksPerBeat == 0:
                    if (i // self.numberOfTicksPerBeat) == 1 or (i // self.numberOfTicksPerBeat) == 3:
                        self.MidiFile.addNote(self.track, self.channel, Percussion.Maracas, bar_start_time + i,
                                              self.numberOfTicksPerBeat, self.volume)
                    elif i // self.numberOfTicksPerBeat == 0 or i // self.numberOfTicksPerBeat == 2:
                        self.MidiFile.addNote(self.track, self.channel, Percussion.LowTom, bar_start_time + i,
                                              self.numberOfTicksPerBeat, self.volume)
        elif self.narcossity_level == 4:
            if self.sambaBeat == -1:
                self.sambaBeat = self._generate_samba_beat()
                self._add_samba_beat(bar_start_time)
            else:
                self._add_samba_beat(bar_start_time)
        else:
            for i in range(0, self.beatsInBar):
                if i % self.numberOfTicksPerBeat == 0:
                    if i == 0:
                        self.MidiFile.addNote(self.track, self.channel, Percussion.LowTom, bar_start_time,
                                              self.numberOfTicksPerBeat, self.volume)
                    else:
                        self.MidiFile.addNote(self.track, self.channel, Percussion.BassDrum, bar_start_time + i,
                                              self.numberOfTicksPerBeat, self.volume)
