class Employee:
    """Collect information about an employee."""
    
    def __init__(self, first, last, annual_salary):
        """Store first and last name and annual salary."""
        self.first = first
        self.last = last
        self.annual_salary = annual_salary
    
    def give_raise(self, raise_amount=5000):
        """Adds $5,000 to the annual salary by default but also accepts a different raise amount."""
        self.annual_salary += raise_amount
