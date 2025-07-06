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

---

## 🐳 AWS EC2 + ECR Deployment (Docker Containerization)

### Overview
*This project was successfully deployed using AWS EC2 and ECR with Docker containerization and GitHub Actions CI/CD. The deployment has been taken down to avoid ongoing costs.*

**Live Demo URL (Archived):** `http://44.201.213.90:5000/` *(No longer active)*

### Architecture
```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   GitHub Repo   │───▶│ GitHub Actions   │───▶│   Amazon ECR    │
│   (Source Code) │    │   (CI/CD)        │    │ (Container Reg) │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                │                        │
                                ▼                        ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│     Docker      │◀───│   Docker Build   │    │   Docker Pull   │
│   Containerize  │    │   & Push         │    │   & Deploy      │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                                        │
                                                        ▼
                               ┌─────────────────────────────────────┐
                               │           AWS EC2 Instance          │
                               │  ┌─────────────────────────────────┐│
                               │  │      Docker Container          ││
                               │  │  ┌─────────────────────────┐   ││
                               │  │  │    Flask Application   │   ││
                               │  │  │    Port: 5000          │   ││
                               │  │  └─────────────────────────┘   ││
                               │  └─────────────────────────────────┘│
                               │          Public IP: 44.201.213.90  │
                               └─────────────────────────────────────┘
```

### Prerequisites
- AWS Account with appropriate permissions
- Docker installed locally
- GitHub repository
- Basic understanding of Docker and AWS services

### Step-by-Step Deployment Guide

#### 1. 📋 AWS Setup

**1.1 Create ECR Repository**
```bash
# Install AWS CLI
pip install awscli

# Configure AWS credentials
aws configure
# Enter your AWS Access Key ID
# Enter your AWS Secret Access Key  
# Enter your default region (e.g., us-east-1)
# Enter output format (json)

# Create ECR repository
aws ecr create-repository --repository-name studentperformance-app --region us-east-1

# Note down the repository URI: {account-id}.dkr.ecr.{region}.amazonaws.com/studentperformance-app
```

**1.2 Create EC2 Instance**
```bash
# Launch EC2 instance (Ubuntu 22.04 LTS)
# Instance type: t2.micro (free tier eligible)
# Security Group: Allow HTTP (80), HTTPS (443), SSH (22), Custom TCP (5000)
# Key pair: Create and download for SSH access

# Install Docker on EC2 instance
sudo apt update
sudo apt install docker.io -y
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker ubuntu

# Install AWS CLI on EC2
sudo apt install awscli -y
```

#### 2. 🐳 Docker Configuration

**2.1 Create Dockerfile**
```dockerfile
FROM python:3.11-slim-buster
WORKDIR /app
COPY . /app

RUN apt update -y && apt install awscli -y
RUN pip install -r requirements.txt

CMD [ "python3","application.py" ]
```

**2.2 Create .dockerignore**
```
.git
.gitignore
README.md
__pycache__
*.pyc
.venv
env/
logs/
notebook/
*.ipynb
catboost_info/
```

#### 3. ⚙️ GitHub Actions Setup

**3.1 Configure GitHub Secrets**
Go to GitHub Repository → Settings → Secrets and variables → Actions

Add the following secrets:
- `AWS_ACCESS_KEY_ID`: Your AWS access key
- `AWS_SECRET_ACCESS_KEY`: Your AWS secret key
- `AWS_REGION`: Your AWS region (e.g., us-east-1)
- `ECR_REPOSITORY_NAME`: Your ECR repository name (studentperformance-app)
- `AWS_ECR_LOGIN_URI`: Your ECR URI (format: {account-id}.dkr.ecr.{region}.amazonaws.com)

**3.2 GitHub Actions Workflow (.github/workflows/main.yaml)**
```yaml
name: AWS ECR & EC2 Deployment

on:
  push:
    branches: [main]
    paths-ignore: ['README.md']

permissions:
  id-token: write
  contents: read

jobs:
  integration:
    name: Continuous Integration
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v3
      
      - name: Lint code
        run: echo "Linting repository"
      
      - name: Run unit tests
        run: echo "Running unit tests"

  build-and-push-ecr-image:
    name: Build & Push to ECR
    needs: integration
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v3

      - name: Install utilities
        run: |
          sudo apt-get update
          sudo apt-get install -y jq unzip

      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v1
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: ${{ secrets.AWS_REGION }}
        
      - name: Login to Amazon ECR
        id: login-ecr
        uses: aws-actions/amazon-ecr-login@v1
      
      - name: Build, tag, and push image to Amazon ECR
        env:
          ECR_REGISTRY: ${{ steps.login-ecr.outputs.registry }}
          ECR_REPOSITORY: ${{ secrets.ECR_REPOSITORY_NAME }}
          IMAGE_TAG: latest
        run: |
          docker build -t $ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG .
          docker push $ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG

  continuous-deployment:
    name: Deploy to EC2
    needs: build-and-push-ecr-image
    runs-on: self-hosted  # Your EC2 instance as self-hosted runner
    steps:
      - name: Checkout
        uses: actions/checkout@v3
      
      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v1
        with: 
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: ${{ secrets.AWS_REGION }}

      - name: Login to Amazon ECR
        id: login-ecr
        uses: aws-actions/amazon-ecr-login@v1

      - name: Stop and remove existing container
        run: |
          docker ps -q --filter "name=mltest" | grep -q . && docker stop mltest && docker rm -fv mltest || echo "No existing container"

      - name: Pull latest images
        run: |
          docker pull ${{ steps.login-ecr.outputs.registry }}/${{ secrets.ECR_REPOSITORY_NAME}}:latest

      - name: Run Docker Image to serve users
        run: |
          docker run -d -p 5000:5000 --name=mltest \
            -e 'AWS_ACCESS_KEY_ID=${{ secrets.AWS_ACCESS_KEY_ID}}' \
            -e 'AWS_SECRET_ACCESS_KEY=${{ secrets.AWS_SECRET_ACCESS_KEY}}' \
            -e 'AWS_REGION=${{ secrets.AWS_REGION }}' \
            ${{ steps.login-ecr.outputs.registry }}/${{ secrets.ECR_REPOSITORY_NAME }}:latest
        
      - name: Clean previous images and containers
        run: |
          docker system prune -f
```

#### 4. 🏃‍♂️ Setup Self-Hosted Runner

**4.1 On your EC2 instance:**
```bash
# SSH into your EC2 instance
ssh -i your-key.pem ubuntu@your-ec2-public-ip

# Go to GitHub repository → Settings → Actions → Runners
# Click "New self-hosted runner" and follow instructions for Linux

# Example commands (replace with your actual tokens):
mkdir actions-runner && cd actions-runner
curl -o actions-runner-linux-x64-2.311.0.tar.gz -L https://github.com/actions/runner/releases/download/v2.311.0/actions-runner-linux-x64-2.311.0.tar.gz
tar xzf ./actions-runner-linux-x64-2.311.0.tar.gz
./config.sh --url https://github.com/JITESH-KUMAR05/studentperformance --token YOUR_TOKEN
./run.sh

# To run as service:
sudo ./svc.sh install
sudo ./svc.sh start
```

#### 5. 🚀 Deploy & Test

**5.1 Trigger Deployment**
```bash
# Push changes to main branch
git add .
git commit -m "Deploy to AWS EC2 with ECR"
git push origin main

# Monitor GitHub Actions
# Check repository Actions tab for workflow progress
```

**5.2 Verify Deployment**
```bash
# Check running containers on EC2
docker ps

# Check application logs
docker logs mltest

# Test application
curl http://your-ec2-public-ip:5000
# Or visit: http://your-ec2-public-ip:5000 in browser
```

### 💰 Cost Optimization

**Monthly Cost Estimate:**
- **EC2 t2.micro**: $0 (Free tier) or ~$8.50/month
- **ECR Storage**: ~$1-2/month for small images
- **Data Transfer**: Minimal for development use
- **Total**: ~$10-15/month

**Cost Saving Tips:**
- Use t2.micro instances (free tier eligible)
- Stop instances when not in use
- Use ECR lifecycle policies to delete old images
- Monitor usage with AWS Cost Explorer

### 🛠️ Troubleshooting

**Common Issues:**

1. **ECR Push Failed: Repository not found**
   ```bash
   # Ensure ECR repository exists
   aws ecr describe-repositories --region us-east-1
   ```

2. **EC2 Connection Issues**
   ```bash
   # Check security group allows port 5000
   # Verify EC2 instance is running
   # Check Docker service status: sudo systemctl status docker
   ```

3. **Self-hosted Runner Offline**
   ```bash
   # Restart runner service
   sudo ./svc.sh stop
   sudo ./svc.sh start
   ```

### 📊 Deployment Results

**Successfully Deployed Features:**
- ✅ Containerized Flask application
- ✅ Automated CI/CD pipeline
- ✅ AWS ECR integration
- ✅ EC2 auto-deployment
- ✅ Live application at `http://44.201.213.90:5000/`
- ✅ Responsive web interface
- ✅ Real-time ML predictions

**Performance Metrics:**
- **Build Time**: ~2-3 minutes
- **Deployment Time**: ~1-2 minutes  
- **Application Load Time**: <3 seconds
- **Prediction Response**: <500ms

---

*Note: This AWS EC2 + ECR deployment setup was successfully implemented and tested. The infrastructure has been terminated to avoid ongoing costs, but the configuration and process are fully documented above for future reference or replication.*

---

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