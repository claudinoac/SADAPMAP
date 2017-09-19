const int tensao = A0;

int sensorValue = 0;
void setup() 
{
  
  Serial.begin(9600);
}

void loop() 
{
  while(millis()%20!=0)
  {}
  sensorValue = analogRead(tensao);
  Serial.print("\nSensor_1 :");
  Serial.print(sensorValue);
  Serial.print(",");
  Serial.print(millis());
  delay(1);
}
