# 🧠 Age Classification Based on Audio Recordings

This project is part of the CS251/CS340 Machine Learning course at the American University of Armenia.  
We aim to build a machine learning pipeline that classifies speakers into age groups based on voice recordings from the [Mozilla Common Voice](https://commonvoice.mozilla.org/en/datasets) dataset.

To run the project without errors:

1. Download the [Common Voice - Armenian - Common Voice Corpus 21.0 | 3/19/2025](https://commonvoice.mozilla.org/en/datasets)
2. Extract the contents and place them into: **data/raw**
3. (Optional) You can run `docker-compose up -d` to preprocess audio and extract features using the container.
4. Preprocessed MFCC features (if already created) will appear in: **data/processed/**

---

## 🧩 Problem Formulation

Given a set of voice recordings labeled with age information, the objective is to:
- Preprocess raw audio data into meaningful features (e.g. MFCCs)
- Train machine learning models to classify speaker age into defined age bins (e.g. `teen`, `adult`, `senior`)
- Evaluate performance using standard classification metrics

---

## 🚀 Getting Started

### 1. 📦 Clone the Repository

```bash
git clone https://github.com/iamdianaaa/Voice-Classification.git
cd Voice-Classification
```

### 🧪 Project Structure
```bash
.
├── data/                   # Raw + processed audio data
│   ├── raw/
│   └── processed/
├── notebooks/              # Jupyter Notebooks for each pipeline stage
│   ├── 01_data_preprocessing.ipynb
│   ├── 02_model_development.ipynb
│   └── 03_model_evaluation.ipynb
├── utils/                  # Helper scripts
│   └── audio_processing.ipynb
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

### 👥 Team Members

- Data Preprocessing - **Albert Simonyan**
- Model Training - **Gayane Hovsepyan**
- Evaluation - **Diana Mkrtchyan**
