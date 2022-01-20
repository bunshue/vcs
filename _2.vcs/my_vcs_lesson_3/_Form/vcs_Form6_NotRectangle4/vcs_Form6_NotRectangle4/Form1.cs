using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

/*
製作不規則窗體

Form1 的 屬性

FormBorderStyle 設置為 None
BackgroundImage 設置為指定的圖片
TransparencyKey 設置指定的顏色
（此屬性告訴應用程序窗體中的哪些部分需要設置為透明。 ）
*/

namespace vcs_Form6_NotRectangle4
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.BackgroundImage = Bitmap.FromFile("../../matlab.png");
            this.BackgroundImageLayout = ImageLayout.Zoom;

            this.FormBorderStyle = FormBorderStyle.None;
            this.TransparencyKey = Color.FromArgb(240, 240, 240);   //指名要變成透明的顏色
            //this.TransparencyKey = Color.White;   //指名要變成透明的顏色
            //全圖的指明顏色部分 都會變成透明可穿透 不只邊緣部分

            this.MouseDown += new System.Windows.Forms.MouseEventHandler(this.WinForm_MouseDown);
            this.MouseUp += new System.Windows.Forms.MouseEventHandler(this.WinForm_MouseUp);
            this.MouseMove += new System.Windows.Forms.MouseEventHandler(this.WinForm_MouseMove);
        }

        private Point mouseOffset; //記錄鼠標指針的坐標
        private bool isMouseDown = false;
        private void WinForm_MouseDown(object sender, System.Windows.Forms.MouseEventArgs e)
        {
            int xOffset;
            int yOffset;
            if (e.Button == MouseButtons.Left)
            {
                xOffset = -e.X - SystemInformation.FrameBorderSize.Width;
                yOffset = -e.Y - SystemInformation.CaptionHeight -
                SystemInformation.FrameBorderSize.Height;
                mouseOffset = new Point(xOffset, yOffset);
                isMouseDown = true;
            }
        }

        private void WinForm_MouseMove(object sender, System.Windows.Forms.MouseEventArgs e)
        {
            if (isMouseDown)
            {
                Point mousePos = Control.MousePosition;
                mousePos.Offset(mouseOffset.X, mouseOffset.Y);
                Location = mousePos;
            }
        }

        private void WinForm_MouseUp(object sender, System.Windows.Forms.MouseEventArgs e)
        {
            // 修改鼠標狀態isMouseDown的值
            // 確保只有鼠標左鍵按下並移動時，才移動窗體
            if (e.Button == MouseButtons.Left)
            {
                isMouseDown = false;
            }
        }
    }
}
