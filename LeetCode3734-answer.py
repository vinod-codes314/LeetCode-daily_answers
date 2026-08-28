class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1

        odd, mid = 0, -1
        for i in range(26):
            if count[i] % 2 == 1:
                odd += 1
                mid = i
        if n % 2 == 0 and odd != 0:
            return ""
        if n % 2 == 1 and odd != 1:
            return ""

        half = n // 2
        left = [count[i] // 2 for i in range(26)]

        def build(first_half):
            reversed_half = first_half[::-1]
            if n % 2 == 1:
                return first_half + chr(ord('a') + mid) + reversed_half
            return first_half + reversed_half

        # Tier 1
        copy = left[:]
        matched = 0
        full_match = True
        for i in range(half):
            c = ord(target[i]) - ord('a')
            if copy[c] == 0:
                full_match = False
                break
            copy[c] -= 1
            matched += 1

        if full_match:
            first_half = target[:half]
            answer = build(first_half)
            if answer > target:
                return answer

        # Tier 2
        use = left[:]
        for i in range(matched):
            use[ord(target[i]) - ord('a')] -= 1

        for pos in range(min(matched, half - 1), -1, -1):
            if pos < matched:
                use[ord(target[pos]) - ord('a')] += 1

            t_char = ord(target[pos]) - ord('a')
            for c in range(t_char + 1, 26):
                if use[c] > 0:
                    use[c] -= 1
                    first_half = target[:pos] + chr(ord('a') + c)
                    rest = []
                    for x in range(26):
                        rest.append(chr(ord('a') + x) * use[x])
                    return build(first_half + "".join(rest))

        return ""