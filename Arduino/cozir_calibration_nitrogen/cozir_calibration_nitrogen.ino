#include "cozirsensor.h"
#include "SoftwareSerial.h"
#include "utils.h" //define endl '\n'
#include "ArduinoJson.h"
SoftwareSerial css(10,11);
cozirsensor czrs;
SoftwareSerial * serialPort;
const size_t bufferSize = JSON_OBJECT_SIZE(4);
  

void setup() {
  long ppm;
  int count = 0;
  Serial.begin(9600);
  Serial.println("alive");
  czrs.init(&css);
  Serial << F("starting calibration program") << endl;
  loop(); loop(); loop();
  Serial << F("insert current co2 value in ppm :");
  while(Serial.available() == 0){
    if(count == 30){
      Serial << '.';
      count = 0;
      }
      count ++;
      delay(100);
    }
  //ppm = Serial.parseInt();
  //Serial << endl << F("inserted value is") << ppm << endl;
  //czrs.calibrate((uint16_t)ppm);
  czrs.calibrateNitrogen();
  delay(2000);
 
}

void loop() {
  
  
   

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


