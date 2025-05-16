# 12-Factor_App

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

# 🍷 Wine Quality Prediction — 12-Factor App with FastAPI

Welcome! This project demonstrates a production-ready machine learning API using **FastAPI**, following the principles of the [12-Factor App methodology](https://12factor.net/).

It includes:

* A trained ML model for wine quality classification (good/bad)
* REST API for predictions
* Dockerized deployment
* Automated CI/CD with GitHub Actions
* Live documentation with MkDocs
* Test suite with `pytest`
* Clean project structure following best practices

---

## 🚀 Features

✅ FastAPI web server
✅ ML model using scikit-learn and XGBoost
✅ Docker & Docker Compose
✅ Environment-based configuration
✅ GitHub Actions CI/CD
✅ Pre-commit hooks
✅ MkDocs technical documentation
✅ Fully tested with `pytest`

---

## 📦 Getting Started

To get started quickly, check out the [📘 Getting Started Guide](docs/docs/getting-started.md).

Or follow these quick steps:

### 🔧 Prerequisites

* Python 3.10+
* Docker & Docker Compose
* Git

### 🔄 Clone the Project

```bash
git clone https://github.com/your-username/12-factor_app.git
cd 12-factor_app
```

### 🧪 Run Locally (no Docker)

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Visit: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🐳 Run with Docker Compose

To spin up both the FastAPI API and MkDocs site:

```bash
docker-compose up --build
```

* FastAPI: [http://localhost:8000](http://localhost:8000)
* Docs: [http://localhost:8001](http://localhost:8001)

---

## 📊 API Endpoint

### `/predict` (POST)

Predicts wine quality (good or bad).

#### Request Body:

```json
{
  "fixed_acidity": 7.4,
  "volatile_acidity": 0.7,
  "citric_acid": 0.0,
  "residual_sugar": 1.9,
  "chlorides": 0.076,
  "free_sulfur_dioxide": 11.0,
  "total_sulfur_dioxide": 34.0,
  "density": 0.9978,
  "pH": 3.51,
  "sulphates": 0.56,
  "alcohol": 9.4
}
```

#### Response:

```json
{
  "prediction": "good"
}
```

---

## ✅ Running Tests

```bash
pytest
```

You’ll find tests in the `tests/` folder, testing the `/predict` endpoint.

---

## 📚 Documentation

You can browse developer docs at:

```bash
mkdocs serve
```

Or view them at: [http://localhost:8001](http://localhost:8001)

To build static docs:

```bash
mkdocs build
```

---

## 🔁 Continuous Integration

GitHub Actions is set up to:

* Run `pytest` on push/pull request
* Build and push a Docker image to Docker Hub (if secrets are configured)

See `.github/workflows/cicd.yml`

---

## 🧪 Tech Stack

* FastAPI
* scikit-learn, XGBoost
* Pydantic
* MkDocs Material
* Docker & Docker Compose
* Pytest
* GitHub Actions

---

## 📁 Project Structure (Simplified)

```
.
├── app/               # FastAPI app code
├── docs/              # MkDocs documentation
├── tests/             # Test files
├── models/            # Trained model
├── data/              # CSV dataset
├── Dockerfile         # For FastAPI
├── docker-compose.yml # To run app + docs
├── mkdocs.yml         # MkDocs config
└── requirements.txt   # Python dependencies
```

---

## 🙏 Contributing

Feel free to fork this repo, improve it, and open a pull request! Suggestions and bug reports are welcome.

---

## 🛡 License

This project is licensed under the MIT License.

---

## 💡 Credits

Built with ❤️ using FastAPI, Docker, and the 12-Factor methodology.
