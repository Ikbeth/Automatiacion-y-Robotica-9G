int matrizDireccion[4][4] = {
  { 1, 0, 1, 0 },
  { 0, 1, 1, 0 },
  { 1, 0, 0, 1 },
  { 0, 0, 0, 0 }
};

int matrizVelocidad[4][2] = {
  { 90, 90 },
  { 120, 120 },
  { 120, 120 },
  { 0, 0 }
};

String matrizEstados[4] = {
  {"0000"},
  {"1000"},
  {"0001"},
  {"1111"}
};

int inputs[4] = { 2, 3, 7, 8 };  // in1, in2, in3, in4 --pines digitales
int enables[2] = { 5, 6 };         // pines PWM...
int tcrt[4] = {4, 9, 12, 13};
String cadena= "";

void SetDireccion(int estado) {
  for (int i = 0; i < 4; i++) {
    digitalWrite(inputs[i], matrizDireccion[estado][i]);
  }
  for (int i = 0; i < 2; i++) {
    analogWrite(enables[i], matrizVelocidad[estado][i]);
  }
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  for (int i = 0; i < 4; i++) {
    pinMode(inputs[i], OUTPUT);
  }
  for (int i = 0; i < 2; i++) {
    pinMode(enables[i], OUTPUT);
  }
  for (int i=0; i<4; i++) {
    pinMode(tcrt[i], INPUT);
  }

}

void loop() {
  // put your main code here, to run repeatedly:

  for (int i=0; i<4; i++) {
    int v = digitalRead(tcrt[i]);
    cadena = cadena + String(v);
  }
  Serial.println(cadena);

  for (int i=0; i<4; i++) {
    if (cadena == matrizEstados[i]) {
      SetDireccion(i);
      if (i != 0 && i != 5) {
        delay(1000);
      }
    }
  }

  cadena = "";

}
