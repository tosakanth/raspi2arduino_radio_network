#include <SPI.h>
#include "nRF24L01.h"
#include "RF24.h"
#include "printf.h"

/* Set up nRF24L01 radio on SPI bus plus pin 9 for CE and pin 10 for CSN */

RF24 radio(9,10);


/* Network topology is peer to peer between Arduino and Raspberry PI */
/* Radio pipe addresses for the 2 nodes to communicate. One for reading pipe and another for writing pipe.*/
const uint64_t pipes[2] = { 0xF0F0F0F0A1LL, 0xF0F0F0F0A2LL };



void setup(void){
  Serial.begin(57600);
  
  /*this is needed when you want Arduino to show all details.*/
  printf_begin();
  

  //
  // Setup and configure rf radio
  //

  radio.begin();
  
  /*This is not good idea but this is a demo.*/
  radio.enableDynamicPayloads();
  
  /*I found this data rate would works fine.*/
  radio.setDataRate(RF24_1MBPS);
  
  /*
  The first 15 is duration for each retry is equals to 15 x 250usec, 
  the secound is number of retries.
  */
  radio.setRetries(15,15);
  
  radio.setChannel(70);
  radio.openReadingPipe(1,pipes[0]);
  radio.openWritingPipe(pipes[1]);

  /*For this demo, Arduino takes default role as listener.*/
  radio.startListening();  
  
  /*To show up details*/
  radio.printDetails();
}


void loop(void){
  
  if (radio.available()){
    bool done=false;
    char msg_buf[20];
    while (!done){
      done=radio.read(msg_buf,sizeof(msg_buf));
    }
    String pi_msg = String(msg_buf);
    Serial.println(pi_msg);
    sendReply()
  }
  delay(100);
}

void sendReply(){
  char msg[20]="I am arduino";
  radio.stopListening();
  bool ok = radio.write(&msg,sizeof(msg));
  radio.startListening();  

}
