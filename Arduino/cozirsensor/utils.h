#ifndef UTILS_H
#define UTILS_H
#define endl '\n' //def new line charater to be used with stram operator

template<class T> inline Print &operator <<(Print &obj, T arg) { obj.print(arg); return obj; }
// stream operator to replace Serial.print

/*
void serialFlush(){  //for clearing Serial rx buffer
  while(serial.available() > 0) {
    char t = Serial.read();
  }
}   
*/
#endif
