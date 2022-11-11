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
                sh 'docker build -t flask_score_app /root/workspace/linux-test/World-of-Games/'
            }
        }
                stage('run') {
            steps {
                sh 'cd /root/workspace/linux-test/World-of-Games/'
                sh 'docker-compose up'
            }
        }
                stage('Test') {
            steps {
                sh 'pwd'
            }
        }
                stage('Finalize') {
            steps {
                sh 'docker commit b085b49dccd2 omriv/flask_score_app'
                sh 'docker image push omriv/flask_score_app:tag'
            }
        }
    }
}
