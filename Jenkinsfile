pipeline {

    agent any

    environment {
        AWS_ACCOUNT_ID = "232932848445"
        AWS_DEFAULT_REGION = "ap-south-1"
        IMAGE_REPO_NAME = "churn-app"
        IMAGE_TAG = "latest"
    }

    stages {

        stage('Clean Old Docker') {
            steps {
                sh '''
                docker rm -f churn-container || true
                docker rmi churn-app || true
                docker system prune -af || true
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t churn-app .
                '''
            }
        }

        stage('Login to ECR') {
            steps {
                sh '''
                aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin 232932848445.dkr.ecr.ap-south-1.amazonaws.com
                '''
            }
        }

        stage('Tag Docker Image') {
            steps {
                sh '''
                docker tag churn-app:latest 232932848445.dkr.ecr.ap-south-1.amazonaws.com/churn-app:latest
                '''
            }
        }

        stage('Push Docker Image to ECR') {
            steps {
                sh '''
                docker push 232932848445.dkr.ecr.ap-south-1.amazonaws.com/churn-app:latest
                '''
            }
        }

        stage('Run Docker Container') {
            steps {
                sh '''
                docker rm -f churn-container || true

                docker run -d \
                --name churn-container \
                -p 8000:8000 \
                -v /var/lib/jenkins/.aws:/root/.aws \
                churn-app
                '''
            }
        }

    }

    post {

        success {
            echo 'Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed!'
        }
    }
}