// Practical 6: Board 2 - Server Receiver
void setup(){
  Serial.begin(9600);
}

void loop(){
  if(Serial.available() > 0){
    float receivedTemp = Serial.parseFloat();
    Serial.print("Server received Temp: ");
    Serial.println(receivedTemp);
  }
}
