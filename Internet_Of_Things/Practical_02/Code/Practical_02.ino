// Practical 2: IR Obstacle Detection with LED Notification
// Hardware: IR Sensor OUT -> D7, LED Anode -> D13 (via 220 ohm), LED Cathode -> GND

const int irPin = 7;     // IR sensor digital OUT pin
const int ledPin = 13;   // Notification LED pin

void setup() {
  pinMode(irPin, INPUT);
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
  Serial.println("IR Obstacle Detection Started");
}

void loop() {
  int state = digitalRead(irPin);  // Active LOW module

  if (state == LOW) {
    digitalWrite(ledPin, HIGH);
    Serial.println("Obstacle Detected - LED ON");
  } else {
    digitalWrite(ledPin, LOW);
    Serial.println("No Obstacle - LED OFF");
  }
  delay(500);
}
