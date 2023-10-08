#include <Servo.h>
//********************************************************
/*
 * Configure Pins Here 
 */
#define IN1 10
#define IN2 7
#define IN3 8
#define IN4 9
#define EN1 5
#define EN2 6
#define Gpin 3
//**********************************************************
char message ;
unsigned int Speed = 0   ;
char direction ;
Servo myservo;
//***********************************************************
void setup() {
  Serial.begin(9600) ;
  pinMode(EN1,OUTPUT);
  pinMode(EN2,OUTPUT);
  pinMode(IN1,OUTPUT);
  pinMode(IN2,OUTPUT);
  pinMode(IN3,OUTPUT);
  pinMode(IN4,OUTPUT);
  digitalWrite(EN1,LOW);
  digitalWrite(EN2,LOW);
  digitalWrite(IN1,LOW);
  digitalWrite(IN2,LOW);
  digitalWrite(IN3,LOW);
  digitalWrite(IN4,LOW);
  myservo.attach(Gpin); 
}

void loop() {
//Get the Recieved message 
message = u8GetMessage()  ; 
// update Speed 
  analogWrite(EN1,Speed) ;
  analogWrite(EN2,Speed) ;

  if (message == 'F') {
  digitalWrite(IN1,LOW);
  digitalWrite(IN2,HIGH);
  digitalWrite(IN3,HIGH);
  digitalWrite(IN4,LOW);
  }
 else if (message == 'B') {
  digitalWrite(IN1,HIGH);
  digitalWrite(IN2,LOW);
  digitalWrite(IN3,LOW);
  digitalWrite(IN4,HIGH);
  
 }
  else if (message == 'R') {
  digitalWrite(IN1,LOW);
  digitalWrite(IN2,HIGH);
  digitalWrite(IN3,LOW);
  digitalWrite(IN4,LOW);
  }
  else if (message == 'L') {
  digitalWrite(IN1,LOW);
  digitalWrite(IN2,LOW);
  digitalWrite(IN3,LOW);
  digitalWrite(IN4,HIGH);
  }
  else if (message == 'O')
  {
   myservo.write(55) ;
  }
  else if (message =='C')
  {
   myservo.write(135) ;
  }
  else if  (message == 'S') {
  digitalWrite(IN1,LOW);
  digitalWrite(IN2,LOW);
  digitalWrite(IN3,LOW);
  digitalWrite(IN4,LOW);
  }
  if(((message >= '1' ) && ( message <= '9' )) || message == 'q') // handle Car Speed 
  {
  if (message == 'q')
  {
    Speed = 255 ; // max Speed
  }
  else
  {
    Speed = (message -48)*255/10 ;
  }
  }
}
char u8GetMessage(){
if (Serial.available()){
return (Serial.read()) ;
}
}
