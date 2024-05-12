pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build and Scan Service 1') {
            steps {
                sh 'docker build -t godinfo_service1 ./service1'
                sh 'trivy image godinfo_service1'
            }
        }

        stage('Build and Scan Service 2') {
            steps {
                sh 'docker build -t godinfo_service2 ./service2'
                sh 'trivy image godinfo_service2'
            }
        }

        stage('Build and Scan Frontend') {
            steps {
                sh 'docker build -t godinfo_frontend./frontend'
                sh 'trivy image godinfo_frontend'
            }
        }
    }
}
