REPOSITORY=/home/ubuntu/qcard
cd $REPOSITORY

echo "> Build Docker Image"
docker build -t qcard-ai .

echo "> Run Docker Container"
sudo docker run --name qcard-ai -p 80:80 qcard-ai
