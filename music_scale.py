OCTAVE_NOTES = {
    "c":1,
    "c#":2,
    "db":2,
    "d":3,
    "d#":4,
    "eb":4,
    "e":5,
    "f":6,
    "f#":7,
    "gb":7,
    "g":8,
    "g#":9,
    "ab":9,
    "a":10,
    "a#":11,
    "bb":11,
    "b":12,
}

def split_note(note_and_octave):
    characters = list(note_and_octave)
    octave = characters.pop()
    note = ''.join(characters)
    return { "note": note, "octave": octave}

def note_half_steps_from_a(note):
    note = note.lower()
    note_index = OCTAVE_NOTES[note]
    a_index = OCTAVE_NOTES['a']
    print note_index - a_index
    return note_index - a_index
