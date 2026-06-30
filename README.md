


# Acoustic Corpus Preprocessing and Partitioning Toolkit for SIV

An automated acoustic pipeline for processing raw speech corpora into uniform fixed-length utterances and performing stochastic train/test partitioning for CNN-based Speaker Identification and Verification (SIV).

## Overview
This repository provides two primary utilities designed for text-independent Speaker Identification and Verification (SIV) tasks:
1. **Audio Segmentation:** Extracts fixed-length acoustic chunks from raw speech recordings (`.ogg` format) to generate uniform data structures for high-dimensional feature extraction (e.g., 2D log Mel-spectrograms).
2. **Stochastic Partitioning:** Divides the processed dataset into training and testing subsets using reproducible random sampling to prevent temporal and sequential bias.

## Features
* **Uniform Segmentation:** Partitions continuous audio streams into precise, fixed-duration chunks (default: 1.0 second) for computational parameter efficiency.
* **Stochastic Sampling:** Implements random seed generation for unbiased and reproducible train/test splits, strictly adhering to academic integrity standards.
* **Non-Destructive Operations:** Employs file copying by default to preserve the structural integrity of the original raw corpus during dataset splitting.
* **Fault Tolerance:** Integrates robust exception handling to bypass corrupted acoustic samples without halting the pipeline execution.

## Prerequisites
Ensure the following dependencies are installed in your environment:
* Python 3.8+
* `pydub`
* `tqdm`
* `FFmpeg` (Must be installed natively and appended to the system `PATH`)

**Installation:**
``bash
pip install -r requirements.txt


Usage
1. Audio Segmentation
Execute the chunking pipeline to normalize utterance duration.
python audio_chunker.py --input /path/to/raw/dataset --chunk_ms 1000


2. Dataset Partitioning
Split the segmented dataset into training and testing subsets. The default split ratio is 15% for testing (0.15).

python dataset_splitter.py --source /path/to/segmented/dataset --test /path/to/test/output --ratio 0.15 --mode copy


Associated Dataset & Cross-Reference
This codebase was originally engineered to construct and partition a proprietary biometric dataset for Central Kurdish.

If you deploy this architecture in your research, or utilize the associated dataset, please refer to the primary repository:

Dataset Access: 10.17632/7rv22xjmdx.3

Citation:

Abdulrahman, Ayub Othman; Ali, Ahmad; jamal, Muhamad Jamal; Bakr, Zhyar (2026), “A Comprehensive Kurdish Speech Corpus for Speaker Identification and Verification in a Low-Resource Language Environment”, Mendeley Data, V3, doi: 10.17632/7rv22xjmdx.3

License
Distributed under the MIT License.
