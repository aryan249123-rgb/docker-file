pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                bat '"C:\Users\Asus\AppData\Local\Microsoft\WindowsApps\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run Application') {
            steps {
                bat '"C:\Users\Asus\AppData\Local\Microsoft\WindowsApps\python.exe" app.py'
            }
        }
    }
}