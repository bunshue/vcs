using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_KeyDown4_MoveForm
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files1\picture1.jpg";
            this.BackgroundImage = Image.FromFile(filename);//设置窗体的背景图片
            this.ClientSize = this.BackgroundImage.Size;
            this.StartPosition = FormStartPosition.CenterScreen; //居中顯示

            this.KeyPreview = true;
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            Point point = this.Location;
            switch (e.KeyData)
            {
                case Keys.Up:
                    point.Y -= 2;
                    break;
                case Keys.Down:
                    point.Y += 2;
                    break;
                case Keys.Right:
                    point.X += 2;
                    break;
                case Keys.Left:
                    point.X -= 2;
                    break;
                case Keys.X:
                    this.Close();
                    break;
                case Keys.Escape:
                    this.Close();
                    break;
                default: break;
            }
            this.Location = point;
        }
    }
}
