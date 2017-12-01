#include "cozirsensor.h"
#include "SoftwareSerial.h"
#include "utils.h"

SoftwareSerial css(10,11);
cozirsensor czrs;
SoftwareSerial * serialPort;

void setup() {
 Serial.begin(9600);
 Serial.println("alive");
// serialPort = &css;
// serialPort->begin(9600);
// delay(10000);
// serialPort->print("K 1\r\n"); // streaming mode
 czrs.init(&css);
 
 

}

void loop() {
  Serial << "temparature :" << czrs.Temperature() << endl;
  Serial << "humidity :" << czrs.Humidity() << endl;
  Serial << "co2 :" << czrs.Co2() << endl;
  //Serial << "mult:" <<czrs.getco2multiplier() << endl;
  //czrs.calibrateFreshAir();
  delay(4000);
//  char buffer[26];
//  uint8_t i = 0;
//  
//    
//    while ( serialPort->available() && i < 25) // for cicle to avoid buffer overflow (size is 25)
//    {
//        buffer[i] = serialPort->read();
//        if (buffer[i] == '\n') break;
//        i ++;
//
//    }
//    while(serialPort->available() > 0) //clears serial port buffer
//    {
//        char t = serialPort->read();
//    }
//
//    buffer[i] = '\0';
//    Serial << F("buffer: " )<< buffer << "|" << endl;

}
