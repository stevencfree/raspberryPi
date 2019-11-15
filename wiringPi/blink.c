#include <wiringPi.h>
#include <stdio.h>

const int LED = 9;
const int CHANGE_DELAY = 500;
const int debug = 1;

void setup()
{
    pinMode(LED, OUTPUT);
    digitalWrite(LED, 0);
}

int main(void)
{
    if(wiringPiSetup() == -1)
        return 1;

    printf("Begin blinky program:\n");

    while(1)
    {
        digitalWrite(LED, 1);
        if(debug) 
            printf("LED on\n");
        delay(CHANGE_DELAY);
        digitalWrite(LED, 0);
        if(debug)
            printf("LED off\n");
        delay(CHANGE_DELAy);
    }
    return 0;
}