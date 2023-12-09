int tcrt[4] = {4, 9, 12, 13};


void setup() {
  // put your setup code here, to run once:
  for (int i=0; i<4; i++) {
    pinMode(tcrt[i], INPUT);
  }
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  for (int i=0; i<4; i++) {
    int v = digitalRead(tcrt[i]);
    Serial.print(v);
  }
  Serial.println("");
  delay(100);

}
