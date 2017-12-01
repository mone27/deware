
#include <SoftwareSerial.h>

SoftwareSerial CoSerial(12, 13);
void setup(){
    Serial.begin(9600);
    Serial.println("starting co2 sensor read");

    CoSerial.begin(9600);
    



}
void loop(){
    Serial.println("started reading");
    //CoSerial.print("H\r\n");
    delay(2000);
    Serial.write(CoSerial.read());
    

}
