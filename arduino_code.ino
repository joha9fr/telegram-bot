
int led = 13;
char sel;
void setup(){
  pinMode(led,OUTPUT);
  Serial.begin(9600);
}

void ctrl_luces(char c){
    while(c=='L'){
      char d = Serial.read();
      if(d=='I'){
        Serial.println("luces encender");
        c='S';
        digitalWrite(led,HIGH);
      }
      else if (d=='O'){
        Serial.println("luces apagar");          
        c='S';
        digitalWrite(led, LOW);
      }
    }
}

void ctrl_ventiladores(char c){
    while(c=='V'){
      char d = Serial.read();
      if(d=='I'){
        Serial.println("vent encender");
        c='S';
        digitalWrite(led,HIGH);
      }
      else if (d=='O'){
        Serial.println("vent apagar");          
        c='S';
        digitalWrite(led, LOW);
      }
    }
}

void ctrl_cortinas(char c){
    while(c=='C'){
      char d = Serial.read();
      if(d=='0'){
        Serial.println("cortinas cerradas");
        c='S';
        digitalWrite(led,LOW);
      }
      else if (d=='1'){
        Serial.println("cortinas 20");          
        c='S';
        digitalWrite(led, LOW);
      }
      else if (d=='2'){
        Serial.println("cortinas 40");          
        c='S';
        digitalWrite(led, LOW);
      }
      else if (d=='3'){
        Serial.println("cortinas 60");          
        c='S';
        digitalWrite(led, LOW);
      }
      else if (d=='4'){
        Serial.println("cortinas 80");          
        c='S';
        digitalWrite(led, LOW);
      }
      else if (d=='5'){
        Serial.println("cortinas 100");          
        c='S';
        digitalWrite(led, LOW);
      }
    }
}

void envio_datos(char c){
    if(c=='S'){
      Serial.println("1999");
      int temp =2;
      int dist =200;
      int hum = 80;
      int luz = 450;
      Serial.println(temp);
      Serial.println(dist);
      Serial.println(hum);
      Serial.println(luz);
      delay(2000);
    }
}

void loop(){
  envio_datos(sel);
  Serial.println(sel);
  if(Serial.available()){
    sel = Serial.read();
    ctrl_luces(sel);
    ctrl_ventiladores(sel);
    ctrl_cortinas(sel);
  }
}
