// VALUE -----------------------------------------------
#include <Servo.h>
Servo servo;
int servoPin=6;

int pin_led = A0;
int pin_shock = 3;
int min_value = 544;
int max_value = 2400;

int Vo = A1;  // dust 센서
int V_LED = 2;   //dust LED 2번핀

volatile int count = 0;
int shock = 1;
int soundcnt = 0;
String chledLight; /* 아두이노 센서값 문자열로 라즈베리파이 파이썬에서 받기 위해 문자열 변환*/
String chcount;
String chsoundL;
String chsoundR;
String chdust;

String shockok = "1";
String shockno = "0";
String soundokno = "0";

float Vo_value = 0;
float Voltage = 0;
int dustDensity = 0;
// VALUE -----------------------------------------------

void setup() {
  
  Serial.begin(9600);
  pinMode(pin_shock,INPUT);
  attachInterrupt(digitalPinToInterrupt(3),HIT_ISR,FALLING); 
  servo.attach(6);
  pinMode(V_LED, OUTPUT);
  pinMode(Vo, INPUT);
  
}

void loop() {
  
  // put your main code here, to run repeatedly:
  // LED --------------------------------------------
  int light = analogRead(pin_led);
  int shock = analogRead(pin_shock);
  int ledLight = map(light, 0, 1023, 255, 0);
  int soundd1 = analogRead(A2);
  int soundd2 = analogRead(A4);
  
  analogWrite(11, ledLight);
  if(ledLight<77) {
    analogWrite(11, LOW);
  }
  
  //----------------------servo-----------------
  soundokno = "0";
  if(soundd1 > 160) {
    soundokno = "1";
    servo.write(30);
  } else if(soundd2 > 150) {
    servo.write(150);
    soundokno = "1";
  }
  
  chledLight = String(ledLight);
  
  chcount = String(count);
  //sound LR ------------------------
  chsoundL = String(soundd1);
  chsoundR = String(soundd2);
  //sound LR ------------------------
  
  // DUST ------------------------------
  digitalWrite(V_LED,LOW);
  delayMicroseconds(280);

  Vo_value = analogRead(Vo); 

  delayMicroseconds(40);

  digitalWrite(V_LED,HIGH); 

  delayMicroseconds(9680);

  Voltage = Vo_value * 5.0 / 1024.0;

  dustDensity = (Voltage - 0.3)/0.005;
  dustDensity = abs(dustDensity);
  chdust = String(dustDensity);
  
  if(count >= 1) {
    count = count +1 ;

    if(count == 3) {
      count = 0 ;
    }
  }
  if ( soundokno != '1') {
    if(soundcnt == 3) {
      soundcnt = 0;
      soundokno = '0';
    }
  }
  Serial.println(chledLight+","+shockno+","+soundokno+","+chdust);

  //Serial.println(chledLight+" "+shockok+" "+chsoundL+" "+chsoundR+" "+chdust);
  
  delay(4950);
}
  void HIT_ISR(void) {
    count++;
  }
