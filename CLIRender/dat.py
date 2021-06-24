# contains:
#
#    x position (generic typing because python but should be an int in most cases)
#    y position (the same)
#
class Vector2:  # to be honest this is me showing off
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):  # returns a formatted string for the vector2
        return "({v.x}, {v.y})".format(v=self)

    def __add__(self, other):  # allows adding of vector2s, and ints
        if isinstance(other, Vector2):
            return Vector2(self.x + other.x, self.y + other.y)
        elif isinstance(other, (int, float)):
            return Vector2(self.x + other, self.y + other)
        else:
            raise ValueError("Accepted data types are float, int and Vector2.")

    def __mul__(self, other):  # multiplies a vector2 by an int, or by another vector2
        if isinstance(other, Vector2):
            return Vector2(self.x * other.x, self.y * other.y)
        elif isinstance(other, (int, float)):
            return Vector2(self.x * other, self.y * other)
        else:
            raise ValueError("Accepted data types are float, int and Vector2.")

    def __truediv__(self, other):  # returns a FLOAT value (true div)
        if isinstance(other, Vector2):
            return Vector2(self.x / other.x, self.y / other.y)
        elif isinstance(other, (int, float)):
            return Vector2(self.x / other, self.y / other)
        else:
            raise ValueError("Accepted data types are float, int and Vector2.")

    def __floordiv__(self, other):  # returns an INT value (floor div)
        if isinstance(other, Vector2):
            return Vector2(self.x // other.x, self.y // other.y)
        elif isinstance(other, (int, float)):
            return Vector2(self.x // other, self.y // other)
        else:
            raise ValueError("Accepted data types are float, int and Vector2.")

    def __pos__(self):
        return Vector2(abs(self.x), abs(self.y))

    def __neg__(self):
        return Vector2(-self.x, -self.y)
        
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def Magnitude(self):  # returns the magnitude of the vector2. (length of the vector)
        return ((self.x ** 2) + (self.y ** 2)) ** (1/2) #sqrt


class Vector3:  # to be honest this is me showing off
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):  # returns a formatted string for the Vector3
        return "({v.x}, {v.y}, {v.z})".format(v=self)

    def __add__(self, other):  # allows adding of Vector3s, and ints
        if isinstance(other, Vector3):
            return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
        elif isinstance(other, (int, float)):
            return Vector3(self.x + other, self.y + other, self.z + other)
        else:
            raise ValueError("Accepted data types are float, int and Vector3.")

    def __mul__(self, other):  # multiplies a Vector3 by an int, or by another Vector3
        if isinstance(other, Vector3):
            return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)
        elif isinstance(other, (int, float)):
            return Vector3(self.x * other, self.y * other, self.z * other)
        else:
            raise ValueError("Accepted data types are float, int and Vector3.")

    def __truediv__(self, other):  # returns a FLOAT value (true div)
        if isinstance(other, Vector3):
            return Vector3(self.x / other.x, self.y / other.y, self.z / other.z)
        elif isinstance(other, (int, float)):
            return Vector3(self.x / other, self.y / other, self.z / other)
        else:
            raise ValueError("Accepted data types are float, int and Vector3.")

    def __floordiv__(self, other):  # returns an INT value (floor div)
        if isinstance(other, Vector3):
            return Vector3(self.x // other.x, self.y // other.y, self.z // other.z)
        elif isinstance(other, (int, float)):
            return Vector3(self.x // other, self.y // other, self.z // other)
        else:
            raise ValueError("Accepted data types are float, int and Vector3.")

    def __pos__(self):
        return Vector3(abs(self.x), abs(self.y), abs(self.z))

    def __neg__(self):
        return Vector3(-self.x, -self.y, -self.z)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def Magnitude(self):  # returns the magnitude of the Vector3. (length of the vector)
        return ((self.x ** 2) + (self.y ** 2) + (self.z ** 2)) ** (1 / 2)  # sqrt
