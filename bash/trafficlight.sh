gpio -g mode 17 out #green
gpio -g mode 27 out #yellow
gpio -g mode 22 out #red

while true; do
gpio -g write 22 0
gpio -g write 17 1
sleep 2

gpio -g write 17 0
gpio -g write 27 1
sleep 1

gpio -g write 27 0
gpio -g write 22 1
sleep 3
done