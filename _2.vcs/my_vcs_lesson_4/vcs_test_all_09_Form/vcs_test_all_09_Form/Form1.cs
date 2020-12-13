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
        private Form2 F2;   // A variable that refers to the instance of Form2.

        public Form1()
        {
            InitializeComponent();
            show_item_location();

            // Initialize the form variables.
            // Make the Form2.
            F2 = new Form2();

            // Initialize the Form2's variable.
            //F2.TheForm1 = this;
            F2.F1 = this;

            // Make both forms stay on top.
            this.TopMost = true;
            F2.TopMost = true;
        }

        // Load the picture from the startup directory.
        private void Form1_Load(object sender, EventArgs e)
        {
            //方案總管/加入/現有項目/選圖片
            //圖片之屬性 複製到輸出目錄 改成 有更新時才複製
            BackgroundImage = new Bitmap("picture1.jpg");
            //ClientSize = BackgroundImage.Size;    //表單符合圖片大小
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 12;
            y_st = 12;
            dx = 205;
            dy = 50;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);
            button10.Location = new Point(x_st + dx * 0, y_st + dy * 10);
            button11.Location = new Point(x_st + dx * 0, y_st + dy * 11);

            button12.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button20.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button21.Location = new Point(x_st + dx * 1, y_st + dy * 9);
            button22.Location = new Point(x_st + dx * 1, y_st + dy * 10);
            button23.Location = new Point(x_st + dx * 1, y_st + dy * 11);

            button24.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button25.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button26.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button27.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button28.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button29.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button30.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button31.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            button32.Location = new Point(x_st + dx * 2, y_st + dy * 8);
            button33.Location = new Point(x_st + dx * 2, y_st + dy * 9);
            button34.Location = new Point(x_st + dx * 2, y_st + dy * 10);
            button35.Location = new Point(x_st + dx * 2, y_st + dy * 11);

            button36.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            button37.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            button38.Location = new Point(x_st + dx * 3, y_st + dy * 2);
            button39.Location = new Point(x_st + dx * 3, y_st + dy * 3);

            bt_exit.Location = new Point(x_st + dx * 3+50, y_st + dy * 12);

            label1.Location = new Point(x_st + dx * 0, y_st + dy * 12);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void button0_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "表單顯示在螢幕最右下方\n";
            const int margin = 10;
            int x = Screen.PrimaryScreen.WorkingArea.Right - this.Width - margin;
            int y = Screen.PrimaryScreen.WorkingArea.Bottom - this.Height - margin;
            this.Location = new Point(x, y);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "表單變大 50點\n";
            this.Height += 50;
            this.Width += 50;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "表單縮小 50點\n";
            this.Height -= 50;
            this.Width -= 50;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "顯示表單\n";
            this.Show();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "隱藏表單\n";
            this.Hide();

            //same
            //Hide();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "設定表單的螢幕位置\n";
            this.Location = new Point(100, 500);
        }

        private void button6_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "顯示表單屬性\n";
            string message = "";
            message += "The Name is: " + this.Name + Environment.NewLine;
            message += "The ProductName is: " + this.ProductName + Environment.NewLine;
            message += "The ProductVersion is: " + this.ProductVersion + Environment.NewLine;
            message += "The CompanyName is: " + this.CompanyName + Environment.NewLine;
            MessageBox.Show(message);
        }

        private void button7_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "改變表單背景顏色\n";
            this.BackColor = Color.Red;
        }

        private void button8_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "取得目前表單大小\n";
            string message = "";
            message += "Width : " + this.Width + Environment.NewLine;
            message += "Height : " + this.Height + Environment.NewLine;
            MessageBox.Show(message);
        }

        private void button9_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "表單最大化\n";
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
            richTextBox1.Text += "表單最小化\n";
            this.WindowState = FormWindowState.Minimized;   //設定表單最小化

            //same
            //WindowState = FormWindowState.Minimized;
        }

        private void button11_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "表單預設大小\n";
            this.WindowState = FormWindowState.Normal;      //設定表單預設大小
        }

        bool flag_TopMost = false;
        private void button12_Click(object sender, EventArgs e)
        {
            if (flag_TopMost == false)
            {
                flag_TopMost = true;
                richTextBox1.Text += "表單最上層顯示\n";
                button12.Text = "取消表單最上層顯示";
                this.TopMost = true;    //設定表單最上層顯示
            }
            else
            {
                flag_TopMost = false;
                richTextBox1.Text += "取消表單最上層顯示\n";
                button12.Text = "表單最上層顯示";
                this.TopMost = false;    //設定表單最上層顯示
            }
        }

        private void button13_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "關此表單, 開新表單\n";
            // Switch to the Form2.
            this.Hide();
            F2.Show();
        }

        private void button14_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "xxx\n";
        }

        private void button15_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "xxx\n";
        }

        private void button16_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "xxx\n";
        }

        private void button17_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "游移表單\n";
            richTextBox1.Text += "表單位置 " + this.Location.X.ToString() + ", " + this.Location.Y.ToString() + "\n";
            richTextBox1.Text += "表單大小 " + this.Size.Width.ToString() + " X " + this.Size.Height.ToString() + "\n";
            richTextBox1.Text += "表單大小 " + this.ClientSize.Width.ToString() + " X " + this.ClientSize.Height.ToString() + "\n";

            //int screenWidth = Screen.PrimaryScreen.Bounds.Width;
            //int screenHeight = Screen.PrimaryScreen.Bounds.Height;
            richTextBox1.Text += "目前的螢幕解析度 :" + Screen.PrimaryScreen.Bounds.Width.ToString() + " * " + Screen.PrimaryScreen.Bounds.Height.ToString() + "\n";
            
            //改變表單位置
            //this.Location = new Point(1920 / 2, 0);
        }

        private void button18_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "移動表單位置\n";
            this.Top = 30;
            this.Left = 30;
        }

        private void button19_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "無法改變Form大小\n";
            this.FormBorderStyle = FormBorderStyle.FixedDialog;
        }

        private void button20_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "表單變大\n";
            this.Width += 50;
            this.Height += 50;
        }

        private void button21_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "表單變小\n";
            this.Width -= 50;
            this.Height -= 50;
        }

        private void button22_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "表單背景色恢復\n";
            this.BackColor = default(Color);

            button24.BackColor = default(Color);
            button24.UseVisualStyleBackColor = true;
            button22.BackColor = default(Color);
            button22.UseVisualStyleBackColor = true;
        }

        private void button23_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "顯示桌面\n";
            Type shellType = Type.GetTypeFromProgID("Shell.Application");
            object shellObject = System.Activator.CreateInstance(shellType);
            shellType.InvokeMember("ToggleDesktop", System.Reflection.BindingFlags.InvokeMethod, null, shellObject, null);
        }

        private void button24_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "表單背景色改變\n";
            this.BackColor = Color.Pink;
            button24.BackColor = Color.Blue;
            button22.BackColor = Color.Blue;
        }

        private void button25_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "透明-\n";
            this.Opacity += 0.1;
        }

        private void button26_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "透明+\n";
            this.Opacity -= 0.1;
        }

        bool flag_full_screen = false;
        private void button27_Click(object sender, EventArgs e)
        {
            if (flag_full_screen == false)
            {
                richTextBox1.Text += "全螢幕\n";
                flag_full_screen = true;
                button27.Text = "恢復一般螢幕";

                this.FormBorderStyle = FormBorderStyle.None;
                //this.WindowState = FormWindowState.Maximized;
                this.WindowState = FormWindowState.Maximized;  // 設定表單最大化
            }
            else
            {
                richTextBox1.Text += "恢復一般螢幕\n";
                flag_full_screen = false;
                button27.Text = "全螢幕";

                this.FormBorderStyle = FormBorderStyle.Sizable;
                //this.WindowState = FormWindowState.Maximized;
                this.WindowState = FormWindowState.Normal;  // 設定表單恢復一般螢幕
            }
        }

        bool flag_border_none = false;
        private void button28_Click(object sender, EventArgs e)
        {
            if (flag_border_none == false)
            {
                richTextBox1.Text += "去掉外框\n";
                flag_border_none = true;
                button28.Text = "恢復外框";

                //same
                //this.FormBorderStyle = FormBorderStyle.None;

                //same
                FormBorderStyle = FormBorderStyle.None;
            }
            else
            {
                richTextBox1.Text += "恢復外框\n";
                flag_border_none = false;
                button28.Text = "去掉外框";

                //same
                //this.FormBorderStyle = FormBorderStyle.Sizable;

                //same
                FormBorderStyle = FormBorderStyle.Sizable;
            }
        }

        private void button29_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "xxx\n";
        }

        private void button30_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "表單變 1200 X 900\n";
            this.Size = new Size(1200, 900);

            //same
            //Size = new Size(1200, 900);
        }

        private void button31_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "表單變 1000 X 700\n";
            this.Size = new Size(1000, 700);
        }

        private void button32_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Button變大\n";
            button33.Size = new Size(button33.Size.Width + 5, button33.Size.Height + 5);
        }

        private void button33_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Button變大變小\n";
            button33.Size = new Size(button33.Size.Width + 5, button33.Size.Height + 5);
        }

        private void button34_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Button變小\n";
            button33.Size = new Size(button33.Size.Width - 5, button33.Size.Height - 5);
        }

        private void button35_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "FormSize ClientSize\n";
            richTextBox1.Text += "Form Size : w = " + this.Width.ToString() + " h = " + this.Height.ToString() + "\n";
            richTextBox1.Text += "Form ClientSize : w = " + this.ClientSize.Width.ToString() + " h = " + this.ClientSize.Height.ToString() + "\n";
        }

        private void button36_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "改變表單大小\n";
            this.Size = new Size(1920 / 2, 1080 / 2);
        }

        private void button37_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "改變表單位置\n";
            this.Location = new Point(1920 / 2, 0);
        }

        private void button38_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "沒有標題的Form\n";
            this.Text = string.Empty;
            this.ControlBox = false;
        }

        bool flag_ShowInTaskbar = true;
        private void button39_Click(object sender, EventArgs e)
        {
            if (flag_ShowInTaskbar == true)
            {
                flag_ShowInTaskbar = false;
                this.ShowInTaskbar = false;     //false : 表單不顯示在 Windows 工作列中
                richTextBox1.Text += "表單不顯示在 Windows 工作列中\n";
                button39.Text = "表單顯示在 Windows 工作列中";
            }
            else
            {
                flag_ShowInTaskbar = true;
                this.ShowInTaskbar = true;     //true : 表單顯示在 Windows 工作列中
                richTextBox1.Text += "表單顯示在 Windows 工作列中\n";
                button39.Text = "表單不顯示在 Windows 工作列中";
            }
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Exit\n";
            Application.Exit();
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
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

            /*
            //或是
            //關閉程式前 確認視窗
            DialogResult Result = MessageBox.Show("尚未儲存確定要關閉程式?", "關閉確認", MessageBoxButtons.YesNo);
            if (Result == System.Windows.Forms.DialogResult.Yes)
            {
                // 關閉Form 
                e.Cancel = false;
            }
            else
            {
                e.Cancel = true;
            }
            */
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Graphics g = e.Graphics;
            g.DrawRectangle(new Pen(Color.Green), new Rectangle(00, 00, this.ClientSize.Width - 1, this.ClientSize.Height - 1));
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

        // On left button, let the user drag the form.
        private void label2_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                // Release the mouse capture started by the mouse down.
                label2.Capture = false;

                // Create and send a WM_NCLBUTTONDOWN message.
                const int WM_NCLBUTTONDOWN = 0x00A1;
                const int HTCAPTION = 2;
                Message msg =
                    Message.Create(this.Handle, WM_NCLBUTTONDOWN,
                        new IntPtr(HTCAPTION), IntPtr.Zero);
                this.DefWndProc(ref msg);
            }
        }



    }
}
