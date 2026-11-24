pipeline {
    agent any
    stages {
        stage('Setup') {
            steps {
                sh'''
                    python3 -m venv .venv
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
            post {
                always {
                    archiveArtifacts artifacts: 'htmlcov/**', allowEmptyArchive: true
                }
            }
        }
    }
}
