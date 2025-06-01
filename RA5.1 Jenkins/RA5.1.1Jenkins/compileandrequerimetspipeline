pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/pps13030596/calculadora'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Compile') {
            steps {
                // Verifica que todos los archivos .py son válidos
                sh 'python -m py_compile $(find . -name "*.py")'
                
                // Verifica que todos los módulos se puedan importar
                sh 'flake8 . --max-line-length=120'
            }
        }
        stage('Unit Test') {
            steps {
                sh 'python -m unittest discover -s . -p "test_*.py"'
            }
        }
    }
}
