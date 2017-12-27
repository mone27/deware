#include "cozirsensor.h"
#include "Arduino.h"

cozirsensor::cozirsensor()
     //ssc software serial connection
{
    /*
    serialPort->begin(9600);
    co2multiplier = userco2multiplier;
    delay(1000);
    serialPort.print("K 2\r\n"); // set polling mode
    Serial << F("finish inizialize") << endl;
*/
}
void cozirsensor::init(SoftwareSerial * css)
      //ssc software serial connection
{
    serialPort = css;
    //Serial << F("serialPort = css ")<<endl;
    serialPort->begin(9600);
    //Serial << F("serialPort->begin(9600);")<< endl;
    //Temperature(); Temperature(); // fake reading to clear error to be fixed!!!
    serialPort->flush();
    while(serialPort->available() > 0) //clears serial port buffer
    {
        char t = serialPort->read();
    }

    //Serial << ("multiplier :") << getco2multiplier() << endl;
    //co2multiplier = getco2multiplier();
    co2multiplier = getco2multiplier();
    //Serial << F("co2multiplier = 5;") << endl;
    delay(10000);
    serialPort->print("K 2\r\n"); // set polling mode
    Serial << F("finish inizialize") << endl;

}
uint32_t cozirsensor::Request(char command)
{
    char buffer[26];
   //Serial << F("command receiveid :") << command<< endl;

    while(serialPort->available() > 0) //clears serial port buffer
    {
        char t = serialPort->read();
    }

    //serialPort.print(command);
    serialPort->print(command);
    serialPort->print("\r\n");
    //Serial << F("sent command: ") << command  ;
    //Serial.print("\r\n");
    //Serial << endl;

    delay(120); // needed if sensor is reading value so does non respond
    uint8_t i = 0;
    while ( serialPort->available() && i < 25) // 25 is size of buffer needed to avoid overflow
    {
        buffer[i] = serialPort->read();
        if (buffer[i] == '\n') break;
        i ++;

    }

    buffer[i] = '\0';
    //Serial << F("buffer : " )<< buffer << "|" << endl;
    uint32_t value = atoi(&buffer[3]);
    return value;
}
float cozirsensor::Temperature()
{
    return (float)(Request('T') - 1000)/10;//to convert to celisus degree see datasheet
}
float cozirsensor::Humidity()
{
    return (float) Request('H')/10;//do get %RH
}
uint32_t cozirsensor::Co2()
{
    return Request('Z')*co2multiplier;
}
uint32_t cozirsensor::getco2multiplier() // should be renamed
{

    serialPort->print(".\r\n");
    char buffer[26];
    delay(100); // needed if sensor is reading value so does non respond
    uint8_t i = 0;
    while ( serialPort->available() && i < 25) // 25 is size of buffer needed to avoid overflow
    {
        buffer[i] = serialPort->read();
        if (buffer[i] == '\n') break;
        i ++;

    }

    buffer[i] = '\0';
    //Serial << F("buffer of multilplier : " )<< buffer << "|" << endl;
    return atoi(&buffer[3]);



}
void cozirsensor::calibrateFreshAir()
{
    serialPort->print("G\r\n");
    delay(1000);
    Serial << F("calibrated");

}
void cozirsensor::calibrate(uint16_t ppm)
{
    serialPort->print("X ");
    serialPort->print(ppm/10);
    serialPort->print("\r\n");
    char buffer[26];
    delay(120); // needed if sensor is reading value so does non respond
    uint8_t i = 0;
    while ( serialPort->available() && i < 25) // 25 is size of buffer needed to avoid overflow
    {
        buffer[i] = serialPort->read();
        if (buffer[i] == '\n') break;
        i ++;

    }

    buffer[i] = '\0';
    Serial << F("value returned after calibration : " )<< buffer << endl;

}
void cozirsensor::calibrateNitrogen(){
  serialPort->print("U\r\n");
  char buffer[26];
  while(serialPort->available() > 0) //clears serial port buffer
  {
      char t = serialPort->read();
  }
  delay(120); // needed if sensor is reading value so does non respond
  uint8_t i = 0;
  while ( serialPort->available() && i < 25) // 25 is size of buffer needed to avoid overflow
  {
      buffer[i] = serialPort->read();
      if (buffer[i] == '\n') break;
      i ++;

  }

  buffer[i] = '\0';
  Serial << F("value returned after calibration : " )<< buffer << "|" << endl;


}
