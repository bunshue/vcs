using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Wallpaper2
{
    public partial class FrmMyScr : Form
    {
        public FrmMyScr()
        {
            InitializeComponent();

            this.DoubleBuffered = true;//设置本窗体

            SetStyle(ControlStyles.UserPaint, true);
            SetStyle(ControlStyles.AllPaintingInWmPaint, true);
            SetStyle(ControlStyles.DoubleBuffer, true);
        }

        Timer NowTime = new Timer();

        private void FrmMyScr_Load(object sender, EventArgs e)
        {
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__pic\_scenery\ggb1.jpg";
            this.BackgroundImage = new Bitmap(filename);

            this.Click += new System.EventHandler(Exit);
            this.BackColor = System.Drawing.Color.White;
            this.lblTimeNow.Location = new System.Drawing.Point((this.Size.Width / 10), this.Size.Height / 5 * 4);

            NowTime.Interval = 10;
            this.NowTime.Tick += new System.EventHandler(LableTimeText);
            NowTime.Start();
        }

        private void Exit(object sender, EventArgs e)
        {
            Application.Exit();
        }
        private void LableTimeText(object sender, EventArgs e)
        {
            lblTimeNow.Text = DateTime.Now.ToString();
        }

        private void FrmMyScr_Deactivate(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
