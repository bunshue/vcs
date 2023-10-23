using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;//滙入靜態類別

namespace ExCompany
{
    public class Business
    {
        private string name;
        private string principal;
        private int number;

        public void GetInfo()
        {
            Write("請輸入公司名稱：");
            name = ReadLine();
            Write("請輸入負責人：");
            principal = ReadLine();
            Write("請輸入員工人數：");
            number = int.Parse(ReadLine());
        }

        public void DispInfo()
        {
            WriteLine("公司的名字為：" +name);
            WriteLine("公司的負責人為：" + principal);
            WriteLine("公司現有人數：" + number);
        }
    }


    public class Company : Business
    {
        private int Money;

        public void GetMoney()
        {
            GetInfo();
            Write("請輸入資本額(單位為萬):");
            Money = int.Parse(ReadLine());
        }

        public void Capital()
        {
            DispInfo();
            WriteLine("該公司的資本額:新台幣" + Money + "萬元");
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Company Fortune = new Company();
            Fortune.GetMoney();
            Fortune.Capital();
            ReadLine();
        }
    }
}