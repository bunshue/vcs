using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;

namespace CH0808
{
    class Employ
    {
        static void Main(string[] args)
        {
            //父類別Worker，子類別有Hireling, PartTime
            Worker unknown = new Worker();
            Hireling claire = new Hireling();
            PartTime michael = new PartTime();

            WriteLine("方法一：呼叫父類別的方法");

            //方法一：各物件呼叫Display()，只有只有正式員工算出月薪         
            unknown.Display();
            michael.Display();
            claire.Display(); //覆寫，算出月薪
            WriteLine("-----------------------------------");

            WriteLine("方法二：呼叫自己的方法，計算薪資");
            //直接存取本身所定義的方法，修飾詞用了new和override
            michael.TotalSalary();
            claire.TotalSalary();
            WriteLine("-----------------------------------");

            WriteLine("方法三：父類別為型別，子類別為值");
            DispalyHy();

            ReadKey();
        }

        /* 方法三：以父類別為型別，子類別為其值
           override 擴充基底類別方法   */
        public static void DispalyHy()
        {
            Worker unknown = new PartTime();
            Worker fullWork = new Hireling();
            //呼叫父類別的方法
            unknown.TotalSalary();
            fullWork.TotalSalary();//呼叫子類別的方法
        }
    }
}
