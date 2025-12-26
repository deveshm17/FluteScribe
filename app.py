import sys
from transcriber.melody_extractor import extract_flute_melody

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python app.py <audio_file>")
        sys.exit(1)

    extract_flute_melody(sys.argv[1])
