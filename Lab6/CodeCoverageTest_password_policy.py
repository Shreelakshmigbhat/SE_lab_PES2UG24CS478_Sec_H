import pytest
from password_policy import check_password, strength, suggest_fix

# Baseline tests from the starter file
def test_valid_password_has_no_issues():
    assert check_password("Abcdef1!") == []

def test_valid_password_is_good():
    assert strength("Abcdef1!") == "good"

# Added for line coverage
def test_too_short():
    assert "too short" in check_password("Ab1!")

def test_common_password():
    assert "common" in check_password("password")

def test_missing_uppercase():
    assert check_password("abcdef1!") == ["no uppercase"]

def test_missing_lowercase():
    assert check_password("ABCDEF1!") == ["no lowercase"]

def test_missing_digit():
    assert check_password("Abcdefg!") == ["no digit"]

def test_missing_special():
    assert check_password("Abcdefg1") == ["no special"]

def test_strength_strong():
    assert strength("Abcdefghijklm1!") == "strong"

def test_strength_weak():
    assert strength("abcdef1!") == "weak"

def test_strength_very_weak():
    assert strength("abc") == "very weak"

def test_suggest_fix_none():
    assert suggest_fix([]) == "none needed"

def test_suggest_fix_too_short():
    assert suggest_fix(["too short"]) == "add more characters"

def test_suggest_fix_common():
    assert suggest_fix(["common"]) == "avoid common passwords"

def test_suggest_fix_missing_class():
    assert suggest_fix(["no digit"]) == "add digit"
