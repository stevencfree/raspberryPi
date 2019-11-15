gpio -g mode 17 out

while true; do
gpio -g write 17 1 #turn light on
sleep 1            #adjust this number to change how quickly the light blinks

gpio -g write 17 0 #turn light off
sleep 1

done