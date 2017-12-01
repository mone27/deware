#include <cozir.h>
template<class T> inline Print &operator <<(Print &obj, T arg) {
  obj.print(arg);
  return obj;
}
#define endl  '\n'

// declariation for cozir sensor
#include <SoftwareSerial.h>
SoftwareSerial nss(10, 11);
czrlib czr = czrlib(nss);

//declaration for dht22 sensor
#include <dht.h>
dht DHT;
#define DHT22_PIN 5



void setup()
{
  Serial.begin(9600);
  Serial << F("starting..") << endl;
  delay(5000);
  Serial << F(".done") << endl;
  //czr.SetOperatingMode(CZR_POLLING);
  //czr.SetOperatingMode(CZR_STREAMING);
  //czr.CalibrateFreshAir();
  // czr.SetDigiFilter(64);
  czr.SetOperatingMode(CZR_COMMAND);
  //Serial << F("mult value: ") << czr.Request('.');
  czr.Command('.');
  Serial << F("read: ") << endl;
  czr.SetOperatingMode(CZR_POLLING);



}
//char * dirty_read() {
//  char buffer[30];
//  delay(2000);
//  Serial.readBytes(buffer, 30);
//  return buffer;
//}
////char * dirty_read_string() {
//  char buffer[30];
//  uint8_t idx = 0;
//  delay(250);
//  while (buffer[idx - 1] != 0x0A)
//  {
//    if (CZR_Serial.available())
//    {
//      buffer[idx] = CZR_Serial.read();
//      idx++;
//    }
//  }
//  buffer[idx] = '\0';
//  return buffer;
//}
void loop()
{
  delay(4000);
  Serial << F("reading :") <<  endl ;
  read_cozir();
  read_dht22();

}

void read_cozir() {
  float t = czr.Celsius();
  float h = czr.Humidity();
  int c = czr.CO2();
  int digi = czr.GetDigiFilter();

  Serial.print("Celcius : "); Serial.println(t);
  Serial.print("Humidity : "); Serial.println(h);
  Serial.print("CO2 : "); Serial.println(c);
  Serial.print("Digital Filter : "); Serial.println(digi);
  Serial.println("");
}

void read_dht22() {
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
}
