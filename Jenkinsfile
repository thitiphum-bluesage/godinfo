pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                // Build Docker images for each service
                dir('frontend') {
                    sh 'docker build -t frontend .'
                }
                
                dir('service1') {
                    sh 'docker build -t service1 .'
                }
                
                dir('service2') {
                    sh 'docker build -t service2 .'
                }
            }
        }
    }
}
