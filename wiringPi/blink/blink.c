#include <wiringPi.h>
#include <stdio.h>

const int LED = 0;
const int CHANGE_DELAY = 500;

void setup()
{
	pinMode(LED, OUTPUT);
	digitalWrite(LED, 0);
}

int main(void)
{
	if(wiringPiSetup() == -1)
		return 1;
	
	while(1)
	{
		digitalWrite(LED, 1);
		delay(CHANGE_DELAY);

		digitalWrite(LED, 0);
		delay(CHANGE_DELAY);
	}
	return 0;
}
