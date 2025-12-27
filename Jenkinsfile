pipeline {
    agent any

    options {
        timestamps()
        ansiColor('xterm')
    }

    environment {
        VENV_DIR = ".venv"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Python version') {
            steps {
                bat 'python --version'
            }
        }

        stage('Create venv') {
            steps {
                bat 'python -m venv %VENV_DIR%'
            }
        }

        stage('Install dependencies') {
            steps {
                bat '%VENV_DIR%\\Scripts\\python -m pip install --upgrade pip'
                bat '%VENV_DIR%\\Scripts\\python -m pip install -r requirements.txt'
            }
        }

        stage('Run tests (pytest)') {
            steps {
                bat '%VENV_DIR%\\Scripts\\python -m pytest -q'
            }
        }
    }

    post {
        always {
            echo 'Build finished.'
        }
        success {
            echo '✅ SUCCESS: Tests passed.'
        }
        failure {
            echo '❌ FAILURE: Tests failed. Check console output.'
        }
    }
}
