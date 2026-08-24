pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                    python3 --version
                    python3 -m venv .venv
                    .venv/bin/python -m pip install --upgrade pip
                    .venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    .venv/bin/python -m pytest -v tests/
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build -t devops-devsecops-portfolio:ci .
                '''
            }
        }
    }

    post {
        success {
            echo 'Jenkins CI pipeline completed successfully.'
        }

        failure {
            echo 'Jenkins CI pipeline failed.'
        }

        always {
            echo 'Pipeline execution finished.'
        }
    }
}
