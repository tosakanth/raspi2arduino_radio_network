
#include <SPI.h>
#include "nRF24L01.h"
#include "RF24.h"
#include "stdlib.h"

RF24 radio(9,10);
char soil_moisture[4];


void setup() {
Serial.begin(9600);
setupRadio();
delay(2000);/*option*/
}


void loop() {
// read the input on analog pin A1:
/*
absolute dry 1023
dry soil : 750 - 900
is ok : 550 - 750
very moist soil :350 - 550
in water : less than 350
*/
int moisture=analogRead(A1);
dtostrf(sm,4,0,soil_moisture);
sendData();
delay(2000);
}

void setupRadio(){
  radio.begin();
  radio.setPayloadSize(20);
  radio.setDataRate(RF24_1MBPS);
  radio.setRetries(15,15);
  radio.setChannel(0x5a);/*channel=90*/
  radio.setAutoAck(1);
  radio.disableCRC();

  radio.openWritingPipe(0xF0F0F0F0C3LL);

  radio.powerUp();
  radio.printDetails();
  
}
void sendData(){
  char data[10];
  data[0]='0';
  data[1]='0';
  data[2]='0';
  data[3]='0';
  data[4]='1'; 
  for(int i=0;i<4;i++)
     data[i+5]=soil_moisture[i];
  radio.stopListening();
  bool ok = radio.write(&data,10);
  radio.startListening();  

}
