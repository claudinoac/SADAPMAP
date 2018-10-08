#include <Wire.h>
#include <ADS1115.h>
#include <ThermoCouple.h>
#include <string.h>


ADS1115 ads0(0x48);
ADS1115 ads1(0x49);

ThermoCouple term1;

int16_t adc0, adc1, adc2, adc3, adc4, adc5, adc6, adc7;
String interface;
int channelNr = 0;

void setup(void)
{
  Serial.begin(115200);
  //Serial.println("Hello!");

  //Serial.println("Getting single-ended readings from AIN0..3");
  //Serial.println("ADC Range: +/- 6.144V (1 bit = 3mV/ADS1015, 0.1875mV/ADS1115)");

  ads0.begin();
  ads1.begin();
  Serial.println("");
  while(!Serial.available());
  interface = Serial.readString();

  if(interface.startsWith("press"))
  {
    channelNr = 2;
  }
  else if(interface.startsWith("temp"))
  {
    channelNr = 3;
  }



}

void loop(void)
{
  adc0 = ads0.readADC_SingleEnded(0);
  adc1 = ads0.readADC_SingleEnded(1);
  if(channelNr == 3)
  {
    adc2 = ads0.readADC_SingleEnded(2);
  }
  /*adc3 = ads0.readADC_SingleEnded(3);
  adc4 = ads1.readADC_SingleEnded(0);
  adc5 = ads1.readADC_SingleEnded(1);
  adc6 = ads1.readADC_SingleEnded(2);
  adc7 = ads1.readADC_SingleEnded(3);*/
  Serial.print(adc0);
  Serial.print(" ");
  Serial.print(adc1);
  if(channelNr == 3)
  {
    Serial.print(" ");
    Serial.print(adc2);
  }
  /*Serial.print(" ");
  Serial.print(adc3);
  Serial.print(" ");
  Serial.print(adc4);
  Serial.print(" ");
  Serial.print(adc5);
  Serial.print(" ");
  Serial.print(adc6);
  Serial.print(" ");
  Serial.print(adc7);
  Serial.print(" ");
  Serial.print(millis());*/
  Serial.print("\n");
  while(millis()%100!=0);


}
