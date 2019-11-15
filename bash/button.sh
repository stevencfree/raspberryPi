gpio -g mode 25

while true; do
if [ gpio]
sleep 2

gpio -g write 27 0
gpio -g write 22 1
sleep 1

gpio -g write 22 0
gpio -g write 17 1
sleep 3digitalWrite(LED, 0);
        if(debug)
            printf("LED off\n");
        delay(CHANGE_DELAy);
done