import pytest
import counter

@pytest.mark.parametrize("text,expected", [
    ("The quick brown fox jumps over the lazy dog", 9),
    ("Artificial\nIntelligence is\nchanging the\nworld", 6),
    ("Hello\nworld\nPython", 3),
    ("", 0),
    ("NoSpacesHereJustWords", 1),
    ("One, two, three, four, five, six.", 6),
])
def test_number_of_words(text, expected):
    assert counter.number_of_words(text) == expected

@pytest.mark.parametrize("text,expected", [
    ("The quick brown fox jumps over the lazy dog", 1),
    ("Artificial\nIntelligence is\nchanging the\nworld", 4),
    ("Hello\nworld\n\nPython", 4),
    ("", 1),
    ("Line one\nLine two\nLine three\n", 4),
    ("\n\n", 3),
])
def test_number_of_lines(text, expected):
    assert counter.number_of_lines(text) == expected

@pytest.mark.parametrize("text,expected", [
    ("The quick brown fox jumps over the lazy dog", 35),
    ("Artificial\nIntelligence\nis\nchanging\nthe\nworld", 40),  
    ("Hello\nworld\nPython", 16),  
    ("", 0),
    ("NoSpacesHereJustWords", 21),
    ("This is a sentence with punctuation! Isn't it?", 39),
])
def test_number_of_characters(text, expected):
    assert counter.number_of_characters(text) == expected

