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
TWELFTH_ROOT_OF_2 = 2**(1/float(12))
A4_FREQUENCY = 440

def note_to_frequency(note_and_octave):
    half_steps = note_half_steps_from_a(note_and_octave)
    return A4_FREQUENCY * TWELFTH_ROOT_OF_2 ** half_steps


def split_note(note_and_octave):
    characters = list(note_and_octave)
    octave = int(characters.pop())
    note = ''.join(characters)
    return { "note": note, "octave": octave}

def note_half_steps_from_a(note_and_octave):
    note_and_octave = note_and_octave.lower()
    note_and_octave = split_note(note_and_octave)

    note_index = OCTAVE_NOTES[note_and_octave['note']]
    a_index = OCTAVE_NOTES['a']
    octave_modifier = 12 * (note_and_octave['octave'] - 4)
    return note_index - a_index + octave_modifier
