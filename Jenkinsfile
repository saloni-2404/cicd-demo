pipeline {
    agent {
        docker {
            image 'python:3.11-slim'
            args '-u root'
        }
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'feature/jenkins-setup', url: 'https://github.com/saloni-2404/cicd-demo.git'
            }
        }

        stage('List files') {
            steps {
                sh 'ls -la'
            }
        }

        stage('Check Python') {
            steps {
                sh '''
                    python --version
                    pip --version
                '''
            }
        }

        stage('Install dependencies') {
            steps {
                sh '''
                    pip install --upgrade pip
                    pip install pytest

                    if [ -f requirements.txt ]; then
                        pip install -r requirements.txt
                    else
                        echo "No requirements.txt found"
                    fi
                '''
            }
        }

        stage('Run tests') {
            steps {
                sh '''
                    pytest -v
                '''
            }
        }
    }
}
