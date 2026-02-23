
# 🌿 ARANYANI – Complete Feature Breakdown


1. Core User Features
2. Intelligence Features (ML-driven)
3. Automation Features
4. Data & Tracking Features
5. Infrastructure Features
6. Stretch / Advanced Features

---

# 1️⃣ Core User Features (Visible Layer)

These are what users directly interact with.

## 1. User Authentication

**Purpose:** Secure user identity.

**Includes:**

* Sign up / Login (Auth0 + JWT)
* Token validation
* Session persistence

**Engineering Insight:** Stateless backend with token-based authentication.

---

## 2. Plant Identification Scanner

**Input:** Image from CameraX
**Processing:** TFLite EfficientNet
**Output:**

* Common name
* Scientific name
* Basic description
* Add to library option

**System Behavior:**
On-device inference → Metadata lookup → Response render

---

## 3. Plant Disease Detection

**Input:** Leaf image
**Processing:** TFLite disease CNN
**Output:**

* Disease name
* Severity (optional future)
* Organic recovery steps


---

## 4. Personalized Plant Library

**Purpose:** Persistent plant tracking per user.

**Includes:**

* Rename plant
* Store location
* Store pot size, soil type
* Care history
* Growth images

**Storage:** PostgreSQL + TimescaleDB

---

## 5. Garden Area Scanner

**Input:** Garden scan + layout
**Processing:**

* MediaPipe segmentation
* Feature extraction
* Crop suitability model

**Output:**

* Recommended crops
* Layout structure
* Seasonal suitability

This is spatial + predictive ML combined.

---

# 2️⃣ Intelligence Features (ML Core)


---

## 6. Care Recommendation Engine

**Inputs:**

* Plant species
* Location
* Weather
* Pot size
* Soil
* Sunlight

**Model:** XGBoost

**Outputs:**

* Watering frequency
* Fertilizer suggestion
* Soil recommendation
* Sunlight requirement


---

## 7. Crop Suitability Prediction

**Inputs:**

* Garden size
* Location
* Weather forecast
* Soil input

**Model:** XGBoost

**Output:**

* Ranked crop list
* Suitability score



---

## 8. Weather-Based Alerts

**Input:** Open-Meteo API
**Logic:**

* Rain alert → Adjust watering
* Heatwave → Shade suggestion
* High humidity → Disease risk alert

**Tech:** Redis cache + FCM



---

# 3️⃣ Automation Features

These reduce cognitive load.

---

## 9. Smart Reminders

**Tech:** WorkManager + Redis + FCM

* Water reminders
* Fertilizer reminders
* Growth check reminders

---

## 10. Auto Plant Identification in Existing Garden

Scan multiple plants → Auto-generate list
Useful for onboarding existing users.

---

# 4️⃣ Data & Tracking Features

This adds depth beyond simple scanning.

---

## 11. Growth Tracking Timeline

**Input:** Periodic plant photos
**Processing:**

* Height estimation (future enhancement)
* Visual difference analysis

**Output:**

* Growth chart
* Health trend

Stored in TimescaleDB (time-series optimized).

---

## 12. Care History Logs

Every:

* Watering
* Fertilizing
* Disease detection
* Weather event

This enables:

* Trend detection
* Future model retraining

---

# 5️⃣ Infrastructure Features (Hidden but Critical)

---

## 13. Image Storage

Firebase storage for:

* Scan history
* Growth images

---

## 14. Caching Layer

Redis:

* Weather cache
* Reminder queue
* Fast lookups

Reduces API latency.

---

## 15. Time-Series Optimization

TimescaleDB:

* Efficient growth tracking
* Performance at scale

---

# 6️⃣ Stretch Features

---

## 16. Local Language Generation

* Backend text generation
* Multi-language support

---

## 17. Voice Narration

Text-to-speech output for:

* Care instructions
* Alerts

Improves accessibility.

---



