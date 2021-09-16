using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace xCh11_2_11
{
    public class Student
    {
        public string Name { get; set; }
        public int ID { get; set; }
        public List<int> Scores;
    }

    class Program
    {
        public static List<Student> GetStudents()
        {
            List<Student> students = new List<Student>
            {
                new Student {Name="張無忌", ID=111, Scores= new List<int> {97, 72, 81, 60}},
                new Student {Name="令孤沖", ID=112, Scores= new List<int> {75, 84, 91, 39}},
                new Student {Name="洪七公", ID=113, Scores= new List<int> {99, 89, 91, 95}},
                new Student {Name="周芷若", ID=114, Scores= new List<int> {72, 81, 65, 84}},
                new Student {Name="黃藥師", ID=115, Scores= new List<int> {97, 89, 85, 82}} 
            };

            return students;
        }

        static void Main(string[] args)
        {
            // Step 01. 資料來源
            List<Student> students = GetStudents();

            // Step 02. 查詢運算式
            var booleanGroupQuery =
                from student in students
                group student by student.Scores.Average() >= 80;

            // Step 03. 執行查詢
            foreach (var studentGroup in booleanGroupQuery)
            {
                Console.WriteLine(studentGroup.Key == true ? "高分組" : "低分組");
                foreach (var student in studentGroup)
                {
                    Console.WriteLine("   {0}: {1}", student.Name, student.Scores.Average());
                }
            }
        }
    }
}


