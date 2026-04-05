# RemoPhysEmo: A Multimodal Emotion Dataset with Remotely Sensed Physiological Signals via Video and Radar

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

## 📊 Sample Visualization

[TODO: add sample images here, e.g., data collection setup, signal visualization, emotion annotation examples]

## 📂 Dataset Structure

```
mmdataset/
├── mmwave/                                # Millimeter-wave radar data
│   ├── {subject_id}/                      # e.g., 12/
│   │   ├── {subject_id}_{session}/        # e.g., 12_1/
│   │   │   ├── {subject_id}_{chunk}.mat   # Radar raw signal
│   │   │   └── rf_time.npy                # RF timestamp
│   │   └── ...
│   └── ...
│
├── webcam/                                # RGB webcam video frames
│   ├── {subject_id}/                      # e.g., 12/
│   │   ├── {subject_id}_{session}/        # e.g., 12_01/
│   │   │   ├── 0001.png                   # Video frame
│   │   │   ├── 0002.png
│   │   │   └── ...
│   │   └── ...
│   └── ...
│
├── ppg/                                   # PPG (photoplethysmography) data
│   ├── {subject_id}/                      # e.g., 12/
│   │   ├── {subject_id}_{session}.npy     # e.g., 12_1.npy
│   │   └── ...
│   └── ...
│
├── mmdataset3_30.xlsx                     # Emotion labels
└── fold.xlsx                              # Data split folds
```

**Naming convention:**
- `{subject_id}` — Subject index (e.g., `12`)
- `{subject_id}_{session}` — The N-th recording session of a subject (e.g., `12_1` means session 1 of subject 12)
- Each subject typically contains 8 sessions. All three modalities are temporally synchronized.

## 🗂️ Repository Structure

```
RemoPhysEmo/
├── data/       # Data preprocessing scripts
├── models/     # Baseline model implementations (e.g., ContrastPhys+, VitaNet, MER-MFVA, MVP)
├── scripts/    # Training and evaluation scripts
└── README.md
```

## 📥 Dataset Access

The dataset is available for download at: **[TODO: download link]**

The data are password-protected. Please download and sign the [End User License Agreement (EULA)]([TODO: EULA link]) and send it to **[TODO: email address]** to request access.

## ✏️ Citation

If you find our dataset or code helpful, please cite our paper:

```bibtex
@inproceedings{anonymous2026remophysemo,
  title={RemoPhysEmo: A multimodal emotion dataset with remotely sensed physiological signals via video and radar},
  author={Anonymous Author(s)},
  booktitle={Proceedings of the 33rd ACM International Conference on Multimedia},
  year={2026}
}
```
