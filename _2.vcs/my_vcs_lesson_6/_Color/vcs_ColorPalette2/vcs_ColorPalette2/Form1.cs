using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

/*

記住目前的設定值，下次程式開啟時，可以拿來用。

方案總管/Properties/Settings settings/
加入：
名稱 Argbs
型別 System.Int32[]
範圍 User

目前找不到設定型態的位置，只好到Settings settings檔案改成以下：
<Setting Name="Argbs" Type="System.Int32[]" Scope="User">

*/

namespace vcs_ColorPalette2
{
    public partial class Form1 : Form
    {
        // The size used for each color patch.
        const int PatchWidth = 50, PatchHeight = 50;
        const int PatchMargin = 2;
        const int NumRows = 6, NumCols = 8;

        public Form1()
        {
            InitializeComponent();
        }

        // Initialize the colors.
        private void Form1_Load(object sender, EventArgs e)
        {
            // Make the PictureBox the right size.
            pictureBox1.ClientSize =
                new Size(
                    NumCols * PatchWidth + (NumCols - 1) * PatchMargin,
                    NumRows * PatchHeight + (NumRows - 1) * PatchMargin);
            //pictureBox1.Left = ClientSize.Width - pictureBox1.Width - pictureBox1.Top;
            pictureBox1.Location = new Point(50, 50);

            // Load the saved colors.
            LoadColors();
        }

        // Load the colors.
        private void LoadColors()
        {
            //richTextBox1.Text += "111 = " + Properties.Settings.Default.Argbs.ToString() + "\n";
            //richTextBox1.Text += "len = " + Properties.Settings.Default.Argbs.Length.ToString() + "\n";
            if ((Properties.Settings.Default.Argbs == null) || (Properties.Settings.Default.Argbs.Length == 0))
            {
                // Use default colors.
                Properties.Settings.Default.Argbs = DefaultColors();
            }
        }

        // Set some default colors.
        private int[] DefaultColors()
        {
            richTextBox1.Text += "DefaultColors()\n";
            Color[] colors =
            {
                Color.White,
                Color.FromArgb(255, 255, 192, 192),
                Color.FromArgb(255, 255, 224, 192),
                Color.FromArgb(255, 255, 255, 192),
                Color.FromArgb(255, 192, 255, 192),
                Color.FromArgb(255, 192, 255, 255),
                Color.FromArgb(255, 192, 192, 255),
                Color.FromArgb(255, 255, 192, 255),

                Color.FromArgb(255, 224, 224, 224),
                Color.FromArgb(255, 255, 128, 128),
                Color.FromArgb(255, 255, 192, 128),
                Color.FromArgb(255, 255, 255, 128),
                Color.FromArgb(255, 128, 255, 128),
                Color.FromArgb(255, 128, 255, 255),
                Color.FromArgb(255, 128, 128, 255),
                Color.FromArgb(255, 255, 128, 255),

                Color.FromArgb(255, 192, 192, 192),
                Color.Red,
                Color.FromArgb(255, 255, 128, 0),
                Color.Yellow,
                Color.FromArgb(255, 0, 192, 0),
                Color.Cyan,
                Color.Blue,
                Color.FromArgb(255, 255, 0, 255),

                Color.Gray,
                Color.FromArgb(255, 192, 0, 0),
                Color.FromArgb(255, 192, 64, 0),
                Color.FromArgb(255, 192, 192, 0),
                Color.Green,
                Color.FromArgb(255, 0, 192, 192),
                Color.FromArgb(255, 0, 0, 192),
                Color.FromArgb(255, 192, 0, 192),

                Color.FromArgb(255, 64, 64, 64),
                Color.FromArgb(255, 128, 0, 0),
                Color.FromArgb(255, 128, 64, 0),
                Color.FromArgb(255, 128, 128, 0),
                Color.FromArgb(255, 0, 128, 0),
                Color.FromArgb(255, 0, 128, 128),
                Color.FromArgb(255, 0, 0, 128),
                Color.FromArgb(255, 128, 0, 128),

                Color.Black,
                Color.FromArgb(255, 64, 0, 0),
                Color.FromArgb(255, 96, 32, 0),
                Color.FromArgb(255, 64, 64, 0),
                Color.FromArgb(255, 0, 64, 0),
                Color.FromArgb(255, 0, 64, 64),
                Color.FromArgb(255, 0, 0, 64),
                Color.FromArgb(255, 64, 0, 64),
            };

            int[] argbs = new int[colors.Length];
            for (int i = 0; i < colors.Length; i++)
                argbs[i] = colors[i].ToArgb();
            return argbs;
        }

        // Display the colors.
        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            int max_x = PatchWidth * NumCols;
            int x = 0, y = 0;
            foreach (int argb in Properties.Settings.Default.Argbs)
            {
                Color color = Color.FromArgb(argb);
                richTextBox1.Text += "get color " + color.ToString() + "\n";
                using (SolidBrush br = new SolidBrush(color))
                {
                    e.Graphics.FillRectangle(br, x, y,
                        PatchWidth, PatchHeight);
                }
                x += PatchWidth + PatchMargin;
                if (x > max_x)
                {
                    x = 0;
                    y += PatchHeight + PatchMargin;
                }
            }
        }

        // Let the user select a color.
        private void pictureBox1_MouseClick(object sender, MouseEventArgs e)
        {
            // See which color was clicked.
            int row = (int)(e.Y / (PatchHeight + PatchMargin));
            int col = (int)(e.X / (PatchWidth + PatchMargin));
            int index = row * NumCols + col;

            // Let the user pick a color.
            colorDialog1.Color = Color.FromArgb(
                Properties.Settings.Default.Argbs[index]);
            if (colorDialog1.ShowDialog() == DialogResult.OK)
            {
                // The user clicked OK. Save the selected color.
                Properties.Settings.Default.Argbs[index] =
                    colorDialog1.Color.ToArgb();
                pictureBox1.Refresh();
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Properties.Settings.Default.Argbs = DefaultColors();
        }

        // Save the current colors.
        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            SaveColors();
        }

        // Save the current colors.
        private void SaveColors()
        {
            Properties.Settings.Default.Save();
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }
    }
}
