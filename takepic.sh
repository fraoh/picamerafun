DATE=$(date +"%Y-%m-%d_%H%M")

raspistill -vf -hf -rot 90 -o /home/pi/camera/$DATE.jpg
