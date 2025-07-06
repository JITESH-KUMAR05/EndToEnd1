# 🎓 Student Performance Predictor - End-to-End Machine Learning Project

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.3.3-green)](https://flask.palletsprojects.com/)
[![AWS](https://img.shields.io/badge/AWS-Elastic%20Beanstalk-orange)](https://aws.amazon.com/elasticbeanstalk/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.7.0-red)](https://scikit-learn.org/)

## 📖 Overview

This is my **first complete end-to-end machine learning project** that predicts student math scores based on various demographic and academic factors. The project demonstrates the full ML lifecycle from data ingestion to production deployment on AWS.

## 🎯 Project Objectives

- Build a regression model to predict student math scores
- Create a robust ML pipeline with proper data preprocessing
- Deploy the model as a web application
- Implement CI/CD pipeline for automated deployments
- Demonstrate production-ready ML engineering practices

## 🏗️ Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Data Source   │───▶│  Data Pipeline   │───▶│  Model Training │
│   (CSV File)    │    │  - Ingestion     │    │  - Multiple     │
└─────────────────┘    │  - Validation    │    │    Algorithms   │
                       │  - Transformation│    │  - Evaluation   │
                       └──────────────────┘    └─────────────────┘
                                │                        │
                                ▼                        ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Flask Web     │◀───│   Artifacts      │◀───│  Best Model     │
│   Application   │    │  - model.pkl     │    │  Selection      │
│                 │    │  - preprocessor  │    │                 │
└─────────────────┘    └──────────────────┘    └─────────────────┘
         │
         ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   GitHub        │───▶│  AWS CodePipeline│───▶│ AWS Elastic     │
│   Repository    │    │  - Auto Trigger  │    │ Beanstalk       │
│                 │    │  - Build & Test  │    │ - Production    │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## 📊 Dataset Features

The model uses the following features to predict math scores:

| Feature | Type | Description |
|---------|------|-------------|
| **Gender** | Categorical | Student's gender (male/female) |
| **Race/Ethnicity** | Categorical | Student's ethnic background (groups A-E) |
| **Parental Education** | Categorical | Highest education level of parents |
| **Lunch Type** | Categorical | Free/reduced vs standard lunch |
| **Test Preparation** | Categorical | Completed test prep course or not |
| **Reading Score** | Numerical | Score in reading test (0-100) |
| **Writing Score** | Numerical | Score in writing test (0-100) |

**Target Variable:** Math Score (0-100)

## 🔧 Technical Implementation

### Data Pipeline
```
Data Ingestion → Data Validation → Data Transformation → Model Training → Model Evaluation
```

1. **Data Ingestion** (`data_ingestion.py`)
   - Loads raw dataset
   - Performs train-test split
   - Saves data artifacts

2. **Data Transformation** (`data_transformation.py`)
   - Handles categorical encoding (One-Hot Encoding)
   - Numerical feature scaling (StandardScaler)
   - Creates preprocessing pipeline
   - Saves preprocessor artifact

3. **Model Training** (`model_trainer.py`)
   - Tests multiple algorithms:
     - Linear Regression
     - Random Forest Regressor
     - Decision Tree Regressor
     - Gradient Boosting Regressor
     - AdaBoost Regressor
   - Hyperparameter tuning with GridSearchCV
   - Model evaluation and selection
   - Saves best model artifact

### ML Algorithms Tested

| Algorithm | R² Score | Features |
|-----------|----------|----------|
| **Gradient Boosting** | ~0.91 | Sequential learning, best performance |
| **Random Forest** | ~0.90 | Ensemble, feature importance |
| **AdaBoost** | ~0.89 | Adaptive boosting |
| **Linear Regression** | ~0.88 | Simple, interpretable |
| **Decision Tree** | ~0.85 | Tree-based decisions |

*Note: Actual performance may vary based on hyperparameter tuning and data splits.*

## 🚀 Deployment Architecture

### AWS Infrastructure

```
┌─────────────────┐
│   GitHub Repo   │
│   (Source Code) │
└─────────┬───────┘
          │ Push Event
          ▼
┌─────────────────┐
│ AWS CodePipeline│
│ ┌─────────────┐ │
│ │   Source    │ │ ← GitHub Integration
│ └─────────────┘ │
│ ┌─────────────┐ │
│ │   Build     │ │ ← Install Dependencies
│ └─────────────┘ │
│ ┌─────────────┐ │
│ │   Deploy    │ │ ← Deploy to EB
│ └─────────────┘ │
└─────────┬───────┘
          │
          ▼
┌─────────────────┐
│ Elastic Beanstalk│
│ ┌─────────────┐ │
│ │   EC2       │ │ ← Application Server
│ │   Instance  │ │
│ └─────────────┘ │
│ ┌─────────────┐ │
│ │   Load      │ │ ← Auto Scaling
│ │   Balancer  │ │
│ └─────────────┘ │
│ ┌─────────────┐ │
│ │   Health    │ │ ← Monitoring
│ │   Monitoring│ │
│ └─────────────┘ │
└─────────────────┘
```

### Deployment Components

1. **AWS Elastic Beanstalk**
   - Platform: Python 3.11 running on 64bit Amazon Linux 2
   - Environment: Single instance (t2.micro for cost optimization)
   - Auto-scaling and load balancing capabilities
   - Health monitoring and log management

2. **AWS CodePipeline**
   - **Source Stage**: GitHub repository integration
   - **Build Stage**: Automated dependency installation
   - **Deploy Stage**: Automatic deployment to Elastic Beanstalk
   - Triggers on every push to main branch

3. **GitHub Integration**
   - Source code version control
   - Webhook integration with CodePipeline
   - Automated CI/CD on code changes

## 🛠️ Project Structure

```
studentperformance/
├── 📁 src/
│   ├── __init__.py
│   ├── exception.py          # Custom exception handling
│   ├── logger.py            # Logging configuration
│   ├── utlis.py             # Utility functions
│   ├── 📁 components/
│   │   ├── data_ingestion.py    # Data loading and splitting
│   │   ├── data_transformation.py # Feature engineering
│   │   └── model_trainer.py     # Model training and evaluation
│   └── 📁 pipeline/
│       ├── predict_pipeline.py  # Prediction pipeline
│       └── train_pipeline.py    # Training pipeline
├── 📁 artifacts/
│   ├── model.pkl            # Trained model
│   ├── preprocessor.pkl     # Data preprocessor
│   └── *.csv               # Processed datasets
├── 📁 templates/
│   └── home.html           # Web application template
├── 📁 static/
│   └── css/style.css       # Web application styling
├── 📁 notebook/
│   ├── EDA_Student_performance.ipynb  # Exploratory Data Analysis
│   └── Model_training.ipynb           # Model experimentation
├── 📁 .ebextensions/
│   └── python.config       # AWS EB configuration
├── application.py          # Flask web application
├── requirements.txt        # Python dependencies
├── setup.py               # Package setup
└── README.md              # Project documentation
```

## 📱 Web Application Features

### User Interface
- **Modern, responsive design** with CSS Grid and Flexbox
- **Interactive form** with client-side validation
- **Real-time predictions** with loading animations
- **Result visualization** with score display
- **Mobile-friendly** responsive layout

### Backend Features
- **Flask REST API** for predictions
- **Error handling** and logging
- **Input validation** and sanitization
- **Model artifact loading** and caching
- **Production-ready** configuration

## 🔧 Installation & Setup

### Local Development

1. **Clone the repository**
```bash
git clone <repository-url>
cd studentperformance
```

2. **Create virtual environment**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the training pipeline**
```bash
python src/components/data_ingestion.py
python src/components/data_transformation.py
python src/components/model_trainer.py
```

5. **Start the web application**
```bash
python application.py
```

6. **Access the application**
   - Open browser and go to `http://localhost:5000`

### AWS Deployment Setup

1. **Create Elastic Beanstalk Application**
   - Platform: Python 3.11
   - Environment: Web server environment

2. **Setup CodePipeline**
   - Source: GitHub repository
   - Build: AWS CodeBuild (optional)
   - Deploy: Elastic Beanstalk application

3. **Configure Environment Variables**
   - Set any required environment variables in EB console

## 📈 Model Performance

### Evaluation Metrics
- **R² Score**: 0.91 (Best performing model selected automatically)
- **Mean Absolute Error**: ~5.8 points
- **Root Mean Square Error**: ~7.6 points

### Model Selection Process
The system automatically selects the best performing model based on R² score:
1. **Gradient Boosting** typically performs best (~0.91 R²)
2. **Random Forest** close second (~0.90 R²) 
3. **AdaBoost** strong performer (~0.89 R²)
4. **Linear Regression** baseline model (~0.88 R²)

*The actual best model is determined during training via GridSearchCV and automatic selection.*

### Feature Importance
1. **Reading Score** - Highest correlation with math performance
2. **Writing Score** - Strong predictor of overall academic ability
3. **Parental Education** - Significant socioeconomic factor
4. **Test Preparation** - Notable impact on performance
5. **Lunch Type** - Indicator of socioeconomic status

## 🔍 Key Learnings & Challenges

### Model Selection Insights
**Why not always Linear Regression?** 
- While Linear Regression is simple and interpretable, ensemble methods like Random Forest and Gradient Boosting typically perform better on this dataset
- The automated model selection process chooses the highest performing model based on cross-validation
- **Gradient Boosting** often wins due to its ability to capture non-linear relationships and feature interactions
- **Random Forest** provides good performance with less risk of overfitting
- **Linear Regression** serves as an excellent baseline and is used when interpretability is crucial

### Technical Challenges Solved
1. **Package Version Compatibility**: Resolved numpy version mismatch between local and AWS environments
2. **Model Serialization**: Handled pickle compatibility across different Python environments
3. **AWS Deployment**: Configured proper WSGI settings and environment variables
4. **CI/CD Pipeline**: Set up automated deployment with proper error handling

### Best Practices Implemented
- **Modular Code Structure**: Separation of concerns with dedicated modules
- **Exception Handling**: Custom exception classes with detailed logging
- **Configuration Management**: Environment-specific configurations
- **Version Control**: Proper Git workflow with meaningful commits
- **Documentation**: Comprehensive README and code comments

## 🚀 Future Enhancements

### Model Improvements
- [ ] Feature engineering with polynomial features
- [ ] Advanced algorithms (XGBoost, Neural Networks)
- [ ] Hyperparameter optimization with Bayesian methods
- [ ] Cross-validation and ensemble methods

### Application Features
- [ ] User authentication and data persistence
- [ ] Batch prediction capabilities
- [ ] Model performance monitoring
- [ ] A/B testing framework
- [ ] API rate limiting and security

### Infrastructure
- [ ] Multi-environment setup (dev/staging/prod)
- [ ] Containerization with Docker
- [ ] Kubernetes deployment
- [ ] Database integration for user data
- [ ] Monitoring and alerting with CloudWatch

## 📞 Contact & Support

<div align="center">

### 👨‍💻 **Jitesh Kumar**

[![Email](https://img.shields.io/badge/Email-jitesh.kumar05official%40gmail.com-red?style=for-the-badge&logo=gmail&logoColor=white)](mailto:jitesh.kumar05official@gmail.com)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Jitesh%20Kumar-blue?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jiteshkumar05/)

[![GitHub](https://img.shields.io/badge/GitHub-JITESH--KUMAR05-black?style=for-the-badge&logo=github&logoColor=white)](https://github.com/JITESH-KUMAR05)

---

### 🌟 **Show Your Support**

If you found this project helpful, please give it a ⭐!

[![GitHub stars](https://img.shields.io/github/stars/JITESH-KUMAR05/studentperformance?style=social)](https://github.com/JITESH-KUMAR05/studentperformance)
[![GitHub forks](https://img.shields.io/github/forks/JITESH-KUMAR05/studentperformance?style=social)](https://github.com/JITESH-KUMAR05/studentperformance)

</div>

---

<div align="center">

### 💡 **About This Project**

*This project represents my journey into practical machine learning engineering, demonstrating the complete lifecycle from data to production deployment.*

**From Data Science to Production • 🤖 ML Engineering • ☁️ AWS Deployment**

</div>
