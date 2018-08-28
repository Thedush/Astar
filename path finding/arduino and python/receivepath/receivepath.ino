int e1=10,e2=11,m1=8,m11=9,m2=12,m21=13;

int i=0,len=0;char array[100]={};
int x=0;
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
while(Serial.available()>0){
    array[i]=Serial.read();
    //Serial.println(array[i]);
    i=i+1;

}
pinMode(e1,OUTPUT);
pinMode(e2,OUTPUT);
pinMode(m1,OUTPUT);
pinMode(m11,OUTPUT);
pinMode(m2,OUTPUT);
pinMode(m21,OUTPUT);
digitalWrite(m1,LOW);
digitalWrite(m11,LOW);
digitalWrite(m2,LOW);
digitalWrite(m21,LOW);
digitalWrite(e1,HIGH);
digitalWrite(e2,HIGH);

}

void loop() {
 if(array[x]=='l'){
digitalWrite(m1,HIGH);
digitalWrite(m11,LOW);
digitalWrite(m2,LOW);
digitalWrite(m21,LOW);
delay(1000);
 }
if(array[x]=='r'){
   digitalWrite(m1,LOW);
digitalWrite(m11,LOW);
digitalWrite(m2,HIGH);
digitalWrite(m21,LOW);
delay(1000);
 }
if(array[x]=='u'){
   digitalWrite(m1,HIGH);
digitalWrite(m11,LOW);
digitalWrite(m2,HIGH);
digitalWrite(m21,LOW);
delay(1000);
 }
if(array[x]=='d'){
digitalWrite(m1,LOW);
digitalWrite(m11,HIGH);
digitalWrite(m2,LOW);
digitalWrite(m21,HIGH);
 delay(1000);
 }

x++;
}


