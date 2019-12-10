pipeline {
    agent none
    stages {
        stage('Build') {
            steps {
                sh 'pwd'
                sh 'virtualenv -p /opt/rh/rh-python36/root/bin/python3.6 env'
                sh '. env/bin/activate'
                sh 'python --version'
                sh 'env/bin/pip install -r requirements.txt'
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