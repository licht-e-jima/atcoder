from dataclasses import dataclass
import sys
from typing import List, Tuple

COINS: List[Tuple[str, float]] = [
    ('ONE_HUNDRED', 100.00),
    ('FIFTY', 50.00),
    ('TWENTY', 20.00),
    ('TEN', 10.00),
    ('FIVE', 5.00),
    ('TWO', 2.00),
    ('ONE', 1.00),
    ('HALF_DOLLAR', .50),
    ('QUARTER', .25),
    ('DIME',  .10),
    ('NICKEL', .05),
    ('PENNY', .01),
]

@dataclass
class Change:
    PENNY: int = 0
    NICKEL: int = 0
    DIME: int = 0
    QUARTER: int = 0
    HALF_DOLLER: int = 0
    ONE: int = 0
    TWO: int = 0
    FIVE: int = 0
    TEN: int = 0
    TWENTY: int = 0
    FIFTY: int = 0
    ONE_HUNDRED: int = 0

    def __str__(self) -> str:
        attrs: List[str] = [key for key in type(self).__dict__.keys() if not key.startswith("_")]
        # sort by alphabeticall order
        attrs.sort()
        result: str = ""
        for a in attrs:
            # get coin name from attribute name
            coin_name = a.replace("_", " ")
            for _ in range(getattr(self, a)):
                result += coin_name + ","
        # cut last comma that is added in above iterator
        return result[:-1]


def get_change(change: float) -> Change:
    """calculate change by greedy method"""
    result = Change()
    # make sure that COINS is sorted by value
    COINS.sort(key=lambda k: k[1], reverse=True)

    for c in COINS:
        num: int = int(change // c[1])
        change -= c[1] * num
        setattr(result, c[0], num)

    return result


def solve(PP: float, CH: float) -> str:
    if CH < PP:
        return "ERROR"
    elif CH == PP:
        return "ZERO"
    else:
        change = get_change(CH-PP)
        return str(change)

for line in sys.stdin:
    PP, CH = map(float, line.split(";"))
    ans = solve(PP, CH)
    print(ans, end="")
