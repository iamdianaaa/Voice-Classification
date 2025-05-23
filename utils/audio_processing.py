import librosa
import numpy as np
import matplotlib.pyplot as plt
import librosa.display

def load_audio(file_path, sr=16000, max_len=3):
    y, sr = librosa.load(file_path, sr=sr)
    max_samples = sr * max_len
    if len(y) > max_samples:
        y = y[:max_samples]
    else:
        y = np.pad(y, (0, max_samples - len(y)))
    return y, sr

def extract_mfcc(y, sr, num_mfcc=13):
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=num_mfcc)
    return mfcc

def extract_mfcc_from_file(file_path, sample_rate=16000, num_mfcc=13, max_len=3):
    try:
        y, sr = load_audio(file_path, sr=sample_rate, max_len=max_len)
        mfcc = extract_mfcc(y, sr, num_mfcc)
        return mfcc
    except Exception as e:
        print(f"⚠️ Error with {file_path}: {e}")
        return None

def visualize_waveform_and_mel(file_path, sr=16000, max_len=3):
    y, sr = load_audio(file_path, sr=sr, max_len=max_len)
    
    mel_spec = librosa.feature.melspectrogram(y=y, sr=sr)
    mel_db = librosa.power_to_db(mel_spec, ref=np.max)

    print(f"Signal shape: {y.shape}, Mel shape: {mel_db.shape}")

    plt.figure(figsize=(14, 5))

    plt.subplot(1, 2, 1)
    plt.title("Waveform")
    librosa.display.waveshow(y, sr=sr)

    plt.subplot(1, 2, 2)
    plt.title("Mel Spectrogram")
    librosa.display.specshow(mel_db, x_axis='time', y_axis='mel', sr=sr, fmax=8000)
    plt.colorbar(format='%+2.0f dB')

    plt.tight_layout()
    plt.show()