pipeline {
    agent any
    stages {
        stage('Deploy') {
            when {
                branch 'master'
            }
            steps {
                withCredentials([sshUserPrivateKey(credentialsId: 'ssh-credentials', keyFileVariable: 'SSH_KEY', passphraseVariable: '', usernameVariable: 'SSH_USERNAME')]) {
                    sh 'ssh -o StrictHostKeyChecking=no -i $SSH_KEY $SSH_USERNAME@108.142.129.104'
                    script {
                        remote = [:]
                        remote.name = 'remote'

                        sshCommand remote: remote, command: 'sudo git clone https://github.com/xRizur/FlaskProject'
                        sshCommand remote: remote, command: 'cd FlaskProject && sudo docker build -t my-flask-app .'
                     }
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t my-flask-app .'
            }
        }
        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', passwordVariable: 'DOCKERHUB_PASSWORD', usernameVariable: 'DOCKERHUB_USERNAME')]) {
                    sh 'docker login -u $DOCKERHUB_USERNAME -p $DOCKERHUB_PASSWORD'
                }
                sh 'docker push my-flask-app'
            }
        }
    }
}