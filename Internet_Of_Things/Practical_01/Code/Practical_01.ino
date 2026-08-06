// Practical 1: Connectivity of Arduino UNO with TMP36 Sensor
const int sensorPin = A0;

void setup() {
  Serial.begin(9600);
  Serial.println("IoT Sensor Connectivity Started");
}

void loop() {
  // Read TMP36 sensor
  int sensorValue = analogRead(sensorPin);

  // Convert analog reading to voltage (0 to 5V)
  float voltage = sensorValue * (5.0 / 1023.0);

  // Convert voltage to temperature in Celsius
  float temperatureC = (voltage - 0.5) * 100.0;

  // Display sensor data
  Serial.print("ADC: ");
  Serial.print(sensorValue);
  Serial.print(" | Voltage: ");
  Serial.print(voltage, 2);
  Serial.print(" V | Temperature: ");
  Serial.print(temperatureC, 1);
  Serial.println(" C");

  delay(1000);
}
