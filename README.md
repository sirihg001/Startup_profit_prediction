# Startup Profit Prediction

This is an application to predict the profit that a business can make based on various input variables.

## 🏗 Project Structure
```
startup_pred_proj/
│-- app.py
│-- model.pkl
│-- requirements.txt
│-- README.md
│-- templates/
│   └── index.html
│-- static/
```

## 🚀 Getting Started

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/your-repo/startup_pred_proj.git
cd startup_pred_proj
```

### 2️⃣ **Create a Virtual Environment**
Creating a virtual environment is recommended to avoid package conflicts.
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
```

### 3️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 4️⃣ **Run the Application**
```bash
python app.py
```

### 5️⃣ **Access the Web App**
Open a browser and go to:
```
http://127.0.0.1:5000/
```

## 📂 Important Notes
- The `index.html` file **must be placed inside the `templates/` folder** since Flask looks for templates in that directory.
- The `model.pkl` file should be a trained machine learning model compatible with Flask.

## 🛠 Troubleshooting
- If you encounter missing package errors, ensure all dependencies are installed via `pip install -r requirements.txt`.
- If Flask fails to find `index.html`, verify it is inside the `templates/` folder.

---

Happy coding! 🚀

