using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace vcs_Console_2_sort
{
    public class Student
    {
        public string Name;
        public int Score;
        public Student(string name, int score)
        {
            this.Name = name;
            this.Score = score;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            List<Student> students = new List<Student>(){ new Student("Student A", 90),
                                                          new Student("Student B", 75),
                                                          new Student("Student C", 83),
                                                          new Student("Student D", 94),
                                                          new Student("Student E", 60),
                                                          new Student("Student F", 56),
                                                          new Student("Student G", 30),
                                                          new Student("Student I", 73),
                                                          new Student("Student J", 68),
                                                          new Student("Student K", 46)};
            foreach (var stu in students)
                Console.WriteLine("Name: {0}, Score: {1} ", stu.Name, stu.Score);



            students.Sort((x, y) => { return -x.Score.CompareTo(y.Score); });

            Console.WriteLine("\nAfter sorting\n");

            foreach (var stu in students)
                Console.WriteLine("Name: {0}, Score: {1} ", stu.Name, stu.Score);

            Console.ReadKey();
        }

    }
}
