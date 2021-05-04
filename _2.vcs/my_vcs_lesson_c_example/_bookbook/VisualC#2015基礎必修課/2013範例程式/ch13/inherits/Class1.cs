using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace inherits
{
    public class Empolyee      //定義Employee類別
    {
        public string Name;    //Name姓名欄位
        private int _Salary;   //_Salary薪水欄位
        public int Salary      //Salary薪水介於20000~40000之間
        {
            get
            {
                return _Salary;
            }
            set
            {
                if (value <= 20000) value = 20000;  //薪水最少20000
                if (value >= 40000) value = 40000;  //薪水最多40000
                _Salary = value;
            }
        }
    }
    //Manager經理類別繼承自Empolyee員工類別
    public class Manager : Empolyee
    {
        private int _Bonus;		 //加入_Bonus獎金欄位
        public int Bonus         //_Bonus獎金介於10000~50000之間
        {
            get
            {
                return _Bonus;
            }
            set
            {
                if (value <= 10000) value = 10000;  //獎金最少10000
                if (value >= 50000) value = 50000;  //獎金最多50000
                _Bonus = value;
            }
        }
        public string GetTotal()   	 //定義GetTotal()方法
        {
            return "經理姓名：" + Name +
                "\n實領薪水：" + Convert.ToString(Salary) +
                "\n實領獎金：" + Convert.ToString(Bonus) +
                "\n合計薪資：" + Convert.ToString(Bonus + Salary);
        }
    }
}
