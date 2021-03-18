"""
File: student.py
Resources to manage a student's name and test scores.
"""

class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for i in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name
  
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self.scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)
 
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))


    def __eq__(self, student):
        """Returns the output of the equal comparison"""
        if self.name == student.name:
            return True
        else:
            return False
    
    def __lt__(self, student):
        """Returns the output of the less than comparison"""
        if self.name < student.name:
            return True
        else:
            return False
    
    def __ge__(self, student):
        """Returns the output of the greter than or equal to comparison"""
        if self.name >= student.name:
            return True
        else:
            return False

def main():
    """A simple test."""
    student1 = Student("Ken", 5)
    print(student1)
    for i in range(1, 6):
        student1.setScore(i, 100)
    print(student1)

    student2 = Student("Kat", 5)
    print(student2)
    for i in range(1, 6):
        student2.setScore(i, 80)
    print(student2)

    print("The scores of Ken and Kat are equal")
    print (student1.__eq__(student2))
    print("The scores of Ken is less than the scores of Kat")
    print (student1.__lt__(student2))
    print("The scores of Ken is greater than or equal to the scores of Kat")
    print (student1.__ge__(student2))

if __name__ == "__main__":
    main()
