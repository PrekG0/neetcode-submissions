class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_map = {}
        max_val = 0
        left = 0
        output = 0

        for right in range(len(s)):
            right_char = s[right]
            char_map[right_char] = char_map.get(right_char, 0) + 1
            max_val = max(max_val, char_map[right_char])

            while (right - left + 1) - max_val >k:
                char_map[s[left]] -= 1
                left += 1

            output = max(output, right - left + 1)
        return output    
        