pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Trivy') {
            steps {
                // Downloading Trivy package
                sh 'curl -sfL https://github.com/aquasec/trivy/releases/download/v0.51.1/trivy_0.51.1_Linux-64bit.deb -o trivy.deb'
                // Installing Trivy package, assuming sudo rights are available
                sh 'sudo dpkg -i trivy.deb'
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
                sh 'docker build -t godinfo_frontend ./frontend'
                sh 'trivy image godinfo_frontend'
            }
        }
    }
}
