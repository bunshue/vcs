using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CH0604
{
    class Circle
    {
        private double ra;
        private double pi = Math.PI;
        private double area;
        //以屬性存取私有欄位-半徑ra

        public double Radius
        {
            get => ra;   //運算式主體
            set
            {
                ra = value;   //運算式主體
                              //取得半徑計算面積
                area = pi * ra * ra;
            }
        }

        //以屬性存取私有欄位-面積area
        public double Space
        {
            get => area;
            set
            {
                area = value;
                //呼叫Math類別的Sqrt()來取得平方根
                ra = Math.Sqrt(area / pi);
            }
        }
    }
}