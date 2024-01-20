// Face Tracker using OpenCV and Arduino
// by Palak Totala - 2001CS84

#include<Servo.h>

Servo x, y;
int width = 640, height = 480;  // total resolution of the video
int xpos = 90, ypos = 90;  // initial positions of both Servos
void setup() {

  Serial.begin(9600);
  x.attach(9); // servo x is attached to digital pin 9
  y.attach(10); // servo y is attached to digital pin 10
  x.write(xpos); // sets the angle of the shaft of servo x (90 degrees), moving the shaft to that orientation.
  y.write(ypos); // sets the angle of the shaft of servo y (90 degrees), moving the shaft to that orientation.
}
const int angle = 2;   // degree of increment or decrement

void loop() // loop function that executes repeatedly
{
  if (Serial.available() > 0) // It will only send data when the received data is greater than 0.
  {
    int x_mid, y_mid; // initialising variables to store center coordinates
    if (Serial.read() == 'X') // reads out the first available byte from the serial receive buffer. After it reads it out, it removes that byte from the buffer.
    {
      x_mid = Serial.parseInt();  // read center x-coordinate (scans down the serial receive buffer one byte at a time in search of the first valid numerical digit)
      if (Serial.read() == 'Y')
        y_mid = Serial.parseInt(); // read center y-coordinate
    }
    
    // adjust the servo within the squared region if the coordinates is outside it
    
    if (x_mid > width / 2 + 30)
      xpos += angle;
    if (x_mid < width / 2 - 30)
      xpos -= angle;
    if (y_mid < height / 2 + 30)
      ypos -= angle;
    if (y_mid > height / 2 - 30)
      ypos += angle;


    // if the servo degree is outside its range
    
    if (xpos >= 180)
      xpos = 180;
    else if (xpos <= 0)
      xpos = 0;
    if (ypos >= 180)
      ypos = 180;
    else if (ypos <= 0)
      ypos = 0;

    x.write(xpos);
    y.write(ypos);
  }
}
