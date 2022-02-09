using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Form3_Dock
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.TopMost = true;
        }

        //表單自動停靠在左上右邊 類似QQ的收縮功能 ST

        //用C#代碼實現類似QQ窗體的“上、左、右”停靠功能
        //表單收縮至畫面的左、上、右邊
        int QQ_MODE = 0, QQ_T = 3, QQ_XY = 6;//0為不停靠,1為X軸,2為Y軸,3為頂部；QQ_T為顯示的像素；QQ_XY為誤差
        //QQ_MODE(用於記錄窗體當前的停靠狀態，即0為不停靠,1為X軸,2為Y軸,3為頂部)
        //QQ_T(窗體縮放時顯示出來的邊緣大小)
        //QQ_XY(鼠標坐標與窗體邊緣多少像素時為可見區)

        /*
        邏輯思考：如果鼠標左鍵在當前窗體按下時，無論窗體位置在哪，那麼此窗體一定是顯示的，並且可能為拖動狀態，即不停靠；
        如果鼠標移到到窗口內或到移動到邊緣差為QQ_XY內區域時窗體可見；
        當鼠標離開窗體時則判斷是否滿足伸縮的條件，即“上、左、右”，其中“上”為優先級；
        */
        private void timer1_Tick(object sender, EventArgs e)
        {
            //如果左鍵按下就不處理當前邏輯[是否收縮]
            if (MouseButtons == MouseButtons.Left)
            {
                return;
            }

            //鼠標的位置
            int x = MousePosition.X, y = MousePosition.Y;

            //鼠標移動到窗口內，顯示
            if (x > (this.Location.X - QQ_XY) && x < (this.Location.X + this.Width + QQ_XY) && y > (this.Location.Y - QQ_XY) && y < (this.Location.Y + this.Height + QQ_XY))
            {
                if (this.QQ_MODE == 1)
                {
                    this.Location = new Point(QQ_T, this.Location.Y);
                }
                else if (this.QQ_MODE == 2)
                {
                    this.Location = new Point(Screen.PrimaryScreen.WorkingArea.Width - this.Width - QQ_T, this.Location.Y);
                }
                else if (this.QQ_MODE == 3)
                {
                    this.Location = new Point(this.Location.X, QQ_T);
                }
            }
            else//鼠標移動到窗口外，隱藏
            {
                if (this.Location.Y <= QQ_T)//上
                {
                    this.Location = new Point(this.Location.X, QQ_T - this.Height);
                    this.QQ_MODE = 3;
                }
                else if (this.Location.X <= QQ_T)//左
                {
                    this.Location = new Point(QQ_T - this.Width, this.Location.Y);
                    this.QQ_MODE = 1;
                }
                else if (this.Location.X >= Screen.PrimaryScreen.WorkingArea.Width - this.Width - QQ_T)//右
                {
                    this.Location = new Point(Screen.PrimaryScreen.WorkingArea.Width - QQ_T, this.Location.Y);
                    this.QQ_MODE = 2;
                }
                else
                {
                    this.QQ_MODE = 0;
                }
            }
        }

        //移動窗體時，解決QQ邏輯
        private void Form1_Move(object sender, EventArgs e)
        {
            this.QQ_MODE = 0;
        }

        //表單自動停靠在左上右邊 類似QQ的收縮功能 SP
    }
}
