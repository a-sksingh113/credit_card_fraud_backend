from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas.request_schema import TransactionData
from model.predict import predict_transaction

app = FastAPI()

origins = [
    "http://localhost:5173", 
    "https://credit-card-fraud-frontend-ruby.vercel.app"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Credit Card Fraud Detection API"}

@app.post("/predict")
def predict(data: TransactionData):
    result = predict_transaction(data.features)
    return {"prediction": "Fraud" if result == 1 else "Not Fraud"}
