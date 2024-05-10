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
                    // Use Jenkins workspace environment variable for clarity
                    sh 'docker run --rm -v /var/run/docker.sock:/var/run/docker.sock -v ${WORKSPACE}/frontend:/root/.cache/ aquasec/trivy image --exit-code 1 --no-progress frontend-image'
                }
                dir('service1') {
                    sh 'docker run --rm -v /var/run/docker.sock:/var/run/docker.sock -v ${WORKSPACE}/service1:/root/.cache/ aquasec/trivy image --exit-code 1 --no-progress service1-image'
                }
                dir('service2') {
                    sh 'docker run --rm -v /var/run/docker.sock:/var/run/docker.sock -v ${WORKSPACE}/service2:/root/.cache/ aquasec/trivy image --exit-code 1 --no-progress service2-image'
                }
            }
        }
    }
    post {
        failure {
            // Actions to take if the pipeline fails
            mail to: 'your-email@example.com',
                 subject: "Failed Pipeline: ${env.JOB_NAME} [${env.BUILD_NUMBER}]",
                 body: "Something is wrong with this build: ${env.BUILD_URL}"
        }
    }
}
