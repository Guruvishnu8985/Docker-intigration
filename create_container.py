import subprocess


image = input("Enter the image name: ")
container = input("Enter the name of the container: ")
detach = input("Do you want to run in detached mode:y/n ")


if detach == 'y':
    subprocess.call("docker run --name %s -d -p %s"%(container,image),shell=True)
elif detach == 'n':
    subprocess.call("docker run --name %s -p %s"%(container,image),shell=True)
else:
    print("invalid option")

