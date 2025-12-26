from basic_pitch.inference import predict
from basic_pitch import ICASSP_2022_MODEL_PATH
import pretty_midi

def extract_flute_melody(audio_path):
    _, midi_data, _ = predict(audio_path, ICASSP_2022_MODEL_PATH)

    output_midi = pretty_midi.PrettyMIDI()
    flute = pretty_midi.Instrument(
        program=pretty_midi.instrument_name_to_program("Flute")
    )

    for instrument in midi_data.instruments:
        for note in instrument.notes:
            # Flute playable range
            if 60 <= note.pitch <= 96:
                flute.notes.append(note)

    output_midi.instruments.append(flute)
    output_midi.write("flute_output.mid")

    print("Generated flute_output.mid")
