import music21
import librosa

def process_midi_file(midi_file_name):

    note_sequences = []
    current_note_sequence_index = 0

    parsed = music21.converter.parse(midi_file_name)
    current_note_sequence = []

    for elem in parsed.flatten().notesAndRests:
        if elem.isRest and elem.fullName == 'Whole Rest':
            print(elem.fullName)
            # reset the current note sequence and increment index
            note_sequences.append(current_note_sequence)
            current_note_sequence = []
            current_note_sequence_index += 1 
        
        if elem.isNote:
            note_number = elem.pitches[0].midi
            note_name = librosa.midi_to_note(note_number)

             # Decode the unicode sharp and flat characters
            decoded_note_name = (
                     note_name.encode()
                     .decode("utf-8")
                     .replace(u"\u266f", "#")
                     .replace(u"\266D", "b")
                     )

            # Add note name to array
            current_note_sequence.append(decoded_note_name)

    if (len(current_note_sequence) > 0):
        note_sequences.append(current_note_sequence)


    print(note_sequences)


    return note_sequences

