def count_vowels(s: str) -> int:
    vowels = "аеиоуыэюяАЕИОУЫЭЮЯ"
    return sum(1 for char in s if char in vowels)