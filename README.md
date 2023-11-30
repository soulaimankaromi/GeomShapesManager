# GeomShapesManager
The Rectangle class represents rectangles with methods for dimensions, perimeter, surface area, and equality checks. The Parallelepipede subclass extends it for parallelepipeds, adding height, volume, and surface area calculations. Both classes track the number of instances created. The code demonstrates their usage with instances and operations.

Class: Rectangle
Description:
The Rectangle class represents a rectangle and includes methods to perform various operations on rectangles such as calculating perimeter, surface area, and checking equality.

Attributes:
__longueur: Private instance variable for the length of the rectangle.
__largeur: Private instance variable for the width of the rectangle.
_count: Class variable to keep track of the number of Rectangle objects created.
Methods:
__init__(self, longueur=0, largeur=0): Constructor to initialize the Rectangle object with length and width.
Getlongueur(self): Getter method for the length.
setlongueur(self, longueur): Setter method for the length.
Getlargeur(self): Getter method for the width.
setlargeur(self, largeur): Setter method for the width.
Getcount(self): Getter method for the count of Rectangle objects.
Equals(self, Rec1): Check if the current Rectangle object is equal to another Rectangle object.
Perimetre(self): Calculate and return the perimeter of the rectangle.
Surface(self): Calculate and return the surface area of the rectangle.
ToString(self): Return a string representation of the Rectangle object.
Class: Parallelepipede (Inherits from Rectangle)
Description:
The Parallelepipede class is a subclass of the Rectangle class, representing a parallelepiped. It extends the functionality of Rectangle by adding methods to calculate volume and surface area for a parallelepiped.

Additional Attributes:
__hauter: Private instance variable for the height of the parallelepiped.
_count1: Class variable to keep track of the number of Parallelepipede objects created.
Additional Methods:
__init__(self, longueur=0, largeur=0, hauter=0): Constructor to initialize the Parallelepipede object with length, width, and height.
Gethauter(self): Getter method for the height.
sethauter(self, hauter): Setter method for the height.
Getcount1(self): Getter method for the count of Parallelepipede objects.
Equals(self, par): Check if the current Parallelepipede object is equal to another Parallelepipede object.
Surface(self): Calculate and return the surface area of the parallelepiped (overrides the method in the base class).
Volume(self): Calculate and return the volume of the parallelepiped.
ToString(self): Return a string representation of the Parallelepipede object.
Example Usage:
The provided code demonstrates the usage of these classes by creating instances of Rectangle and Parallelepipede and performing operations on them.
