

#include <SPI.h>
#include "nRF24L01.h"
#include "RF24.h"
#include "printf.h"

RF24 radio(9,10);

//
// Topology
//

// Radio pipe addresses for the 2 nodes to communicate.
//const uint64_t pipes[2] = { 0xF0F0F0F0E1LL, 0xF0F0F0F0D2LL };
const uint64_t pipes[2] = {0xe2e2e2e2e2LL,0xc7c7c7c7c7LL};


void setup(void)
{
  Serial.begin(57600);
  printf_begin();
  

  //
  // Setup and configure rf radio
  //

  radio.begin();
  radio.enableDynamicPayloads();
  radio.setDataRate(RF24_1MBPS);
  radio.setRetries(15,15);
  radio.setChannel(70);
  radio.openReadingPipe(1,pipes[1]);
  radio.openWritingPipe(pipes[0]);

  //
  // Start listening
  //


  //radio.powerUp();
  radio.printDetails();
  radio.startListening();  
}
String a ="";

void loop(void){
  
  if (radio.available()){
    Serial.println("Incomming.");
    
  }
  delay(1000);
}
