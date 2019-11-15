#include <wiringPi.h>
#include <stdio.h>

const int green = 27;
const int yellow = 22;
const int red = 17; 

void setup()
{
    pinMode(green, OUTPUT);
    pinMode(yellow, OUTPUT);
    pinMode(red, OUTPUT);
    digitalWrite(green, 0);
    digitalWrite(yellow, 0);
    digitalWrite(red, 0);
}

int main(void)
{
    if(wiringPiSetup() == -1)
        return 1;

    while(1)
    {
        digitalWrite(red, 0);
        digitalWrite(green, 1);
        delay(2000);

        digitalWrite(green, 0);
        digitalWrite(yellow, 1);
        delay(1000);

        digitalWrite(yellow, 0);
        digitalWrite(red, 1);
        delay(3000);

    }
    return 0;
}