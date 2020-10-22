int L = A3; // left sensor
int M = A4; // middle sensor
int R = A5; // right sensor

int enA = 9;
int enB = 10;

int in1 = 6; // 오른쪽 모터 뒤로
int in2 = 7; // 오른쪽 모터 앞으로
int in3 = 11; // 왼쪽 모터 앞으로 구르기
int in4 = 12; // 왼쪽 모터 뒤로 구르기

void setup()
{
  pinMode(L, INPUT);
  pinMode(R, INPUT);
  pinMode(M, INPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);

  pinMode(enA, OUTPUT); //오른쪽 모터 속도제어
  pinMode(enB, OUTPUT); //왼쪽 모터 속도제어
}

void loop()
{
  //하얀색이 0
  if (digitalRead(L) == HIGH && digitalRead(M) == HIGH && digitalRead(R) == LOW) {
    //직진
    forward();
  }
  if (digitalRead(L) == HIGH && digitalRead(M) == LOW && digitalRead(R) == LOW) {
    //좌회전
    Bleft();
  }
  if (digitalRead(L) == LOW  && digitalRead(M) == HIGH && digitalRead(R) == HIGH) {
    //직진
    forward();
  }
  if (digitalRead(L) == LOW  && digitalRead(M) == LOW && digitalRead(R) == HIGH) {
    //우회전
    Bright();
  }
  if (digitalRead(L) == LOW && digitalRead(M) == HIGH && digitalRead(R) == LOW) {
    //직진
    forward();
  }
if (digitalRead(L) == LOW && digitalRead(M) == LOW && digitalRead(R) == LOW) {
    //값 없음
  }
  if (digitalRead(L) == HIGH && digitalRead(M) == HIGH && digitalRead(R) == HIGH) {
    //직진
    forward();
  }
  if (digitalRead(L) == HIGH && digitalRead(M) == LOW && digitalRead(R) == HIGH) {
    //직진
    forward();
  }
}
void forward() {
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
  analogWrite(enA, 100);   //오른쪽 모터 속도, 숫자로 속도 제어가능
  analogWrite(enB, 100);
}
void Bright() {
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
  analogWrite(enA, 0);
  analogWrite(enB, 100);
}
void Bleft() {
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);
  analogWrite(enA, 100);
  analogWrite(enB, 0);
}
