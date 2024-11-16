from collections import Counter
import math

file_paths = [
    "C:\\Users\\user\\Desktop\\python\\data-compression\\whiteUniformNoise_uint8.raw",
    "C:\\Users\\user\\Desktop\\python\\data-compression\\whiteGaussianNoise_uint8.raw",
    "C:\\Users\\user\\Desktop\\python\\data-compression\\coloredGaussianNoise_uint8.raw",
    "C:\\Users\\user\\Desktop\\python\\data-compression\\Queen_sint8.raw",
    "C:\\Users\\user\\Desktop\\python\\data-compression\\imageData.raw",
    "C:\\Users\\user\\Desktop\\python\\data-compression\\englishText.txt"
]

def calculate_marginal_entropy(data):
    counts = Counter(data)
    entropy = 0
    for c in counts.values():
        p = c / len(data)
        entropy -= p * math.log2(p)
    return entropy

def calculate_conditional_entropy(data):
    pairs = Counter((data[i], data[i+1]) for i in range(len(data)-1))
    singles = Counter(data)
    cond_entropy = 0
    for (a, b), cnt in pairs.items():
        p_pair = cnt / (len(data) - 1)
        p_a = singles[a] / len(data)
        cond_entropy -= p_pair * math.log2(p_pair / p_a)
    return cond_entropy

def calculate_block_entropy(data):
    pairs = Counter((data[i], data[i+1]) for i in range(len(data)-1))
    entropy = 0
    for cnt in pairs.values():
        p = cnt / (len(data) - 1)
        entropy -= p * math.log2(p)
    return entropy, entropy / 2

for file_path in file_paths:
    with open(file_path, "rb") as f:
        data = f.read()

    marginal_entropy = calculate_marginal_entropy(data)
    conditional_entropy = calculate_conditional_entropy(data)
    block_entropy, half_block_entropy = calculate_block_entropy(data)
    
    print(f"{file_path} Marginal entropy: {marginal_entropy}")
    print(f"{file_path} 1-st order conditional entropy: {conditional_entropy}")
    print(f"{file_path} Block entropy: {block_entropy}")
    print(f"{file_path} Block entropy/2: {half_block_entropy}")
    print("--------------------------------------------------")

'''
What can you conclude about the potential to compress these files?

1. whiteUniformNoise and whiteGaussianNoise= these files contain high randomness, therefore the entropy is high. 
High entropy makes it difficult to compress the data effectively, so these files are not very compressible.

2. Queen_sint8 and imageData: these datas have some repeated patterns so they're not randomness too much. Therefore, they have low entropy.
So they can be compressed better. We can probably achieve good compression rates.

3. coloredGaussianNoise: this data may have some structure or correlation due to the color information. 
While it is still noisy, it might have slightly lower entropy than pure white noise and it makes that more compressible.

4. englishText: Natural language has a lot of repetitive patterns, and it makes the entropy lower. 
This makes text files compressible.

'''
