node {

    try {
        stage 'Checkout'
            checkout scm

        stage 'Test'
            sh 'virtualenv -p /opt/rh/rh-python36/root/bin/python3.6 env'
            sh '. env/bin/activate'
            sh 'python --version'
            sh 'env/bin/pip install -r requirements.txt'
            sh 'env/bin/python3.5 manage.py test --testrunner=djtrump.tests.test_runners.NoDbTestRunner'

        stage 'Deploy'
            sh 'echo desplegando'
    }

    catch (err) {
        throw err
    }

}