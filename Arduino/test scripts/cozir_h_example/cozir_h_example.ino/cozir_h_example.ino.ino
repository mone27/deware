#include <cozir.h>
template<class T> inline Print &operator <<(Print &obj, T arg) { obj.print(arg); return obj; }
#define endl '\n'
#include <SoftwareSerial.h>
SoftwareSerial nss(10, 11);
czrlib czr = czrlib(nss);

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
}

void loop()
{
 delay(4000);
 Serial << F("reading :") <<  endl ;
 float t = czr.Celsius();
// float f = czr.Fahrenheit();
 float h = czr.Humidity();
 int c = czr.CO2();
 int digi = czr.GetDigiFilter();

 Serial.print("Celcius : ");Serial.println(t);
// Serial.print("Fahrenheit : ");Serial.println(f);
 Serial.print("Humidity : ");Serial.println(h);
 Serial.print("CO2 : ");Serial.println(c);
 Serial.print("Digital Filter : ");Serial.println(digi);
 Serial.println("");
}
