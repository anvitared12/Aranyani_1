from unittest import result
from urllib import response

from fastapi import FastAPI, HTTPException
import pandas as pd
from pathlib import Path

app = FastAPI(title="Garden Planner API")

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten this in production
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------- PATH --------
CURRENT_FILE = Path(__file__).resolve()
BACKEND_DIR = CURRENT_FILE.parent.parent

PLANT_DATASET_PATH = BACKEND_DIR / "Textual_Datasets" / "GardenScannerData.xlsx"
CARE_DATASET_PATH = BACKEND_DIR / "Textual_Datasets" / "CareGardenScanner.xlsx"

print("\n--- PATH DEBUG ---")
print("Plant Dataset:", PLANT_DATASET_PATH, PLANT_DATASET_PATH.exists())
print("Care Dataset:", CARE_DATASET_PATH, CARE_DATASET_PATH.exists())
print("------------------\n")

def load_plant_data():
    try:
        df = pd.read_excel(PLANT_DATASET_PATH)
        df.columns = df.columns.str.strip()
        return df
    except Exception as e:
        print("PLANT LOAD ERROR:", e)
        return None

def load_care_data():
    try:
        df = pd.read_excel(CARE_DATASET_PATH)
        df.columns = df.columns.str.strip()
        return df
    except Exception as e:
        print("CARE LOAD ERROR:", e)
        return None


@app.get("/recommendations/")
async def get_recommendations(diameter: float, height: float):
    df = load_plant_data()

    if df is None:
        raise HTTPException(status_code=500, detail="Plant dataset failed to load")

    required_cols = [
        "MIN_DIAMETER",
        "MAX_DIAMETER",
        "MIN_HEIGHT",
        "POT HEIGHT",
        "FOOD PLANT YOU CAN GROW"
    ]

    for col in required_cols:
        if col not in df.columns:
            raise HTTPException(status_code=500, detail=f"Missing column: {col}")

    df["MIN_DIAMETER"] = pd.to_numeric(df["MIN_DIAMETER"], errors="coerce")
    df["MAX_DIAMETER"] = pd.to_numeric(df["MAX_DIAMETER"], errors="coerce")
    df["MIN_HEIGHT"] = pd.to_numeric(df["MIN_HEIGHT"], errors="coerce")
    df["POT HEIGHT"] = pd.to_numeric(df["POT HEIGHT"], errors="coerce")

    df = df.dropna()

    matched_plants = []

    for _, row in df.iterrows():
        if (
            row["MIN_DIAMETER"] <= diameter <= row["MAX_DIAMETER"] and
            row["MIN_HEIGHT"] <= height <= row["POT HEIGHT"]
        ):
            plants = str(row["FOOD PLANT YOU CAN GROW"])
            plant_list = [p.strip() for p in plants.split(",") if p.strip()]
            matched_plants.extend(plant_list)

    return {
        "input": {
            "diameter": diameter,
            "height": height
        },
        "recommended_plants": list(set(matched_plants))
    }


@app.get("/care/{plant_name}")
async def get_care(plant_name: str):
    df = load_care_data()

    if df is None:
        raise HTTPException(status_code=500, detail="Care dataset failed to load")

    required_cols = ["Plant", "How to Grow", "Sunlight", "Care Recommendation"]

    for col in required_cols:
        if col not in df.columns:
            raise HTTPException(status_code=500, detail=f"Missing column: {col}")

    df["Plant"] = df["Plant"].astype(str).str.strip().str.lower()

    plant_name_clean = plant_name.strip().lower()

    result = df[df["Plant"].str.contains(plant_name_clean, case=False, na=False)]

    if result.empty:
        raise HTTPException(status_code=404, detail=f"No care info found for '{plant_name}'")

    response = []

    for _, row in result.iterrows():
        response.append({
        "Plant": row["Plant"],
        "How to Grow": row["How to Grow"],
        "Sunlight": row["Sunlight"],
        "Care recommendation": row["Care Recommendation"]
    })

    return response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)