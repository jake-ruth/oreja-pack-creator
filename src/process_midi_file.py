import mido
import librosa

def process_midi_file(midi_file_name):
    note_names = []

    # Open the MIDI file
    mid = mido.MidiFile(midi_file_name)

    # first track is the title 
    title_track = mid.tracks[0]
    notes_track = mid.tracks[1]
    title = ''

    for msg in title_track:
        if msg.type == 'track_name':
            title = msg.name

    # Iterate over each message in the track
    for msg in notes_track:
        print(msg)
        if msg.type == 'track_name':
            print('Track Name: ' + msg.name)

        # Check if the message is a note-on or note-off event
        if msg.type == 'note_on':
            print(msg)
            # Extract the note number
            note_number = msg.note
            # Convert note number to note name (assuming MIDI standard tuning)
            note_name = librosa.midi_to_note(note_number)
            # Decode the unicode sharp and flat characters
            decoded_note_name = (
                     note_name.encode()
                     .decode("utf-8")
                     .replace(u"\u266f", "#")
                     .replace(u"\266D", "b")
                     )
            # Add note name to array
            note_names.append(decoded_note_name)

    return note_names, title

