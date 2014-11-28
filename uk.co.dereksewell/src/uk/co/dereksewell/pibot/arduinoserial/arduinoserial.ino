// Serial Read - Read commands and inputs from serial window
// Developed by: Mushfiq Sarker ( http://inventige.com )
 
/* How to use:
*  Send commands such as: 'a 10 1000' 
*  The code will strip out command a and then individually the numbers.
*  Can be used to do a menu type system.
*/
 
/* To do:
*  Cannot handle negative numbers.
*  Cannot handle decimal (floating point) values.
*/
 
#include <AFMotor.h>


/************************* Private Variables*****************/
unsigned long loopTime, currentTime;
const int serStrLen = 30;
char serInStr[ serStrLen ];  // array that will hold the serial input string
AF_DCMotor motor1(1, MOTOR12_64KHZ);
AF_DCMotor motor2(2, MOTOR12_64KHZ);
/*************************************************************/
 
 
 
/************* Setup *******************************/
void setup() {
  Serial.begin(115200);
   
  Serial.flush();
  Serial.println("Command example:  a <input1> <input2>");
   
} 
/***************************************************/
 
 
/************* Main Arduino Loop *******************************/
void loop(){ 
 
  if( readSerialString() ) {
     
    unsigned long input1, input2;
     
    Serial.println(serInStr);  // Print the command for user to see.
    char cmd = serInStr[0];    // First character is the command
    char* str = serInStr;      // Save the remaining string for inputs.
     
    while( *++str == ' ' );    // After command, remove all spaces 
    input1 = atoi(str); // Next command is input1, capture and save it.
    while( *++str == ' ' );    // After input1, remove all spaces 
    input2 = atoi(str);  // Next command is input2, capture and save it.
 
    delay(30);                 // Delay to settle the UART buffer.
     
    /* input1, input2 CONTAIN the input numbers to be used throughout program.*/
    
    /*** Act on what was given *******/
    if(input1 == 1)
    {
        motor1.setSpeed(input2);
        Serial.println("Set motor 1 speed to: ");
        Serial.println(input2);
        
        if(cmd == 'f') {
           motor1.run(FORWARD);
           Serial.println("Running motor 1 forwards");  
        }
        
        if(cmd == 'b') {
           motor1.run(BACKWARD);
           Serial.println("Running motor 1 backwards");  
        }
        
        if(cmd == 'r') {
           motor1.run(RELEASE);
           Serial.println("Running motor 1 release");  
        }
        
    }
    
    if(input1 == 2)
    {
        motor2.setSpeed(input2);
        Serial.println("Set motor 2 speed to: ");
        Serial.println(input2);
        
        if(cmd == 'f') {
           motor2.run(FORWARD);
           Serial.println("Running motor 2 forwards");  
        }
        
        if(cmd == 'b') {
           motor2.run(BACKWARD);
           Serial.println("Running motor 2 backwards");  
        }
        
        if(cmd == 'r') {
           motor2.run(RELEASE);
           Serial.println("Running motor 2 release");  
        }
        
    }

  } 
 
}
/*********************************************************************/
 
 
/************* EXTRA FUNCTIOONs **************************************/
 
uint8_t readSerialString()
{
  if(!Serial.available()) {
    return 0;
  }
  delay(10);  // wait a little for serial data
 
  memset( serInStr, 0, sizeof(serInStr) ); // set it all to zero
  int i = 0;
  while(Serial.available() && i<serStrLen ) {
    serInStr[i] = Serial.read();   // FIXME: doesn't check buffer overrun
    i++;
  }
  return i;  // return number of chars read
}
 
/*******************************************************************************/
