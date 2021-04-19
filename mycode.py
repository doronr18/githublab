def encrypt(sentence, s):
    answer = ""
    for i in range(len(sentence)):
        char = sentence[i]
        if char.isupper():
            answer += chr((ord(char) + s-65) % 26 + 65)
        else:
            answer += chr((ord(char) + s - 97) % 26 + 97)
    return answer
  
sentence = "Congress shall make no law respecting an establishment of religion, or prohibiting the free exercise thereof; or abridging the freedom of speech, or of the press; or the right of the people peaceably to assemble, and to petition the government for a redress of grievances."
shift = 1
print ("Text  : " + sentence)
print ("Shift : " + str(shift))
print ("Cipher: " + encrypt(sentence, shift))
