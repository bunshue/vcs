using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for Metafile

namespace vcs_ReadWrite_EMF_WMF
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string filename1 = "C:\\______test_files1\\__RW\\_emf_wmf\\test.emf";
            string filename2 = "C:\\______test_files1\\__RW\\_emf_wmf\\Volleyball.wmf";

            Metafile mf1 = (Metafile)Metafile.FromFile(filename1);
            pictureBox1.Image = mf1;

            Metafile mf2 = (Metafile)Metafile.FromFile(filename2);
            pictureBox2.Image = mf2;
        }
    }
}
