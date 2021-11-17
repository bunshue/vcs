using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace vcs_Form6_NotRectangle2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            GraphicsPath gp = new GraphicsPath();
            Rectangle rect = new Rectangle(new Point(0, 0), new Size(this.Width, this.Height));
            gp.AddEllipse(rect);
            this.Region = new Region(gp);
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

    }
}
