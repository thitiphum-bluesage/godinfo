pipeline {
    agent any

    environment {
        // Define registry address and credentials ID
        REGISTRY = '62.72.58.117:9999'
        REGISTRY_CREDENTIALS_ID = 'harbor-credentials'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build and Scan Service 1') {
            steps {
                script {
                    // Build the Docker image
                    sh 'docker build -t godinfo_service1 ./service1'
                    // Scan the image
                    sh 'trivy image godinfo_service1'
                    // Tag the image for the registry
                    sh 'docker tag godinfo_service1 $REGISTRY/myproject/godinfo_service1:latest'
                    // Log in to Harbor registry
                    withCredentials([usernamePassword(credentialsId: REGISTRY_CREDENTIALS_ID, usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                        sh 'echo $PASSWORD | docker login $REGISTRY --username $USERNAME --password-stdin'
                    }
                    // Push the image to Harbor
                    sh 'docker push $REGISTRY/myproject/godinfo_service1:latest'
                }
            }
        }

        stage('Build and Scan Service 2') {
            steps {
                script {
                    sh 'docker build -t godinfo_service2 ./service2'
                    sh 'trivy image godinfo_service2'
                    sh 'docker tag godinfo_service2 $REGISTRY/myproject/godinfo_service2:latest'
                    withCredentials([usernamePassword(credentialsId: REGISTRY_CREDENTIALS_ID, usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                        sh 'echo $PASSWORD | docker login $REGISTRY --username $USERNAME --password-stdin'
                    }
                    sh 'docker push $REGISTRY/myproject/godinfo_service2:latest'
                }
            }
        }

        stage('Build and Scan Frontend') {
            steps {
                script {
                    sh 'docker build -t godinfo_frontend ./frontend'
                    sh 'trivy image godinfo_frontend'
                    sh 'docker tag godinfo_frontend $REGISTRY/myproject/godinfo_frontend:latest'
                    withCredentials([usernamePassword(credentialsId: REGISTRY_CREDENTIALS_ID, usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                        sh 'echo $PASSWORD | docker login $REGISTRY --username $USERNAME --password-stdin'
                    }
                    sh 'docker push $REGISTRY/myproject/godinfo_frontend:latest'
                }
            }
        }
    }
}
