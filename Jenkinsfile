pipeline {
    agent any

    stages {

        stage('Setup') {
            steps {
                // Pull Trivy image at the beginning to ensure it's updated
                sh 'docker pull aquasec/trivy'
            }
        }

        stage('Build Docker Images') {
            steps {
                dir('frontend') {
                    sh 'docker build -t frontend-image .'
                }
                dir('service1') {
                    sh 'docker build -t service1-image .'
                }
                dir('service2') {
                    sh 'docker build -t service2-image .'
                }
            }
        }

        stage('Trivy Scan') {
            steps {
                dir('frontend') {
                    sh 'docker run --rm -v /var/run/docker.sock:/var/run/docker.sock -v $(pwd):/root/.cache/ aquasec/trivy image --exit-code 1 --no-progress frontend-image'
                }
                dir('service1') {
                    sh 'docker run --rm -v /var/run/docker.sock:/var/run/docker.sock -v $(pwd):/root/.cache/ aquasec/trivy image --exit-code 1 --no-progress service1-image'
                }
                dir('service2') {
                    sh 'docker run --rm -v /var/run/docker.sock:/var/run/docker.sock -v $(pwd):/root/.cache/ aquasec/trivy image --exit-code 1 --no-progress service2-image'
                }
            }
        }
    }
}
