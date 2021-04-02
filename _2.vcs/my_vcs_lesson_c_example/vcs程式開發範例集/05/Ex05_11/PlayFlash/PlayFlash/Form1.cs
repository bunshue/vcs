using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace PlayFlash
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            
        }

        private void button1_Click(object sender, EventArgs e)
        {
            try
            {
                openFileDialog1.Filter = "Flash文件(*.swf)|*.swf|所有文件(*.*)|*.*";
                if (openFileDialog1.ShowDialog() == DialogResult.OK)
                {
                    string MyFileName = openFileDialog1.FileName;
                    this.axShockwaveFlash1.Movie = MyFileName;
                }
            }
            catch (Exception ey)
            {
                MessageBox.Show(ey.Message);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
          this.axShockwaveFlash1.Stop();
        }

        private void button3_Click(object sender, EventArgs e)
        {
          this.axShockwaveFlash1.Rewind();
        }

        private void button4_Click(object sender, EventArgs e)
        {
          this.axShockwaveFlash1.Back();   
        }

        private void button5_Click(object sender, EventArgs e)
        {
          this.axShockwaveFlash1.Forward();
        }

        private void button6_Click(object sender, EventArgs e)
        {
            this.axShockwaveFlash1.Rewind();
            this.axShockwaveFlash1.Play();
        }
        private void button7_Click(object sender, EventArgs e)
        {
          
            Application.Exit();
        }
    }
}