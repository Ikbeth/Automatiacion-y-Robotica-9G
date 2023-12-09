#include <SoftwareSerial.h>

SoftwareSerial bt(10, 11); // RX TX

// BT - ARUINO
// 5V - 5V
// GND - GND
// TX - RX (10)
// RX - TX (11)

// STATE - NO CONECTAR
// ENABLE - NO CONECTAR

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); // VELOCIDAD DE CONFIGURACION
  bt.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()) {
    bt.write(Serial.read());
  }

  if (bt.available()) {
    Serial.write(bt.read());
  }

}

// CARGAR 