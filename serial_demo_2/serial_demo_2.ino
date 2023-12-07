#define POT_PIN A0 // Pin where the light sensor is connected

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int sensorValue = analogRead(POT_PIN); // Read the potentiometer value
  Serial.println(sensorValue); // Send the value over serial

  delay(100); 

  if (Serial.available() > 0) {
    char incomingByte = Serial.read();
    if (incomingByte == 'H') {
      digitalWrite(LED_BUILTIN, HIGH);
    } else if (incomingByte == 'L') {
      digitalWrite(LED_BUILTIN, LOW);
    }
  }
}
