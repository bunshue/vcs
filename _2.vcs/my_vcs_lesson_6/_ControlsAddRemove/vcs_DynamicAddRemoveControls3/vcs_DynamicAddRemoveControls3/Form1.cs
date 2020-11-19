using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for Directory

//所有的PNG檔要選屬性/複製到輸出目錄/選 有更新時才複製

namespace vcs_DynamicAddRemoveControls3
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Display all of the images in the Buttons folder.
        private void button1_Click(object sender, EventArgs e)
        {
            const int wid = 40;
            const int hgt = 40;
            const int margin = 3;
            int x = margin;
            int y = margin;
            const int num_columns = 10;
            const int xmax = num_columns * (wid + margin);

            // Find the images.
            foreach (string filename in Directory.GetFiles("Buttons", "*.png"))
            {
                // Make a new Button.
                Button btn = new Button();
                btn.Parent = this;
                btn.Image = new Bitmap(filename);
                btn.Size = new Size(32, 32);
                btn.Location = new Point(x, y);
                x += wid + margin;
                if (x > xmax)
                {
                    x = margin;
                    y += hgt + margin;
                }

                FileInfo file_info = new FileInfo(filename);
                toolTip1.SetToolTip(btn, file_info.Name);
            }

            // Size the form to fit.
            //this.ClientSize = new Size(xmax + margin, y + hgt + margin);


        }
    }
}
