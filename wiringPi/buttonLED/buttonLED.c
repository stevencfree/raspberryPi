#include <wiringPi.h>
#include <stdio.h>

const int LED = 0;
const int button = 6;

void setup()
{
	pinMode(LED, OUTPUT);
	digitalWrite(LED, 0);
    pinMode(button, INPUT);
}

int main(void)
{
	if(wiringPiSetup() == -1)
		return 1;
	
    bool toggle = false;

	while(1)
	{
        digitalWrite(LED, toggle);

		if (digitalRead(button))
            toggle = !toggle;
            while(digitalRead(button))

	}
	return 0;
}
