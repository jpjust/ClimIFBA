#include <DHT.h>

// Configurações do sensor DHT22
#define DHT_PIN 8       // Porta digital
#define DHT_TYPE DHT22  // Tipo
#define ID "1"          // ID do sensor

DHT dht(DHT_PIN, DHT_TYPE);

void setup()
{
  Serial.begin(9600);
  dht.begin();
}

void loop()
{
  // Delay para a leitura do sensor
  delay(2000);

  Serial.print(ID);
  Serial.print(";");
  Serial.print(dht.readTemperature());
  Serial.print(";");
  Serial.println(dht.readHumidity());

  // Dorme por 5 minutos
  delay(300000);
}
