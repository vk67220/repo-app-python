pipeline {
    agent any

    environment {
        IMAGE_NAME = 'kastrov/kastro-exam-app'
        IMAGE_TAG = "v${BUILD_NUMBER}"
        EKS_CLUSTER_NAME = 'your-eks-cluster-name'
        AWS_REGION = 'your-region'
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/yourusername/Kastro-Exam-App.git'
            }
        }

        stage('Docker Build & Tag') {
            steps {
                dir('backend') {
                    script {
                        sh "docker build -t $IMAGE_NAME:$IMAGE_TAG ."
                    }
                }
            }
        }

        stage('Docker Push') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                        sh """
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push $IMAGE_NAME:$IMAGE_TAG
                        """
                    }
                }
            }
        }

        stage('Update K8s Deployment') {
            steps {
                script {
                    sh """
                    aws eks update-kubeconfig --name $EKS_CLUSTER_NAME --region $AWS_REGION
                    kubectl config set-context --current --namespace=devopsapp

                    kubectl set image deployment/kastro-exam-deployment kastro-exam-container=$IMAGE_NAME:$IMAGE_TAG
                    kubectl rollout restart deployment/kastro-exam-deployment
                    """
                }
            }
        }
    }

    post {
        success {
            echo "🎉 Build and deploy successful!"
        }
        failure {
            echo "❌ Build or deploy failed!"
        }
    }
}
