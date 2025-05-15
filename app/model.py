# app/model.py

from pathlib import Path

import joblib
import numpy as np

from app.schemas import WineInput
from app.utils import compute_engineered_features


def load_model():
    BASE_DIR = Path(__file__).resolve().parent.parent

    # Define the path to the model
    model_path = BASE_DIR / "models" / "wine_predictor.joblib"

    # Load the model
    model = joblib.load(model_path)
    if not model_path.exists():
        raise FileNotFoundError(f"Model file not found at {model_path}")
    model = joblib.load(model_path)
    return model


def predict_quality(model, data: WineInput) -> str:
    # Base features
    fixed_acidity = data.fixed_acidity
    volatile_acidity = data.volatile_acidity
    residual_sugar = data.residual_sugar
    alcohol = data.alcohol
    free_SO2 = data.free_sulfur_dioxide
    total_SO2 = data.total_sulfur_dioxide

    derived = compute_engineered_features(data)

    # Full feature vector (update this to match the training model’s order)
    features = np.array(
        [
            [
                fixed_acidity,
                volatile_acidity,
                data.citric_acid,
                residual_sugar,
                data.chlorides,
                free_SO2,
                total_SO2,
                data.density,
                data.pH,
                data.sulphates,
                alcohol,
                *derived,  # Unpack derived features
            ]
        ]
    )

    prediction = model.predict(features)
    label = "good" if prediction[0] == 1 else "bad"
    return label
