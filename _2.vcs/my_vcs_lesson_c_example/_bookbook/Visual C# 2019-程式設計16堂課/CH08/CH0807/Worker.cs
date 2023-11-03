using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CH0807
{
    class Worker : Person   //子類別
    {
        public string Job { get; set; }
        public int Subsidy { get; set; }

        //以base()取得父類別的建構函式
        public Worker(string title) : base(title)
        {
            Job = title;
        }

        //覆寫父類別的同名方法，設定職務加給
        public override int Display(int grade)
        {
            if (grade == 1)
                Subsidy = 500;
            else if (grade == 2)
                Subsidy = 800;
            else
                Subsidy = 1_200;
            return Subsidy;
        }
    }
}
