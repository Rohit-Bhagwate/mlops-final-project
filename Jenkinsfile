pipeline {
agent any

environment {
    AWS_ACCOUNT_ID = "232932848445"
    AWS_REGION = "ap-south-1"
    ECR_REPO = "churn-app"
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
            aws ecr get-login-password --region $AWS_REGION | \
            docker login --username AWS --password-stdin \
            $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com
            '''
        }
    }

    stage('Tag Docker Image') {
        steps {
            sh '''
            docker tag churn-app:latest \
            $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPO:$IMAGE_TAG
            '''
        }
    }

    stage('Push Docker Image to ECR') {
        steps {
            sh '''
            docker push \
            $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPO:$IMAGE_TAG
            '''
        }
    }

    stage('Run Docker Container') {
        steps {
            sh '''
            docker run --name churn-container \
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
