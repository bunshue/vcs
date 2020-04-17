using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class digitsystem : Form
    {
        public digitsystem()
        {
            InitializeComponent();
        }

        private void btnConvert_Click(object sender, EventArgs e)
        {
            /* ----------------------------------*
             * 第7章: 使用switch來處理數字的對應 *
             *-----------------------------------*/
           /*
            int a, n, r;
            string s = "";

            a = Convert.ToInt32(txtNum.Text);

            if (rdb2.Checked) n = 2;
            else if (rdb8.Checked) n = 8;
            else n = 16;

            for ( ; a > 0; a = a / n) {

                r = a % n; // 取得餘數
                
                switch (r) // 處理16進位
                {
                    case 10: s = "A" + s; break; // 對應後再串到左邊
                    case 11: s = "B" + s; break;
                    case 12: s = "C" + s; break;
                    case 13: s = "D" + s; break;
                    case 14: s = "E" + s; break;
                    case 15: s = "F" + s; break;
                    default: s = r + s; break;  // 0-9直接串到左邊
                }
                
                // s = r + s; ; // 串到左邊
            }

            lblResult.Text = s;
            */

            /* --------------------------------*
             * 第8章: 使用陣列來處理數字的對應 *
             *---------------------------------*/
            
            int a, n, r;
            string[] m = {"0", "1", "2", "3",
                           "4", "5", "6", "7",
                           "8", "9", "A", "B",
                           "C", "D", "E", "F"};
            string s = "";

            a = Convert.ToInt32(txtNum.Text);

            if (rdb2.Checked) n = 2;
            else if (rdb8.Checked) n = 8;
            else n = 16;

            for ( ; a > 0; a = a / n)
            {
                r = a % n;  //取得餘數

                s = m[r] + s; // 查表，串列左邊

            }

            lblResult.Text = s;
           
        }
         
        
    }
}
