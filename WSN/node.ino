#include <DHT.h>
#include <DHT_U.h>
#include <Adafruit_Sensor.h>

// Configurações do sensor DHT11
#define DHT_PIN A1      // Porta
#define DHT_TYPE DHT11  // Tipo

DHT dht(DHT_PIN, DHT_TYPE);

// Variáveis globais
char data[7];
int t, h;

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  t = dht.readTemperature();
  h = dht.readHumidity();
  sprintf(data, "%d;%d\n", t, h);
  Serial.print(data);
  delay(2000);
}
