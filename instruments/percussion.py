import random


class Percussion:
    bass_drum = 35
    low_tom = 41
    maracas = 70

    def __init__(self, track, channel, volume, beats_in_bar, midi_file, narcossity_level):
        self.midi_file = midi_file
        self.track = track
        self.channel = channel
        self.volume = volume
        self.beats_in_bar = beats_in_bar
        self.number_of_ticks_per_beat = beats_in_bar // 4
        self.samba_beat = -1
        self.narcossity_level = narcossity_level

    def _generate_samba_beat(self):
        samba_beat_list = list()
        for i in range(0, self.beats_in_bar):
            samba_beat_list.insert(i, list())
            if i % self.number_of_ticks_per_beat == 0:
                samba_beat_list[i].append(61)
            else:
                samba_beat_list[i].append(60)
        for i in range(0, self.beats_in_bar // 2):
            samba_beat_list[2 * i].append(54)
            samba_beat_list[2 * i + 1].append(44)
        for i in range(0, 25):
            samba_beat_list[random.randint(0, self.beats_in_bar - 1)].append(random.randint(35, 81))
        return samba_beat_list

    def _add_samba_beat(self, time):
        for i in range(0, self.beats_in_bar):
            for note in self.samba_beat[i]:
                self.midi_file.addNote(self.track, self.channel, note, time + i, 1, self.volume)

    def generate_until_bar(self, bar_start_time):
        if self.narcossity_level == 3:
            beat_count = self.number_of_ticks_per_beat // 2
            for i in range(0, self.beats_in_bar):
                if beat_count != 0 and i % beat_count == 0:
                    if i // beat_count % 8 == 0 or i // beat_count % 8 == 3 or i // beat_count % 8 == 5 or i // beat_count % 8 == 7:
                        self.midi_file.addNote(self.track, self.channel, Percussion.low_tom, bar_start_time + i,
                                               beat_count, self.volume)
                    else:
                        self.midi_file.addNote(self.track, self.channel, Percussion.bass_drum, bar_start_time + i,
                                               beat_count, self.volume)
                elif beat_count == 0:
                    if i % 4 == 0:
                        self.midi_file.addNote(self.track, self.channel, Percussion.low_tom, bar_start_time,
                                               1, self.volume)
                    else:
                        self.midi_file.addNote(self.track, self.channel, Percussion.bass_drum, bar_start_time,
                                               1, self.volume)
        elif self.narcossity_level == 2:
            for i in range(0, self.beats_in_bar):
                if i % self.number_of_ticks_per_beat == 0:
                    if (i // self.number_of_ticks_per_beat) == 1 or (i // self.number_of_ticks_per_beat) == 3:
                        self.midi_file.addNote(self.track, self.channel, Percussion.maracas, bar_start_time + i,
                                               self.number_of_ticks_per_beat, self.volume)
                    elif i // self.number_of_ticks_per_beat == 0 or i // self.number_of_ticks_per_beat == 2:
                        self.midi_file.addNote(self.track, self.channel, Percussion.low_tom, bar_start_time + i,
                                               self.number_of_ticks_per_beat, self.volume)
        elif self.narcossity_level == 4:
            if self.samba_beat == -1:
                self.samba_beat = self._generate_samba_beat()
                self._add_samba_beat(bar_start_time)
            else:
                self._add_samba_beat(bar_start_time)
        else:
            for i in range(0, self.beats_in_bar):
                if i % self.number_of_ticks_per_beat == 0:
                    if i == 0:
                        self.midi_file.addNote(self.track, self.channel, Percussion.low_tom, bar_start_time,
                                               self.number_of_ticks_per_beat, self.volume)
                    else:
                        self.midi_file.addNote(self.track, self.channel, Percussion.bass_drum, bar_start_time + i,
                                               self.number_of_ticks_per_beat, self.volume)
