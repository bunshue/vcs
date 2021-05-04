using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace _66product
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        // 表單載入時執行
        private void Form1_Load(object sender, EventArgs e)
        {
            string str = "";
            for (int i = 1; i <= 6; i++)		// 被乘數
            {
                for (int j = 1; j <= 6; j++) 		// 乘數
                {   // 將 i x j = (i * j) 合併str後再指定給str
                    str += i + "x" + j + "=" + (i * j) + '\t'; 
                }
                str += '\n';   // 換行
            }
            MessageBox.Show(str);  //顯示結果
            Application.Exit(); // 結束程式
        }
    }
}
