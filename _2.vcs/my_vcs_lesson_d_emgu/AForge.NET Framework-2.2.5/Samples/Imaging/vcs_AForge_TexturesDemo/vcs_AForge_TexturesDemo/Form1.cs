using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using AForge.Imaging;
using AForge.Imaging.Textures;

namespace vcs_AForge_TexturesDemo
{
    public partial class Form1 : Form
    {
        ITextureGenerator textureGenerator = null;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            textureGenerator = new CloudsTexture();
            ShowTexture();
        }

        private void rb_texture_CheckedChanged(object sender, EventArgs e)
        {
            if (rb1.Checked == true)
            {
                richTextBox1.Text += "Clouds\n";
                textureGenerator = new CloudsTexture();

            }
            else if (rb2.Checked == true)
            {
                richTextBox1.Text += "Marble\n";
                textureGenerator = new MarbleTexture();

            }
            else if (rb3.Checked == true)
            {
                richTextBox1.Text += "Wood\n";
                textureGenerator = new WoodTexture(7);

            }
            else if (rb4.Checked == true)
            {
                richTextBox1.Text += "Labyrinth\n";
                textureGenerator = new LabyrinthTexture();

            }
            else if (rb5.Checked == true)
            {
                richTextBox1.Text += "Textile\n";
                textureGenerator = new TextileTexture();

            }
            else
            {
                richTextBox1.Text += "Clouds\n";
                //textureGenerator = null;
                textureGenerator = new CloudsTexture();
            }

            ShowTexture();
        }

        // Generate and show texture
        private void ShowTexture()
        {
            // check generator
            if (textureGenerator == null)
            {
                pictureBox1.Image = null;
                return;
            }

            int width = pictureBox1.ClientRectangle.Width;
            int height = pictureBox1.ClientRectangle.Height;

            // generate texture
            float[,] texture = textureGenerator.Generate(width, height);

            // create bitmap from the texture
            Bitmap image = TextureTools.ToBitmap(texture);

            // show image
            pictureBox1.Image = image;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (textureGenerator != null)
            {
                textureGenerator.Reset();
                ShowTexture();
            }
        }
    }
}

