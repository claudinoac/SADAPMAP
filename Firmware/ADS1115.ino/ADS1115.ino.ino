#include <Wire.h>
#include <Adafruit_ADS1015.h>

Adafruit_ADS1115 ads;  
int16_t adc0, adc1, adc2, adc3;
  float val0;
void setup(void) 
{
  Serial.begin(115200);
  //Serial.println("Hello!");
  
  //Serial.println("Getting single-ended readings from AIN0..3");
  //Serial.println("ADC Range: +/- 6.144V (1 bit = 3mV/ADS1015, 0.1875mV/ADS1115)");
  
  ads.setGain(GAIN_TWOTHIRDS);        // ganho 1x   +/- 4.096V  1 bit = 2mV      0.125mV
  ads.begin();
}

void loop(void) 
{
  adc0 = ads.readADC_SingleEnded(0);
  adc1 = ads.readADC_SingleEnded(1);
  adc2 = ads.readADC_SingleEnded(2);
  adc3 = ads.readADC_SingleEnded(3);;
  Serial.print(adc0);
  Serial.print(" ");
  Serial.print(adc1);
  Serial.print(" ");
  Serial.print(adc2);
  Serial.print(" ");
  Serial.print(adc3);
  Serial.print("\n");
  while(millis()%20!=0)
  {}
  
}
