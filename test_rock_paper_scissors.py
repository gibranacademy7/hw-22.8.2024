import pytest
from rock_paper_scissors import validity_check
from rock_paper_scissors import check_winner

# Lowercase tests:
def test_validity_check_lowercase_rock():
    assert validity_check("rock") == 2

def test_validity_check_lowercase_paper():
    assert validity_check("paper") == 0

def test_validity_check_lowercase_scissors():
    assert validity_check("scissors") == 1

# Uppercase tests:
def test_validity_check_uppercase_rock():
    assert validity_check("ROCK") == 2

def test_validity_check_uppercase_paper():
    assert validity_check("PAPER") == 0

def test_validity_check_uppercase_scissors():
    assert validity_check("SCISSORS") == 1

# Mixed case tests:
def test_validity_check_mixedcase_rock():
    assert validity_check("RoCk") == 2

def test_validity_check_mixedcase_paper():
    assert validity_check("PaPeR") == 0

def test_validity_check_mixedcase_scissors():
    assert validity_check("sCissoRs") == 1

# Invalid input test:
def test_validity_check_invalid_choice():
    with pytest.raises(ValueError, match="Illigal Choice!"):
        validity_check("invalid_choice")

# -------------------------------------------------

def test_rock_vs_rock():
    assert check_winner(2, 2) == 0

def test_rock_vs_paper():
    assert check_winner(2, 0) == 2

def test_rock_vs_scissors():
    assert check_winner(2, 1) == 1

def test_paper_vs_rock():
    assert check_winner(0, 2) == 1

def test_paper_vs_paper():
    assert check_winner(0, 0) == 0

def test_paper_vs_scissors():
    assert check_winner(0, 1) == 2

def test_scissors_vs_rock():
    assert check_winner(1, 2) == 2

def test_scissors_vs_paper():
    assert check_winner(1, 0) == 1

def test_scissors_vs_scissors():
    assert check_winner(1, 1) == 0

def test_invalid_player1_choice():
    with pytest.raises(ValueError):
        check_winner(3, 0);

def test_invalid_player2_choice():
    with pytest.raises(ValueError):
        check_winner(0, -1);