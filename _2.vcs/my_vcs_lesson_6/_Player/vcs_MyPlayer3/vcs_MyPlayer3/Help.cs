using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_MyPlayer3
{
    public partial class Help : Form
    {
        public Help()
        {
            InitializeComponent();
        }

        private void Help_Load(object sender, EventArgs e)
        {

        }

        private void Help_Paint(object sender, PaintEventArgs e)
        {
            int ww = 640;
            int hh = 480;
            int margin = 30;
            this.Visible = true;
            this.BackColor = Color.White;
            this.Size = new Size(ww, hh);
            this.BringToFront();
            this.Location = new Point(600, 450);

            e.Graphics.FillRectangle(new SolidBrush(Color.Pink), 0, 0, this.ClientSize.Width, this.ClientSize.Height);
            e.Graphics.DrawRectangle(new Pen(Color.Navy, 2), margin, margin, this.ClientSize.Width - margin * 2, this.ClientSize.Height - margin * 2);

            string debug1 = "O : 開啟檔案";
            string debug2 = "Enter / Space : 播放 / 暫停播放";
            string debug3 = "ESC / X : 離開程式";
            string debug4 = "H : 幫助畫面";
            string debug5 = "上 / 下 : 音量調整";
            string debug6 = "左 / 右 : 播放位置移動 10 秒";
            string debug7 = "(Ctrl)左 / 右 : 播放位置移動 60 秒";
            string debug8 = "(Shift)左 / 右 : 播放位置移動 120 秒";
            string debug9 = "(Alt)左 / 右 : 播放位置移動 180 秒";

            int x_st = 60;
            int y_st = 50;
            int dy = 40;

            e.Graphics.DrawString(debug1, new Font("標楷體", 20), new SolidBrush(Color.Blue), new PointF(x_st, y_st + dy * 0));
            e.Graphics.DrawString(debug2, new Font("標楷體", 20), new SolidBrush(Color.Blue), new PointF(x_st, y_st + dy * 1));
            e.Graphics.DrawString(debug3, new Font("標楷體", 20), new SolidBrush(Color.Blue), new PointF(x_st, y_st + dy * 2));
            e.Graphics.DrawString(debug4, new Font("標楷體", 20), new SolidBrush(Color.Blue), new PointF(x_st, y_st + dy * 3));
            e.Graphics.DrawString(debug5, new Font("標楷體", 20), new SolidBrush(Color.Blue), new PointF(x_st, y_st + dy * 4));
            e.Graphics.DrawString(debug6, new Font("標楷體", 20), new SolidBrush(Color.Blue), new PointF(x_st, y_st + dy * 5));
            e.Graphics.DrawString(debug7, new Font("標楷體", 20), new SolidBrush(Color.Blue), new PointF(x_st, y_st + dy * 6));
            e.Graphics.DrawString(debug8, new Font("標楷體", 20), new SolidBrush(Color.Blue), new PointF(x_st, y_st + dy * 7));
            e.Graphics.DrawString(debug9, new Font("標楷體", 20), new SolidBrush(Color.Blue), new PointF(x_st, y_st + dy * 8));
        }
    }
}
