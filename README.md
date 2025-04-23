# 🧠 Age Classification Based on Audio Recordings

This project is part of the CS251/CS340 Machine Learning course at the American University of Armenia.  
We aim to build a machine learning pipeline that classifies speakers into age groups based on voice recordings from the [Mozilla Common Voice](https://commonvoice.mozilla.org/en/datasets) dataset.

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

### 2. 🐳 Docker Setup (Recommended)

### 🔧 Build and Run

```bash
docker-compose build
docker-compose up
```

This will build the environment with all required Python packages and mount your local data.

### 💾 Docker Volume Mounts
The local folders are mounted into the container as:

- **data/** → **/app/data/**
- **notebooks/** → **/app/notebooks/**

This setup ensures large datasets are never copied into the image itself, but remain accessible from inside the container.

### 🌐 Access JupyterLab

After running docker-compose up, open the following URL in your browser:

```bash
http://localhost:8888
```

You will be prompted for a token.

### 🔍 Finding the Token

To find your JupyterLab access token, open a new terminal and run:

```bash
docker ps
```

Copy your container name or ID, then run:
```bash
docker exec -it <your_container_id_or_name> jupyter server list
```

Example output:
```bash
Currently running servers:
http://127.0.0.1:8888/lab?token=abc123def456... :: /app
```
Paste the token (**abc123def456...**) into the login screen.

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
