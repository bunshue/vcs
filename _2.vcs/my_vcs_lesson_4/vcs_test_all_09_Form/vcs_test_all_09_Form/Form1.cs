using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D; //for GraphicsPath

namespace vcs_test_all_09_Form
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.Height += 50;
            this.Width += 50;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            this.Height -= 50;
            this.Width -= 50;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            this.Show();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            this.Hide();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            this.Location = new Point(100, 500);
        }

        private void button6_Click(object sender, EventArgs e)
        {
            string message = "";
            message += "The Name is: " + this.Name + Environment.NewLine;
            message += "The ProductName is: " + this.ProductName + Environment.NewLine;
            message += "The ProductVersion is: " + this.ProductVersion + Environment.NewLine;
            message += "The CompanyName is: " + this.CompanyName + Environment.NewLine;
            MessageBox.Show(message);
        }

        private void button7_Click(object sender, EventArgs e)
        {
            this.BackColor = Color.Red;
        }

        private void button8_Click(object sender, EventArgs e)
        {
            string message = "";
            message += "Width : " + this.Width + Environment.NewLine;
            message += "Height : " + this.Height + Environment.NewLine;
            MessageBox.Show(message);
        }

        private void button9_Click(object sender, EventArgs e)
        {
            this.FormBorderStyle = FormBorderStyle.FixedSingle;
            //this.WindowState = FormWindowState.Maximized;
            this.WindowState = FormWindowState.Maximized;  // 設定表單最大化
            /*
                FormBorderStyle為None，去掉外框。
                WindowState為Maximized，視窗最大化。
                TopMost為true，最上層。

            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
            this.TopMost = true;
                        */
        }

        private void button10_Click(object sender, EventArgs e)
        {
            this.WindowState = FormWindowState.Minimized;   //設定表單最小化
        }

        private void button11_Click(object sender, EventArgs e)
        {
            this.WindowState = FormWindowState.Normal;      //設定表單預設大小
        }

        private void button12_Click(object sender, EventArgs e)
        {
            this.TopMost = true;    //設定表單最上層顯示
        }

        private void button13_Click(object sender, EventArgs e)
        {
            this.TopMost = false;    //取消表單最上層顯示
        }

        private void button14_Click(object sender, EventArgs e)
        {

        }

        private void button17_Click(object sender, EventArgs e)
        {

        }

        private void button16_Click(object sender, EventArgs e)
        {

        }

        private void button15_Click(object sender, EventArgs e)
        {

        }

        private void button18_Click(object sender, EventArgs e)
        {
            //移動表單位置
            this.Top = 30;
            this.Left = 30;

        }

        private void button20_Click(object sender, EventArgs e)
        {
            //表單變大
            this.Width += 50;
            this.Height += 50;

        }

        private void button21_Click(object sender, EventArgs e)
        {
            //表單變小
            this.Width -= 50;
            this.Height -= 50;

        }

        private void button19_Click(object sender, EventArgs e)
        {
            //表單換位置
            this.Top = 30;
            this.Left = 30;

        }

        private void button26_Click(object sender, EventArgs e)
        {
            this.Opacity -= 0.1;
        }

        private void button25_Click(object sender, EventArgs e)
        {
            this.Opacity += 0.1;
        }

        private void button24_Click(object sender, EventArgs e)
        {
            this.BackColor = Color.Pink;
            button24.BackColor = Color.Blue;
            button22.BackColor = Color.Blue;

        }

        private void button22_Click(object sender, EventArgs e)
        {
            this.BackColor = default(Color);

            button24.BackColor = default(Color);
            button24.UseVisualStyleBackColor = true;
            button22.BackColor = default(Color);
            button22.UseVisualStyleBackColor = true;

        }

        private void button19_Click_1(object sender, EventArgs e)
        {
            this.FormBorderStyle = FormBorderStyle.FixedDialog;
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            //在退出程序前彈出確認退出程序的對話框

            if (e.CloseReason != CloseReason.WindowsShutDown)
            {
                if (MessageBox.Show("是否確定要關閉程式", "關閉程式", MessageBoxButtons.YesNo) == DialogResult.No)
                {
                    e.Cancel = true;
                }
            }

            /*
            //或是
            if (MessageBox.Show("真的要退出程序嗎？", "退出程序", MessageBoxButtons.OKCancel) == DialogResult.Cancel)
            {
                e.Cancel = true;
            }
            */
        }

        private void button27_Click(object sender, EventArgs e)
        {
            this.FormBorderStyle = FormBorderStyle.None;
            //this.WindowState = FormWindowState.Maximized;
            this.WindowState = FormWindowState.Maximized;  // 設定表單最大化
        }

        #region 引用方法:為窗體繪製圓角(新增至窗體Resize事件)
        //此方法設定窗體有效區域為圓角矩形
        public void SetWindowRegion()
        {
            System.Drawing.Drawing2D.GraphicsPath FormPath;
            FormPath = new System.Drawing.Drawing2D.GraphicsPath();
            Rectangle rect = new Rectangle(0, 0, this.Width, this.Height);
            FormPath = GetRoundedRectPath(rect, 60);
            this.Region = new Region(FormPath);
        }

        //輔助方法:此方法用來建立圓角矩形路徑
        private GraphicsPath GetRoundedRectPath(Rectangle rect, int radius)
        {
            int diameter = radius;
            Rectangle arcRect = new Rectangle(rect.Location, new Size(diameter, diameter));
            GraphicsPath path = new GraphicsPath();

            // 左上角
            path.AddArc(arcRect, 180, 90);

            // 右上角
            arcRect.X = rect.Right - diameter;
            path.AddArc(arcRect, 270, 90);

            // 右下角
            arcRect.Y = rect.Bottom - diameter;
            path.AddArc(arcRect, 0, 90);

            // 左下角
            arcRect.X = rect.Left;
            path.AddArc(arcRect, 90, 90);
            path.CloseFigure();//閉合曲線
            return path;
        }

        //在窗體尺寸改變的時候我們需要呼叫SetWindowRegion()將窗體變成圓角的
        private void Form1_Resize(object sender, EventArgs e)
        {
            SetWindowRegion();
        }
        #endregion

        private void button28_Click(object sender, EventArgs e)
        {
            this.FormBorderStyle = FormBorderStyle.None;
        }

        private void button29_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Graphics g = e.Graphics;
            g.DrawRectangle(new Pen(Color.Green), new Rectangle(00, 00, this.ClientSize.Width - 1, this.ClientSize.Height - 1));
        }

        private void button31_Click(object sender, EventArgs e)
        {
            this.Size = new Size(1000, 700);
        }

        private void button30_Click(object sender, EventArgs e)
        {
            this.Size = new Size(1200, 900);
        }

        private void button33_Click(object sender, EventArgs e)
        {
            button33.Size = new Size(button33.Size.Width + 5, button33.Size.Height + 5);
        }

        private void button32_Click(object sender, EventArgs e)
        {
            button33.Size = new Size(button33.Size.Width + 5, button33.Size.Height + 5);
        }

        private void button34_Click(object sender, EventArgs e)
        {
            button33.Size = new Size(button33.Size.Width - 5, button33.Size.Height - 5);
        }

        private void button35_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Form Size : w = " + this.Width.ToString() + " h = " + this.Height.ToString() + "\n";
            richTextBox1.Text += "Form ClientSize : w = " + this.ClientSize.Width.ToString() + " h = " + this.ClientSize.Height.ToString() + "\n";

        }

        private void button36_Click(object sender, EventArgs e)
        {
            //改變表單大小
            this.Size = new Size(1920 / 2, 1080 / 2);

        }

        private void button37_Click(object sender, EventArgs e)
        {
            //改變表單位置
            this.Location = new Point(1920 / 2, 0);

        }

        private void button38_Click(object sender, EventArgs e)
        {
            this.Text = string.Empty;
            this.ControlBox = false;
        }

        private void button39_Click(object sender, EventArgs e)
        {
            //表單不顯示在 Windows 工作列中
            this.ShowInTaskbar = false;
        }

        private void button23_Click(object sender, EventArgs e)
        {
            //顯示桌面
            Type shellType = Type.GetTypeFromProgID("Shell.Application");
            object shellObject = System.Activator.CreateInstance(shellType);
            shellType.InvokeMember("ToggleDesktop", System.Reflection.BindingFlags.InvokeMethod, null, shellObject, null); 
        }

    }
}
