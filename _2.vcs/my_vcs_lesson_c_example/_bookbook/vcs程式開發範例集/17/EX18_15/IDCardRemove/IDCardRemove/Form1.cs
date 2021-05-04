using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;

namespace IDCardRemove
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            textBox2.Text = Shen(textBox1.Text);
        }
        public string Shen(string id)
        {
            int[] w = new int[] { 7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2, 1 };
            char[] a = new char[] { '1', '0', 'x', '9', '8', '7', '6', '5', '4', '3', '2' };
            string newID = "";
            if (id.Length == 15)
            {

                int s = 0;
                newID = id.Insert(6, "19");
                for (int i = 0; i < 17; i++)
                {
                    int k = Convert.ToInt32(newID[i]) * w[i];
                    s = s + k;
                }
                int h = 0;
                Math.DivRem(s, 11, out h);
                newID = newID + a[h];
            }
            return newID;
        }
    }
}