#include "cozirsensor.h"
#include "SoftwareSerial.h"
#include "utils.h" //define endl '\n'
#include "ArduinoJson.h"
#define tab   << '\t'
SoftwareSerial css(10,11);
cozirsensor czrs;
SoftwareSerial * serialPort;
const size_t bufferSize = JSON_OBJECT_SIZE(4);
  

void setup() {
 Serial.begin(9600);
 Serial.println("alive");
 czrs.init(&css);
 
 

}

void loop() {
  // this code prints data in json format
  // thi hand made system is not a wise idea it should be used a library such as arduino-json
  /*Serial  << endl
  << "temp "  << czrs.Temperature() << ',' << endl 
   tab << "hum " << czrs.Humidity() << ',' << endl
   tab << "co2 " << czrs.Co2() <<  ',' << endl
    << endl ;*/
   

  StaticJsonBuffer<83> jsonBuffer;
  JsonObject& root = jsonBuffer.createObject();
  root["time"] = 1351824120;
  root["temp"] = czrs.Temperature();
  root["hum"] = czrs.Humidity();
  root["co2"] = czrs.Co2();
  
  root.printTo(Serial);
 Serial << endl;
  delay(4000);

}
