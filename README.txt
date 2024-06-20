
Detection of Endometriosis using Advanced Deep Learning Techniques
This repository contains the code and data for my Bachelor’s thesis on detecting endometriosis using advanced deep learning techniques.

UNIVERSITATEA “ALEXANDRU IOAN CUZA” DIN IAȘI
FACULTATEA DE INFORMATICĂ
LUCRARE DE LICENȚĂ

Detecția endometriozei folosind tehnici avansate de deep learning

Propusă de: Cristian-Ioan Roman
Sesiunea: Iulie, 2024
Coordonator științific: Lector Dr. Cristian Frăsinaru

Introduction
Endometriosis is a chronic gynecological condition where tissue similar to the lining inside the uterus grows outside of it, causing severe pain, abnormal bleeding, and infertility. The early detection of endometriosis is crucial for effective symptom management, which is why this project aims to leverage artificial intelligence for its detection using advanced deep learning techniques.

Project Overview
The project involves the following key components:

Data Collection: The data used in this project is sourced from the Medical Decathlon dataset, which can be accessed here. For more detailed information on the dataset, refer to the paper available here. Only the heart and prostate images from this dataset were used.
Deep Learning Models: The project employs various deep learning models, including classical neural networks, convolutional neural networks, and graph-based networks.
Segmentation Architecture: The core architecture used for image segmentation is the U-Net, a popular structure known for its effectiveness in medical image segmentation tasks.
Image Processing: The goal is to automatically identify ovarian cysts resulting from endometriosis in transvaginal ultrasound images. The output of the neural network is a binary image where white represents the cyst and black represents normal tissue.
Features
Automatic Detection: Uses deep learning to automatically detect ovarian cysts in ultrasound images.
Image Segmentation: Employs U-Net architecture for precise image segmentation.
Evaluation Metrics: Accuracy, recall, and F1-score metrics to evaluate the performance of the models.
