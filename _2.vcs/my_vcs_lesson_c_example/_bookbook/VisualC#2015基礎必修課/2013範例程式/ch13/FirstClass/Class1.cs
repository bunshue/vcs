using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
//引用System.Windows.Forms命名空間
//在此檔才能使用MessageBox.Show()方法
using System.Windows.Forms;

namespace FirstClass
{
    public class Student           // 定義Student類別
    {
        public string Name;        // Name姓名欄位
        public int Score;          // Score成績欄位
        public void ShowMsg()      // ShowMsg顯示姓名與成績的方法
        {
            MessageBox.Show(Name + "同學的分數是 " + Convert.ToString(Score));
        }
    }
}
