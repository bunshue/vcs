using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;//匯入靜態類別

namespace CH0606
{
    class Square
    {
        //宣告欄位-space, 
        private float space;
        //公用屬性-保留存取子get，只能唯讀
        public float area
        {
            get { return space; }
        }
        //公用屬性-保留存取子set，只能唯寫
        public float length  //公用屬性
        {
            set { space = value * value; }
        }
    }
}
