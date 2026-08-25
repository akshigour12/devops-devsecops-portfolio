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
                    docker build -t akshigour12/devops-devsecops-portfolio:latest .
                '''
            }
        }

        stage('Push Docker Image') {
            steps {
                withDockerRegistry([credentialsId: 'dockerhub', url: '']) {
                    sh '''
                        docker push akshigour12/devops-devsecops-portfolio:latest
                    '''
                }
            }
        }

        stage('Deploy to EC2') {
            steps {
                sshagent(credentials: ['ec2-ssh']) {
                    sh '''
                        ssh -o StrictHostKeyChecking=no ec2-user@13.201.21.141 << EOF
                        docker pull akshigour12/devops-devsecops-portfolio:latest

                        docker stop devops-devsecops-portfolio || true
                        docker rm devops-devsecops-portfolio || true

                        docker run -d \
                          --name devops-devsecops-portfolio \
                          --restart always \
                          -p 80:5000 \
                          akshigour12/devops-devsecops-portfolio:latest
                        EOF
                    '''
                }
            }
        }
    }

    post {
        success {
            echo 'Jenkins CI/CD pipeline completed successfully.'
        }

        failure {
            echo 'Jenkins CI/CD pipeline failed.'
        }

        always {
            echo 'Pipeline execution finished.'
        }
    }
}
