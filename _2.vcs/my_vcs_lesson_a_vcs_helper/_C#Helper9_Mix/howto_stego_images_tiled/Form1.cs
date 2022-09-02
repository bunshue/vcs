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

        // Hide and then recover the image.
        private void btnGo_Click(object sender, EventArgs e)
        {
            Cursor = Cursors.WaitCursor;
            int num_bits = (int)nudHiddenBits.Value;

            // Hide the image3.
            Bitmap combined;
            combined = Stego.HideTiledImages(
                (Bitmap)picMainOriginal.Image,
                (Bitmap)picHiddenOriginal1.Image,
                (Bitmap)picHiddenOriginal2.Image,
                (Bitmap)picHiddenOriginal3.Image,
                (Bitmap)picHiddenOriginal4.Image,
                num_bits);
            picCombined.Image = combined;

            // Recover the hidden images.
            Bitmap hidden1, hidden2, hidden3, hidden4;
            Stego.RecoverTiledImages(combined, out hidden1,
                out hidden2, out hidden3, out hidden4, num_bits);
            picHiddenRecovered1.Image = hidden1;
            picHiddenRecovered2.Image = hidden2;
            picHiddenRecovered3.Image = hidden3;
            picHiddenRecovered4.Image = hidden4;

            Cursor = Cursors.Default;
        }
    }
}
