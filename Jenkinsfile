pipeline {
    agent {label 'linux_label'}

    stages {
        stage('Checkout') {
            steps {
                sh 'git clone https://github.com/omriv88/World-of-Games.git'
            }
        }
                stage('Build') {
            steps {
                sh 'docker build -t omriv/flask_score_app:latest /root/workspace/linux-test/World-of-Games/'
            }
        }
                stage('run') {
            steps {
                sh 'docker-compose -f /root/workspace/linux-test/World-of-Games/docker-compose.yaml up'
            }
        }
                stage('Test') {
            steps {
                sh 'pwd'
            }
        }
                stage('Finalize-login') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKER_HUB_CREDENTIALS_USR --password-stdin'
            }
        }
                stage('Finalize') {
            steps {
                sh 'docker push omriv/flask_score_app:latest'
            }
        }
    }
}
