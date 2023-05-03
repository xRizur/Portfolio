pipeline {
    agent any
    environment {
        AZURE_VM_SSH_CREDENTIALS = credentials('azure-vm-ssh-credentials-id')
        AZURE_VM_PUBLIC_IP = '108.142.129.104'
    }
    stages {
        stage('Deploy') {
            steps {
                script {
                    sshagent(['azure-vm-ssh-credentials-id']) {
                        sshScript remote: "ssh -o StrictHostKeyChecking=no -l xrizur ${AZURE_VM_PUBLIC_IP}",
                            script: """
                                git clone https://github.com/xRizur/FlaskProject.git
                                cd FlaskProject
                                docker build -t my-flask-app .
                                docker-compose up -d
                            """
                    }
                }
            }
        }
    }
}