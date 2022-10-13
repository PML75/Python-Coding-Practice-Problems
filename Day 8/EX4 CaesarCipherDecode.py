alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#print(alphabet.index('u')) = 20
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
  for letter in text:
    if (alphabet.index(letter)+shift < len(alphabet)):     
      print(alphabet[alphabet.index(letter) + shift], end= "")
    else: 
      #cycles the alphabet again
      print(alphabet[(alphabet.index(letter) - len(alphabet)) + shift], end = "")

def decode(text, shift):
  for letter in text:
    if alphabet.index(letter)-shift >= 0:     
      print(alphabet[alphabet.index(letter) - shift], end= "")
    else: 
      #cycles the alphabet again
      print(alphabet[(alphabet.index(letter) + len(alphabet)) - shift], end = "")      

if "encode" in direction:
  encrypt(text, shift)
else:
  decode(text, shift)
