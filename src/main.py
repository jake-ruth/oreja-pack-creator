from create_packs import create_packs
from process_midi_file import process_midi_file
import sys

midi_file_name = '../TestMidi.mid'
title = sys.argv[1]

note_sequences = process_midi_file(midi_file_name)
create_packs(title, title, note_sequences);
