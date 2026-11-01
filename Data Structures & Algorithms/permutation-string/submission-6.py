class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = {}
        s1Map = {}

        for c in s1:
            s1Map[c] = s1Map.get(c, 0) + 1

        for index, character in enumerate(s2):
            # Rimuovo il carattere che esce dalla window
            if index >= len(s1):
                left_char = s2[index - len(s1)]

                window[left_char] -= 1

                if window[left_char] == 0:
                    window.pop(left_char)

            # Aggiungo il nuovo carattere
            window[character] = window.get(character, 0) + 1

            if window == s1Map:
                return True

        return False