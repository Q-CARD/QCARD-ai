REPOSITORY=/home/ubuntu/qcard
cd $REPOSITORY

echo "> Docker compose down"

sudo docker rm -f $(sudo docker ps -aq)
sudo docker rmi -f $(sudo docker images -q)