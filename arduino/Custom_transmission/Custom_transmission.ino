
int freq;
String msg;
unsigned char char_to_send;

// the setup function runs once when you press reset or power the board
void setup() {
  pinMode(4, OUTPUT);
  // pinMode(5, INPUT);

  Serial.begin(115200);
  Serial.setTimeout(-1);
  Serial.println("Give frequency in Hz:");
// freq = 1000;
// 300 - 10K bps  :  3333 - 100 us for AM
// 0.5 - 30 ksps  :  5000 - 33 us for FM
  freq = Serial.readStringUntil('\n').toInt();
  Serial.println("Give message to be transmitted:");
  msg = Serial.readStringUntil('\n');
}

// the loop function runs over and over again forever
void loop() {
  for(unsigned char i = 0; i<msg.length(); i++){
    char_to_send = msg[i] - '0';
    digitalWrite(4, char_to_send);
//    Serial.print(msg[(i-1)%msg.length()]); 
//    Serial.println(digitalRead(5));
    
    delayMicroseconds(1000000/freq);
  }
}
