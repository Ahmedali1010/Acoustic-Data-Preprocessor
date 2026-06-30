import os
import shutil
import argparse
import random

def split_dataset(source_dir, test_dir, split_percentage, mode='copy', seed=42):
    """
    Partitions the acoustic dataset into training and testing subsets.
    Uses reproducible stochastic sampling to prevent temporal bias.
    """
    print(f"--- Initializing Dataset Splitter ({split_percentage * 100}% per speaker) ---")
    
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)

    # Set random seed for reproducibility in academic research
    random.seed(seed)

    speakers_processed = 0
    total_files_processed = 0
    
    for speaker_id in os.listdir(source_dir):
        source_speaker_path = os.path.join(source_dir, speaker_id)
        
        if os.path.isdir(source_speaker_path):
            all_files = sorted(os.listdir(source_speaker_path))
            audio_files = [f for f in all_files if f.endswith(('.wav', '.ogg', '.mp3'))]
            
            total_files = len(audio_files)
            files_to_move_count = int(total_files * split_percentage)
            
            if files_to_move_count > 0:
                # Stochastic sampling ensures unbiased test distribution
                selected_files = random.sample(audio_files, files_to_move_count)
                
                dest_speaker_path = os.path.join(test_dir, speaker_id)
                if not os.path.exists(dest_speaker_path):
                    os.makedirs(dest_speaker_path)
                
                for filename in selected_files:
                    src_file = os.path.join(source_speaker_path, filename)
                    dst_file = os.path.join(dest_speaker_path, filename)
                    
                    if not os.path.exists(dst_file):
                        if mode == 'move':
                            shutil.move(src_file, dst_file)
                        else:
                            # Preserves file metadata during copy
                            shutil.copy2(src_file, dst_file)
                        total_files_processed += 1
                
                speakers_processed += 1

    print(f"\n--- Data Partitioning Complete ---")
    print(f"Operation Mode: {mode.upper()}")
    print(f"Total Speakers Processed: {speakers_processed}")
    print(f"Total Files Processed: {total_files_processed}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Dataset Train/Test Splitter for Acoustic Corpora")
    parser.add_argument("--source", type=str, required=True, help="Path to the main dataset directory")
    parser.add_argument("--test", type=str, required=True, help="Path to the destination test directory")
    parser.add_argument("--ratio", type=float, default=0.15, help="Test split ratio (default: 0.15 for 15%)")
    parser.add_argument("--mode", type=str, choices=['copy', 'move'], default='copy', help="Action to perform (default: copy)")
    
    args = parser.parse_args()

    if not os.path.exists(args.source):
        print(f"[ERROR] Source directory '{args.source}' does not exist.")
        exit(1)
        
    split_dataset(args.source, args.test, args.ratio, args.mode)
