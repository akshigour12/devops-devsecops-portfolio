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
