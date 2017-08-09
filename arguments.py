import argparse


def get_arguments():
    parser = argparse.ArgumentParser(description=("MIDI music generator is a script for generating "
                                                  "simple MIDI music with different opions"))
    parser.add_argument('--narcossity', '-n', type=int, choices=range(1, 5), dest='narcossity_level', default=1,
                        help="Change the level of narcossity.")
    parser.add_argument('-p', "--path", type=str, dest="fileName", default="myMidi.mid",
                        help=("Sets the path of the generated midi file. Note, that the name "
                              "should end witch .mid. If only a name is given the file is created in"
                              "working directory"))
    parser.add_argument('-k', '--key', type=int, dest='key', default=7,
                        help="Set the base key for whole midi file. The KEY should be"
                             "between 0 and 12.")
    parser.add_argument('-b', '--beats', type=int, dest='beats_per_bar', default=16,
                        help="Set the number of beats per bar. BEATS_PER_BAR should be between 4 and 64")
    parser.add_argument('-B', '--bars', type=int, dest='number_of_bars', default=16,
                        help="Set the number of bars = length of the music")
    parser.add_argument('-j', '--jazz', dest='genre', action='store_const', const=1,
                        help='Sets genre type to jazz. Setting flag -j is similar to setting: '
                             '-n 2 -b 20')
    parser.add_argument('-s', '--samba', dest='genre', action='store_const', const=2,
                        help='Sets genre type to samba. Setting flag -s is similar to setting: '
                             '-n 4 -b 16')

    arguments = parser.parse_args()

    if arguments.key not in range(0, 12) or arguments.beats_per_bar not in range(4, 65):
        print("Bad arguments, type -h or --help to see help message")
        exit(1)

    if arguments.genre == 1:
        arguments.narcossity_level = 2
        arguments.beats_per_bar = 20
    elif arguments.genre == 2:
        arguments.narcossity_level = 4
        arguments.beats_per_bar = 16

    return arguments
