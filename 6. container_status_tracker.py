import docker  # Import the docker library to interact with Docker

# Create a Docker client using environment variables
client = docker.from_env()

# Iterate over all containers (including stopped ones)
for container in client.containers.list(all=True):
    # Print the container's name and current status
    print(f"{container.name}: {container.status}")
    # Check if the container is running
    if container.status == 'running':
        # Get the container's IP address from its attributes
        ip_address = container.attrs['NetworkSettings']['IPAddress']
        print(f"Container {container.name} is running with IP address: {ip_address}")
    else:
        # Inform if the container is not running
        print(f"Container {container.name} is not running.")