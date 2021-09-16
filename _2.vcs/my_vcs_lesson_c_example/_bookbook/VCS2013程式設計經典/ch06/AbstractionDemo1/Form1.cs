using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace AbstractionDemo1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // 定義Draw方法用來在表單上繪製圖形
        // 若vType等於0則畫圓, vType等於1則畫線, vType等於2則畫弧形
        private void Draw(int vType)
        {
            Graphics g;   
            Pen p = new Pen(Color.Red);  // 建立一支紅色的筆
            g = this.CreateGraphics();   // 取得畫布
            g.Clear(Color.White);        // 清除畫布
            switch (vType)
            {
                case 0:
                    g.DrawEllipse(p, 90, 30, 90, 90);      // 畫圓
                    break;
                case 1:
                    g.DrawLine(p, 90, 50, 180, 100);       // 畫線
                    break;
                case 2:
                    g.DrawArc(p, 90, 30, 90, 90, 0, 250);  // 畫弧形
                    break;
            }
        }
        // 按 [畫圓] 鈕執行btnCircle_Click事件處理函式
        private void btnCircle_Click(object sender, EventArgs e)
        {
            Draw(0);
        }
        // 按 [畫線] 鈕執行btnLine_Click事件處理函式 
        private void btnLine_Click(object sender, EventArgs e)
        {
            Draw(1); 
        }
        // 按 [畫圓弧] 鈕執行btnArc_Click事件處理函式 
        private void btnArc_Click(object sender, EventArgs e)
        {
            Draw(2);
        }


  
    }
}
