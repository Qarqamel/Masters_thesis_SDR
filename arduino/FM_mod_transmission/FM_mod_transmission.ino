
int sent_val = 0;
int ctr = 0;

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(4, OUTPUT);
  pinMode(5, INPUT);
  pinMode(13, OUTPUT);
  digitalWrite(13, LOW); // for addtional GND
  Serial.begin(115200);
}

// the loop function runs over and over again forever
void loop() {
  int sent_val_prev = sent_val;
  sent_val = (ctr++)%2; //random(2);
  digitalWrite(4, sent_val); // random data generation
  int read_val = digitalRead(5);
  Serial.print(sent_val_prev);
  Serial.println(read_val);
  delayMicroseconds(1000); // 0.5 - 30 ksps  :  5000 - 33 us
}
