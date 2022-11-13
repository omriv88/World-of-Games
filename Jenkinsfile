pipeline {
    agent {label 'linux_label'}
    environment {
        DOCKERHUB_CREDENTIALS=credentials('docker-hub-omri')
    }
    
    stages {
        stage('Checkout-check the Ripository') {
            steps {
                sh 'git clone https://github.com/omriv88/World-of-Games.git'
                sh 'ls -l'
            }
        }
                stage('Build-Build The APP') {
            steps {
                sh 'docker build -t omriv/flask_score_app:latest /root/workspace/linux-test/World-of-Games/'
            }
        }
                stage('Run-Run The APP') {
            steps {
                sh 'docker-compose -f /root/workspace/linux-test/World-of-Games/docker-compose.yaml up --build -d '
                sh 'docker ps'
            }
        }
                stage('Test-Test The APP With Selenium') {
                    agent {label 'label_local_pc'}
            steps {
                git branch: 'main', url: 'https://github.com/omriv88/World-of-Games.git'
                bat 'python e2e.py'
            }
        }
                stage('Finalize-DockerHub') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        }
                stage('Finalize Push The Image To Dockerhub') {
            steps {
                sh 'docker push omriv/flask_score_app:latest'
            }
        }
    }
    post {
      always {
        sh 'docker logout'
      }
    }
}
