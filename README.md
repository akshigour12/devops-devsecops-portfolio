# 🚀 DevOps & DevSecOps Portfolio

A production-ready **DevOps & DevSecOps Portfolio Website** built using **Python Flask** and deployed through a fully automated **CI/CD pipeline** using **Jenkins, Docker, GitHub Webhooks, Docker Hub, AWS EC2, and Nginx**.

The project demonstrates modern DevOps practices including automated testing, containerization, image publishing, and zero-touch deployment on every GitHub push.

---

# 📌 Features

- Responsive Portfolio Website
- Python Flask Backend
- Dockerized Application
- Jenkins CI/CD Pipeline
- GitHub Webhook Integration
- Automated Docker Image Build
- Docker Hub Integration
- Automatic Deployment to AWS EC2
- Nginx Reverse Proxy
- Unit Testing with Pytest
- Secure SSH-based Deployment
- Production-style DevOps Workflow

---

# 🛠 Tech Stack

### Backend
- Python
- Flask

### Frontend
- HTML5
- CSS3
- JavaScript

### DevOps
- Docker
- Jenkins
- GitHub
- GitHub Webhooks
- Docker Hub
- AWS EC2
- Nginx
- Linux
- SSH

### Testing
- Pytest

---

# 📂 Project Structure

```
devops-devsecops-portfolio/
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│
├── tests/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── Jenkinsfile
├── .dockerignore
└── README.md
```

---

# ⚙️ CI/CD Workflow

```
Developer
      │
      ▼
GitHub Repository
      │
      ▼
GitHub Webhook
      │
      ▼
Jenkins Pipeline
      │
      ├── Checkout Source Code
      ├── Setup Python Environment
      ├── Install Dependencies
      ├── Run Unit Tests
      ├── Build Docker Image
      ├── Push Image to Docker Hub
      └── Deploy to AWS EC2
                    │
                    ▼
              Docker Container
                    │
                    ▼
                 Nginx
                    │
                    ▼
           Portfolio Website
```

---

# 🚀 Jenkins Pipeline Stages

✔ Checkout Source Code

✔ Setup Python Virtual Environment

✔ Install Project Dependencies

✔ Run Pytest Unit Tests

✔ Build Docker Image

✔ Push Docker Image to Docker Hub

✔ SSH into AWS EC2

✔ Pull Latest Docker Image

✔ Stop Previous Container

✔ Deploy Updated Container

✔ Remove Old Docker Images

---

# 🐳 Docker

### Build Image

```bash
docker build -t devops-devsecops-portfolio .
```

### Run Container

```bash
docker run -d -p 5000:5000 devops-devsecops-portfolio
```

---

# 💻 Run Locally

Clone Repository

```bash
git clone https://github.com/akshigour12/devops-devsecops-portfolio.git
```

Go to project folder

```bash
cd devops-devsecops-portfolio
```

Create Virtual Environment

```bash
python -m venv .venv
```

Activate Environment

Linux

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

Install Requirements

```bash
pip install -r requirements.txt
```

Run Application

```bash
python app.py
```

Open browser

```
http://127.0.0.1:5000
```

---

# 🧪 Run Tests

```bash
pytest tests/
```

---

# 📸 Project Screenshots

- Home Page
- About Page
- Skills
- Projects
- Certifications
- Contact Page
- Jenkins Pipeline Success
- Docker Hub Repository
- AWS EC2 Deployment
- Live Portfolio Website

---

# 📈 Future Improvements

- HTTPS using Let's Encrypt
- Terraform Infrastructure
- Kubernetes Deployment
- SonarQube Code Analysis
- Trivy Image Scanning
- Prometheus Monitoring
- Grafana Dashboard
- AWS Load Balancer
- GitHub Actions Pipeline
- Blue-Green Deployment

---

# 🙏 Acknowledgments

This portfolio project is part of my learning journey in **DevOps, DevSecOps, Cloud Computing, and Cyber Security**.

I would like to express my sincere gratitude to **Shubham Gour** for sharing high-quality educational content, practical DevOps guidance, and real-world project ideas through YouTube and LinkedIn. His tutorials and hands-on approach have been an important source of inspiration and have significantly contributed to my learning journey.

### Connect with Shubham Gour

<p align="left">

<a href="https://www.youtube.com/@Shubhamgourtech">
<img src="https://img.shields.io/badge/YouTube-Shubham%20Gour-FF0000?style=for-the-badge&logo=youtube&logoColor=white">
</a>

<a href="https://www.linkedin.com/in/theshubhamgour/">
<img src="https://img.shields.io/badge/LinkedIn-Shubham%20Gour-0077B5?style=for-the-badge&logo=linkedin&logoColor=white">
</a>

</p>

Thank you for inspiring and guiding aspiring DevOps engineers through your educational content.

---

# 👩‍💻 Author

## Akshita Gour

<p align="left">

<a href="https://github.com/akshigour12">
<img src="https://img.shields.io/badge/GitHub-akshigour12-181717?style=for-the-badge&logo=github&logoColor=white">
</a>

<a href="https://www.linkedin.com/in/akshita-g-6a24871a4/">
<img src="https://img.shields.io/badge/LinkedIn-Akshita%20Gour-0077B5?style=for-the-badge&logo=linkedin&logoColor=white">
</a>

</p>

---


