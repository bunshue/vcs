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

        private void addButton_Click(object sender, EventArgs e)
        {
            resultVal.Text = (int.Parse(Val1.Text) + int.Parse(Val2.Text)).ToString();
        }

        private void minButton_Click(object sender, EventArgs e)
        {
            resultVal.Text = (int.Parse(Val1.Text) - int.Parse(Val2.Text)).ToString();
        }

        private void mulButton_Click(object sender, EventArgs e)
        {
            resultVal.Text = (int.Parse(Val1.Text) * int.Parse(Val2.Text)).ToString();
        }

        private void divButton_Click(object sender, EventArgs e)
        {
            resultVal.Text = (int.Parse(Val1.Text) / int.Parse(Val2.Text)).ToString();
        }

        private void eqlButton_Click(object sender, EventArgs e)
        {
            resultVal.Text = int.Parse(Val1.Text) == int.Parse(Val2.Text) ? "是" : "否";
        }

        private void noteqlButton_Click(object sender, EventArgs e)
        {
            resultVal.Text = int.Parse(Val1.Text) != int.Parse(Val2.Text) ? "是" : "否";
        }

        private void biggerButton_Click(object sender, EventArgs e)
        {
            resultVal.Text = int.Parse(Val1.Text) > int.Parse(Val2.Text) ? "是" : "否";
        }

        private void smallerButton_Click(object sender, EventArgs e)
        {
            resultVal.Text = int.Parse(Val1.Text) < int.Parse(Val2.Text) ? "是" : "否";
        }
    }
}
