pipeline {
    agent any
    stages {
        stage('Deploy') {
            steps {
                withCredentials([sshUserPrivateKey(credentialsId: 'ssh-credentials', keyFileVariable: 'SSH_KEY', passphraseVariable: '', usernameVariable: 'SSH_USERNAME')]) {
                    sh 'ssh -o StrictHostKeyChecking=no -i $SSH_KEY $SSH_USERNAME@108.142.129.104 "docker-compose down && docker-compose up -d"'
                }
            }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t pyapp .'
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
}