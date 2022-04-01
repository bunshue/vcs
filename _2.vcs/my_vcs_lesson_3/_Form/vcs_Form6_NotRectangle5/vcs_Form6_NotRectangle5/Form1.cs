using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D; //for GraphicsPath

namespace vcs_Form6_NotRectangle5
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //Region的用法
            GraphicsPath gp = new GraphicsPath();
            gp.AddEllipse(60, 80, 400, 300);
            Region r = new Region(gp);
            this.Region = r; 

        }

        private void button1_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
