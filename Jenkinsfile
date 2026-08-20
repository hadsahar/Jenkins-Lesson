pipeline{
    agent any

    stages {
        stage('Build') {
            steps {
                echo '====== Build Stage ======'
                sh 'echo "Jenkins Task <<Build stage>>" > app.txt'
                sh 'cat app.txt' 
            }
        }
        stage('Test') {
            steps {
                echo '====== Test Stage ======'
                sh 'echo "Checking if the file exists"'
                sh 'test -f app.txt && echo "File exists" || echo "File does not exist"'
            }
        }
        stage('Deploy') {
            steps {
                echo '====== Deploy Stage ======'
                sh 'mkdir -p deploy'
                sh 'cp app.txt deploy/'
                sh 'ls -l deploy/'
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