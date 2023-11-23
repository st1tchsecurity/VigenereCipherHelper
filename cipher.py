class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet
        self.key_length = len(key)
        self.alphabet_length = len(alphabet)
        self.key_indices = [alphabet.index(k) for k in key]

    def encode(self, text):
        return self._cipher(text, 'encode')

    def decode(self, text):
        return self._cipher(text, 'decode')

    def _cipher(self, text, mode):
        result = []
        for i, char in enumerate(text):
            if char in self.alphabet:
                shift = self.key_indices[i % self.key_length]
                old_index = self.alphabet.index(char)
                if mode == 'encode':
                    new_index = (old_index + shift) % self.alphabet_length
                else:
                    new_index = (old_index - shift) % self.alphabet_length
                result.append(self.alphabet[new_index])
            else:
                result.append(char)
        return ''.join(result)
