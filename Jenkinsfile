pipeline {
    agent any

    environment {
        IMAGE_NAME = "akshigour12/devops-devsecops-portfolio:latest"
        EC2_HOST = "13.232.53.81"
    }

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
                    docker build -t ${IMAGE_NAME} .
                '''
            }
        }

        stage('Push Docker Image') {
            steps {
                withDockerRegistry([credentialsId: 'dockerhub', url: '']) {
                    sh '''
                        docker push ${IMAGE_NAME}
                    '''
                }
            }
        }

        stage('Deploy to EC2') {
            steps {
                withCredentials([
                    sshUserPrivateKey(
                        credentialsId: 'ec2-ssh',
                        keyFileVariable: 'SSH_KEY',
                        usernameVariable: 'SSH_USER'
                    )
                ]) {
                    sh '''
                        chmod 600 $SSH_KEY

                        ssh -i $SSH_KEY \
                            -o StrictHostKeyChecking=no \
                            $SSH_USER@$EC2_HOST << EOF

                        docker pull ${IMAGE_NAME}

                        docker stop devops-devsecops-portfolio || true
                        docker rm devops-devsecops-portfolio || true

                        docker run -d \
                            --name devops-devsecops-portfolio \
                            --restart always \
                            -p 80:5000 \
                            ${IMAGE_NAME}

                        docker image prune -f

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
