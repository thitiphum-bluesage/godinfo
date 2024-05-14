pipeline {
    agent any

    environment {
        // Define registry address and credentials ID
        REGISTRY = '62.72.58.117:9999'
        REGISTRY_CREDENTIALS_ID = 'harbor-credentials'
    }

    stages {
        stage('Setup') {
            steps {
                script {
                    // Checkout the source code
                    checkout scm
                    // Login to Docker registry before starting the build and push processes
                    withCredentials([usernamePassword(credentialsId: REGISTRY_CREDENTIALS_ID, usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                        sh 'echo $PASSWORD | docker login $REGISTRY --username $USERNAME --password-stdin'
                    }
                }
            }
        }

        stage('Build and Scan Service 1') {
            steps {
                script {
                    sh 'docker build -t godinfo_service1 ./service1'
                    sh 'trivy image godinfo_service1'
                    sh 'docker tag godinfo_service1 $REGISTRY/myproject/godinfo_service1:$BUILD_NUMBER'
                    sh 'docker push $REGISTRY/myproject/godinfo_service1:$BUILD_NUMBER'
                    // Also tag and push the 'latest' if needed
                    sh 'docker tag godinfo_service1 $REGISTRY/myproject/godinfo_service1:latest'
                    sh 'docker push $REGISTRY/myproject/godinfo_service1:latest'
                }
            }
        }

        stage('Build and Scan Service 2') {
            steps {
                script {
                    sh 'docker build -t godinfo_service2 ./service2'
                    sh 'trivy image godinfo_service2'
                    sh 'docker tag godinfo_service2 $REGISTRY/myproject/godinfo_service2:$BUILD_NUMBER'
                    sh 'docker push $REGISTRY/myproject/godinfo_service2:$BUILD_NUMBER'
                    sh 'docker tag godinfo_service2 $REGISTRY/myproject/godinfo_service2:latest'
                    sh 'docker push $REGISTRY/myproject/godinfo_service2:latest'
                }
            }
        }

        stage('Build and Scan Frontend') {
            steps {
                script {
                    sh 'docker build -t godinfo_frontend ./frontend'
                    sh 'trivy image godinfo_frontend'
                    sh 'docker tag godinfo_frontend $REGISTRY/myproject/godinfo_frontend:$BUILD_NUMBER'
                    sh 'docker push $REGISTRY/myproject/godinfo_frontend:$BUILD_NUMBER'
                    sh 'docker tag godinfo_frontend $REGISTRY/myproject/godinfo_frontend:latest'
                    sh 'docker push $REGISTRY/myproject/godinfo_frontend:latest'
                }
            }
        }
    }
}
