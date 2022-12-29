from student1 import student1
import unittest
class test_student(unittest.TestCase):
    def test_email(self):

        s1=student1("banda","pavithra",50)
        self.assertEqual(s1.email,"banda.pavithra@gmail.com")

    def test_fullname(self):
       # print("test_fullname")
        s1=student1("banda","pavithra",50)
        self.assertEqual(s1.fullname,"banda.pavithra")
    def test_apply_bonus(self):
        #print("test_apply_bonus")
        s1 = student1("banda", "pavithra", 50)
        self.assertEqual(s1.marks,50,50)
        s1.apply_bonus()
        self.assertEqual(s1.marks,75,75)

    def test_something(self):
        s1=student1("banda","pavithra",30)
        self.assertEqual(s1.somevalue,"")
        s1.something("rupa")
        self.assertEqual(s1.somevalue,"banda.pavithra@gmail.combanda.pavithrarupa")





if __name__ == "__main__":

    #unittest.main()
    unittest.main(verbosity=2)








