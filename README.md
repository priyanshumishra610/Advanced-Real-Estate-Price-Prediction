# 🏠 Advanced Property Price Prediction MLOps Pipeline

An end-to-end production-ready machine learning project built using **ZenML**, **MLflow**, **BentoML**, and **GitHub Actions**. It predicts California housing prices and follows the best MLOps practices including CI/CD, model tracking, evaluation, service deployment, and health monitoring.

---

## 🚀 Project Highlights

✅ ZenML-powered modular ML pipelines  
✅ MLflow integration for experiment tracking  
✅ Multiple models trained (Linear, Ridge, Lasso, Random Forest)  
✅ Model comparison & visualization  
✅ BentoML service for real-time predictions  
✅ GitHub Actions CI/CD workflow with conditional deployment  
✅ Code quality checks, rollback, and automated deployment

---

## 🧠 Tech Stack

| Tool           | Purpose                              |
|----------------|--------------------------------------|
| ZenML          | Pipeline orchestration               |
| MLflow         | Model tracking and artifact logging  |
| BentoML        | Model serving and REST API creation  |
| GitHub Actions | CI/CD automation                     |
| Scikit-learn   | ML models and preprocessing          |
| Pytest + Black | Testing and code formatting          |

---

## 📂 Project Structure
├── src/
│ └── data_loader.py
├── steps/
│ └── preprocessing.py, model_trainer.py, evaluator.py ...
├── bentoml/
│ ├── bentoml_service.py
│ └── bentofile.yaml
├── .github/
│ └── workflows/mlops-pipeline.yml
├── zenml_pipeline.py
├── enhanced_zenml_pipeline.py
├── training_pipeline.py
├── requirements.txt
├── pyproject.toml
└── README.md


---

## 🧪 Run Locally

```bash
# Clone and set up virtual environment
git clone https://github.com/<your-username>/property-price-prediction.git
cd property-price-prediction
python -m venv venv && source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

# Initialize ZenML and run pipeline
zenml init
python zenml_pipeline.py  # or enhanced_zenml_pipeline.py

📊 View MLflow UI
mlflow ui --host 0.0.0.0 --port 5000
# Visit http://localhost:5000 in browser

🔁 CI/CD Pipeline
GitHub Actions auto-triggers on every push:

✅ Lint & format check

✅ Unit tests

✅ ML pipeline run

✅ BentoML service build

✅ Health check

✅ Deploy on success

✅ Rollback on failure

Workflow file: .github/workflows/mlops-pipeline.yml

🌐 REST API with BentoML
After running the pipeline:
bentoml serve bentoml_service:PropertyPriceService
# Visit http://localhost:3000 for Swagger UI

👨‍💻 Author
Priyanshu Mishra
“Driven to build world-class AI products with clean MLOps”Priyanshu Mishra
🔗 [GitHub](https://github.com/priyanshumishra610)

⭐️ Star the Repo
If you like this project, leave a ⭐️ — it helps others discover high-quality MLOps templates.

---

### ✅ Next Step:
You can copy this content into your `README.md`, tweak your GitHub/LinkedIn links, and optionally:
- Add screenshots
- Link to your blog/Notion write-up (if any)
- Write a post tagging [@ZenML](https://twitter.com/zenml_io)

Would you like help adding badges or screenshots too?
