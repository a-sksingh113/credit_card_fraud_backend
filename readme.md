
#  Credit Card Fraud Detection API with FastAPI - Backend Server

This is a backend API for detecting fraudulent credit card transactions using a trained ML model (CatBoost/LightGBM/etc.) served through FastAPI.

---

##  Folder Structure

```
.
├── model/
│   ├── predict.py
│   └── credit card fraud model.pkl
├── schemas/
│   └── request_schema.py
├── main.py
├── requirements.txt
└── .gitignore
```

---

##  Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/credit_card_fraud_backend.git
cd credit_card_fraud_backend
```

---

### 2. Create and activate virtual environment

```bash
# Create virtual environment
python -m venv myenv

# Activate it
# On Windows
myenv\Scripts\activate

# On macOS/Linux
source myenv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run the FastAPI server with uvicorn

```bash
uvicorn main:app --reload
```

This will start the server at:

```
http://127.0.0.1:8000
```

---

## API Endpoints

### ➤ Root Endpoint

```http
GET /
```

Returns a simple welcome message.

### ➤ Predict Endpoint

```http
POST /predict
```

**Request body**:

```json
{
  "features": [0.0, -1.3598, ..., 149.62]
}
```

**Response**:

```json
{
  "prediction": "Fraud"  // or "Not Fraud"
}
```

---

##  CORS Configured For

Frontend URL:

```bash
http://localhost:5173
```

> Change this in `main.py` if needed.

---

##  Deployment (Render)

If deploying on [Render](https://render.com):

1. Upload code to GitHub.
2. Set **Python Version**:
   - Add `.python-version` file with `3.10` inside it
   - OR set `PYTHON_VERSION=3.10` in Render environment variables.
3. Use **Build Command**:

```bash
pip install -r requirements.txt
```

4. Use **Start Command**:

```bash
uvicorn main:app --host 0.0.0.0 --port 10000
```

---

##  .gitignore (sample)

```gitignore
__pycache__/
myenv/
*.pyc
.env
```

---

##  Author

Built by Data Seekers for credit card fraud detection.
