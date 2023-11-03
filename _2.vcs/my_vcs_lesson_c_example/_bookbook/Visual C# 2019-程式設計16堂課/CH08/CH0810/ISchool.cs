using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CH0810
{
    interface ISchool
    {
        //屬性
        int Grade { get; set; }
        string Title { get; set; }
        void Display();   //方法
    }
}
