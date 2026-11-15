pipeline {
    agent any
    stages {
        stage('Setup') {
            steps {
                sh'''
                    python -m venv .venv
                    . .venv/bin/activate
                    pip install -r requriments.txt
                '''
            }
        }
        stage('Test') {
            steps {
                sh '''
                    . .venv/bin/activate
                    pytest
                '''
            }
        }
    }
}