pipeline {
    agent any

    stages {
        stage('Compile') {
            steps {
                bat 'javac Palindrome.java'
            }
        }

        stage('Run') {
            steps {
                bat 'java Palindrome'
            }
        }
    }
}