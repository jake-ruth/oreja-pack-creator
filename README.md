### Goal of this Software
Given a MIDI file, output a Neurofret pack in the proper format 
```
  {
    "id": "c06a3838-9a3c-4b8d-b203-6c3b47c607eb",
    "title": "Triads",
    "root": "C",
    "scale": "major",
    "noteSequences": [
      ["C3", "E3", "G3"],
      ["F3", "A3", "C4"],
      ["G3", "B3", "D4"],
      ["E3", "G3", "B3"]
    ],
    "description": "Basic Triads",
    "difficulty": 1,
    "isPremium": false,
    "isFeatured": true,
    "isActive": true
  }
```

The program should take in a midi file (or multiples) and the number of notes per sequence

id - random UUID
title - obtained from the midi file
root - obtained from midi file?
scale - midi file?
noteSequences - this will be determined by the input
description - obtained from midi file
difficulty - obtained from input 
audit fields - auto-set to true for all

### Virtual Environment

Create the venv:
`python3 -m venv project_env`

Activate the venv
`source project_env/bin/activate`

Now, `which python` will show the python used in the venv

Now we can just use `pip install x` to install libraries

`pip freeze > requirements.txt`

Install from requirements.txt
`python -m pip install -r requirements.txt`

Deactivate the venv:
`deactivate`




