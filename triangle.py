from math import sqrt

class Triangle:
    def __init__(self, a:float, b:float, c:float):
        self.a = a
        self.b = b
        self.c = c

    def is_valid(self) -> bool:
        '''
        This method checks if the triangle is valid.
        
        Args: 
            No
        Returns:
            bool: True if the triangle is valid, False otherwise
        '''
        a=self.a
        b=self.b
        c=self.c

        return a+b>c and a+c>b and b+c>a and a>0 and b>0 and c>0

    
    def get_type(self) -> str:
        '''
        This method finds the type of the triangle.
        ''' 
        a=self.a
        b=self.b
        c=self.c
        if not Triangle.is_valid:
            if a==b and b==c:
                return "Teng tomonli uchburchak"

            if (a==b and a!=c) or (b==c and b!=a) or (a==c and a!=b):
                return "Teng yonli uchburchak"
            
            else:
                return "Oddiy uchburchak"
        else:
            return 0


    def perimeter(self):
    
        '''
        This method finds the perimeter of the triangle.

        Args:
            No
        Returns:
            int or float: return perimeter of the triangle if the triangle is valid, 0 otherwise
        '''
        if not Triangle.is_valid:
            return self.a+self.b+self.c
        else:
            return 0


    def area(self):
        '''
        This method finds the area of the triangle.

        Args:
            NO
        Returns:
            int or float: return area of the triangle if the triangle is valid, 0 otherwise
        '''
        
        
        if not Triangle.is_valid:
            a=self.a
            b=self.b
            c=self.c
            p=(a+b+c)/2
            return sqrt(p*(p-a)*(p-b)*(p-c))
        else:
            return 0
        
y=Triangle(1,2,5)
print(y.area())