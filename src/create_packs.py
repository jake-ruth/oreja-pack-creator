import os
import json
import uuid

def create_packs(title, description, note_sequences):
    print(note_sequences)

    print('generating note sequences...')

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

