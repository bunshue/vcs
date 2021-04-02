using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Runtime.InteropServices;

namespace InspeckWhetherBuildinClamour
{
    public partial class Form1 : Form
    {
        [DllImport("winmm.dll", EntryPoint = "waveOutGetNumDevs")]
        public static extern int waveOutGetNumDevs();
        public Form1()
        {
            InitializeComponent();
        }
       
        private void Form1_Load(object sender, EventArgs e)
        {
            if (waveOutGetNumDevs() != 0)
            { this.radioButton1.Select(); }
            else
            { this.radioButton2.Select(); }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}