#ifndef COZIRSENSOR_H
#define COZIRSENSOR_H
#include "SoftwareSerial.h"
#include "utils.h"
#include "Arduino.h"

class cozirsensor
{
public:
    cozirsensor();
    float Temperature();
    float Humidity();
    void init(SoftwareSerial * css );
    uint32_t Co2();
    uint32_t getco2multiplier();
    void calibrateFreshAir();
    void calibrate(uint16_t ppm);
    void calibrateNitrogen();

private:
    SoftwareSerial * serialPort;
    uint8_t co2multiplier;
    uint32_t Request(char);
};

#endif // COZIRSENSOR_H
