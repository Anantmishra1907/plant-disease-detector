# 🌿 LeafScan — Plant Disease Detection

A full-stack web application for plant disease detection powered by a PyTorch MobileNetV2 model trained on the PlantVillage dataset.

## 📸 Demo

Upload any plant leaf photo → get instant diagnosis with:
- Disease name and confidence score
- Severity rating (Healthy / Low / Medium / High / Critical)
- Detailed symptoms, causes, treatment, and prevention advice
- Organic remedies
- Top 3 predictions with confidence bars

---

## 🏗️ Architecture

```
plant-disease-detector/
├── frontend/
│   └── index.html           # Beautiful vanilla HTML/CSS/JS UI
├── backend/
│   ├── main.py              # FastAPI application
│   ├── train.py             # Model training script
│   ├── download_weights.py  # Download pretrained weights
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── model/
│   │   ├── predictor.py     # PyTorch MobileNetV2 inference
│   │   ├── class_labels.py  # 38 PlantVillage class names
│   │   └── weights/         # ← Place trained .pth file here
│   └── utils/
│       └── disease_info.py  # Disease information database
├── nginx/
│   └── default.conf         # Reverse proxy config
├── docker-compose.yml
└── README.md
```

**Stack:**
- **Frontend:** Vanilla HTML5 / CSS3 / JavaScript (zero dependencies)
- **Backend:** FastAPI + Uvicorn
- **ML Model:** PyTorch MobileNetV2 (fine-tuned on PlantVillage)
- **Deployment:** Docker + Docker Compose + Nginx

---

## 🚀 Quick Start

### Option A — Docker (Recommended)

```bash
git clone <repo-url>
cd plant-disease-detector

# Build and start both services
docker compose up --build

# Open in browser
open http://localhost
```

The backend API will be available at `http://localhost:8000`.

---

### Option B — Local Development

#### 1. Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Option 1: Create demo weights (ImageNet pretrained, for testing UI)
python download_weights.py --source demo

# Option 2: Download community weights from Hugging Face
pip install huggingface_hub
python download_weights.py --source huggingface

# Start the API server
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

#### 2. Frontend

Open `frontend/index.html` directly in your browser, or serve it:

```bash
cd frontend
python -m http.server 3000
# → http://localhost:3000
```

---

## 🧠 Training the Model

### Step 1 — Download the PlantVillage Dataset

From Kaggle (free account required):
- https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset

Expected structure:
```
/path/to/PlantVillage/
    train/
        Apple___Apple_scab/
            image001.jpg
            ...
        Apple___healthy/
        ...
    valid/
        Apple___Apple_scab/
        ...
```

### Step 2 — Train

```bash
cd backend
python train.py \
    --data_dir /path/to/PlantVillage \
    --epochs 25 \
    --batch_size 32 \
    --lr 0.001
```

Training strategy (automatic):
- Phase 1 (epochs 1–5): Train classification head only (frozen backbone)
- Phase 2 (epochs 6–25): Full fine-tuning with lower LR

Expected results on PlantVillage:
| Metric | Value |
|--------|-------|
| Val Accuracy | ~96–98% |
| Inference time | ~20ms (CPU) / ~5ms (GPU) |

### Step 3 — Use Your Trained Model

The best model is saved automatically to `backend/model/weights/plant_disease_model.pth`.  
Restart the server and it will load automatically.

---

## 🌐 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| GET | `/health` | Detailed health status |
| POST | `/predict` | Upload image, get prediction |
| GET | `/classes` | List all 38 disease classes |

### Example — cURL

```bash
curl -X POST http://localhost:8000/predict \
  -F "file=@/path/to/leaf.jpg"
```

### Example Response

```json
{
  "success": true,
  "prediction": {
    "disease": "Tomato___Late_blight",
    "confidence": 94.7,
    "is_healthy": false,
    "plant": "Tomato",
    "disease_short": "Late Blight",
    "severity": "Critical",
    "description": "Tomato late blight caused by Phytophthora infestans...",
    "symptoms": ["Pale green, water-soaked spots..."],
    "treatment": ["Apply protectant fungicides..."],
    "prevention": ["Plant resistant varieties..."],
    "organic_remedies": ["Bordeaux mixture..."]
  },
  "top_3_predictions": [...],
  "inference_time_ms": 18.4,
  "filename": "leaf.jpg"
}
```

---

## 🌱 Supported Plants & Diseases (38 classes)

| Plant | Diseases |
|-------|----------|
| Apple | Apple Scab, Black Rot, Cedar Apple Rust, Healthy |
| Blueberry | Healthy |
| Cherry | Powdery Mildew, Healthy |
| Corn | Gray Leaf Spot, Common Rust, Northern Leaf Blight, Healthy |
| Grape | Black Rot, Esca, Leaf Blight, Healthy |
| Orange | Citrus Greening (HLB) |
| Peach | Bacterial Spot, Healthy |
| Bell Pepper | Bacterial Spot, Healthy |
| Potato | Early Blight, Late Blight, Healthy |
| Raspberry | Healthy |
| Soybean | Healthy |
| Squash | Powdery Mildew |
| Strawberry | Leaf Scorch, Healthy |
| Tomato | Bacterial Spot, Early Blight, Late Blight, Leaf Mold, Septoria, Spider Mites, Target Spot, TYLCV, Mosaic Virus, Healthy |

---

## ☁️ Deploying to Cloud

### Render (Free tier available)
1. Push to GitHub
2. Create a new Web Service on render.com
3. Set build command: `pip install -r backend/requirements.txt`
4. Set start command: `cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Upload model weights as an environment secret or use HF Hub download

### Railway
```bash
railway login
railway init
railway up
```

### AWS EC2
```bash
# On EC2 instance (Ubuntu 22.04)
sudo apt install docker.io docker-compose -y
git clone <repo> && cd plant-disease-detector
docker compose up -d --build
```

---

## ⚙️ Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `PORT` | `8000` | API server port |
| `MODEL_PATH` | `model/weights/plant_disease_model.pth` | Path to model weights |

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

## 🙏 Credits

- **Dataset:** PlantVillage Dataset (Penn State University)
- **Model Architecture:** MobileNetV2 (Google, via torchvision)
- **Framework:** FastAPI, PyTorch, Nginx
