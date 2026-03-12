from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn
import io
import time
from PIL import Image

from model.predictor import PlantDiseasePredictor
from utils.disease_info import get_disease_info

app = FastAPI(
    title="Plant Disease Detection API",
    description="Detect plant diseases from leaf images using deep learning",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize predictor once at startup
predictor = None

@app.on_event("startup")
async def startup_event():
    global predictor
    print("Loading plant disease detection model...")
    predictor = PlantDiseasePredictor()
    print("Model loaded successfully!")

@app.get("/")
async def root():
    return {"message": "Plant Disease Detection API is running", "status": "healthy"}

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "model_loaded": predictor is not None,
        "version": "1.0.0"
    }

@app.post("/predict")
async def predict_disease(file: UploadFile = File(...)):
    """
    Upload a plant leaf image to detect diseases.
    Accepts: JPG, JPEG, PNG, WEBP
    Returns: Disease name, confidence, treatment advice
    """
    # Validate file type
    allowed_types = {"image/jpeg", "image/jpg", "image/png", "image/webp"}
    if file.content_type not in allowed_types:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid file type: {file.content_type}. Please upload JPG, PNG, or WEBP."
        )

    # Validate file size (max 10MB)
    contents = await file.read()
    if len(contents) > 10 * 1024 * 1024:
        raise HTTPException(status_code=400, detail="File too large. Maximum size is 10MB.")

    try:
        # Open and validate image
        image = Image.open(io.BytesIO(contents)).convert("RGB")
    except Exception:
        raise HTTPException(status_code=400, detail="Could not process image. Please upload a valid image file.")

    try:
        start_time = time.time()
        # Run prediction
        predictions = predictor.predict(image)
        inference_time = round((time.time() - start_time) * 1000, 2)

        # Get top prediction
        top_pred = predictions[0]
        disease_name = top_pred["class"]
        confidence = top_pred["confidence"]

        # Get detailed disease information
        disease_details = get_disease_info(disease_name)

        return JSONResponse(content={
            "success": True,
            "prediction": {
                "disease": disease_name,
                "confidence": confidence,
                "is_healthy": disease_details["is_healthy"],
                "plant": disease_details["plant"],
                "disease_short": disease_details["disease_short"],
                "severity": disease_details["severity"],
                "description": disease_details["description"],
                "symptoms": disease_details["symptoms"],
                "causes": disease_details["causes"],
                "treatment": disease_details["treatment"],
                "prevention": disease_details["prevention"],
                "organic_remedies": disease_details["organic_remedies"],
            },
            "top_3_predictions": predictions[:3],
            "inference_time_ms": inference_time,
            "filename": file.filename
        })

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")

@app.get("/classes")
async def get_classes():
    """Return all supported plant/disease classes"""
    from model.class_labels import CLASS_LABELS
    return {"classes": CLASS_LABELS, "total": len(CLASS_LABELS)}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
