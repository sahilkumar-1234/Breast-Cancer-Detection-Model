# Breast Cancer Detection Model 🎗️
This project uses a logistic regression model trained on the Wisconsin Breast Cancer Dataset to predict whether a tumor is malignant or benign based on its characteristics.
A web application powered by machine learning and Flask for early detection of breast cancer. Users can predict tumor malignancy through form input or medical images.

---

## 📂 Project Structure

```
model/
├── best_model.pkl           # Trained ML model (pickle)
├── scaler.pkl               # Scaler for preprocessing
├── model_details.json       # Metadata & evaluation metrics
├── train_model.py           # Script to train and save model
└── data.csv                 # Original dataset for training (Breast Cancer Wisconsin)

web/
├── app.py                   # Flask web application (routes and API)
├── requirements.txt         # Python dependencies for the web app
├── static/                  # CSS/JS assets
├── templates/
│   ├── index.html           # Landing & input form
│   ├── result.html          # Prediction result display
│   └── error.html           # Error pages
└── uploads/                 # Uploaded images for analysis

README.md                    # Project overview (this file)
requirements.txt            # Shared environment dependencies
```

---

## 🧠 Overview

This project builds a user-friendly web service to classify breast tumors as **Malignant** or **Benign** using a model trained on the *Breast Cancer Wisconsin* dataset. Users can:

* Enter numeric diagnostic inputs.
* Predict results instantly via web form or API.
* Optionally upload an image for image-based prediction (if extended).

---

## ⚙️ Features

* **Tabular data prediction:** Model accepts numerical features and predicts tumor type.
* **Image upload support:** (Optional) Enables prediction from a breast scan image.
* **Detailed output:** Displays prediction, probability score, and accessible UI feedback.
* **Reusable pipeline:** Preprocessing (scaler) and model saved for deployment ease.
* **Simple retraining:** Adjust `train_model.py` to pick different algorithms or hyperparameters.

---

## 🛠️ Technologies

* **Backend:** Python, Flask
* **ML:** scikit-learn (Logistic Regression, SVM, Random Forest, etc.) ([github.com][1], [github.com][2])
* **Data processing:** Pandas, NumPy
* **Frontend:** HTML, CSS, JavaScript (Bootstrap optional)
* **Serialization:** Pickle (for model & scaler persistence)

---

## 🚀 Installation & Setup

1. **Clone repository**

   ```bash
   git clone https://github.com/sahilkumar-1234/Breast-Cancer-Detection-Model.git
   cd Breast-Cancer-Detection-Model
   ```

2. **Create & activate virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Train or use pre-trained model**

   * *To train:*

     ```bash
     python model/train_model.py
     ```
   * *To use existing model:* Skip training.

5. **Launch web application**

   ```bash
   cd web
   python app.py
   ```

   Navigate to `http://127.0.0.1:5000` in your browser.

---

## 🧾 How It Works

* **Training pipeline:**

  * Dataset loaded from `data.csv`
  * Missing values handled; features scaled using `Scaler`
  * Multiple models tested, best selected and saved (see `model_details.json`)
* **Flask app flow:**

  * User inputs diagnostic values or uploads image
  * Request received by `app.py`, validated and preprocessed
  * Model predicts outcome and renders result template

---

## 🧪 Usage Examples

* **Numeric Input (via form or API):**

  ```json
  {
    "features": [5.1, 3.5, …]  // Feature vector with same order as training
  }
  ```

  * Returns class label (`Benign` / `Malignant`) and confidence score

* **Image Upload (optional):**

  * Upload `.jpg` or `.png` woman’s scan image
  * Extract features and predict tumor type

---

## 📈 Model Performance

Your model’s evaluation results are saved in `model/model_details.json`: accuracy, precision, recall, etc. For reference, similar projects show:

* Random Forest/SVM: \~97% accuracy
* Logistic Regression: \~95% ([github.com][3], [gist.github.com][4], [github.com][2], [github.com][1])

You can extend it to include metrics visualization.

---

## 🔧 Customization & Extensions

* Experiment with different algorithms (KNN, Decision Tree, AdaBoost)
* Add:

  * ROC curve display
  * Confusion matrix in results
  * Image preprocessing (if image support)
  * User authentication
  * Dockerfile for containerization
* Deploy to Heroku, AWS, or GCP

---

## 🎓 Acknowledgements

* Dataset: UCI Breast Cancer Wisconsin dataset
* Model comparison inspired by existing implementations&#x20;
* Flask app structuring based on common ML web patterns

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for details.

---

## 💬 Contact

Created by **Sahil Kumar**. Feel free to open issues or submit pull requests to enhance the project!
