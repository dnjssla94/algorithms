#define enA 9 //주황
#define enB 10
#define in1 6 //초록
#define in2 7 //보라
#define in3 11
#define in4 12
#define button 4

int rotDirection = 0;
int pressed = false;
int sensor1 = A3;
int sensor2 = A4;
int sensor3 = A5;

void setup() {
    Serial.begin(9600);  
    pinMode(enA, OUTPUT);
    pinMode(in1, OUTPUT);
    pinMode(in2, OUTPUT);

    pinMode(enB, OUTPUT);
    pinMode(in3, OUTPUT);
    pinMode(in4, OUTPUT);

    pinMode(button, INPUT);
    digitalWrite(in1, LOW);
    digitalWrite(in2, HIGH);
    digitalWrite(in3, LOW);
    digitalWrite(in4, HIGH);

    Serial.begin(9600);
}

void loop() {
  int potValue = analogRead(A0);
  int pwmOutput = map(potValue, 0, 1023, 0, 255);
  analogWrite(enA, pwmOutput);
  analogWrite(enB, pwmOutput);

  if (digitalRead(button)==true) {
    pressed = !pressed;
    }
  while (digitalRead(button)==true);
  delay(20);
  //=================센서============================
  int val1 = digitalRead(sensor1);
  int val2 = digitalRead(sensor2);
  int val3 = digitalRead(sensor3);
  Serial.print(val1);
  Serial.print(val2);
  Serial.print(val3);
  Serial.println();
  delay(100);

  // 검은 줄을 감지할때 1, 아닐때 0
  //=========================================
  if (pressed == true & rotDirection == 0) {
    digitalWrite(in1, HIGH);
    digitalWrite(in2, LOW);
    digitalWrite(in3, HIGH);
    digitalWrite(in4, LOW);
    rotDirection =1;
    delay(20);
  }
//    if (val1 == 0 &val2 == 0 &val3 == 0){
//      digitalWrite(in1, HIGH);
//      digitalWrite(in2, LOW);
//      digitalWrite(in3, HIGH);
//      digitalWrite(in4, LOW);  
//      delay(20);
//    }
//    else if (val1 == 0 &val2 == 1 &val3 == 0){
//      digitalWrite(in1, HIGH);
//      digitalWrite(in2, LOW);
//      digitalWrite(in3, HIGH);
//      digitalWrite(in4, LOW);  
//      delay(20);
//    }
//    else if (val1 == 1 &val2 == 1 &val3 == 1){
//      digitalWrite(in1, HIGH);
//      digitalWrite(in2, LOW);
//      digitalWrite(in3, HIGH);
//      digitalWrite(in4, LOW);  
//      delay(20);
//    }
//    else if (val1 == 1 &val2 == 0 &val3 == 0){
//      digitalWrite(in1, HIGH);  
//      digitalWrite(in2, HIGH);
//      digitalWrite(in3, HIGH);
//      digitalWrite(in4, LOW);
//      delay(20);
//    }
//    else if (val1 == 0 &val2 == 0 &val3 == 1){
//      digitalWrite(in1, HIGH);  
//      digitalWrite(in2, LOW);
//      digitalWrite(in3, HIGH);
//      digitalWrite(in4, HIGH);
//      delay(20);
//    }

//

  if (pressed == false & rotDirection == 1){                 // => 현재 필요없는 코드. 버튼 누르면 방향 반대로 가는 
    digitalWrite(in1, LOW);
    digitalWrite(in2, HIGH);
    digitalWrite(in3, LOW);
    digitalWrite(in4, HIGH);
    rotDirection =0;
    delay(20);
    }

}