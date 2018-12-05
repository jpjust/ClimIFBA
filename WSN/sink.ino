// Variáveis globais
String data;
int t, h;

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  if (Serial.available())
  {
    data = Serial.readString();
    Serial.print(data);
  }
}
