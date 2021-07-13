using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;   //for DllImport

namespace vcs_Mouse
{
    public partial class Form1 : Form
    {
        bool drag = false;//記錄是否可拖曳，預設不可拖曳
        int sX, sY;       //記錄滑鼠按下時的座標值

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.MouseWheel += new MouseEventHandler(label_Zoom);
        }

        private void label_Zoom(object sender, MouseEventArgs e)
        {
            if (e.Delta > 0)
            {
                label1.Text = "滾輪向上";
                label1.Width += 5;
                label1.Height += 5;
            }
            else
            {
                label1.Text = "滾輪向下";
                label1.Width -= 5;
                label1.Height -= 5;
            }
        }

        private void label1_Click(object sender, EventArgs e)
        {
            label1.Text = "點按";
        }

        private void label1_DoubleClick(object sender, EventArgs e)
        {
            label1.Text = "快按兩下";
        }

        private void label1_MouseClick(object sender, MouseEventArgs e)
        {
            // 哪一個滑鼠按鍵處於按下狀態的值。
            label1.Text = "點按 ";
            if (e.Button == MouseButtons.Right)
                label1.Text += "滑鼠右鍵";
            else if (e.Button == MouseButtons.Left)
                label1.Text += "滑鼠左鍵";
            else if (e.Button == MouseButtons.Middle)
                label1.Text += "滑鼠中鍵";
            else if (e.Button == MouseButtons.XButton1)
                label1.Text += "滑鼠XB1鍵";
            else if (e.Button == MouseButtons.XButton2)
                label1.Text += "滑鼠XB2鍵";
            else
                label1.Text += "滑鼠其他鍵";
        }

        private void label1_MouseDoubleClick(object sender, MouseEventArgs e)
        {
            label1.Text = "快按兩下";
            if (e.Button == MouseButtons.Right)
                label1.Text += "滑鼠右鍵";
            else if (e.Button == MouseButtons.Left)
                label1.Text += "滑鼠左鍵";
            else if (e.Button == MouseButtons.Middle)
                label1.Text += "滑鼠中鍵";
            else if (e.Button == MouseButtons.XButton1)
                label1.Text += "滑鼠XB1鍵";
            else if (e.Button == MouseButtons.XButton2)
                label1.Text += "滑鼠XB2鍵";
            else
                label1.Text += "滑鼠其他鍵";
        }

        private void label1_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)  //若是按滑鼠左鍵
            {
                drag = true;//設drag=true，表可拖曳
                sX = e.X; sY = e.Y;  //記錄滑鼠的座標值
            }
        }

        private void label1_MouseMove(object sender, MouseEventArgs e)
        {
            if (drag)      //若設drag=true
            {
                label1.Left += e.X - sX;
                label1.Top += e.Y - sY;
            }
        }

        private void label1_MouseUp(object sender, MouseEventArgs e)
        {
            drag = false; //設drag=false，表不可拖曳
        }

        private void button1_Click(object sender, EventArgs e)
        {

            //取得滑鼠資訊
            if (SystemInformation.MousePresent)  // 是否安裝滑鼠
            {
                richTextBox1.Text += "是否安裝滑鼠 : 是\n";
            }
            else
            {
                richTextBox1.Text += "是否安裝滑鼠 : 否\n";
            }

            // 滑鼠按鈕的數目
            richTextBox1.Text += "滑鼠按鈕的數目 : " + SystemInformation.MouseButtons.ToString() + "\n";

            if (SystemInformation.MouseWheelPresent) // 滑鼠是否有滾輪
            {
                richTextBox1.Text += "滑鼠是否有滾輪 : 是\n";
            }
            else
            {
                richTextBox1.Text += "滑鼠是否有滾輪 : 否\n";
            }

            // 滑鼠速度 (1 ~ 20)
            richTextBox1.Text += "滑鼠速度 (1 ~ 20) : " + SystemInformation.MouseSpeed.ToString() + "\n";
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            //this.Text = Control.MousePosition.ToString();
            this.Text = "(" + Control.MousePosition.X.ToString() + ", " + Control.MousePosition.Y.ToString() + ")";
        }

        //切換滑鼠左右鍵 ST
        [DllImport("user32.dll", EntryPoint = "SwapMouseButton")]
        public extern static int SwapMouseButton(int bSwap);
        [DllImport("user32.dll")]
        public extern static int GetSystemMetrics(int nIndes);

        private void button2_Click(object sender, EventArgs e)
        {
            //切換滑鼠左右鍵
            if (button2.Text == "切換滑鼠左右鍵")
            {
                SwapMouseButton(1);//切換滑鼠游標左右鍵
                button2.Text = "恢復滑鼠左右鍵";
            }
            else
            {
                SwapMouseButton(0);//恢復，設定左鍵為主鍵
                button2.Text = "切換滑鼠左右鍵";
            }
        }
        //切換滑鼠左右鍵 SP
    }
}
