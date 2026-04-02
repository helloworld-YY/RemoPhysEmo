# PhysEmo: A multimodal emotion dataset with remotely sensed physiological signals via video and radar

This repository contains the official implementation and dataset introduction for the paper **"RemoPhysEmo: A multimodal emotion dataset with remotely sensed physiological signals via video and radar"**.

## 📖 Introduction

Emotion recognition is a fundamental task in affective computing. Existing multimodal emotion research concerns more of non-physiological modalities, such as video, audio, and text, whereas physiological signals remain insufficiently explored. 

To bridge this gap, we introduce **RemoPhysEmo**, a new multimodal emotion dataset with remotely sensed physiological signals consisting of photoplethysmography (PPG), millimeter-wave radar, and facial videos. 

## ✨ Key Features

* **Multimodal Sensing**: Synchronized facial videos and millimeter-wave radar data collected during emotion elicitation tasks.
* **Large-Scale**: Contains 149 subjects' multimodal data.
* **Rich Annotations**: Provides clip-level categorical emotion labels, dimensional valence-arousal scores, and fine-grained emotion intensity fluctuation scores for every 3-second segment.

## 🚀 Tasks Supported

Our dataset and baselines support the following two main tasks:
1. **Task 1: Multimodal rPPG Measurement**
2. **Task 2: Multimodal Emotion Recognition**

## 📂 Repository Structure

- `data/` : Contains scripts for data preprocessing.
- `models/` : Implementations of baseline models (e.g., ContrastPhys+, VitaNet, MER-MFVA, MVP).
- `scripts/` : Training and evaluation scripts.

## 🛠️ Getting Started

### 1. Dataset Access
The pre-processed version of the dataset will be shared online. The data sharing process will be regulated by signing a license agreement. *(Instructions and links for downloading will be updated here).*

### 2. Environment Setup
*(To be updated: Environment dependencies and instructions)*

### 3. Training and Evaluation
*(To be updated: Instructions for running baseline models)*

## ✏️ Citation

If you find our dataset or code helpful, please cite our paper:

```bibtex
@inproceedings{anonymous2026remophysemo,
  title={RemoPhysEmo: A multimodal emotion dataset with remotely sensed physiological signals via video and radar},
  author={Anonymous Author(s)},
  booktitle={Proceedings of the 33rd ACM International Conference on Multimedia},
  year={2026}
}
