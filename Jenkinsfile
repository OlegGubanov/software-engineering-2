pipeline {
    agent any
    
    stages {
        stage('checkout') {
            steps {
                git url: 'https://github.com/OlegGubanov/software-engineering-2', branch: 'main' 
            }
        }
        
        stage('dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        
        stage('test') {
            steps {
                sh 'pip install pytest'
                sh 'python3 -m pytest'
            }
        }
    }
}
