using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;

/*
程式啟動後
最小化至系統列
每一秒檢查一次
10分鐘後跳到最上層顯示
人按ack後 再最小化至系統列
直到10分鐘後再跳出來
最好能做到快捷鍵
*/

/*
WIN32系統托盤程序
程序運行後駐留系統托盤，左鍵呼出，右鍵退出。後續可加右鍵菜單。
注冊系統按鍵WIN+F10,呼出程序。
重寫系統消息，最小化和關閉按鈕隱藏程序
*/

//熱鍵部分已搬出

namespace vcs_Clock
{
    public enum HotkeyModifiers
    {
        Alt = 1,
        Ctrl = 2,
        Shift = 4,
        WindowsKey = 8
    }

    public partial class Form1 : Form
    {
        bool flag_always_show = false;

        [DllImport("user32.dll")]
        private static extern bool RegisterHotKey(IntPtr hWnd, int id, int modifiers, Keys vk);

        [DllImport("user32.dll")]
        private static extern bool UnregisterHotKey(IntPtr hWnd, int id);

        const int WM_HOTKEY = 0x312;
        const int WM_SYSCOMMAND = 0X112;
        const int SC_MAXMIZE = 0xf030;
        const int SC_MINMIZE = 0xf020;
        const int SC_CLOSE = 0xf060;

        protected override void WndProc(ref Message m)
        {
            switch (m.Msg)
            {
                case WM_SYSCOMMAND:
                    int code = m.WParam.ToInt32();
                    if (code == SC_CLOSE || code == SC_MINMIZE)
                    {
                        this.Visible = false;
                        return;//Must Prevent WndProc
                    }
                    break; //others, such as SC_MAXMIZE must in WndProc.
                case WM_HOTKEY:
                    this.Text = DateTime.Now.ToString();
                    this.Activate();
                    this.Visible = true;

                    this.WindowState = FormWindowState.Normal;
                    this.ShowInTaskbar = true;
                    this.TopMost = true;
                    show_seconds = 0;

                    break;
            }
            base.WndProc(ref m);
        }

        public Form1()
        {
            InitializeComponent();

            //RegisterHotKey //熱鍵部分已搬出
            bool bOK = RegisterHotKey(this.Handle, 0, (int)HotkeyModifiers.WindowsKey, Keys.F10);

            this.Closing += delegate
            {
                UnregisterHotKey(this.Handle, 0);
            };

            NotifyIcon ni = new NotifyIcon() { Icon = this.Icon, Visible = true };

            ni.MouseDown += (sender, e) =>
            {
                if (e.Button == MouseButtons.Left) //系統列 按左鍵
                {
                    this.Activate();
                    this.Visible = true;

                    this.WindowState = FormWindowState.Normal;
                    this.ShowInTaskbar = true;
                    this.TopMost = true;
                    show_seconds = 0;
                }
                if (e.Button == MouseButtons.Right) //系統列 按右鍵
                {
                    if (DialogResult.Yes == MessageBox.Show("Quit? Realy?", "Quit", MessageBoxButtons.YesNo))
                    {
                        this.Close();
                    }
                }
            };
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //this.FormBorderStyle = FormBorderStyle.None;//設定無邊框
            //this.WindowState = FormWindowState.Minimized;
            //this.ShowInTaskbar = false;

            //pictureBox1 連結 ContextMenuStrip (快捷功能表 / 右鍵選單)
            pictureBox1.ContextMenuStrip = contextMenuStrip1;

            int x_st = 30;
            int y_st = 30;
            int w = 100;
            int h = 100;
            int dx = 10;

            int W = x_st + w * 3 + dx * 2 + x_st;
            int H = y_st + h + y_st;

            pictureBox1.ClientSize = new Size(W, H);
            pictureBox1.Location = new Point(0, 0);
            this.ClientSize = new Size(W, H);

            int SW = Screen.PrimaryScreen.Bounds.Width;
            this.Location = new Point(SW - W, 0);
        }

        int show_seconds = 0;
        private void timer1_Tick(object sender, EventArgs e)
        {
            this.pictureBox1.Invalidate();

            if (flag_always_show == true)
            {
                return;
            }

            show_seconds++;
            if (show_seconds > 10)
            {
                this.TopMost = false;
                this.WindowState = FormWindowState.Minimized;
                this.ShowInTaskbar = false;
            }

            DateTime dt = DateTime.Now;//現在時間

            //this.Text = dt.ToLongTimeString();

            if (((dt.Minute % 30) == 0) && (dt.Second < 2))
            {
                this.WindowState = FormWindowState.Normal;
                this.ShowInTaskbar = true;
                this.TopMost = true;
                show_seconds = 0;
            }
        }

        private void pictureBox1_DoubleClick(object sender, EventArgs e)
        {
            Application.Exit();
        }

        //***********************
        private Point mouseOffset;//記錄滑鼠座標
        private bool isMouseDown = false;//是否按下滑鼠
        //***********************
        #region 移動無邊框表單
        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            int xOffset;
            int yOffset;
            if (e.Button == MouseButtons.Left)
            {
                xOffset = -e.X;
                yOffset = -e.Y;
                mouseOffset = new Point(xOffset, yOffset);
                isMouseDown = true;
            }
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (isMouseDown)
            {
                Point mousePos = Control.MousePosition;
                mousePos.Offset(mouseOffset.X, mouseOffset.Y);
                Location = mousePos;
            }
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                isMouseDown = false;
            }
        }
        #endregion

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            int hh = DateTime.Now.Hour;
            int mm = DateTime.Now.Minute;
            int ss = DateTime.Now.Second;

            int x_st = 30;
            int y_st = 30;
            int w = 100;
            int h = 100;
            int dx = 10;

            e.Graphics.Clear(Color.Red);

            for (int i = 0; i < 3; i++)
            {
                e.Graphics.FillRectangle(new SolidBrush(Color.Black), x_st + (w + dx) * i, y_st, w, h);
            }

            e.Graphics.DrawLine(new Pen(Color.Red, 6), x_st, y_st + h / 2, x_st + 380, y_st + h / 2);

            int dy = 15;
            e.Graphics.DrawString(hh.ToString("D2"), new Font("標楷體", 55, FontStyle.Bold), Brushes.White, x_st, y_st + dy);
            e.Graphics.DrawString(mm.ToString("D2"), new Font("標楷體", 55, FontStyle.Bold), Brushes.White, x_st + (w + dx) * 1, y_st + dy);
            e.Graphics.DrawString(ss.ToString("D2"), new Font("標楷體", 55, FontStyle.Bold), Brushes.White, x_st + (w + dx) * 2, y_st + dy);
        }

        private void toolStripMenuItem1_Click(object sender, EventArgs e)
        {
            ToolStripMenuItem menu_item = sender as ToolStripMenuItem;

            //位置
            ToolStripMenuItem[] items =
            {
                toolStripMenuItem1a,
                toolStripMenuItem1b,
                toolStripMenuItem1c,
                toolStripMenuItem1d
            };
            foreach (ToolStripMenuItem item in items)
            {
                item.Checked = (item == menu_item);
            }
        }

        private void toolStripMenuItem2_Click(object sender, EventArgs e)
        {
            //數位時鐘
        }

        private void toolStripMenuItem3_Click(object sender, EventArgs e)
        {
            //總是顯示
            toolStripMenuItem3.Checked = !toolStripMenuItem3.Checked;
            flag_always_show = toolStripMenuItem3.Checked;
            show_seconds = 0;
        }

        private void toolStripMenuItem4_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
