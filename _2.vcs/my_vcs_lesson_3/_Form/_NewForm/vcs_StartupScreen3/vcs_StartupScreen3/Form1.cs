using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_StartupScreen3
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //建立一個新的視窗物件
            using (Form f = new Form())
            {
                f.FormBorderStyle = FormBorderStyle.None;  // 設定無邊框
                f.BackColor = Color.Yellow;//視窗背景顏色
                f.Opacity = 0.5;//視窗透明度
                f.Size = new Size(500, 300);
                f.StartPosition = FormStartPosition.CenterScreen;//視窗置中
                f.Show();//顯示視窗
                Graphics g = f.CreateGraphics();
                g.DrawString("程式啟動中", new Font("標楷體", 60), new SolidBrush(Color.Green), new PointF(30, 110));

                System.Threading.Thread.Sleep(1000);//休息一秒
            }
            //視窗物件自動Dispose
        }
    }
}
