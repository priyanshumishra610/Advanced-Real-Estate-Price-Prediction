# 🏠 Advanced Property Price Prediction MLOps Pipeline

An end-to-end **production-ready** machine learning project built using **ZenML**, **MLflow**, **BentoML**, and **GitHub Actions**. It predicts **California housing prices** and follows modern **MLOps best practices**, including CI/CD, model tracking, experiment management, deployment, and health monitoring.

![CI/CD](https://github.com/priyanshumishra610/property-price-prediction/actions/workflows/mlops-pipeline.yml/badge.svg)
![ZenML](https://img.shields.io/badge/MLOps-ZenML-orange)
![MLflow](https://img.shields.io/badge/Tracking-MLflow-blue)
![BentoML](https://img.shields.io/badge/Serving-BentoML-green)
![License](https://img.shields.io/badge/license-MIT-brightgreen)
![Python](https://img.shields.io/badge/Python-3.10%2B-yellow)

---

## 🚀 Project Highlights

✅ Modular ZenML pipelines

✅ MLflow integration for experiment tracking

✅ Multiple models trained and compared (Linear, Ridge, Lasso, Random Forest)

✅ Automated model comparison & evaluation

✅ BentoML service for real-time API predictions

✅ GitHub Actions CI/CD workflow with linting, testing, deployment, and rollback

✅ Code quality checks and health monitoring

---

## 🧠 Tech Stack

| Tool           | Purpose                                |
| -------------- | -------------------------------------- |
| ZenML          | Pipeline orchestration                 |
| MLflow         | Experiment tracking & artifact logging |
| BentoML        | Model serving & REST API creation      |
| GitHub Actions | CI/CD automation                       |
| Scikit-learn   | ML models & preprocessing              |
| Pytest + Black | Testing & code formatting              |

---

## 📂 Project Structure

```plaintext
property-price-prediction/
├── src/
│   ├── data_loader.py
│   ├── feature_engineering.py
│   └── utils.py
├── steps/
│   ├── preprocessing.py
│   ├── model_trainer.py
│   ├── evaluator.py
│   └── deployment.py
├── bentoml/
│   ├── bentoml_service.py
│   └── bentofile.yaml
├── .github/
│   └── workflows/
│       └── mlops-pipeline.yml
├── zenml_pipeline.py
├── enhanced_zenml_pipeline.py
├── training_pipeline.py
├── requirements.txt
├── pyproject.toml
└── README.md
```

---

## 🧪 Run Locally

```bash
# 1️⃣ Clone the repo & set up virtual environment
git clone https://github.com/<your-username>/property-price-prediction.git
cd property-price-prediction
python -m venv venv && source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# 2️⃣ Initialize ZenML & run pipeline
zenml init
python zenml_pipeline.py  # Or: python enhanced_zenml_pipeline.py

# 3️⃣ View MLflow UI
mlflow ui --host 0.0.0.0 --port 5000
# Access MLflow at: http://localhost:5000

# 4️⃣ Serve REST API with BentoML
bentoml serve bentoml_service:PropertyPriceService
# Access Swagger UI at: http://localhost:3000
```

---

## 🔁 CI/CD Pipeline

**GitHub Actions** automatically runs on every push:

* ✅ Lint & format check
* ✅ Unit tests with Pytest
* ✅ Run ZenML pipeline
* ✅ Build BentoML service
* ✅ Perform health checks
* ✅ Deploy on success
* ✅ Rollback on failure

**Workflow:** `.github/workflows/mlops-pipeline.yml`

---

## 👨‍💻 Author

**Priyanshu Mishra**
*“Driven to build world-class AI products with robust MLOps.”*
🔗 [GitHub](https://github.com/priyanshumishra610)

---

## ⭐️ Star This Repo

If you find this project helpful, **star ⭐️ it** — it motivates open-source contributors and helps others discover high-quality **MLOps templates**.

