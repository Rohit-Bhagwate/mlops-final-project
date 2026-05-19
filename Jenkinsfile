pipeline {
agent any

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