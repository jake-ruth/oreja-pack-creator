import mido
import librosa

# Replace 'your_file.mid' with the path to your MIDI file
midi_file = 'Bergonzi.midi'

# array to store note names
note_names = []

# Open the MIDI file
mid = mido.MidiFile(midi_file)

track_name = 'Lines'

# Iterate over each message in the track
for msg in mid.tracks[3]:
    if msg.type == 'track_name':
        print(msg.name)
    # Check if the message is a note-on or note-off event
    if msg.type == 'note_on':
        # Extract the note number
        note_number = msg.note
        # Convert note number to note name (assuming MIDI standard tuning)
        note_name = librosa.midi_to_note(note_number)
        # note_name = 'G' 
        # Add note name to set
        note_names.append(note_name)

# Print out all unique note names
print("All Note Names:", note_names)

