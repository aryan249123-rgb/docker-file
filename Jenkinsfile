pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\Aryan\\AppData\\Local\\Programs\\Python\\Python39\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run Application') {
            steps {
                bat '"C:\\Users\\Aryan\\AppData\\Local\\Programs\\Python\\Python39\\python.exe" app.py'
            }
        }
    }
}