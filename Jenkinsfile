node {

    try {
        stage 'Checkout'
            checkout scm

        stage 'Test'
            sh 'yum install python-devel'
            sh 'mkvirtualenv -p /opt/rh/rh-python36/root/bin/python3.6 env'
            sh '. env/bin/activate'
            sh 'python --version'
            sh 'env/bin/pip install -r requirements.txt'
            sh 'pwd'

        stage 'Deploy'
            sh 'echo desplegando'
    }

    catch (err) {
        throw err
    }

}