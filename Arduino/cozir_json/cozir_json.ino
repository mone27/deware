#include "cozirsensor.h"
#include "SoftwareSerial.h"
#include "utils.h" //define endl '\n'
#include "ArduinoJson.h"
#include <Wire.h>
#include <TimeLib.h>
#include <DS1307RTC.h>


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
  tmElements_t tm;
  
  if(RTC.read(tm)){
    root["time"] = String(tm.Hour) + ':' + String(tm. Minute) + ':' + String(tm.Second)
                    + ' ' + String(tm.Day) + '/' +  String(tm.Month) 
                    + '/' + String(tmYearToCalendar(tm.Year));
  }
  else{
    Serial << F("error reading time");
  }
  
    root["temp"] = czrs.Temperature();
  root["hum"] = czrs.Humidity();
  root["co2"] = czrs.Co2();
  
  root.printTo(Serial);
 Serial << endl;
  delay(4000);

}
