using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Collections;

namespace xCh11_7_1_11
{
    public class Student
    {
        public string Name { get; set; }
        public int ID { get; set; }
        public int[] Scores { get; set; }
    }

    class Program
    {
        static void Main(string[] args)
        {
            ArrayList arrList = new ArrayList();
            arrList.Add(
                new Student
                    {
                        Name="張無忌", ID=111, Scores = new int[] { 97, 72, 81, 60 }
                    }
            );
            arrList.Add(
                new Student
                    {
                       Name="令孤沖", ID=112, Scores = new int[] { 75, 84, 91, 39 }
                    }
            );
            arrList.Add(
                new Student
                    {
                        Name="洪七公", ID=113, Scores = new int[] { 99, 89, 91, 95 }
                    }
            );
            arrList.Add(
                new Student
                    {
                       Name="周芷若", ID=114, Scores = new int[] {72, 81, 65, 84 }
                    }
            );
           arrList.Add(
                new Student
                    {
                      Name="黃藥師", ID=115, Scores = new int[] {97, 89, 85, 82 }
                    }
            );

            var query = from Student student in arrList
                        where student.Scores[0] > 80
                        select student;

            foreach (Student s in query)
                Console.WriteLine(s.Name + ": " + s.Scores[0]);
        }
    }
}
