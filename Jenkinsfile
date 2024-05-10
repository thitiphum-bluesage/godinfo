pipeline {
    agent any

    environment {
        // Define common image tag, e.g., based on Jenkins build number or a tag
        IMAGE_TAG = "latest"
    }

    stages {
        stage('Pull Trivy Image') {
            steps {
                script {
                    // Ensures the Trivy image is always up to date
                    sh 'docker pull aquasec/trivy:latest'
                }
            }
        }

        stage('Build Docker Images') {
            parallel {
                stage('Build Frontend Image') {
                    steps {
                        dir('frontend') {
                            sh "docker build -t frontend-image:${IMAGE_TAG} ."
                        }
                    }
                }
                stage('Build Service1 Image') {
                    steps {
                        dir('service1') {
                            sh "docker build -t service1-image:${IMAGE_TAG} ."
                        }
                    }
                }
                stage('Build Service2 Image') {
                    steps {
                        dir('service2') {
                            sh "docker build -t service2-image:${IMAGE_TAG} ."
                        }
                    }
                }
            }
        }

        stage('Trivy Security Scan') {
            parallel {
                stage('Scan Frontend Image') {
                    steps {
                        script {
                            sh "docker run --rm -v /var/run/docker.sock:/var/run/docker.sock aquasec/trivy image --exit-code 1 --no-progress frontend-image:${IMAGE_TAG}"
                        }
                    }
                }
                stage('Scan Service1 Image') {
                    steps {
                        script {
                            sh "docker run --rm -v /var/run/docker.sock:/var/run/docker.sock aquasec/trivy image --exit-code 1 --no-progress service1-image:${IMAGE_TAG}"
                        }
                    }
                }
                stage('Scan Service2 Image') {
                    steps {
                        script {
                            sh "docker run --rm -v /var/run/docker.sock:/var/run/docker.sock aquasec/trivy image --exit-code 1 --no-progress service2-image:${IMAGE_TAG}"
                        }
                    }
                }
            }
        }
    }

    post {
        always {
            // Clean-up operations, e.g., stopping Docker containers
            echo "Clean-up operations..."
        }
    }
}
