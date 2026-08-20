pipeline{
    agent any

    environment {
        APP_VERSION = '1.0'
        APP_NAME = 'myapp'
        DOCKER_REPO = "hadsahar/${APP_NAME}"
        BUILD_INFO_FILE = 'build_info.txt'
        FILE_TO_TEST = "${BUILD_INFO_FILE}"
    }
    stages {
        stage('Build') {
            steps {
                echo '====== Build Stage ======'
                sh 'echo "Jenkins Task <<Build stage>>" > app.txt'
                sh 'cat app.txt'
                sh '''
                {
                    echo "APP_NAME=${APP_NAME}"
                    echo "APP_VERSION=${APP_VERSION}"
                    echo "BUILD_NUMBER=${BUILD_NUMBER}"
                    echo "BUILD_DATE=$(date -u +%Y-%m-%d_%H-%M-%S)"
                } > ${BUILD_INFO_FILE}
                cat ${BUILD_INFO_FILE}
                '''
                sh 'echo "The repo path is: DOCKER_REPO=${DOCKER_REPO}"'

            }
        }
        stage('Test') {
            stages{
                stage('Test Init') {
                    steps {
                        echo '====== Test Stage ======'
                    }
                }
                stage('Run Tests') {
                    parallel {
                        stage('File Stage') {
                            steps {
                                sh '''
                                    if [ -f app.txt ]; then
                                        echo "File app.txt exists."
                                    else
                                        echo "ERROR: File app.txt does not exist."
                                        exit 1
                                    fi
                                '''
                            }
                        }
                        stage('Build Info Stage') {
                            steps {
                                sh 'python3 test.py myapp'
                            }
                        }
                    }
                }
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