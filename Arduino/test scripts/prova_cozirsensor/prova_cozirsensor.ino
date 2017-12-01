#include "cozirsensor.h"
#include "SoftwareSerial.h"
#include "utils.h"

SoftwareSerial css(10,11);
cozirsensor czrs;

void setup() {
 Serial.begin(9600);
 Serial.print("alive");
 
 czrs.init(&css);
 
 

}

void loop() {
  Serial << "temparature :" << czrs.Temperature() << endl;
  delay(2000);
  

}
