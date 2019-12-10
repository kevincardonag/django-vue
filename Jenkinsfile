node {

    try {
        stage 'Checkout'
            checkout scm

        stage 'Test'
            sh 'rmvirtualenv env'
            sh 'mkvirtualenv env'
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