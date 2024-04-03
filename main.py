import mido
import librosa
import json
import os

# Replace 'your_file.mid' with the path to your MIDI file
midi_file = 'Bergonzi.midi'

# array to store note names
note_names = []

# Open the MIDI file
mid = mido.MidiFile(midi_file)

# first track is the title etc
title_track = mid.tracks[0]
notes_track = mid.tracks[1]
title = ''

for msg in title_track:
    if msg.type == 'track_name':
        title = msg.name

# Iterate over each message in the track
for msg in notes_track:
    if msg.type == 'track_name':
        print(msg.name)

    # Check if the message is a note-on or note-off event
    if msg.type == 'note_on':
        # Extract the note number
        note_number = msg.note
        # Convert note number to note name (assuming MIDI standard tuning)
        note_name = librosa.midi_to_note(note_number)
        # Add note name to array
        note_names.append(note_name)

# Print out all unique note names
print("All Note Names:", note_names)

dictionary ={ 
    "name" : "sathiyajith", 
    "rollno" : 56, 
    "cgpa" : 8.6, 
    "phonenumber" : "9976770500"
} 

if not os.path.exists('packs'):
    os.makedirs('packs')

#open an object with following inputs: 'name_of_file.json', 'w'
#dump the content fromt he dictionary into the outfile
with open("packs/" + title + ".json", "w") as outfile: 
    json.dump(dictionary, outfile)

