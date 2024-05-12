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
                sh 'curl -sfL https://github.com/aquasec/trivy/releases/download/trivy_0.51.1_Linux_amd64.deb -o trivy.deb'
                sh 'sudo dpkg -i trivy.deb'
            }
        }

        stage('Build and Scan Service 1') {
            steps {
                sh 'docker build -t godinfo_service1./service1'
                sh 'trivy image godinfo_service1'
            }
        }

        stage('Build and Scan Service 2') {
            steps {
                sh 'docker build -t godinfo_service2./service2'
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
