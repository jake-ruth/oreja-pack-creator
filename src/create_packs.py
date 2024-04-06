import os
import json
import numpy
import uuid

def create_packs(title, description, notes_per_sequence, all_notes):
    note_sequences = []
    index = 0 

    # using numpy to make array easier to parse
    arr = numpy.array(all_notes)
    print('generating note sequences...')

    while index < len(all_notes):
        sequence = arr[index:index + notes_per_sequence]
        note_sequences.append(sequence.tolist())
        index += notes_per_sequence

    dictionary ={
        "id": str(uuid.uuid4()),
        "title": title,
        "description": description,
        "noteSequences": note_sequences,
        "isFeatured": False,
        "isPremium": True,
        "isActive": True 
    } 

    if not os.path.exists('packs'):
        os.makedirs('packs')
    # have to jsonify the dict 
    with open("packs/" + title + ".json", "w") as outfile: 
        json.dump(dictionary, outfile, indent=2)

