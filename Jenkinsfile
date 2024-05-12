pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // This step is automatically handled by Jenkins if SCM is configured in the job settings
                checkout scm
            }
        }

        stage('Build Docker Images') {
            steps {
                sh 'docker-compose build'
            }
        }
    }
}
