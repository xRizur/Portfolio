pipeline {
    agent any
    stages {
        stage('Deploy') {
            when {
                branch 'master'
            }
            steps {
                withCredentials([sshUserPrivateKey(credentialsId: 'ssh-credentials', keyFileVariable: 'SSH_KEY', passphraseVariable: '', usernameVariable: 'SSH_USERNAME')]) {
                    sh '''
                    ssh -o StrictHostKeyChecking=no -i $SSH_KEY xrizur@108.142.129.104
                        rm -rf FlaskProject
                        git clone https://github.com/xRizur/FlaskProject
                        cd FlaskProject
                        docker build -t my-flask-app .
                        docker-compose down
                        docker-compose up -d
                    '''
                }
            }
        }
        }
    }