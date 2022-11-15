import subprocess

image=input("Enter the imahe to be delected:")
subprocess.call("docker rmi %s"%image,shell=True)
