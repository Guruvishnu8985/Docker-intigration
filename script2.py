import subprocess

subprocess.call("docker network create --drive bridge intelliqit",shell=True)
subprocess.call("docker run --name mydb -d -e MY_SQL_ROOT_PASSWORD=intelliqit --network intelliqit mysql:5",shell=True)
subprocess.call("docker run --name mywordpress -p 8888:80 -d --network intelliqit wordpress",shell=True)

