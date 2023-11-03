using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;

namespace CH0810
{
    class Student : ISchool
    {
        private int course;
        private string sujname;
        private string msg;
        public bool IsMajor { get; set; }
        //實作介面屬性: Grade, Title
        public int Grade
        {
            get { return course; }
            set { course = value; }
        }
        public string Title
        {
            get { return sujname; }
            set { sujname = value; }
        }
        //建構函式，傳入學分數
        public Student(string name, int suj, bool major)
        {
            Title = name;
            Grade = suj;
            IsMajor = major;
            msg = (IsMajor == true) ? "必修" : "選修";
        }
        //實作介面的方法
        public void Display()
        {
            int accout = 1_470;   //每學分費用
            int total = Grade * accout;
            WriteLine($"{Title,-5} {msg,4}{total,10:c0}");
        }
    }
}
