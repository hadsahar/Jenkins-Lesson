pipeline{
    agent any

    environment {
        APP_VERSION = '1.0'
        APP_NAME = 'MyApp'
        DOCKER_REPO = 'hadsahar/${APP_NAME}'
    }
    stages {
        stage('Build') {
            steps {
                echo '====== Build Stage ======'
                sh 'echo "Jenkins Task <<Build stage>>" > app.txt'
                sh 'cat app.txt' 
                sh 'echo "The App version is ${APP_VERSION}"'
                sh 'echo "APP_NAME=${APP_NAME}"'
                sh 'echo "The repo path is: DOCKER_REPO=${DOCKER_REPO}"'
            }
        }
        stage('Test') {
            steps {
                echo '====== Test Stage ======'
                sh 'echo "Checking if the file exists"'
                sh 'test -f app.txt && echo "File exists" || echo "File does not exist"'
                sh 'echo "The pipeline name is ${JOB_NAME}"'
                sh 'echo "The build number is ${BUILD_NUMBER}"'
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