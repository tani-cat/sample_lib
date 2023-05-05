def xor(*data: int) -> int:
    """Exclusive OR calculation"""
    ans: int = 0
    for _d in data:
        ans ^= _d

    return ans
