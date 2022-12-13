class Square:
    def __init__(self, square_side:float):
        """
        is_valid() -> bool
        area() -> float
        perimeter() -> float
        """
        self.s=square_side

    def is_valid(self) -> bool:
        """
        This method checks if the circle is valid.

        Args:
            No
        Returns:
            bool: This method checks if the square is valid.
        """
        return self.s>0

    def area(self):
        
        """
        This method finds the area of the square.

        Args:
            No
        Returns:
            float or int: return area of the square if the square is valid, 0 otherwise
        """
        if Square.is_valid():
            return self.s**2
        else:
            return 0

    def perimeter(self):

        """
        This method finds the perimeter of the square.

        Args:
            No
        Returns:
            float: return perimeter of the square if the square is valid, 0 otherwise
        """
        if Square.is_valid():
            return 4*self.s
        else:
            return 0
