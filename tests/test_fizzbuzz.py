import pytest
from apps.fizzbuzz import fizzbuzz

def test_fizzbuzz():
    result = fizzbuzz()
    assert len(result) == 100
    assert result[2] == "Fizz"   # 3の倍数
    assert result[4] == "Buzz"   # 5の倍数
    assert result[14] == "FizzBuzz"  # 15の倍数
    assert result[0] == "1"      # 1はどの倍数でもない
    assert result[98] == "Buzz"  # 100の倍数

if __name__ == "__main__":
    pytest.main()
