import numpy as np

def read_audio_file(file_path):
    with open(file_path, "rb") as file:
        data = np.frombuffer(file.read(), dtype=np.int8)
    return data

def rice_encoding(data, rice_parameter):
    encoded = []
    for x in data:
        abs_value = abs(x)
        sign_bit = 1 if x < 0 else 0
        quotient = abs_value >> rice_parameter
        remainder = abs_value & ((1 << rice_parameter) - 1)
        encoded.extend([1] * quotient + [0])
        encoded.extend([int(bit) for bit in format(remainder, f"0{rice_parameter}b")])
        encoded.append(sign_bit)
    return encoded

def rice_decoding(encoded_data, rice_parameter):
    decoded_data = []
    index = 0
    while index < len(encoded_data):
        quotient = 0
        while encoded_data[index] == 1:
            quotient += 1
            index += 1
        index += 1
        remainder_bits = encoded_data[index:index + rice_parameter]
        remainder = int("".join(map(str, remainder_bits)), 2)
        index += rice_parameter
        sign_bit = encoded_data[index]
        index += 1
        decoded_value = (quotient << rice_parameter) + remainder
        if sign_bit == 1:
            decoded_value = -decoded_value
        decoded_data.append(decoded_value)
    return np.array(decoded_data, dtype=np.int8)

def calculate():
    file_path = "Queen_sint8.raw"
    rice_parameters = [1,2,3]

    audio_data = read_audio_file(file_path)
    print("Original data:", audio_data[:10])

    for p in rice_parameters:
        encoded_data = rice_encoding(audio_data, p)
        print(f"for rice parameter {p} -> Encoded data: (first 30 bits):", encoded_data[:30])
        print(f"for rice parameter {p} -> Bitstream size: {len(encoded_data)} bits")

        decoded_data = rice_decoding(encoded_data, p)
        print(f"for rice parameter {p} -> Decoded data:", decoded_data[:10])
        print("-----------------------------------------------")
calculate()

