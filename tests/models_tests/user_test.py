import pytest
from tests import OhmTestCase

from models import user as module


class UserTest(OhmTestCase):
    def test_get_multi(self):
        assert self.chuck.get_multi("PHONE") == ['+14086441234', '+14086445678']
        assert self.justin.get_multi("PHONE") == []


@pytest.mark.parametrize(
    'user_tier, comparison_tier, expected',
    [
        ("Platinum", "Platinum", False),
        ("Platinum", "Gold", False),
        ("Platinum", "Silver", False),
        ("Platinum", "Bronze", False),
        ("Platinum", "Carbon", False),
        ("Gold", "Platinum", True),
        ("Gold", "Gold", False),
        ("Gold", "Silver", False),
        ("Gold", "Bronze", False),
        ("Gold", "Carbon", False),
        ("Silver", "Platinum", True),
        ("Silver", "Gold", True),
        ("Silver", "Silver", False),
        ("Silver", "Bronze", False),
        ("Silver", "Carbon", False),
        ("Silver", "Silver", False),
        ("Bronze", "Platinum", True),
        ("Bronze", "Gold", True),
        ("Bronze", "Silver", True),
        ("Bronze", "Bronze", False),
        ("Bronze", "Carbon", False),
        ("Carbon", "Platinum", True),
        ("Carbon", "Gold", True),
        ("Carbon", "Silver", True),
        ("Carbon", "Bronze", True),
        ("Carbon", "Carbon", False),
    ]
)
def test_is_below_tier(user_tier, comparison_tier, expected):
    user = module.User(tier=user_tier)
    assert user.is_below_tier(comparison_tier) == expected


def test_is_below_tier_raises_on_invalid_tier():
    user = module.User()
    with pytest.raises(Exception):
        user.is_below_tier("Invalid tier")
