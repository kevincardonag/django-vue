pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'pwd'
                sh 'cd ..'
                sh 'virtualenv -p /opt/rh/rh-python36/root/bin/python3.6 env'
                sh 'env/bin/activate'
                sh 'pwd'
                sh 'cd superpizzas'
                sh 'env/bin/pip3 install setuptools --upgrade'
                sh 'env/bin/pip3 install -r requirements.txt'
                sh 'pwd'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying'
            }
        }

    }
}