using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleConstructor2
{
    class Student
    {
        private int _Height, _Weight;
        //public Student()
        //{
        //    _Weight = 48;
        //    _Height = 160;
        // }
        // Student類別的建構式，須設定一個引數
        public Student(int w)
        {
            _Weight = w;  		// 初始化_Weight欄位
            _Height = 160;	      	// 初始化_Height欄位的值為160
        }
        // Student類別的建構式，須設定兩個引數
        public Student(int w, int h)
        {
            _Weight = w;
            _Height = h;
        }
        // Student類別的GetShow()方法，可顯示學生的身高和體重
        public void GetShow()
        {
            Console.WriteLine(" 身高是: {0} ", _Height);
            Console.WriteLine(" 體重是: {0} \n", _Weight);
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Student Peter = new Student();
            Console.WriteLine(" Peter的資料-->使用Student()建構式");
            Peter.GetShow();
            Student David = new Student(56);
            Console.WriteLine(" David的資料-->使用Student(56)建構式");
            David.GetShow();
            Student Mary = new Student(48, 150);
            Console.WriteLine(" Mary的資料 -->使用Student(48, 150)建構式");
            Mary.GetShow();
            Console.Read();

        }
    }
}
