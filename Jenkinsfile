pipeline{
    agent any

    stages {
        stage('Build') {
            steps {
                echo '====== Build Stage ======'
            }
        }
        stage('Test') {
            steps {
                echo '====== Test Stage ======'
            }
        }
        stage('Deploy') {
            steps {
                echo '====== Deploy Stage ======'
            }
        }
    }
    post {
        always {
            echo '====== Cleaning Workspace ======'
            cleanWs()
        }
        success {
            echo 'This will run only if successful'
        }
        failure {
            echo 'This will run only if failed'
        }
    }

}