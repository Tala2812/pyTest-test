import pytest
from main import count_vowels  # Импортируем функцию из main.py

def test_only_vowels():
    assert count_vowels("аеёиоуыэюя") == 10  # Обратите внимание, что буква ё также считается гласной
    assert count_vowels("АЕЁИОУЫЭЮЯ") == 10

def test_no_vowels():
    assert count_vowels("вгджзклмнпрстфхцч") == 0
    assert count_vowels("ВГДЖЗКЛМНПРСТФХЦЧ") == 0

def test_mixed_string():
    assert count_vowels("Привет, МИР!") == 3
    assert count_vowels("Домашнее задание!") == 8
    assert count_vowels("ПрекрАснаЯ погОдА") == 7

if __name__ == "__main__":
    pytest.main()