import pytest
from src.utils import get_depersonalized_operations, print_operations


def test_utils():
    assert len(get_depersonalized_operations(operations_cnt=0)) == 0
    assert len(get_depersonalized_operations()) <= 5
    assert len(get_depersonalized_operations(operations_cnt=3)) <= 3


