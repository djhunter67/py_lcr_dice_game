from src.lcr import l_c_r, play_again, roll_sixed_sided_die, user_inquiry
import pytest


def test_roll_sixed_sided_die_returns_int():
    """Test that the user input is a string."""

    assert isinstance(roll_sixed_sided_die(), int) is True


def test_roll_sixed_sided_die_returns_int_between_1_and_6():
    """Test that the user input is a string."""

    assert 1 <= roll_sixed_sided_die() <= 6


def test_roll_sided_die_does_not_return_anything_other_than_int():
    """Test that the user input is a string."""

    assert isinstance(roll_sixed_sided_die(), int) is True


def test_roll_six_sided_die_does_not_return_0():
    """Test that the user input is a string."""
    # iterate over 1000 rolls
    for _ in range(1000):

        assert roll_sixed_sided_die() != 0


def test_roll_six_sided_die_does_not_return_7():
    """Test that the user input is a string."""
    # iterate over 1000 rolls
    for _ in range(1000):

        assert roll_sixed_sided_die() != 7


def test_l_c_r_wins_over_40_percent_of_time():
    """Test that the user input is a string."""
    # iterate over 1000 rolls
    count: int = int()
    for _ in range(1000):
        if l_c_r(roll_sixed_sided_die()):
            count += 1

    assert count > 400


def test_l_c_r_loses_under_40_percent_of_time():
    """Test that the user input is a string."""
    # iterate over 1000 rolls
    count: int = int()
    for _ in range(1000):
        if not l_c_r(roll_sixed_sided_die()):
            count += 1

    assert count > 400


def test_l_c_r_wins_less_than_60_percent_of_time():
    """Test that the user input is a string."""
    # iterate over 1000 rolls
    count: int = int()
    for _ in range(1000):
        if l_c_r(roll_sixed_sided_die()):
            count += 1

    assert count < 600


def test_user_input(mocker):
    """Test that the user input is a string."""

    mocker.patch('builtins.input', side_effect=['Julia', 'Jane', 'done'])

    assert user_inquiry() == ['Julia', 'Jane']


def test_user_input_is_string(mocker):
    """Test that the user input is a string."""

    mocker.patch('builtins.input', side_effect=['Joy', 'done'])

    assert isinstance(user_inquiry()[0], str)

def test_user_input_only_returns_names(mocker):
    """Test that the user input is a string."""

    mocker.patch('builtins.input', side_effect=['Joy', 'done'])

    assert user_inquiry()[-1] != 'done'


def test_user_inquiry_fails_if_not_string(mocker):
    """Test that the user input is a string."""

    mocker.patch('builtins.input', side_effect=[1, 'done'])

    assert isinstance(user_inquiry(), str) is False


def test_user_inquiry_returns_list_when_done(mocker):
    """Test that the user input is a string."""

    mocker.patch('builtins.input', side_effect=['done'])

    assert isinstance(user_inquiry(), list) is True


def test_play_again_returns_true(mocker):
    """Test that the user input is a string."""

    mocker.patch('builtins.input', side_effect=['y'])

    assert play_again() is True


def test_play_again_returns_false(mocker):
    """Test that the user input is a string."""

    mocker.patch('builtins.input', side_effect=['n'])

    assert play_again() is False


def test_play_again_raises_error_if_not_y_or_n(mocker):
    """Test that the user input is a string."""

    mocker.patch('builtins.input', side_effect=['a'])

    with pytest.raises(ValueError):
        play_again()

def test_play_again_raises_error_if_input_not_a_string(mocker):
    """Test that the user input is a string."""

    mocker.patch('builtins.input', side_effect=[1])

    with pytest.raises(ValueError):
        play_again()
