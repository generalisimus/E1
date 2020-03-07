import pytest
import sys
from viss import words, secret_word, visel_testing, error

def test_letter_first():
    assert secret_word in words

def test_letter_second():
    assert str(int()) not in secret_word
