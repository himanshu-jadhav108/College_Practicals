// Practical 4: Gas Leakage Detection System
// Hardware: MQ-2 AO -> A0, Buzzer (+) -> D8, LED Anode -> D13

int gasSensorPin = A0;
int buzzerPin = 8;
int ledPin = 13;

int gasValue = 0;
int threshold = 300;   // Threshold level for gas detection

void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(buzzerPin, OUTPUT);
  Serial.begin(9600);

  digitalWrite(ledPin, LOW);
  digitalWrite(buzzerPin, LOW);

  Serial.println("Gas Leakage Detection System");
  Serial.println("System Ready...");
  delay(2000);
}

void loop() {
  // Read gas sensor
  gasValue = analogRead(gasSensorPin);

  // Display gas value
  Serial.print("Gas Level: ");
  Serial.print(gasValue);

  // Check gas level
  if (gasValue > threshold) {
    digitalWrite(ledPin, HIGH);
    tone(buzzerPin, 1000);
    Serial.println(" -> WARNING! Gas Leakage Detected!");
  } else {
    digitalWrite(ledPin, LOW);
    noTone(buzzerPin);
    Serial.println(" -> Gas Level Normal");
  }

  delay(1000);
}
