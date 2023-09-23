REPOSITORY=/home/ubuntu/qcard
cd $REPOSITORY

echo "> Docker compose down"

sudo docker-compose down

sudo docker rm $(sudo docker ps -aq)
sudo docker rmi $(sudo docker images -q)