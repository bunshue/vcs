using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Reflection;
using System.IO;

namespace MyScreenSaver
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
            Assembly asm = this.GetType().Assembly;
            Stream stream = asm.GetManifestResourceStream("MyScreenSaver.Resources.BgrdImg.jpg");
            this.BackgroundImage = new Bitmap(stream);

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
