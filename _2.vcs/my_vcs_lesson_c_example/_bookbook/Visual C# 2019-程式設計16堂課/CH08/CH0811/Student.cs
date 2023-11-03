using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;

namespace CH0811
{
    class Student : ISchool, IStatus
    {
        private int subject;//學分數
        private string sujname;//科目名稱
        private ushort id; //學生身份
        private string msg;
        public bool IsMajor { get; set; }

        //實作介面屬性: Course, Title, Garde
        public int Course
        {
            get { return subject; }
            set { subject = value; }
        }

        public string Title
        {
            get { return sujname; }
            set { sujname = value; }
        }

        public ushort Grade
        {
            get { return id; }
            set { id = value; }
        }

        //建構函式，傳入4個參數
        public Student(ushort id, string name,
              int subject, bool major)
        {
            Grade = id;         //學生身分
            Title = name;       //科目名稱
            Course = subject;   //學分數
            IsMajor = major;    //選修？必修？
            msg = (IsMajor == true) ? "必修" : "選修";
        }
        //實作介面的方法
        public void Display()
        {
            //每學分費用
            int accout = 1_470, total = 0;
            int pay = 8_500;//研究生指導費

            //Grade = 1為一般生，Grade = 2為研究生
            if (Grade == 1)
                total = Course * accout;
            else if (Grade == 2)
                total = Course * accout + pay;

            WriteLine($"{Title,-5} {msg,4} {Course,4}" +
               $"{total,10:c0}");
        }
    }
}
