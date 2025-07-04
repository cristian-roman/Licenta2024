# 🧠 Detection of Endometriosis Using Advanced Deep Learning Techniques

This repository contains the full implementation of a deep learning pipeline for the automatic detection of endometriosis via medical imaging. It was developed as part of a Bachelor’s thesis at **"Alexandru Ioan Cuza" University of Iași**, Faculty of Computer Science.

> **Title (RO):** Detecția endometriozei folosind tehnici avansate de deep learning  
> **Author:** Cristian-Ioan Roman  
> **Supervisor:** Lector Dr. Cristian Frăsinaru  
> **Session:** July 2024

---

## 📄 Abstract

Endometriosis is a gynecological condition characterized by the growth of uterine tissue outside the uterus, leading to pain and infertility. While laparoscopy remains the gold standard for diagnosis, it is invasive and delayed. This project proposes a non-invasive alternative using U-Net enhanced with **multi-path encoders** and **graph convolutional networks (GCNs)** to segment endometriotic cysts in CT and MRI images.

---

## 🧩 Core Features

- 🏥 **Medical Image Segmentation**: Detect ovarian cysts in transvaginal ultrasound (TVUS), CT, or MRI
- 🧬 **U-Net-based Architecture**: Extended with multi-path encoders and GCN-based refinement
- 📊 **Evaluation Metrics**: Dice, F1-score, Precision, Recall, Accuracy
- 💾 **Custom Preprocessing**: Multithreaded image slicing, grayscale normalization, MongoDB/GridFS integration
- 📈 **Ablation Study**: Measures impact of GCNs and bias layers on performance
- ⚙️ **Two-Stage Training**:
  - **Phase I**: Pretraining on heart and prostate MRI data (Medical Segmentation Decathlon)
  - **Phase II**: Fine-tuning on CT images from a private clinic (73 annotated samples)

---

## 🗂 Repository Structure

```
Licenta2024-main/
├── Extractor/
│   ├── Data/                 # Data loaders, slicers, ref generators
│   ├── StatisticsClasses/    # Data statistics generators
│   ├── app_init/             # Logger and config manager
│   ├── main.py               # Entry point for training
│   ├── config.json           # General configuration file
│   └── example_secrets.json  # Template for DB credentials
├── README.md                 # (This file)
```

---

## 🔧 Requirements

- Python 3.8+
- NumPy, PyTorch
- MongoDB with GridFS
- Optional: NVIDIA GPU for training

---

## 🚀 Running the Project

1. **Setup MongoDB (Optional):**
   ```bash
   bash Extractor/example_create_mongo_docker.sh
   ```

2. **Configure credentials:**
   Copy `example_secrets.json` to `secrets.json` and update it with MongoDB access.

3. **Run Training:**
   ```bash
   cd Extractor
   python main.py
   ```

4. **Output:**
   - Binary segmentation masks (white = cyst, black = normal)
   - Stored in MongoDB or local directory
   - Evaluation logs (Dice, Recall, F1, etc.)

---

## 📈 Key Results

| Metric     | CT Dataset (ours) |
|------------|-------------------|
| Accuracy   | 92%               |
| Precision  | 93%               |
| Recall     | 35%               |
| F1 Score   | 51%               |
| Dice       | 57%               |

Despite limited recall due to dataset size, the model shows high specificity and real-time feasibility (~4 FPS on RTX 3070). Recall is expected to improve with more balanced datasets and threshold tuning.



---

> 🧠 *Towards a non-invasive, intelligent diagnosis system for endometriosis.*
