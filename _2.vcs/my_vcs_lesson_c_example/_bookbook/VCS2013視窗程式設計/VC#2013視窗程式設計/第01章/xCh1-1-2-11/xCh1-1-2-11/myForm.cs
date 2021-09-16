using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh1_1_2_11
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnLoad_Click(object sender, EventArgs e)
        {
            fileDialog.Title = "開啟影像檔";
            fileDialog.Filter = "jpg (*.jpg)|*.jpg|All files (*.*)|*.*";

            if (fileDialog.ShowDialog() == DialogResult.OK)
            {
                picboxImage.Image = new Bitmap(fileDialog.OpenFile());
                lblFileName.Text = fileDialog.FileName;
            }
            picboxImage.Anchor = AnchorStyles.Left | AnchorStyles.Top |
AnchorStyles.Right | AnchorStyles.Bottom;
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}
