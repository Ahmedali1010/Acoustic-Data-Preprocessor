# Acoustic-Data-Preprocessor
An automated acoustic preprocessing pipeline for partitioning raw speech corpora into uniform fixed-length utterances for CNN-based Speaker Identification and Verification (SIV).

# Acoustic Corpus Preprocessor for SIV

An automated acoustic preprocessing pipeline for partitioning raw speech corpora into uniform fixed-length utterances for CNN-based Speaker Identification and Verification (SIV).

## Overview
This repository provides an automated preprocessing pipeline designed for text-independent Speaker Identification and Verification (SIV) tasks. The script extracts fixed-length acoustic chunks from raw speech recordings (`.ogg` format) to generate uniform data structures suitable for high-dimensional acoustic feature extraction (e.g., 2D log Mel-spectrograms) and training Convolutional Neural Networks (CNNs).

## Features
* **Uniform Segmentation:** Partitions continuous audio streams into precise, fixed-duration chunks (default: 1.0 second) to ensure computational parameter efficiency.
* **Batch Processing:** Recursively traverses directory trees to process large-scale low-resource language corpora efficiently using `os.walk`.
* **Fault Tolerance:** Integrates robust exception handling to bypass corrupted acoustic samples without halting the pipeline execution.

## Prerequisites
Ensure the following dependencies are installed in your environment:
* Python 3.8+
* `pydub`
* `tqdm`
* `FFmpeg` (Must be installed natively and appended to the system `PATH`)

**Installation via requirements:**
```bash
pip install -r requirements.txt
Usage
Execute the preprocessing pipeline via the command line interface. Define the target directory containing the raw audio files and specify the desired utterance duration in milliseconds.

Bash
python audio_chunker.py --input /path/to/raw/dataset --chunk_ms 1000
Associated Dataset & Cross-Reference
This codebase was originally engineered to construct and partition a proprietary biometric dataset for Central Kurdish.

If you deploy this architecture in your research, or utilize the associated dataset, please refer to the primary repository:

Dataset Access: 10.17632/7rv22xjmdx.3

Citation:

Abdulrahman, Ayub Othman; Ali, Ahmad; jamal, Muhamad Jamal; Bakr, Zhyar (2026), “A Comprehensive Kurdish Speech Corpus for Speaker Identification and Verification in a Low-Resource Language Environment”, Mendeley Data, V3, doi: 10.17632/7rv22xjmdx.3

License
Distributed under the MIT License.
