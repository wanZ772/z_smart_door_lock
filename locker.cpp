#include <Servo.h>
int target_pin = 13;
int pos = 0;
int limit = 10;
int way = 1;
Servo my_servo;
void setup()
  {
     Serial.begin(9600);
     my_servo.attach(target_pin);
     //my_servo.write(0);
      
  }
 void loop()
  {
      String command = Serial.readStringUntil('\n');
      if (command == "open")
        {
          close_door();
          command = "";
          }
       if (command == "close")
        {
          open_door();
          command = "";
          }
    }
 void open_door()
  {
    
      for (int i = 0; i < 2; i = i + 1)
        {
          my_servo.write(0);
          delay(180);
          }
      my_servo.write(90);
    }
 void close_door()
  {
    
      for (int i = 0; i < 2; i = i + 1)
        {
          my_servo.write(180);
          delay(180);
          }
      my_servo.write(90);
    }