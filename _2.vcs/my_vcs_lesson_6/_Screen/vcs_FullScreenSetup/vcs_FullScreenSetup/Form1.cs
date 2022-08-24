using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_FullScreenSetup
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //全屏空白表單
            this.BackColor = Color.Black;
            //this.Size = new Size(800, 600);
            ControlBox = false;
            MaximizeBox = false;
            MinimizeBox = false;
            ShowIcon = false;
            ShowInTaskbar = false;
            FormBorderStyle = FormBorderStyle.None;
            StartPosition = FormStartPosition.CenterScreen;
            WindowState = FormWindowState.Maximized;
            TopMost = true;
            KeyPreview = true;

            this.DoubleClick += new EventHandler(Form1_DoubleClick);
        }

        void Form1_DoubleClick(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
