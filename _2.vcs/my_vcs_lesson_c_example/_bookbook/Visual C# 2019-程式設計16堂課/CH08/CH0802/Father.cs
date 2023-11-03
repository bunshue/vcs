using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CH0802
{
    class Father
    {
        protected string Hair { get; set; }
        //姓氏唯讀，只有return回傳其值
        protected string Surname
        { get { return "Bacon"; } }
    }
}
