#include <SoftwareSerial.h>
SoftwareSerial css(10,11);
void setup() {
  Serial.begin(9600);
  css.begin(9600);
  Serial.println("starting..");
  Serial.

}

void loop() {
  if( Serial.available()>0) {
    css.print(Serial.read());
    Serial.println("written");
  }
  if( css.available()>0){
    Serial.print(css.read());
    Serial.println("read");
  }

}
