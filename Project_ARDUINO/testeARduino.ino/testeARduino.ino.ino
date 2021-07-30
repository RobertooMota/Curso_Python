/*
  Autor:
  Date:
  Obs:

*/

char value;

void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);

}

void loop() {
  if (Serial.available())
  {
    value = Serial.read();
    if (value == 'L')
    {
      digitalWrite(13, 1);
      Serial.print("LED LIGADO!");
    } else if (value == 'D')
    {
      digitalWrite(13, 0);
      Serial.print("LED DESLIGADO!");
    }
  }


}
