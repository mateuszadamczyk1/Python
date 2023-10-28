#Algorytm Karpa Rabina
#Mateusz Adamczyk

def karp_rabin(text, pattern):
    def hash_string(s, length):
        hash_value = 0
        for char in s[:length]:
            hash_value = (hash_value * BASE + ord(char)) % PRIME
        return hash_value

    def recompute_hash(old_hash, old_char, new_char, pattern_length):
        new_hash = (old_hash - ord(old_char) * (BASE**(pattern_length - 1))) * BASE + ord(new_char)
        return new_hash % PRIME

    BASE = 256  
    PRIME = 101  

    text_length = len(text)
    pattern_length = len(pattern)
    pattern_hash = hash_string(pattern, pattern_length)
    text_hash = hash_string(text, pattern_length)

    results = []  

    for i in range(text_length - pattern_length + 1):
        if text_hash == pattern_hash and text[i:i + pattern_length] == pattern:
            results.append(i)

        if i < text_length - pattern_length:
            text_hash = recompute_hash(text_hash, text[i], text[i + pattern_length], pattern_length)

    return results  


text = """Stoi na stacji lokomotywa,
Ciężka, ogromna i pot z niej spływa
Tłusta oliwa.
Stoi i sapie, dyszy i dmucha,
Żar z rozgrzanego jej brzucha bucha
Buch - jak gorąco!
Uch - jak gorąco!
Puff - jak gorąco!
Uff - jak gorąco!
Już ledwo sapie, już ledwo zipie,
A jeszcze palacz wegiel w nią sypie."""
pattern = "gorąco"
results = karp_rabin(text, pattern)

if results:
    print(f"Znalezione hasła są na indeksach: {results}")
else:
    print("Podanego hasła nie ma w tekście")
