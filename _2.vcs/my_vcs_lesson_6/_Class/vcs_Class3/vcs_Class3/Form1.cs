using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Threading;
using System.Timers;

namespace vcs_Class3
{
    public partial class Form1 : Form
    {
        TimerAlarm timeAlarm = new TimerAlarm();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        void show_item_location()
        {
            //設定執行後的表單起始位置
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point(0, 0);

            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 170 + 10;
            dy = 70 + 10;

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

            button10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 9);

            //最大化螢幕
            //this.FormBorderStyle = FormBorderStyle.None;
            //this.WindowState = FormWindowState.Maximized;

            int w = 0;
            int h = 0;

            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            w = this.ClientSize.Width - richTextBox1.Location.X - 10;   //border : 10
            h = this.ClientSize.Height - richTextBox1.Location.Y - 10;   //border : 10
            richTextBox1.Size = new Size(w, h);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            bt_exit_setup();
        }

        void bt_exit_setup()
        {
            int width = 5;
            int w = 50; //設定按鈕大小 W
            int h = 50; //設定按鈕大小 H

            Button bt_exit = new Button();  // 實例化按鈕
            bt_exit.Size = new Size(w, h);
            bt_exit.Text = "";
            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            Pen p = new Pen(Color.Red, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            g.DrawLine(p, 0, 0, w - 1, h - 1);
            g.DrawLine(p, w - 1, 0, 0, h - 1);
            bt_exit.Image = bmp;

            bt_exit.Location = new Point(this.ClientSize.Width - bt_exit.Width, 0);
            bt_exit.Click += bt_exit_Click;     // 加入按鈕事件

            this.Controls.Add(bt_exit); // 將按鈕加入表單
            bt_exit.BringToFront();     //移到最上層
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //Class 範例 0 ST
        public class Classmate  //事件訂閱者
        {
            private string name;
            public Classmate(string Name)
            {
                name = Name;
            }
            public void SendResponse()  //事件處理函數，要與自定義委托類型匹配
            {
                Console.WriteLine("來自：" + this.name + "的回復: 已經收到邀請，隨時可以開始！");
            }
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //c
            Classmate classmate1 = new Classmate("Alice");
            Classmate classmate2 = new Classmate("Banana");
            Classmate classmate3 = new Classmate("Cherry");
            Classmate classmate4 = new Classmate("Daisy");

            classmate1.SendResponse();
            classmate2.SendResponse();
            classmate3.SendResponse();
            classmate4.SendResponse();

        }
        //Class 範例 0 SP

        //Class 範例 1 ST
        public class Person
        {
            public string Name { get; set; }
            public int Age { get; set; }
            public int Weight { get; set; }
            public int Height { get; set; }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Person p = new Person() { Name = "Hong", Age = 25, Weight = 65, Height = 170 };
        }
        //Class 範例 1 SP

        //Class 範例 2 ST
        public class Shoe
        {
            public string Color;
        }

        public class Dude
        {
            public string Name;
            public Shoe RightShoe;
            public Shoe LeftShoe;

            public Dude CopyDude()
            {
                Dude newPerson = new Dude();
                newPerson.Name = Name;
                newPerson.LeftShoe = LeftShoe;
                newPerson.RightShoe = RightShoe;

                return newPerson;
            }

            public override string ToString()
            {
                return (Name + " : Dude!, I have a " + RightShoe.Color + " shoe on my right foot, and a " + LeftShoe.Color + " on my left foot.");
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Dude Bill = new Dude();
            Bill.Name = "Bill";
            Bill.LeftShoe = new Shoe();
            Bill.RightShoe = new Shoe();
            Bill.LeftShoe.Color = "Blue";
            Bill.RightShoe.Color = "Blue";

            Dude Ted = Bill.CopyDude();
            Ted.Name = "Ted";
            Ted.LeftShoe.Color = "Red";
            Ted.RightShoe.Color = "Red";

            richTextBox1.Text += "Bill\n" + Bill.ToString() + "\n";
            richTextBox1.Text += "Ted\n" + Ted.ToString() + "\n";
        }
        //Class 範例 2 SP

        //Class 範例 3 ST
        public class People
        {
            private string Id;
            private string Name;
            private string Address;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            DataTable dt = new DataTable();
            dt.Columns.Add("Id", typeof(string));
            dt.Columns.Add("Name", typeof(string));
            dt.Columns.Add("Address", typeof(string));
            dt.PrimaryKey = new DataColumn[] { dt.Columns[0] };

            dt.Rows.Add("0001", "張三", "武漢市");
            dt.Rows.Add("0002", "李四", "北京市");
            dt.AcceptChanges();
            dt.Rows.Add("0003", "王五", "深圳市");

            //List<People> allPeople = new List<People>();
            //List<People> allPeople = new List<People>();


            /*
            List<People> allPeople = new List<People>()
            {
              new People(){ Id="0001", Name="張三", Address ="武漢市"},
              new People(){ Id="0002", Name="李四", Address ="北京市"},
              new People(){ Id="0003", Name="王五", Address ="深圳市"}
            };
            */
        }
        //Class 範例 3 SP

        //Class 範例 4 ST
        class P
        {
            private string pname;
            public string Name
            {
                get
                {
                    return "name : " + pname;
                }
                set
                {
                    pname = value;
                }
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //Class 範例 4
            P obj = new P();
            obj.Name = "david wang";            //使用到set
            Console.WriteLine(obj.Name);        //使用到get
        }
        //Class 範例 4 SP

        //Class 範例 5 ST
        /*
        理解多態。
        首先，我們先來看下怎樣用虛方法實現多態

        我們都知道，喜鵲（Magpie）、老鷹（Eagle）、企鵝（Penguin）都是屬於鳥類，我們可以根據這三者的共有特性提取出鳥類（Bird）做為父類，喜鵲喜歡吃蟲子，老鷹喜歡吃肉，企鵝喜歡吃魚。
        */

        //創建基類Bird如下，添加一個虛方法Eat():

        /*
        /// <summary>
        /// 鳥類：父類
        /// </summary>
        public class Bird
        {
            /// <summary>
            /// 吃：虛方法
            /// </summary>
            public virtual void Eat()
            {
                Console.WriteLine("我是一只小小鳥，我喜歡吃蟲子~");
            }
        }
        */

        /// <summary>
        /// 鳥類：基類
        /// </summary>
        public abstract class Bird
        {
            /// <summary>
            /// 吃：抽象方法
            /// </summary>
            public abstract void Eat(); //抽象類Bird內添加一個Eat()抽象方法，沒有方法體。也不能實例化。
        }

        //創建子類Magpie如下，繼承父類Bird，重寫父類Bird中的虛方法Eat()：

        /// <summary>
        /// 飛 接口
        /// </summary>
        public interface IFlyable
        {
            void Fly();
        }

        /*
        /// <summary>
        /// 喜鵲：子類
        /// </summary>
        public class Magpie : Bird
        {
            /// <summary>
            /// 重寫父類中Eat方法
            /// </summary>
            public override void Eat()
            {
                Console.WriteLine("我是一只喜鵲，我喜歡吃蟲子~");
            }
        }

        //創建一個子類Eagle如下，繼承父類Bird，重寫父類Bird中的虛方法Eat()：

        /// <summary>
        /// 老鷹：子類
        /// </summary>
        public class Eagle : Bird
        {
            /// <summary>
            /// 重寫父類中Eat方法
            /// </summary>
            public override void Eat()
            {
                Console.WriteLine("我是一只老鷹，我喜歡吃肉~");
            }
        }
        */

        //喜鵲Magpie實現IFlyable接口，代碼如下：

        /// <summary>
        /// 喜鵲：子類，實現IFlyable接口
        /// </summary>
        public class Magpie : Bird, IFlyable
        {
            /// <summary>
            /// 重寫父類Bird中Eat方法
            /// </summary>
            public override void Eat()
            {
                Console.WriteLine("我是一只喜鵲，我喜歡吃蟲子~");
            }
            /// <summary>
            /// 實現 IFlyable接口方法
            /// </summary>
            public void Fly()
            {
                Console.WriteLine("我是一只喜鵲，我可以飛哦~~");
            }
        }

        //老鷹Eagle實現IFlyable接口，代碼如下：

        /// <summary>
        /// 老鷹：子類實現飛接口
        /// </summary>
        public class Eagle : Bird, IFlyable
        {
            /// <summary>
            /// 重寫父類Bird中Eat方法
            /// </summary>
            public override void Eat()
            {
                Console.WriteLine("我是一只老鷹，我喜歡吃肉~");
            }

            /// <summary>
            /// 實現 IFlyable接口方法
            /// </summary>
            public void Fly()
            {
                Console.WriteLine("我是一只老鷹，我可以飛哦~~");
            }
        }

        //創建一個子類Penguin如下，繼承父類Bird，重寫父類Bird中的虛方法Eat()：

        /// <summary>
        /// 企鵝：子類
        /// </summary>
        public class Penguin : Bird
        {
            /// <summary>
            /// 重寫父類中Eat方法
            /// </summary>
            public override void Eat()
            {
                Console.WriteLine("我是一只小企鵝，我喜歡吃魚~");
            }
        }

        /// <summary>
        /// 飛機類，實現IFlyable接口
        /// </summary>
        public class Plane : IFlyable
        {
            /// <summary>
            /// 實現接口方法
            /// </summary>
            public void Fly()
            {
                Console.WriteLine("我是一架飛機，我也能飛~~");
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //Class 範例 5
            //創建一個Bird基類數組，添加基類Bird對象，Magpie對象，Eagle對象，Penguin對象
            Bird[] birds = { 
                       //new Bird(),    用Abstract, Bird就不能創建對象了
                       new Magpie(),
                       new Eagle(),
                       new Penguin()
            };
            //遍歷一下birds數組
            foreach (Bird bird in birds)
            {
                bird.Eat();
            }

            //創建一個IFlyable接口數組，添加 Magpie對象，Eagle對象
            IFlyable[] flys = { 
                       new Magpie(),
                       new Eagle()
                              };
            //遍歷一下flys數組
            foreach (IFlyable fly in flys)
            {
                fly.Fly();
            }


            //創建一個IFlyable接口數組，添加 Magpie對象，Eagle對象，Plane對象
            IFlyable[] flys2 = { 
                           new Magpie(),
                           new Eagle(),
                           new Plane()
            };
            //遍歷一下flys數組
            foreach (IFlyable fly in flys2)
            {
                fly.Fly();
            }
        }
        //Class 範例 5 SP

        private void button6_Click(object sender, EventArgs e)
        {
            //Class 範例 6 TimerAlarm

            timeAlarm = new TimerAlarm();
            timeAlarm.AlarmTime = FormatConvert.inputToSeconds("12:34:56");

            timeAlarm.Message = "AAAAAAAAA";

            if (timeAlarm.Countdown > 0)
            {
                this.timer6.Enabled = true;
            }

        }

        private void button7_Click(object sender, EventArgs e)
        {

        }

        private void button8_Click(object sender, EventArgs e)
        {

        }

        private void button9_Click(object sender, EventArgs e)
        {

        }

        private void button10_Click(object sender, EventArgs e)
        {

        }

        private void button11_Click(object sender, EventArgs e)
        {

        }

        private void button12_Click(object sender, EventArgs e)
        {

        }

        private void button13_Click(object sender, EventArgs e)
        {

        }

        private void button14_Click(object sender, EventArgs e)
        {

        }

        private void button15_Click(object sender, EventArgs e)
        {

        }

        private void button16_Click(object sender, EventArgs e)
        {

        }

        private void button17_Click(object sender, EventArgs e)
        {

        }

        private void button18_Click(object sender, EventArgs e)
        {

        }

        private void button19_Click(object sender, EventArgs e)
        {

        }

        private void button20_Click(object sender, EventArgs e)
        {

        }

        private void button21_Click(object sender, EventArgs e)
        {

        }

        private void button22_Click(object sender, EventArgs e)
        {

        }

        private void button23_Click(object sender, EventArgs e)
        {

        }

        private void timer6_Tick(object sender, EventArgs e)
        {
            //動態顯示剩下的時間
            if (timeAlarm.Countdown >= 0)
            {
                richTextBox1.Text += FormatConvert.secondsToTime(timeAlarm.Countdown) + " ";
            }
            else
            {

                this.timer6.Enabled = false;
            }
        }
    }

    public class TimerAlarm
    {
        private int clockTime = 0;
        private int alarmTime = 0;
        private string message = "时间到了";
        private System.Timers.Timer timerClock = new System.Timers.Timer();

        public int AlarmTime
        {
            set
            {
                alarmTime = value;
            }
        }

        public int ClockTime
        {
            set
            {
                clockTime = value;
            }
        }

        public string Message
        {
            set
            {
                message = value;
            }
        }

        public int Countdown
        {
            get
            {
                return alarmTime - clockTime;
            }
        }

        public TimerAlarm()
        {
            //MessageBox.Show("TimeAlarm start.");
            timerClock.Elapsed += new ElapsedEventHandler(OnTimer);
            timerClock.Interval = 1000;
            timerClock.Enabled = true;
        }

        public void OnTimer(Object source, ElapsedEventArgs e)
        {
            try
            {
                clockTime++;
                if (clockTime == alarmTime)
                {
                    MessageBox.Show(message, "时间到了", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                }
            }

            catch (Exception ex)
            {
                MessageBox.Show("OnTimer(): " + ex.Message);
            }
        }

        public void StopTimer()
        {
            timerClock.Enabled = false;
        }
    }

    public class FormatConvert
    {
        //inputToSeconds()将一个string型的时间字串转换成一共有多少秒。
        public static int inputToSeconds(string timerInput)
        {
            string[] timeArray = new string[3];
            int minutes = 0;
            int hours = 0;
            int seconds = 0;
            int occurence = 0;
            int length = 0;
            int totalTime = 0;

            occurence = timerInput.LastIndexOf(":");
            length = timerInput.Length;

            //Check for invalid input
            if (occurence == -1 || length != 8)
            {
                MessageBox.Show("Invalid Time Format.");
            }
            else
            {
                timeArray = timerInput.Split(':');
                seconds = Convert.ToInt32(timeArray[2]);
                minutes = Convert.ToInt32(timeArray[1]);
                hours = Convert.ToInt32(timeArray[0]);

                totalTime += seconds;
                totalTime += minutes * 60;
                totalTime += (hours * 60) * 60;
            }
            return totalTime;
        }

        //secondsToTime方法是把秒转换一个时间格式的字串返回。
        public static string secondsToTime(int seconds)
        {
            int minutes = 0;
            int hours = 0;
            while (seconds >= 60)
            {
                minutes += 1;
                seconds -= 60;
            }

            while (minutes >= 60)
            {
                hours += 1;
                minutes -= 60;
            }

            string strHours = hours.ToString();
            string strMinutes = minutes.ToString();
            string strSeconds = seconds.ToString();

            if (strHours.Length < 2)
                strHours = "0" + strHours;

            if (strMinutes.Length < 2)
                strMinutes = "0" + strMinutes;

            if (strSeconds.Length < 2)
                strSeconds = "0" + strSeconds;

            return strHours + ":" + strMinutes + ":" + strSeconds;
        }
    }
}
