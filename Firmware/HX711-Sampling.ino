#include "HX711.h"

// HX711.DOUT	- pin #A1
// HX711.PD_SCK	- pin #A0

HX711 channelA(A1, A0,32);		//Instancia um objeto da classe HX711 vinculado ao canal A 
HX711 channelB(A1, A0,128);    		//Instancia um objeto da classe HX711 vinculado ao canal B
void setup() {
  Serial.begin(115200); //Inicia a Serial com taxa de tranferência de 115200 bps


  channelA.set_scale();       //Reseta a escala do canal A
  channelA.tare();				    //

  channelB.set_scale();       //Reseta a escala do canal B
  channelB.tare();

  Serial.print("Primeira Leitura do Canal A: \t\t");
  Serial.print(channelA.read());                 // Primeira leitura do canal A
  Serial.print("\n\n");

  Serial.print("Primeira Leitura do Canal B: \t\t");
  Serial.print(channelB.read());                 // Primeira leitura do canal B
  Serial.print("\n\n");
  
  Serial.print("Primeira média do canal A (20): \t\t");
  Serial.print(channelA.read_average(20));       // Imprime a média de 20 leituras do canal A
  Serial.print("\n\n");

  Serial.print("Primeira média do canal B (20): \t\t");
  Serial.print(channelB.read_average(20));       // Imprime a média de 20 leituras do canal B
  Serial.print("\n\n");
}

void loop() {
  Serial.print("Leitura (Canal A):"); //Realiza uma leitura do canal A e imprime na serial
  Serial.print(channelA.read());
  Serial.print("\n\n");
  delay(200);
  Serial.print("Leitura (Canal B):"); //Realiza uma leitura do canal B e imprime na serial
  Serial.print(channelB.read());
  Serial.print("\n\n");
 
  delay(500);
}
