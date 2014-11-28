#include <DHT.h>


#include <SPI.h>
#include "nRF24L01.h"
#include "RF24.h"
#include "stdlib.h"

#define DHTPIN 7
#define DHTTYPE DHT22


DHT dht(DHTPIN, DHTTYPE);

RF24 radio(9,10);
char humid[5];
char temp[5];

void setup() {

Serial.begin(9600);
dht.begin();
setupRadio();
delay(2000);
}

void loop() {
  dtostrf(dht.readHumidity(),3,2,humid);
  dtostrf(dht.readTemperature(),3,2,temp);
  sendData();
  
  /*because DHT sensor is slow.*/
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
  radio.openWritingPipe(0xF0F0F0F0C5LL);
  radio.powerUp();
  radio.printDetails();
  
}
void sendData(){
  char data[20];
  
  int i=0;
  for(i=0;i<5;i++)
     data[i+5]=humid[i];
  for(int j=0;j<5;j++)
     data[j+10]=temp[j];

  data[0]='0';
  data[1]='0';
  data[2]='0';
  data[3]='0';
  data[4]='2'; 
  
  /*stop then start is required*/
  radio.stopListening();
  bool ok = radio.write(&data,15);
  radio.startListening();  

}
