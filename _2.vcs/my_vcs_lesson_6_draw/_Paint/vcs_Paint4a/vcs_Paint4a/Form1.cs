using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Paint4a
{
    public partial class Form1 : Form
    {
        Bitmap buffer; // 點陣圖物件　要儲存用的
        Pen pen;　// 畫畫的筆
        int x, y;　// 紀錄上一個筆畫的起始點
        Graphics G; // 紀錄點陣圖物件 的 畫布物件

        public Form1()
        {
            InitializeComponent();
            this.ClientSize = new Size(640, 480);// 設定視窗客戶區的寬高
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            pen = new Pen(Color.Red, 1);// 預設畫筆的顏色與筆寬
            buffer = new Bitmap(this.Width, this.Height);　// 新增點陣圖物件
            G = Graphics.FromImage(buffer); // 由點陣圖物件產生畫布
            G.Clear(Color.White); // 將畫布清為白色
        }

        private void newToolStripMenuItem_Click(object sender, EventArgs e)
        {
            G.Clear(Color.White); // 新增 → 將畫布清為白色
            this.Refresh(); // 要求重繪
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.DrawImage(buffer, 0, 0);　// 將點陣圖物件顯示出來
        }

        private void saveAsToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if (saveFileDialog1.ShowDialog() == DialogResult.OK)
            {
                buffer.Save(saveFileDialog1.FileName); // 儲存 點陣圖物件 
            }
        }

        private void exitToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Application.Exit();　//　結束應用程式
        }

        private void redToolStripMenuItem_Click(object sender, EventArgs e)
        {
            SetColorMenuItem(true, false, false, false);
            pen.Color = Color.Red;
        }

        private void greenToolStripMenuItem_Click(object sender, EventArgs e)
        {
            SetColorMenuItem(false, true, false, false);
            pen.Color = Color.Green;
        }

        private void blueToolStripMenuItem_Click(object sender, EventArgs e)
        {
            SetColorMenuItem(false, false, true, false);
            pen.Color = Color.Blue;
        }

        private void pickAColorToolStripMenuItem_Click(object sender, EventArgs e)
        {
            // 開啟 顏色選取視窗
            if (colorDialog1.ShowDialog() == DialogResult.OK)
            {
                SetColorMenuItem(false, false, false, true);
                pen.Color = colorDialog1.Color; // 設定 畫筆的顏色
                pickAColorToolStripMenuItem.BackColor = colorDialog1.Color; //呈現選色
            }
        }

        // 設定 主選單項目 的勾選狀況 
        void SetColorMenuItem(bool r, bool g, bool b, bool p)
        {
            redToolStripMenuItem.Checked = r;
            greenToolStripMenuItem.Checked = g;
            blueToolStripMenuItem.Checked = b;
            pickAColorToolStripMenuItem.Checked = p;
        }

        private void toolStripMenuItem2_Click(object sender, EventArgs e)
        {
            pen.Width = 1;
        }

        private void toolStripMenuItem3_Click(object sender, EventArgs e)
        {
            pen.Width = 5;
        }

        private void toolStripMenuItem4_Click(object sender, EventArgs e)
        {
            pen.Width = 10;
        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            x = e.X; // 紀錄筆畫的起始點
            y = e.Y;
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left) // 滑鼠的左鍵
            {
                G.DrawLine(pen, x, y, e.X, e.Y);　// 寫到　buffer

                Graphics g1 = this.CreateGraphics();
                g1.DrawLine(pen, x, y, e.X, e.Y);　// 暫時先在 視窗客戶區 顯示出筆畫

                x = e.X; // 結束點 就是 下一次的 開始點
                y = e.Y;
            }
        }

        private void aboutToolStripMenuItem1_Click(object sender, EventArgs e)
        {
            MessageBox.Show("繪圖板 Version 1.0\n作者：lion-mouse 2012.08", "繪圖板");
        }
    }
}
