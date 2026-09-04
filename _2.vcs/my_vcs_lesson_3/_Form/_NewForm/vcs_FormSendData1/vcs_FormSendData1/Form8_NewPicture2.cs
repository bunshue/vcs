using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_FormSendData1
{
    public partial class Form8_NewPicture2 : Form
    {
        //public Form8_NewPicture2()  // 改
        public Form8_NewPicture2(Bitmap bitmap1)
        {
            InitializeComponent();
            int W = bitmap1.Width;
            int H = bitmap1.Height;
            pictureBox1.Image = bitmap1;
            pictureBox1.Size = new Size(W + 5, H + 5);
        }

        private void Form8_NewPicture2_Load(object sender, EventArgs e)
        {

        }
    }
}
