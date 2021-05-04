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
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();  // 內定的指令

            for (int i = 1000; i < 3000; i++) // 迴圈
            {
                if (i % 400 == 0) // 如果 i 可以被400整除
                    listBox1.Items.Add(i);
                else if (i % 4 == 0 && i % 100 != 0) // 如果 i 可以被4整除 而且 i 不能被100整除
                    listBox1.Items.Add(i);

                // 另一種更精簡的寫法
                //if ((i % 400 == 0) || (i % 4 == 0 && i % 100 != 0))
                //    listBox1.Items.Add(i);
            }

            label2.Text = label2.Text + Convert.ToString(listBox1.Items.Count);
        }
    }
}
