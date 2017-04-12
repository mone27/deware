/* file dht22.ino
 *  from DHTstalble lib
 *  author Simone Massaro
 *  date: 12/4/17
 *  reds data from dht22 adn send it over serial port
 */

#include <dht.h>

dht DHT;

#define DHT22_PIN 5

void setup()
{
    Serial.begin(9600);
}

void loop()
{
    // READ DATA
    int chk = DHT.read22(DHT22_PIN);
    //check for error or send ok
    switch (chk)
    {
     case DHTLIB_OK:
        Serial.print("OK,");
        break;
    case DHTLIB_ERROR_CHECKSUM:
        Serial.print("ERR, Checksum error,\t");
        break;
    case DHTLIB_ERROR_TIMEOUT:
        
        Serial.print("ERR, Time out error,\t");
        break;
    default:
        
        Serial.print("ERR, Unknown error,\t");
        break;
    }
    
    // DISPLAY DATA
    Serial.print(DHT.humidity, 1);
    Serial.print(",");
    Serial.print(DHT.temperature, 1);
    Serial.print(",");
    Serial.println();

    delay(2000);
}
//
// END OF FILE
//
