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
            InitializeComponent();
        }

        private void computeButton_Click(object sender, EventArgs e)
        {
            int a = Convert.ToInt32(xSquare.Text);
            int b = Convert.ToInt32(x.Text);
            int c = Convert.ToInt32(constant.Text);
            double key = Math.Pow(b, 2) - (4*a*c);

            if (key < 0) {
                result.Text = "此一元二次方程式有兩虛根，無實數解。";
            }
            else if (key > 0) {
                double sol1 = (-b + Math.Sqrt(key)) / (2 * a);
                double sol2 = (-b - Math.Sqrt(key)) / (2 * a);
                result.Text = "此一元二次方程式有兩實根。 " + sol1 + " 與 " + sol2;
            }
            else{
                double sol = -b / (2 * a);
                result.Text = "此一元二次方程式有兩等根。 " + sol;
            }

        }

    }
}
