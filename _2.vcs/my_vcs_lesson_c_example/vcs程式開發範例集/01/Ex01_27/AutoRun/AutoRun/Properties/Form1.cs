using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.IO;
namespace AutoRun
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            StreamWriter sw = new StreamWriter("AutoRun.inf",false);
            sw.WriteLine("[autorun]");
            sw.WriteLine("OPEN=AUTORUN.EXE");
            sw.WriteLine("ICON=run.ICO");
            sw.Close();
        }
    }
}