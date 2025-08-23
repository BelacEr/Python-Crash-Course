import pytest
from employee import Employee

@pytest.fixture
def sample_employee():
    """Create a sample employee for testing."""
    return Employee("Monika", "Asano", 60000)

def test_give_default_raise(sample_employee):
    sample_employee.give_raise()
    assert sample_employee.annual_salary == 65000

def test_give_custom_raise(sample_employee):
    sample_employee.give_raise(10000)
    assert sample_employee.annual_salary == 70000
