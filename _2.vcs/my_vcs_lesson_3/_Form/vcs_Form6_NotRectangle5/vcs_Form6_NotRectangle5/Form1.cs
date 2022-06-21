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
            //不規則表單 Region
            //通過設置窗體的Region屬性，製作不規則窗體。

            GraphicsPath gp = new GraphicsPath();
            Rectangle rect = new Rectangle(0, 0, 600, 400);
            gp.AddEllipse(rect);
            Region r = new Region(gp);
            this.Region = r;
            //this.Region = new Region(gp); same

            bt_exit.Location = new Point(200, 200);
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
