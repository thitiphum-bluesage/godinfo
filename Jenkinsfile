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
            parallel {
                stage('Build Frontend Image') {
                    steps {
                        dir('frontend') {
                            sh 'docker build -t frontend-image .'
                        }
                    }
                }
                stage('Build Service1 Image') {
                    steps {
                        dir('service1') {
                            sh 'docker build -t service1-image .'
                        }
                    }
                }
                stage('Build Service2 Image') {
                    steps {
                        dir('service2') {
                            sh 'docker build -t service2-image .'
                        }
                    }
                }
            }
        }

        stage('Trivy Scan') {
            parallel {
                stage('Trivy Scan Frontend Image') {
                    steps {
                        dir('frontend') {
                            sh 'docker run --rm -v /var/run/docker.sock:/var/run/docker.sock -v $(pwd):/root/.cache/ aquasec/trivy image --exit-code 1 --no-progress frontend-image'
                        }
                    }
                }
                stage('Trivy Scan Service1 Image') {
                    steps {
                        dir('service1') {
                            sh 'docker run --rm -v /var/run/docker.sock:/var/run/docker.sock -v $(pwd):/root/.cache/ aquasec/trivy image --exit-code 1 --no-progress service1-image'
                        }
                    }
                }
                stage('Trivy Scan Service2 Image') {
                    steps {
                        dir('service2') {
                            sh 'docker run --rm -v /var/run/docker.sock:/var/run/docker.sock -v $(pwd):/root/.cache/ aquasec/trivy image --exit-code 1 --no-progress service2-image'
                        }
                    }
                }
            }
        }

    }
}
