/* 
 Ejemplo de control de motor DC usando modulo L298
 http://electronilab.co/tienda/driver-dual-para-motores-full-bridge-l298n/
 
 Creado 16/05/14
 por Andres Cruz
 ELECTRONILAB.CO

 */

int IN3 = 5;    // Input3 conectada al pin 5
int IN4 = 4;    // Input4 conectada al pin 4 
int ENB = 3;    // ENB conectada al pin 3 de Arduino
const int LEDPin= 13;
const int PIRPin= 2;

const byte BUFFER_SIZE = 10;
char buf[BUFFER_SIZE];

void setup()
{
 Serial.begin(9600);
 Serial.print("init");
 pinMode (ENB, OUTPUT); 
 pinMode (IN3, OUTPUT);
 pinMode (IN4, OUTPUT);
// PIR
 pinMode(LEDPin, OUTPUT);
 pinMode(PIRPin, INPUT);
}
void loop()
{
  while (Serial.available() > 0) 
  {
    int rlen = Serial.readBytesUntil('\n', buf, BUFFER_SIZE);
    byte dir_motor = buf[6] ;
    if(dir_motor == '0')
        {
          MotorAntihorario();
        }
    else if(dir_motor == '1')
        {
          MotorHorario();
        }
    else{
          MotorStop();
        }
    Serial.print("recv");
  }
  
 sensor_pir();
}

void MotorHorario()
{
  //Preparamos la salida para que el motor gire en un sentido
  digitalWrite (IN3, HIGH);
  digitalWrite (IN4, LOW);
  // Aplicamos PWM al pin ENB, haciendo girar el motor, cada 2 seg aumenta la velocidad
  analogWrite(ENB,65);
}
void MotorAntihorario()
{
  //Preparamos la salida para que el motor gire en un sentido
  digitalWrite (IN3, LOW);
  digitalWrite (IN4, HIGH);
  // Aplicamos PWM al pin ENB, haciendo girar el motor, cada 2 seg aumenta la velocidad

}

void MotorStop()
{
  // Apagamos el motor y esperamos 5 seg

  digitalWrite (IN3, LOW);
  digitalWrite (IN4, LOW);
}

void sensor_pir()
{
 int value= digitalRead(PIRPin);
  if (value == HIGH)
  {
    digitalWrite(LEDPin, HIGH);
  }
  else
  {
    digitalWrite(LEDPin, LOW);
  }
}
