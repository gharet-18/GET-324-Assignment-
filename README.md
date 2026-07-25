# Potato Early Blight vs Late Blight Classifier 🥔

A CNN-based binary image classifier that distinguishes Potato Early Blight from Potato Late Blight, built with TensorFlow/Keras and deployed as a Streamlit web app.

**Group:** CO14 | GET 324 Laboratory Exercise 10 (Mini-Project)

## 🔗 Live App
[Add deployed Streamlit URL here]

## 📊 Dataset
[PlantVillage Dataset](https://www.kaggle.com/datasets/arjuntejaswi/plant-village) — Kaggle dataset containing labeled potato leaf images (Early Blight, Late Blight, Healthy). Only the Early Blight and Late Blight classes are used here.

##  Model
- Base: MobileNetV2 (transfer learning, pretrained on ImageNet)
- Head: GlobalAveragePooling2D → Dense(128, ReLU) → Dropout(0.3) → Dense(1, Sigmoid)
- Input size: 224x224
- Loss: Binary Crossentropy | Optimizer: Adam

## 📁 Project Structure
```
potato-blight-classifier/
├── data/
│   └── prepare_data.py       # script to organize/split the downloaded dataset
├── notebooks/
│   ├── train_model.ipynb     # model building + training
│   └── evaluate_model.ipynb  # evaluation metrics + plots
├── results/
│   ├── confusion_matrix.png
│   └── accuracy_loss_curves.png
├── app.py                    # Streamlit application
├── blight_model.h5           # saved trained model
├── requirements.txt
├── .gitignore
├── README.md
└── report.md                 # 100-150 word project report
```

## ⚙️ How to Run Locally
```bash
git clone https://github.com/<your-username>/potato-blight-classifier.git
cd potato-blight-classifier
pip install -r requirements.txt
streamlit run app.py
```
Upload a potato leaf image and the app will return a prediction (Early Blight or Late Blight) with a confidence score.

## ☁️ Deployment
Deployed on Streamlit Community Cloud:
1. Go to https://share.streamlit.io and sign in with GitHub
2. Click "New app" → select this repo, `main` branch, `app.py`
3. Click Deploy

## 🚧 Challenges & Solutions
[Fill in — e.g., dataset size handled with augmentation, model file size for deployment, etc.]

## 👥 Team Members
| Name | Registration Number | GitHub Username |
|------|---------------------|------------------|
| Ebong, Margaret Christopher | 23/EG/CO/036 | gharet-18 |
| Akpan, Idongesit Moses | 23/EG/CO/086 | idongesitakpan197-coder |
| Ibok, Saviour Joseph | 23/EG/CO/056 | Saviour-Ibok1 |
| Okon, Imoh Daniel | 23/EG/CO/006 | danielimoh67-beep |
| Jones, Daniel Williams | 23/EG/CO/116 | — |
| Ukpoh, Godswill Daniel | 23/EG/CO/266 | GWILLSUB |
| Ita, Louis Micheal | 23/EG/CO/016 | louismichealddev |
| Oyemachi, Ifechukwu Stephen | 23/EG/CO/136 | ifechukwuonyemachi16-ai |
| Hycienth, Akunnaya Perpetual | 23/EG/CO/026 | akunnaperpetual21-design |

