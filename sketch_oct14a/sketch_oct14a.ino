//Lettura input da scacchiera
// la rappresentazione di una scacchiera in formato testuale si chiama Forsyth-Edwards Notion (FEN)
void setup() 
{

  Serial.begin(9600);

  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);

  digitalWrite(8, LOW);
}

void loop() 
{
  Serial.println("prova messaggio");
  digitalWrite(2, LOW);
  digitalWrite(3, LOW);
  digitalWrite(4, HIGH);
}


