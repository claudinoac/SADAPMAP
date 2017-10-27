#include "HX711.h"
double a=0,b=0;
// HX711.DOUT	- pin #A1
// HX711.PD_SCK	- pin #A0

HX711 channelA(A1, A0,32);		//Instancia um objeto da classe HX711 vinculado ao canal A 
//HX711 channelB(A1, A0,128);    //Instancia um objeto da classe HX711 vinculado ao canal B
void setup() {
  Serial.begin(9600); //Inicia a Serial com taxa de tranferência de 115200 bps
  

  channelA.set_scale();       //Reseta a escala do canal A
  channelA.tare();				    //

  //channelB.set_scale();       //Reseta a escala do canal B
  //channelB.tare();
  
  //channelA.set_offset(0);
  //channelB.set_offset(0);
  Serial.print("Primeira Leitura do Canal A: \t\t");
  Serial.print(channelA.read());                 // Primeira leitura do canal A
  Serial.print("\n\n");

  /*Serial.print("Primeira Leitura do Canal B: \t\t");
  Serial.print(channelB.read());                 // Primeira leitura do canal B
  Serial.print("\n\n");*/
  
 /* Serial.print("Primeira média do canal A (20): \t\t");
  Serial.print(channelA.read_average(20));       // Imprime a média de 20 leituras do canal A
  Serial.print("\n\n");

  Serial.print("Primeira média do canal B (20): \t\t");
  Serial.print(channelB.read_average(20));       // Imprime a média de 20 leituras do canal B
  Serial.print("\n\n");*/
}

void loop() {
  //channelA.set_gain(128);
  //Serial.print("\nLeitura (Canal A):"); //Realiza uma leitura do canal A e imprime na serial
  a=channelA.read();
  Serial.println(a);
  while(!channelA.is_ready())
  {}
  /*if(a<b)
  {Serial.print("\n\n");
  Serial.print("ESSE:");
  Serial.print(b);
  Serial.print("\n\n");}*/
  
  //while(millis()%100!=0);
  //Serial.println(millis());
  
  /*Serial.print("   ");
  Serial.print(millis());
  Serial.println();*/
  //Serial.print("\n\n");
  
  /*channelA.set_gain(32);
  Serial.print("Leitura (Canal B):"); //Realiza uma leitura do canal B e imprime na serial
  Serial.print(channelA.read_average(5));*/
  
  /*Serial.print("\n\n");
  a=analogRead(A3);
  a=a*5/1023;
  Serial.println(a);
  Serial.println(channelA.get_scale());
  //Serial.println(channelB.get_scale());
  Serial.println(channelA.get_offset());
  //Serial.println(channelB.get_offset());*/
  /*channelA.power_down();
  delay(500);
  channelA.power_up();*/
}

