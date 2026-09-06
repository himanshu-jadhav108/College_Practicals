// Practical 6: Board 1 - IoT Sensor Sender
int sensorPin = A0;
float voltage, temperatureC;

void setup(){
  Serial.begin(9600);
}

void loop(){
  int reading = analogRead(sensorPin);
  voltage = reading * (5.0 / 1023.0);
  temperatureC = (voltage - 0.5) * 100;
  Serial.print("Server received Temp:");
  Serial.println(temperatureC);
  delay(1000);
}
