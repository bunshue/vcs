using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Property
{
    public class Student           //定義Student類別
    {
        public string Name;        //Name姓名欄位宣告為public
        private int _Score;        // _Score成績欄位宣告為private
        public int Score           //建立Score屬性，此屬性限制在0-100
        {
            get
            {
                return _Score;
            }
            set
            {
                if (value >= 100) value = 100;
                if (value <= 0) value = 0;
                _Score = value;
            }
        }
        public void ShowMsg()      //ShowMsg顯示姓名與成績的方法
        {
            MessageBox.Show(Name + "同學的分數是 " + Convert.ToString(Score));
        }
    }
}
