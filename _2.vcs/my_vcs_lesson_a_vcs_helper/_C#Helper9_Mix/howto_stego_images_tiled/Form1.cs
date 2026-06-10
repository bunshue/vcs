using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace howto_stego_images_tiled
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        // Hide and then recover the image.
        private void btnGo_Click(object sender, EventArgs e)
        {
            Cursor = Cursors.WaitCursor;
            int num_bits = (int)nudHiddenBits.Value;

            // Hide the image3.
            Bitmap combined;
            combined = Stego.HideTiledImages((Bitmap)picMainOriginal.Image, (Bitmap)picHiddenOriginal1.Image, (Bitmap)picHiddenOriginal2.Image, (Bitmap)picHiddenOriginal3.Image, (Bitmap)picHiddenOriginal4.Image, num_bits);
            picCombined.Image = combined;

            // Recover the hidden images.
            Bitmap hidden1, hidden2, hidden3, hidden4;
            Stego.RecoverTiledImages(combined, out hidden1, out hidden2, out hidden3, out hidden4, num_bits);
            picHiddenRecovered1.Image = hidden1;
            picHiddenRecovered2.Image = hidden2;
            picHiddenRecovered3.Image = hidden3;
            picHiddenRecovered4.Image = hidden4;

            Cursor = Cursors.Default;
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

/*  可搬出

*/

