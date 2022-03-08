import pytest


@pytest.mark.unit
def test_fastrand_username():
    """Check generation of ``fastrand_username``."""
    from fastrand_fields import fastrand_username

    username = fastrand_username()

    assert username
    assert len(username.split("_")) == 3


@pytest.mark.unit
def test_fastrand_username_no_suffix():
    """Check generation of ``fastrand_username`` with no suffix."""
    from fastrand_fields import fastrand_username

    username = fastrand_username(suffix_uuid=False)

    assert username
    assert len(username.split("_")) == 2


@pytest.mark.unit
def test_fastrand_username_multiple():
    """Check generation of multiple ``fastrand_username``."""
    from fastrand_fields import fastrand_username

    usernames = { 
        fastrand_username()
        for _ in range(100)
    }
    
    assert len(usernames) == 100
