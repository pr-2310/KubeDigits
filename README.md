# DigitDraw Application in Kubernetes

## Project Overview

DigitDraw is a cloud-based web application that recognizes hand-drawn digits in real-time using a machine learning model. The application is containerized using Docker and deployed on Google Cloud Platform (GCP) using Kubernetes, with persistent storage for managing the trained model.

## Prerequisites

To run this project, ensure you have the following installed:

- **Docker**: For containerization.
- **kubectl**: For interacting with Kubernetes clusters.
- **Google Cloud SDK**: For managing GCP resources.
- **Kubernetes Cluster**: Set up on Google Cloud Platform (GCP).

## Repository Structure

- **Dockerfile.app**: Dockerfile for the web application.
- **app.py**: Flask web application for serving digit recognition.
- **deployment.yaml**: Kubernetes deployment configuration for the web application.
- **dockerfile**: Dockerfile for training the machine learning model.
- **index.html**: Frontend interface for drawing digits.
- **pvc.yaml**: Configuration for Persistent Volume Claim in Kubernetes.
- **requirements.txt**: Python dependencies for the project.
- **service.yaml**: Kubernetes service configuration to expose the web application.
- **train.py**: Python script to train the machine learning model.
- **train.yaml**: Kubernetes job configuration to run the training script.

## Setup and Deployment Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/pr-2310/KubeDigits.git
cd digitdraw
```

### 2. Set Up Kubernetes Cluster on GCP

1. Go to the Kubernetes section in GCP and create a Kubernetes Auto-Pilot Cluster.
2. Connect to the cluster using the GCP Cloud Shell.

### 3. Set Up Persistent Volume Claim (PVC)

1. Apply the PVC configuration stored in `pvc.yaml`:

    ```bash
    kubectl apply -f pvc.yaml
    ```

### 4. Build and Push Docker Images

#### For Training the Model:

1. Navigate to the project directory and build the Docker image:

    ```bash
    docker build -t <training-image-name> -f dockerfile .
    ```

2. Push the Docker image to Docker Hub:

    ```bash
    docker push <training-image-name>
    ```

#### For the Web Application:

1. Build the Docker image:

    ```bash
    docker build -t <app-image-name> -f Dockerfile.app .
    ```

2. Push the Docker image to Docker Hub:

    ```bash
    docker push <app-image-name>
    ```

### 5. Run the Training Job

Apply the Kubernetes job configuration stored in `train.yaml` to start the training process:

```bash
kubectl apply -f train.yaml
```

### 6. Deploy the Web Application

Deploy the web application using the deployment configuration stored in `deployment.yaml`:

```bash
kubectl apply -f deployment.yaml
```

### 7. Expose the Web Application

Expose the web application externally using the service configuration stored in `service.yaml`:

```bash
kubectl apply -f service.yaml
```

### 8. Access the Application

1. Obtain the external IP address of the web application:

    ```bash
    kubectl get services
    ```

2. Open a web browser and navigate to `http://<external-ip>`.

### 9. Testing the Application

- Draw a digit on the canvas using your mouse or trackpad.
- Click the "Predict" button to see the model’s prediction.
- Use the "Clear" button to reset the canvas for drawing a new digit.

## Future Enhancements

- Implement user authentication and authorization.
- Add support for multiple languages and character sets.
- Improve the user interface and experience.
- Explore advanced machine learning techniques for enhanced accuracy.
