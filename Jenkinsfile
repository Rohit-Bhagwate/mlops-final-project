pipeline {
    agent any

    stages {

        stage('Clean Old Docker') {
            steps {
                sh '''
                sudo docker rm -f churn-container || true
                sudo docker rmi churn-app || true
                sudo docker system prune -af || true
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                sudo docker build -t churn-app .
                '''
            }
        }

        stage('Run Docker Container') {
            steps {
                sh '''
                sudo docker run --name churn-container --rm churn-app
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