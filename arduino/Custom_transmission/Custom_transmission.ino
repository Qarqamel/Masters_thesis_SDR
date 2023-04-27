
int freq;
String tx_msg;
unsigned char char_to_send;

// the setup function runs once when you press reset or power the board
void setup() {
  pinMode(4, OUTPUT); // output pin to send data to tx module
  // pinMode(5, INPUT); // input pin to receive data from rx module

  // Serial initialization
  Serial.begin(115200);
  Serial.setTimeout(-1);
    
  // Data transmission frequency
  // possible values:
  // 300 - 10K bps  :  3333 - 100 us for AM
  // 0.5 - 30 ksps  :  5000 - 33 us for FM
  Serial.println("Give frequency in Hz:");
  freq = Serial.readStringUntil('\n').toInt();

  // Data to be transmitted
  Serial.println("Give data to be transmitted:");
  tx_msg = Serial.readStringUntil('\n');
}

// the loop function runs over and over again forever
void loop() {
  // Sending data to tx module
  for(unsigned char i = 0; i<msg.length(); i++){
    char_to_send = msg[i] - '0';
    digitalWrite(4, char_to_send);
//  // Comparison between transmitted nad received data
//    Serial.print(msg[(i-1)%msg.length()]); 
//    Serial.println(digitalRead(5));

    // Delay to ensure proper signal freq
    delayMicroseconds(1000000/freq);
  }
}
