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
                sh 'pip install -r requirements.txt || true'
            }
        }

        stage('Run tests') {
            steps {
                sh 'pytest || true'
            }
        }
    }
}
