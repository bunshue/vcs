using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace CH1203
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            lblMsg.Text = "隨意按下滑鼠按鍵\n" +
               "下方標籤中顯示座標及按鍵";
            lblMsg.TextAlign = ContentAlignment.MiddleCenter;
            lblMouse.TextAlign = ContentAlignment.MiddleCenter;
        }

        private void Form1_MouseDown(object sender,
           MouseEventArgs e)
        {
            lblMouse.Text = $"表單--X：{e.X.ToString()} " +
               $"Y: {e.Y.ToString()}";
        }

        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            lblMouse.Text = string.Empty;
            switch (e.Button)
            {
                case MouseButtons.Left:
                    lblMouse.Text = "按下滑鼠左鍵";
                    break;
                case MouseButtons.Right:
                    lblMouse.Text = "按下滑鼠右鍵";
                    break;
                case MouseButtons.XButton1:
                    lblMouse.Text = "按下滑鼠瀏覽鍵";
                    break;
            }
        }

        private void lblMouse_MouseDown(object sender, MouseEventArgs e)
        {
            lblMouse.Text = $"標籤--X：{e.X.ToString()} " +
               $"Y: {e.Y.ToString()}";
        }

        private void lblMouse_MouseUp(object sender,
              MouseEventArgs e)
        {
            lblMouse.Text = string.Empty;
            switch (e.Button)
            {
                case MouseButtons.Left:
                    lblMouse.Text = "按下滑鼠左鍵";
                    break;
                case MouseButtons.Right:
                    lblMouse.Text = "按下滑鼠右鍵";
                    break;
                case MouseButtons.XButton1:
                    lblMouse.Text = "按下滑鼠瀏覽鍵";
                    break;
            }
        }
    }
}
