
void setup() {
  // put your setup code here, to run once:
  pinMode(9, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(6, OUTPUT);
  // BUZZER 13
  Serial.begin(9600);
  Serial.setTimeout(1000);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()) {
    //leemos con una variable tipo char que nos servira para elegir el tipo de eliminacion de ruido que se hara
    String cadena = Serial.readStringUntil('\n');
    Serial.println(cadena.charAt(5));


    // FOCO
    if (cadena.charAt(0) == '1') {
      // REVISAR FOCO
      if (cadena.charAt(5) == '1') {
        if (cadena.charAt(3) == '1') {
          digitalWrite(9, HIGH);
        }
        else {
          if (cadena.charAt(4) == '1') {
            digitalWrite(9, LOW);
          }
        }
      }
      else if (cadena.charAt(5) == '2') {
        if (cadena.charAt(3) == '1') {
          digitalWrite(8, HIGH);
        }
        else {
          if (cadena.charAt(4) == '1') {
            digitalWrite(8, LOW);
          }
        }
      }
      else if (cadena.charAt(5) == '3') {
        if (cadena.charAt(3) == '1') {
          digitalWrite(7, HIGH);
        }
        else {
          if (cadena.charAt(4) == '1') {
            digitalWrite(7, LOW);
          }
        }
      }
    }


    // ESTEREO
    if (cadena.charAt(1) == '1') {
      if (cadena.charAt(3) == '1') {
        tone(5, 600);
      }
      else {
        if (cadena.charAt(4) == '1') {
          noTone(5);
        }
      }
    }

    // TELEVISION
    if (cadena.charAt(2) == '1') {
      if (cadena.charAt(3) == '1') {
        digitalWrite(6, HIGH);
      }
      else {
        if (cadena.charAt(4) == '1') {
          digitalWrite(6, LOW);
        }
      }
    }
  }
}
