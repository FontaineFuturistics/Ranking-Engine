def genStrings(characters: list, template: list) -> list:

    # Length strings
    c_len = len(characters)
    t_len = len(template)

    # Return string
    word = ""

    # Do the generator
    while template[t_len - 1] < c_len:

        # Make the word
        word = ""
        for index in template:
            word += characters[index]

        # Yield it
        yield word

        # Increment
        template[0] += 1
        
        # Do rollover
        for index in range(t_len - 1):
            if template[index] >= c_len:
                template[index] = 0
                template[index + 1] += 1

        #print(f"[{template[0]},{template[1]}]")

NUMBERS = ["1","2","3","4","5","6","7","8","9"]
SSN_template = [0,0,0,0,0,0,0,0,0]

#"""
import base64
#f = open("./numbers.txt", "wb") # Open as bytes
f = open("./numbers.txt", "w") # Open as text
for word in genStrings(NUMBERS,SSN_template):
    ssn = f"{word[0]}{word[1]}{word[2]}-{word[3]}{word[4]}-{word[5]}{word[6]}{word[7]}{word[8]}\n"
    #ascii = ssn.encode("ascii")
    #b64 = base64.b64encode(bytes(ssn, "utf-8"))
    f.write(ssn)

f.close() 
#"""