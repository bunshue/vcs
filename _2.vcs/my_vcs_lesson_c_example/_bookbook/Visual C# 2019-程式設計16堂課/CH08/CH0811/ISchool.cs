using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CH0811
{
    //介面1-與選修科目有關
    interface ISchool
    {
        //屬性-Course, Title
        int Course { get; set; }
        string Title { get; set; }
        void Display();   //方法
    }

    //介面2 - 與學生身分有關
    interface IStatus
    {
        ushort Grade { get; set; }   //屬性-學生身分
    }
}
