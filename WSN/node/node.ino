#include <DHT.h>

// Configurações do sensor DHT22
#define DHT_PIN 8       // Porta digital
#define DHT_TYPE DHT22  // Tipo

DHT dht(DHT_PIN, DHT_TYPE);

void setup()
{
  Serial.begin(9600);
  dht.begin();
}

void loop()
{
  delay(2000);

  Serial.print(dht.readTemperature());
  Serial.print(";");
  Serial.println(dht.readHumidity());
}
