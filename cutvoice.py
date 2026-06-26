import os
import argparse
from pydub import AudioSegment
from tqdm import tqdm

def process_audio_files(input_dir, chunk_ms):
    """
    Processes acoustic .ogg files, normalizing them into fixed-length chunks 
    suitable for 2D-CNN feature extraction.
    """
    folders_to_process = []
    for root, dirs, files in os.walk(input_dir):
        folders_to_process.append((root, files))

    print(f"Found {len(folders_to_process)} directories to process...")

    for root, files in tqdm(folders_to_process, desc="Processing Audio Utterances"):
        original_ogg_file = None
        for f in files:
            if f.endswith(".ogg"):
                original_ogg_file = f
                break
        
        if original_ogg_file:
            file_path = os.path.join(root, original_ogg_file)
            file_stem = os.path.splitext(original_ogg_file)[0]

            try:
                audio = AudioSegment.from_ogg(file_path)
                audio_length = len(audio)

                for i, t in enumerate(range(0, audio_length, chunk_ms)):
                    chunk_start = t
                    chunk_end = t + chunk_ms
                    chunk = audio[chunk_start:chunk_end]

                    # Strictly enforce uniform utterance duration (e.g., 1.0 second)
                    if len(chunk) == chunk_ms:
                        chunk_filename = f"{file_stem}_chunk_{i:04d}.ogg"
                        chunk_output_path = os.path.join(root, chunk_filename)
                        chunk.export(chunk_output_path, format="ogg")

            except Exception as e:
                print(f"\n[ERROR] Audio extraction failed for {file_path}. Root cause: {repr(e)}")


if __name__ == "__main__":
    # Command-line argument parsing for dynamic execution
    parser = argparse.ArgumentParser(description="Acoustic Corpus Preprocessing Script for SIV")
    parser.add_argument("--input", type=str, required=True, help="Path to the raw audio dataset folder")
    parser.add_argument("--chunk_ms", type=int, default=1000, help="Chunk length in milliseconds (default: 1000ms)")
    
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"Error: The directory '{args.input}' does not exist.")
        sys.exit(1)
        
    print(f"Initializing preprocessing pipeline for dataset: {args.input}")
    process_audio_files(args.input, args.chunk_ms)
    print("\nData partitioning and preprocessing complete!")