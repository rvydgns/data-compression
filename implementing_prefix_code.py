def encode(message, code_table):
    encoded_message = ""
    for char in message:
        encoded_message += code_table[char]
    return encoded_message

def decode(encoded_message, code_table):
    reverse_code_table = {value: key for key, value in code_table.items()}
    decoded_message = ""
    current = ""
    for bit in encoded_message:
        current += bit
        if current in reverse_code_table:
            decoded_message += reverse_code_table[current]
            current = ""
    return decoded_message


code_table = {"A": "00",
                  "B": "11",
                  "C": "010",
                  "D": "10"}

message = "ABCDDB"
encoded = encode(message, code_table)
decoded = decode(encoded, code_table)


print("ENCODED:",encoded)
print("DECODED:",decoded)