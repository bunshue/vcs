using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh4_1_2_31
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            try
            {
                // 將使用者輸入的數字轉換成double型別
                if (double.Parse(textBox1.Text) < 0)
                {
                    // 如果輸入的數值小於0的話，用紅色粗體15點的大小呈現
                    textBox1.ForeColor = Color.Red;
                    textBox1.Font = new Font(FontFamily.GenericSansSerif, 13.0F, FontStyle.Bold);
                }
                else
                {
                    // 如果輸入的數值大於0的話，用黑色斜體12點的大小呈現
                    textBox1.ForeColor = Color.Black;
                    textBox1.Font = new Font(FontFamily.GenericSansSerif, 13.0F, FontStyle.Italic);
                }
            }
            catch
            {
                // 如果發生錯誤的話，就使用系統色及10點大小的刪除線加底線樣式呈現
                textBox1.ForeColor = SystemColors.ControlText;
                textBox1.Font = new Font(FontFamily.GenericSansSerif, 13.0F,
                    FontStyle.Strikeout|FontStyle.Underline);
            }
        }
    }
}
