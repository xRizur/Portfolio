import com.hierynomus.sshj.SSHClient
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
                        def sshClient = new SSHClient()
                        sshClient.addHostKeyVerifier("aa:bb:cc:dd:ee:ff:gg:hh:ii:jj:kk:ll:mm:nn:oo:pp")
                        sshClient.connect("${AZURE_VM_PUBLIC_IP}", 22)
                        sshClient.auth(azureVmSshCredentials)
                        sshClient.withSession { session ->
                            session.exec("git clone https://github.com/xRizur/FlaskProject.git")
                            session.exec("cd FlaskProject")
                            session.exec("docker build -t my-flask-app .")
                            session.exec("docker-compose up -d")
                        }
                    }
                }
            }
        }
        }
    }