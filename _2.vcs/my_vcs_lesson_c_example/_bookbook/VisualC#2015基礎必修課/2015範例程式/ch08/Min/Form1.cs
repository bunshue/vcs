using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Min
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        //取兩個整數的最小數
        private int Min(int x, int y)
        {
            if (x < y)
                return x;
            else
                return y;
        }
        //取三個整數的最小數
        private int Min(int x, int y, int z)
        {
            if (x < y)
            {
                if (x < z)
                    return x;
                else
                    return z;
            }
            else
            {
                if (y < z)
                    return y;
                else
                    return z;
            }
        }
        //取整數陣列中的最小數
        private int Min(int[] x)
        {
            int s = x[0];//最小值
            foreach (int y in x)
            {
                if (y < s)
                    s = y;
            }
            return s;
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            MessageBox.Show(Min(5, 9).ToString(), "最小值");
            MessageBox.Show(Min(5, 9, 2).ToString(), "最小值");
            int[] num = new int[] { 5, 9, 2, 1, 7 };
            MessageBox.Show(Min(num).ToString(), "最小值");
            Application.Exit();
        }
    }
}
