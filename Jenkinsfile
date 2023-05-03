pipeline {
    agent any
    environment {
        AZURE_VM_SSH_CREDENTIALS = credentials('azure-vm-ssh-credentials-id')
        AZURE_VM_PUBLIC_IP = '108.142.129.104'
    }
    stages {
        stage('Deploy') {
            steps {
                withCredentials([sshUserPrivateKey(credentialsId: 'azure-vm-ssh-credentials-id', keyFileVariable: 'SSH_KEY_FILE', passphraseVariable: '', usernameVariable: 'SSH_USERNAME')]) {
                    sshCommand remote: [
                        host: "${AZURE_VM_PUBLIC_IP}",
                        port: 22,
                        user: "${SSH_USERNAME}",
                        keyFile: "${SSH_KEY_FILE}",
                        knownHosts: 'ssh-rsa AA... user@host',
                        allowEmptyPassword: true
                    ], command: [
                        "git clone https://github.com/xRizur/FlaskProject.git",
                        "cd FlaskProject",
                        "docker build -t my-flask-app .",
                        "docker-compose up -d"
                    ].join(" && ")
                }
            }
        }
    }
}