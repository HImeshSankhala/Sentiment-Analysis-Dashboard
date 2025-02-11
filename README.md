# 📊 Sentiment, Emotion & Toxicity Analysis Dashboard

## 🚀 Project Overview
This project is a **Sentiment, Emotion & Toxicity Analysis Dashboard** built with **Streamlit**. It leverages **Hugging Face transformers** to analyze text input for sentiment, emotional tone, and toxicity levels. Users can input text manually or upload a CSV file for batch analysis.

---

## 🛠 Features
- **Sentiment Analysis** (Positive, Neutral, Negative)
- **Emotion Detection** (Joy, Sadness, Anger, Fear, etc.)
- **Toxicity Detection** (Safe vs. Toxic Classification)
- **Batch Processing** (Upload CSV files for analysis)
- **Interactive Data Visualization** with **Plotly**

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/HImeshSankhala/Sentiment-Analysis-Dashboard.git
cd Sentiment-Analysis-Dashboard
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv env
source env/bin/activate  # On macOS/Linux
env\Scripts\activate  # On Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application
```bash
streamlit run dashboard/streamlit_app.py
```
The app will start locally at `http://localhost:8501/`.

---

## 📂 Project Structure
```
Sentiment-Analysis-Dashboard/
│-- dashboard/
│   │-- streamlit_app.py  # Streamlit UI
│-- sentiment_analysis/
│   │-- sentiment.py      # Text Analysis Functions
│-- data/
│   │-- sample_reviews.csv # Sample Data for Testing
│-- env/                  # Virtual Environment (Optional)
│-- README.md             # Project Documentation
│-- requirements.txt      # Dependencies
```

---

## 🧠 How It Works
### 🔍 Text Analysis Pipeline
1. **Sentiment Analysis**: Determines if a text is **Positive, Neutral, or Negative**.
2. **Emotion Analysis**: Detects emotions such as **Joy, Sadness, Anger, Love, etc.**
3. **Toxicity Detection**: Classifies text as **Safe or Toxic**.

### 📊 Visualizations
- **Bar Charts**: Sentiment Scores, Emotion Distribution, and Toxicity Levels.
- **Pie Charts**: Sentiment and Toxicity Category Distributions.
- **Batch CSV Processing**: Users can upload a CSV file with text data for bulk analysis.

---

## 🖥 Example Usage
### **Single Text Input**
```plaintext
Text: "I hate how this is happening."
Sentiment Score: 0.99 (Negative)
Emotion Scores: {'Anger': 0.85, 'Sadness': 0.07, 'Joy': 0.06}
Toxicity Score: 0.25 (Safe)
```

### **Batch CSV Upload**
1. Upload a CSV file containing a column of text.
2. The system will analyze all entries and display results in a structured table.

---

## 🏗 Future Improvements
- Enhance **context-aware sentiment analysis**.
- Improve **toxicity detection accuracy**.
- Deploy to **Streamlit Cloud** or **Hugging Face Spaces**.

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

---

## 📝 License
This project is **open-source** and available under the MIT License.

---

## ⭐ Acknowledgments
- **Hugging Face Transformers** for providing **state-of-the-art NLP models**.
- **Streamlit & Plotly** for enabling interactive data visualization.

---

### 🎯 If you find this project useful, give it a ⭐ on GitHub!

