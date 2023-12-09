#include <SoftwareSerial.h>

SoftwareSerial bt(10, 11); // RX TX

int matrizDireccion[5][4] = {
  { 1, 0, 1, 0 },
  { 0, 1, 0, 1 },
  { 1, 0, 0, 1 },
  { 0, 1, 1, 0 },
  { 0, 0, 0, 0 }
};

int matrizVelocidad[5][2] = {
  { 125, 125 },
  { 125, 125 },
  { 160, 160 },
  { 160, 160 },
  { 0, 0 }
};

int inputs[4] = { 2, 3, 7, 8 };  // in1, in2, in3, in4 --pines digitales
int enables[2] = { 5, 6 };         // pines PWM...
int i;
String cadena;

void SetDireccion(int estado) {
  for (i = 0; i < 4; i++) {
    digitalWrite(inputs[i], matrizDireccion[estado][i]);
  }
  for (i = 0; i < 2; i++) {
    analogWrite(enables[i], matrizVelocidad[estado][i]);
  }
}

// BT - ARUINO
// 5V - 5V
// GND - GND
// TX - RX (10)
// RX - TX (11)
// STATE - NO CONECTAR
// ENABLE - NO CONECTAR

// PUENTE H - ARDUINO
// IN1 - 2
// IN2 - 3
// IN3 - 7
// IN4 - 8
// EN1 - 5
// EN2 - 6

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  bt.begin(9600);

  for (int i = 0; i < 4; i++) {
    pinMode(inputs[i], OUTPUT);
  }
  for (int i = 0; i < 2; i++) {
    pinMode(enables[i], OUTPUT);
  }
  

}

void loop() {
  // put your main code here, to run repeatedly:
  if (bt.available()) {
    //Serial.write(bt.read());
    cadena = bt.readString();
    Serial.println(cadena);

    int estado = cadena.toInt();

    SetDireccion(estado);
  }

}