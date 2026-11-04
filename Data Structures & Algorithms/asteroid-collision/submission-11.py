class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            alive = True

            # Collisione possibile solo se:
            # - l'asteroide nello stack va verso destra
            # - quello corrente va verso sinistra
            while stack and stack[-1] > 0 and a < 0:
                if stack[-1] < abs(a):
                    # L'asteroide corrente distrugge quello nello stack
                    stack.pop()

                elif stack[-1] == abs(a):
                    # Entrambi vengono distrutti
                    stack.pop()
                    alive = False
                    break

                else:
                    # L'asteroide corrente viene distrutto
                    alive = False
                    break

            # Inseriamo solo gli asteroidi sopravvissuti
            if alive:
                stack.append(a)

        return stack