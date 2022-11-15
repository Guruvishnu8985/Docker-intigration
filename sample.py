import subprocess

i = 1

while i <= 10:
    subprocess.call("docker network create --driver bridge intelliqit%d"%i,shell=True)

    subprocess.call("docker run --name container%d -d -p --network intelliqit%d mysql"%(i,i),shell=True)
    i = i + 1

