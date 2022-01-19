using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;


//滾動提示窗口

//加入/Windows Form

/*
Form1之FormBorderStyle屬性設置為None（無邊框模式）
Form1之TopMost屬性（總在最上方）屬性設置為True
Form1之把ShowInTaskbar屬性(是否在 Windows 任務欄中顯示窗體)設置為False

1個label
3個timer

label
並在窗體上加上你打算要顯示的文字（實際應用中一般是在程序中動態加載），將窗體的背景設置為你想要的圖片和合適的大小。
timer
最後再放上三個Timer控件，其中，timer1控制窗體滾出的動畫，timer2控制窗體停留時間，timer3控制窗體的滾入動畫，將它們的Interval屬性設置為10
*/

namespace vcs_Form7_ScrollShow
{
    public partial class Form2 : Form
    {
        private int heightMax, widthMax;

        public int HeightMax
        {
            set
            {
                heightMax = value;
            }
            get
            {
                return heightMax;
            }
        }

        public int WidthMax
        {
            set
            {
                widthMax = value;
            }
            get
            {
                return widthMax;
            }
        }

        public void ScrollShow()
        {
            this.Width = widthMax;
            this.Height = 0;
            this.Show();
            this.timer1.Enabled = true;
        }

        //添加一個StayTime屬性設置窗體停留時間（默認為5秒）：

        public int StayTime = 5000;

        //添加ScrollUp和ScrollDown方法來編寫窗體如何滾出和滾入：

        private void ScrollUp()
        {
            if (Height < heightMax)
            {
                this.Height += 3;
                this.Location = new Point(this.Location.X, this.Location.Y - 3);
            }
            else
            {
                this.timer1.Enabled = false;
                this.timer2.Enabled = true;
            }
        }

        private void ScrollDown()
        {
            if (Height > 3)
            {
                this.Height -= 3;
                this.Location = new Point(this.Location.X, this.Location.Y + 3);
            }
            else
            {
                this.timer3.Enabled = false;
                this.Close();
            }
        }

        public Form2()
        {
            InitializeComponent();
        }

        private void Form2_Load(object sender, EventArgs e)
        {
            Screen[] screens = Screen.AllScreens;
            Screen screen = screens[0];//獲取屏幕變量
            this.Location = new Point(screen.WorkingArea.Width - widthMax - 20, screen.WorkingArea.Height - 34);//WorkingArea為Windows桌面的工作區
            this.timer2.Interval = StayTime;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            ScrollUp();
        }

        private void timer2_Tick(object sender, EventArgs e)
        {
            timer2.Enabled = false;
            timer3.Enabled = true;
        }

        private void timer3_Tick(object sender, EventArgs e)
        {
            ScrollDown();
        }
    }
}

