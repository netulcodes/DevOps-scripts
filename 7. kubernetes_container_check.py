from kubernetes import client, config  # Import Kubernetes client and config modules

# Load local kubeconfig (works with minikube)
config.load_kube_config()

# Create a CoreV1Api instance to interact with the Kubernetes API
v1 = client.CoreV1Api()
# List all pods in all namespaces
pods = v1.list_pod_for_all_namespaces(watch=False)

# Iterate through each pod
for pod in pods.items:
    # Print the namespace and pod name
    print(f"Namespace: {pod.metadata.namespace}, Pod: {pod.metadata.name}")
    # Iterate through the status of each container in the pod
    for container_status in pod.status.container_statuses or []:
        # Print the container name and its state
        print(f"  Container: {container_status.name}, State: {container_status.state}")
        # Check if the container is running
        if container_status.state.running:
            print(f"    Container {container_status.name} is running.")
        else:
            print(f"    Container {container_status.name} is not running.")