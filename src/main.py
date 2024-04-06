from create_packs import create_packs
from process_midi_file import process_midi_file

notes_per_sequence = 4
midi_file_name = '../TestMidi.mid'

note_names, title = process_midi_file(midi_file_name)
create_packs(title, title, notes_per_sequence, note_names);
