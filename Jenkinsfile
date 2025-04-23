pipeline {
    agent any

    environment {
        DOCKER_HUB_REPO = 'aman2409/stock_pred'
        DOCKER_IMAGE_TAG = "latest"
        DOCKER_CREDENTIALS_ID = 'docker-hub-credentials'
        GIT_REPO = 'https://github.com/aman-ch09/Stock-Market-Prediction-Using-LSTM.git'  // 🔁 Replace this
        GITHUB_CREDENTIALS_ID = 'github-credentials'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main',
                    credentialsId: "${GITHUB_CREDENTIALS_ID}",
                    url: "${GIT_REPO}"
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    bat "docker build -t ${DOCKER_HUB_REPO}:${DOCKER_IMAGE_TAG} ."
                }
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: "${DOCKER_CREDENTIALS_ID}", usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        bat """
                        echo|set /p="%DOCKER_PASSWORD%" | docker login -u %DOCKER_USERNAME% --password-stdin
                        docker push ${DOCKER_HUB_REPO}:${DOCKER_IMAGE_TAG}
                        """
                    }
                }
            }
        }

        stage('Deploy Docker Container') {
            steps {
                script {
                    bat '''
                    echo Stopping and removing old container (if exists)...
                    FOR /F %%i IN ('docker ps -a -q --filter "name=stock_pred"') DO (
                        docker rm -f %%i
                    )
                    echo Running new container...
                    docker run -d --name stock_pred -p 8005:8000 aman2409/stock_pred:latest
                    '''
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}
