#include <wiringPi.h>
#include <stdio.h>

const int button = 6;

void setup()
{
	pinMode(button, INPUT);
}

int main(void)
{
	if(wiringPiSetup() == -1)
		return 1;
	
	while(1)
	{
		if (digitalRead(button))
            printf("button pressed");

		else
            printf("button not pressed");

		delay(100);
	}
	return 0;
}
