# 🌾 Crop Prediction Web App using Machine Learning

This is a **machine learning web application** that recommends the best crop to grow based on input parameters like nitrogen, phosphorus, potassium, temperature, humidity, pH, and rainfall.

It uses a **Random Forest Classifier** model trained on real agricultural data and provides predictions through a simple **Flask-based web interface**.

---

## 💡 Features

- Input: Soil and environmental features
- Output: Most suitable crop to grow
- Backend: Flask (Python)
- Model: RandomForestClassifier (pickled using `pickle`)
- UI: HTML + CSS (clean and responsive)

---

## 🔧 How to Run the Project

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/Crop_Prediction.git
cd Crop_Prediction
```

### 2.Create and Activate a Virtual Environment
```bash
python3 -m venv myenv
source myenv/bin/activate   
```

### 3.Install Required Packages
```bash
pip install -r requirements.txt
```
### 4.Run the Flask App
```bash
python app.py
```

### 5.Open the Web App
Go to http://127.0.0.1:5000 in your browser.

---

## 📊 Dataset Features

| Feature      | Type     | Description                                    |
|--------------|----------|------------------------------------------------|
| `Nitrogen`   | `float`  | **Required.** Nitrogen content in soil (N)     |
| `Phosphorus` | `float`  | **Required.** Phosphorus content in soil (P)   |
| `Potassium`  | `float`  | **Required.** Potassium content in soil (K)    |
| `Temperature`| `float`  | **Required.** Temperature in degrees Celsius   |
| `Humidity`   | `float`  | **Required.** Relative humidity in percentage  |
| `pH`         | `float`  | **Required.** Soil pH level                    |
| `Rainfall`   | `float`  | **Required.** Rainfall in millimeters          |


- 📁 Source: [Crop Recommendation Dataset on Kaggle](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset)

---

## 🙋 Author
Tanush Reddy
GitHub: https://github.com/tanux22



