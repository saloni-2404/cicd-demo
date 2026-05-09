pipeline {
    agent any

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

        stage('Install dependencies') {
            steps {
                sh '''
                    python3 --version
                    python3 -m pip --version
                    python3 -m pip install --upgrade pip
                    python3 -m pip install pytest
                '''
            }
        }

        stage('Run tests') {
            steps {
                sh '''
                    python3 -m pytest
                '''
            }
        }
    }
}
