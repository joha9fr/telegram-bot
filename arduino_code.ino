
int led = 13;
char sel;
int led_luz = 1;
int led_vent = 2;
int led_20 = 3;
int led_40 = 4;
int led_60 = 5;
int led_80 = 6;
int led_100 = 7;

//Variables Sensor Temperatura y humedad

//Libraries
#include <DHT.h>;
#include <NewPing.h>
//Constants
#define DHTPIN 7     // what pin we're connected to
#define DHTTYPE DHT22   // DHT 22  (AM2302)
DHT dht(DHTPIN, DHTTYPE); //// Initialize DHT sensor for normal 16mhz Arduino
/*Aqui se configuran los pines donde debemos conectar el sensor*/
#define TRIGGER_PIN  12
#define ECHO_PIN     11
#define MAX_DISTANCE 200
/*Crear el objeto de la clase NewPing*/
NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE);
//Variables
int chk;
int hum;  //Stores humidity value
int temp; //Stores temperature value

//Variables Sensor Luminosidad

int sensorPin = A0;
int ledPin = 7;
int sensorValue = 0;

// Variables Sensor de Proximidad
const int trigPin = 9;
const int echoPin = 10;
long duration;
int distance;


/////////////////////////////////////////////////////////////////////////////////
void setup() {
  //Led de acciones
  pinMode(led_luz, OUTPUT);
  pinMode(led_vent, OUTPUT);
  pinMode(led_20, OUTPUT);
  pinMode(led_40, OUTPUT);
  pinMode(led_60, OUTPUT);
  pinMode(led_80, OUTPUT);
  pinMode(led_100, OUTPUT);

  //Variables Sensor Luminosidad
  pinMode(ledPin, OUTPUT);
  pinMode(led, OUTPUT);
  //Sensor de proximidad
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPin, INPUT); // Sets the echoPin as an Input
  //Sensor de Humedad y temperatura
  dht.begin();

  pinMode(led, OUTPUT);
  Serial.begin(9600);
}
/////////////////////////////////////////////////////////////////////////////////

int lectura_hum() {
  hum = dht.readHumidity();
  return hum;
}
int lectura_temp() {
  temp = dht.readTemperature();
  return temp;
}
int lectura_luz() {
  sensorValue = analogRead(sensorPin);
  return sensorValue;
}
int lectura_dist() {
  // Clears the trigPin
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  // Sets the trigPin on HIGH state for 10 micro seconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);
  // Calculating the distance
  distance = duration * 0.034 / 2;
  return distance;
}

void ctrl_luces(char c) {
  while (c == 'L') {
    char d = Serial.read();
    if (d == 'I') {
      Serial.println("luces encender");
      c = 'S';
      digitalWrite(led_luz, HIGH);
    }
    else if (d == 'O') {
      Serial.println("luces apagar");
      c = 'S';
      digitalWrite(led_luz, LOW);
    }
  }
}
/////////////////////////////////////////////////////////////////////////////////


void ctrl_ventiladores(char c) {
  while (c == 'V') {
    char d = Serial.read();
    if (d == 'I') {
      Serial.println("vent encender");
      c = 'S';
      digitalWrite(led_vent, HIGH);
    }
    else if (d == 'O') {
      Serial.println("vent apagar");
      c = 'S';
      digitalWrite(led_vent, LOW);
    }
  }
}
/////////////////////////////////////////////////////////////////////////////////

void ctrl_cortinas(char c) {
  while (c == 'C') {
    char d = Serial.read();
    if (d == '0') {
      Serial.println("cortinas cerradas");
      c = 'S';
      digitalWrite(led_20, LOW);
      digitalWrite(led_40, LOW);
      digitalWrite(led_60, LOW);
      digitalWrite(led_100, LOW);
      digitalWrite(led_100, LOW);
    }
    else if (d == '1') {
      Serial.println("cortinas 20");
      c = 'S';
      digitalWrite(led_20, HIGH);
      digitalWrite(led_40, LOW);
      digitalWrite(led_60, LOW);
      digitalWrite(led_80, LOW);
      digitalWrite(led_100, LOW);
    }
    else if (d == '2') {
      Serial.println("cortinas 40");
      c = 'S';
      digitalWrite(led_20, HIGH);
      digitalWrite(led_40, HIGH);
      digitalWrite(led_60, LOW);
      digitalWrite(led_80, LOW);
      digitalWrite(led_100, LOW);
    }
    else if (d == '3') {
      Serial.println("cortinas 60");
      c = 'S';
      digitalWrite(led_20, HIGH);
      digitalWrite(led_40, HIGH);
      digitalWrite(led_60, HIGH);
      digitalWrite(led_80, LOW);
      digitalWrite(led_100, LOW);
    }
    else if (d == '4') {
      Serial.println("cortinas 80");
      c = 'S';
      digitalWrite(led_20, HIGH);
      digitalWrite(led_40, HIGH);
      digitalWrite(led_60, HIGH);
      digitalWrite(led_80, HIGH);
      digitalWrite(led_100, LOW);
    }
    else if (d == '5') {
      Serial.println("cortinas 100");
      c = 'S';
      digitalWrite(led_20, HIGH);
      digitalWrite(led_40, HIGH);
      digitalWrite(led_60, HIGH);
      digitalWrite(led_80, HIGH);
      digitalWrite(led_100, HIGH);
    }
  }
}
/////////////////////////////////////////////////////////////////////////////////

void envio_datos(char c) {
  if (c == 'S') {
    //Serial.println("1999"); Supongo que esto era una prueba
    int temperatura = lectura_temp();
    int distancia = lectura_dist();
    int humedad = lectura_hum();
    int light = lectura_luz();
    Serial.println(temperatura);
    Serial.println(distancia);
    Serial.println(humedad);
    Serial.println(light);
    delay(2000);
  }
}
/////////////////////////////////////////////////////////////////////////////////


void loop() {
  envio_datos(sel);
  Serial.println(sel);
  if (Serial.available()) {
    sel = Serial.read();
    ctrl_luces(sel);
    ctrl_ventiladores(sel);
    ctrl_cortinas(sel);
  }
}
