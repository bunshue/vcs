using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Runtime.InteropServices;

namespace TaskMessageWindow
{
    public partial class MainForm : Form
    {
        public MainForm()
        {
            InitializeComponent();
            //开启显示提示窗口的计时器
            displayCounter.Start();
            //初始化工作区的大小
            System.Drawing.Rectangle rect = System.Windows.Forms.Screen.GetWorkingArea(this);//实例化一个当前窗口的对象
            this.Rect = new System.Drawing.Rectangle(rect.Right - this.Width - 1,rect.Bottom - this.Height - 1,this.Width,this.Height); //为实例化的对象创建工作区域
        }

        #region 声明的变量
        public static int SW_SHOWNOACTIVATE = 4;//该变量决定窗体的显示方式
        public static int CurrentState;//该变量标识当前窗口状态
        public static bool MainFormFlag=true ;
        private System.Drawing.Rectangle Rect;//定义一个存储矩形框的区域
        private FormState InfoStyle = FormState.Hide;//定义变量为隐藏
        public static bool MouseState; //该变量标识当前鼠标状态
        bool IconFlag = true;//用来标识图标闪动
        public static bool IconFlickerFlag;//运用本标识避免单击“关闭”按钮时弹出訊息框
        #endregion

        #region 声明API函数
        [DllImportAttribute("user32.dll")]
        private static extern Boolean ShowWindow(IntPtr hwnd,Int32 cmdShow);  //该方法用来显示窗体
        #endregion

        #region 定义标识窗体移动状态的枚举值
        protected enum FormState
        {
            //隐藏窗体
            Hide = 0,
            //显示窗体
            Display = 1,
            //隐藏窗体中
            Hiding=3,
            //显示窗体中
            Displaying = 4,
        }
        #endregion

        #region 鼠标控制图片的变化
        private void pictureBox1_MouseEnter(object sender,EventArgs e)
        {
            pictureBox1.Image = imageList1.Images[1];  //设定当鼠标进入PictureBox控件时PictureBox控件的图片
        }

        private void pictureBox1_MouseLeave(object sender,EventArgs e)
        {
            pictureBox1.Image = imageList1.Images[0];  //设定当鼠标离开PictureBox控件时PictureBox控件的图片
        }
        #endregion

        #region 用属性标识当前状态
        protected FormState FormNowState
        {
            get { return this.InfoStyle; }   //返回窗体的当前状态
            set { this.InfoStyle = value; }  //设定窗体当前状态的值
        }
        #endregion

        #region 显示窗体
        public void ShowNewWindow()
        {
            switch(FormNowState) //判断当前窗体处于那种状态
            {
                case FormState.Hide://当提示窗体的状态为隐藏时
                    this.FormNowState = FormState.Displaying;//设置提示窗体的状态为显示中
                    this.SetBounds(Rect.X,Rect.Y + Rect.Height,Rect.Width,0);//显示提示窗体，并把它放在屏幕底端
                    ShowWindow(this.Handle,4);      //显示窗体
                    displayCounter.Interval = 100;   //设定时间事件的频率为100ms一次
                    displayCounter.Start();         //启动计时器displayCounter          
                    break;
                case FormState.Display://当提示窗体的状态为显示时
                    displayCounter.Stop();          //停止计时器displayCounter
                    displayCounter.Interval = 5000;  //设定时间事件的频率为50000ms一次
                    displayCounter.Start();         //启动计时器displayCounter
                    break;
            }
            taskBarIcon.Icon = Properties.Resources._1;//设定托盘图标
        }
        #endregion

        #region 关闭窗体
        public void CloseNewWindow()
        {
            base.Hide();//隐藏该窗体
            iconCounter.Enabled = false;//设定计时器iconCounter不可用
            taskBarIcon.Icon = Properties.Resources._2;//设定托盘图标
            MainForm.IconFlickerFlag = false;     //更改静态变量IconFlickerFlag的值
        }
        #endregion

        private void pictureBox1_Click(object sender,EventArgs e)
        {
            this.Hide();//隐藏该窗体
            iconCounter.Enabled = false;//设定计时器iconCounter不可用
            CloseNewWindow();//调用关闭窗体方法
        }

        #region 任务栏中的图标进行闪烁
        private void iconCounter_Tick(object sender,EventArgs e)
        {
            if(IconFlag)  //当该值为真时
            {
                taskBarIcon.Icon = Properties.Resources._1;//设定托盘控件taskBarIcon的图标
                IconFlag = false;                       //修改该值为假
            }
            else                                            //当该值为假时
            {
                taskBarIcon.Icon = Properties.Resources._2; //设定托盘控件taskBarIcon的图标
                IconFlag = true;                             //修改该值为真
            }
        }
        #endregion

        public void IconFlicker()//自定义方法用来使托盘图标闪烁
        {
            if(MainForm.IconFlickerFlag != false)     //当托盘闪动图标为真时
            {
                taskBarIcon.Icon = Properties.Resources._1;//托盘图标显示为图像
                iconCounter.Enabled = true;//启动托盘图标的Timer
                titleInform.Text = TaskMessageWindow.MainFormTitle;//在titleInform中显示通知标题
                contentInform.Text = TaskMessageWindow.MainFormContent;//在cententInform中显示通知内容
            }
        }
        //控制窗体的显示
        private void taskBarIcon_MouseDoubleClick(object sender,MouseEventArgs e)
        {
            iconCounter.Enabled = false;//停止闪烁托盘图标计时器
            taskBarIcon.Icon = Properties.Resources._2;//清空托盘中原有的图像
            ShowNewWindow();//调用显示窗体方法
        }
        //从右下角显示窗体
        private void displayCounter_Tick(object sender,EventArgs e)
        {
            switch(this.FormNowState)  //判断当前窗体的状态
            {
                case FormState.Display:  //当窗体处于显示状态时
                    this.displayCounter.Start();//启动计时器displayCounter
                    this.displayCounter.Interval = 100;//设定计时器的时间事件间隔
                    if(!MouseState)     //当鼠标不在窗体上时
                    {
                        this.FormNowState = FormState.Hiding;//隐藏当前窗体
                    }
                    this.displayCounter.Start();            //启动计时器displayCounter
                    break;
                case FormState.Displaying:                  //当窗体处于显示中状态时
                    if(this.Height <= this.Rect.Height - 12) //如果窗体没有完全显示
                    {
                        this.SetBounds(Rect.X,this.Top - 12,Rect.Width,this.Height + 12);//设定窗体的边界
                    }
                    else                                     //当窗体完全显示时
                    {
                        displayCounter.Stop();                //停止计时器displayCounter
                        this.SetBounds(Rect.X,Rect.Y,Rect.Width,Rect.Height);//设定当前窗体的边界
                        this.FormNowState = FormState.Display;  //修改当前窗体所处的状态值
                        this.displayCounter.Interval = 5000;    //设定计时器的时间事件间隔
                        this.displayCounter.Start();           //启动计时器低displayCounter
                    }
                    break;
                case FormState.Hiding:                       //当窗体处于隐藏中时
                    if(MouseState)                             //当鼠标在窗体上边时
                    {
                        this.FormNowState = FormState.Displaying; //修改窗体的状态为显示中
                    }
                    else                                         //当鼠标离开窗体时
                    {
                        if(this.Top <= this.Rect.Bottom - 12)        //当窗体没有完全隐藏时
                        {
                            this.SetBounds(Rect.X,this.Top + 12,Rect.Width,this.Height - 12);//设定控件的边界
                        }
                        else                                    //当窗体完全隐藏时
                        {
                            this.Hide();                         //隐藏当前窗体
                            this.FormNowState = FormState.Hide;     //设定当前的窗体状态
                        }
                    }
                    break;
            }
        }

        private void MainForm_MouseEnter(object sender,EventArgs e)
        {
            MouseState = true;     //设定bool型变量MouseState的值为真
        }

        private void MainForm_MouseLeave(object sender,EventArgs e)
        {
            MouseState = false;   //设定bool型变量MouseState的值为假
        }

        private void MainForm_Load(object sender, EventArgs e)
        {

        }
    }
}
