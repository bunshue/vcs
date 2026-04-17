using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Collections;   //for IEnumerable

namespace vcs_ComboBox0
{
    public partial class Form1 : Form
    {
        private ImageList G_ImageList;//聲明ImageList字段

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            G_ImageList = new ImageList();//創建ImageList對象
            G_ImageList.Images.Add(Properties.Resources.a);//添加圖片
            G_ImageList.Images.Add(Properties.Resources.b);//添加圖片
            G_ImageList.Images.Add(Properties.Resources.c);//添加圖片
            G_ImageList.Images.Add(Properties.Resources.d);//添加圖片

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //字串一維陣列轉comboBox
            //初始化字串一維陣列，再以AddRange()方法加入
            //字串一維陣列
            string[] cities = new string[] { "台北", "新竹", "台中", "台南", "高雄" };
            comboBox0.Items.AddRange(cities);

            //預設選項為第0項
            //comboBox1a.Text = cities[0];

            //預設選項包含關鍵字
            comboBox0.SelectedItem = FindItemContaining(comboBox0.Items, "竹");

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            // 建構 comboBox1 物件，並設定相關的屬性
            //comboBox1.Location = new System.Drawing.Point(15, 15);
            comboBox1.Name = "comboBox1";
            comboBox1.Size = new System.Drawing.Size(200, 50);
            comboBox1.TabIndex = 0;
            comboBox1.Text = "無";

            //加入 comboBox 項目
            string[] installs = new string[] { "滑鼠", "鍵盤", "網卡", "螢幕", "音效卡" };
            comboBox1.Items.AddRange(installs);

            // 預設ComboBox物件的Text為第1個選項
            comboBox1.SelectedIndex = 0;

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //從陣列抓資料到combobox清單內
            //系統內建的全部滑鼠游標圖形
            //系統內建資料轉comboBox
            Cursor[] cursorList = new Cursor[] {
                Cursors.AppStarting, Cursors.Arrow, Cursors.Cross,
                Cursors.Default, Cursors.Hand, Cursors.Help,
                Cursors.HSplit, Cursors.IBeam, Cursors.No,
                Cursors.NoMove2D, Cursors.NoMoveHoriz, Cursors.NoMoveVert,
                Cursors.PanEast, Cursors.PanNE, Cursors.PanNorth,
                Cursors.PanNW, Cursors.PanSE, Cursors.PanSouth,
                Cursors.PanSW, Cursors.PanWest, Cursors.SizeAll,
                Cursors.SizeNESW, Cursors.SizeNS, Cursors.SizeNWSE,
                Cursors.SizeWE, Cursors.UpArrow, Cursors.VSplit, Cursors.WaitCursor};

            foreach (Cursor cursor in cursorList)
            {
                comboBox2.Items.Add(cursor);  // 加入到 comboBox1b 清單內
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //用ComboBox控制元件製作類似瀏覽器的網址輸入框
            comboBox3.Items.Add("http://www.yahoo.com/");//向ComboBox控件中添加網址「http://www.baidu.com/」
            comboBox3.Items.Add("http://www.sina.com/");//向ComboBox控件中添加網址「http://www.sina.com.cn/」
            comboBox3.Items.Add("http://www.google.com/");//向ComboBox控件中添加網址「http://www.163.com/」
            comboBox3.Items.Add("http://www.microsoft.com/");//向ComboBox控件中添加網址「http://www.qq.com/」

            /*
            //comboBox7
            comboBox7.Items.Add("https://www.google.com/");
            comboBox7.Items.Add("http://www.yahoo.com.tw/");
            comboBox7.Items.Add("http://www.baidu.com/");
            comboBox7.Items.Add("http://www.sina.com.cn/");
            comboBox7.Items.Add("http://www.163.com/");
            comboBox7.Items.Add("http://www.qq.com/");
            */

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            // 使用 DataSource
            // 取得或設定此 ComboBox資料來源
            // Initialize an array with data to bind to the combo box.
            var daysOfWeek = new[] { "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday" };

            // Initialize combo box
            var comboBox4 = new ComboBox
            {
                DataSource = daysOfWeek,
                Location = new System.Drawing.Point(20, 450),
                Name = "comboBox",
                Size = new System.Drawing.Size(200, 100),
                DropDownStyle = ComboBoxStyle.DropDownList
            };
            this.Controls.Add(comboBox4);

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //comboBox4b

            string[] strCall = { "AAA", "BBB", "CCC", "DDD" };
            comboBox4b.DataSource = strCall;


            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個



        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;
            int dd = 30;

            x_st = 20;
            y_st = 20;
            dx = 200;
            dy = 100;

            label0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            comboBox0.Location = new Point(x_st + dx * 0, y_st + dy * 0 + dd);
            label1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            comboBox1.Location = new Point(x_st + dx * 0, y_st + dy * 1 + dd);
            label2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            comboBox2.Location = new Point(x_st + dx * 0, y_st + dy * 2 + dd);
            label3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            comboBox3.Location = new Point(x_st + dx * 0, y_st + dy * 3 + dd);
            label4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            comboBox4b.Location = new Point(x_st + dx * 0, y_st + dy * 5 + dd);
            richTextBox1.Text += "location : " + (new Point(x_st + dx * 0, y_st + dy * 4 + dd)).ToString() + "\n";

            int w = 400;
            int h = 150;

            x_st = 10;
            y_st = 10;
            dx = w + 10;
            dy = h + 10;

            richTextBox1.Size = new Size(320, 600);
            richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1180, 800);
            this.Text = "vcs_ComboBox0";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private object FindItemContaining(IEnumerable items, string target)
        {
            foreach (object item in items)
            {
                if (item.ToString().Contains(target))
                {
                    return item;
                }
            }
            return null;
        }

        //6060

        private void comboBox1_DropDown(object sender, EventArgs e)
        {
            System.Windows.Forms.ComboBox myCombo = (System.Windows.Forms.ComboBox)sender;
            richTextBox1.Text += "DropDown : " + myCombo.Text + "\n";
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            System.Windows.Forms.ComboBox myCombo = (System.Windows.Forms.ComboBox)sender;
            richTextBox1.Text += "SelectedIndexChanged : " + myCombo.Text + "\n";
        }

        private void comboBox1_DrawItem(object sender, DrawItemEventArgs e)
        {
            //都不會跑到這~~~~~~~~~~~~~~~

            if (G_ImageList != null)
            {
                richTextBox1.Text += "AAA\n";

                Graphics g = e.Graphics;               //得到繪圖物件
                Rectangle rec = e.Bounds;              //得到繪圖範圍
                Size imageSize = G_ImageList.ImageSize;//取得圖像大小
                if (e.Index >= 0)                      //判斷是否有繪製項 
                {
                    Font font = new Font("微軟正黑體", 50, FontStyle.Bold);//建立字體物件
                    string s = comboBox1.Items[e.Index].ToString();        //得到繪製項的字串
                    DrawItemState dis = e.State;
                    if (e.State == (DrawItemState.NoAccelerator | DrawItemState.NoFocusRect))
                    {
                        g.FillRectangle(new SolidBrush(Color.LightBlue), rec); //畫item背景
                        G_ImageList.Draw(g, rec.Left, rec.Top, e.Index);                //繪製圖像
                        e.Graphics.DrawString(s, font, new SolidBrush(Color.Black),     //顯示字串
                            rec.Left + imageSize.Width, rec.Top);
                        e.DrawFocusRectangle();                                         //顯示取得焦點時的虛線框
                    }
                    else
                    {
                        g.FillRectangle(new SolidBrush(Color.LightGreen), rec);//畫item背景
                        G_ImageList.Draw(e.Graphics, rec.Left, rec.Top, e.Index);       //繪製圖像
                        e.Graphics.DrawString(s, font, new SolidBrush(Color.Black),     //顯示字串 
                            rec.Left + imageSize.Width, rec.Top);
                        e.DrawFocusRectangle();                                         //顯示取得焦點時的虛線框 
                    }
                }
            }
            else
            {
                richTextBox1.Text += "XXXXX\n";

            }
        }

        //6060

        private bool EditState = false;//定義一個全局變量標識
        private void comboBox3_KeyDown(object sender, KeyEventArgs e)
        {
            EditState = (e.KeyCode != Keys.Back && e.KeyCode != Keys.Delete);//當按鍵既不是Back鍵又不是Delete鍵時
            comboBox3.DroppedDown = true;//當有按鍵被按下時顯示下拉列表
        }

        private void comboBox3_TextChanged(object sender, EventArgs e)
        {
            if (EditState)//當變量的值為真時
            {
                string importText = comboBox3.Text;//獲得輸入的文本
                int index = comboBox3.FindString(importText);//在ComboBox集合中查找匹配的文本
                if (index >= 0)                        //當有查找結果時 
                {
                    EditState = false;                //關閉編輯狀態
                    comboBox3.SelectedIndex = index;    //找到對應項
                    EditState = true;                 //打開編輯狀態
                    comboBox3.Select(importText.Length, comboBox3.Text.Length);//設定文本的選擇長度
                }
            }
        }

        /*
        private bool State = false;//定义一个全局变量标识
        private void comboBox7_TextChanged(object sender, EventArgs e)
        {
            if (State == true)//当变量的值为真时
            {
                string importText = comboBox7.Text;//获得输入的文本
                int index = comboBox7.FindString(importText);//在ComboBox集合中查找匹配的文本
                if (index >= 0)//当有查找结果时 
                {
                    State = false;//关闭编辑状态
                    comboBox7.SelectedIndex = index;//找到对应项
                    State = true;//打开编辑状态
                    comboBox7.Select(importText.Length, comboBox7.Text.Length);//设定文本的选择长度
                }
            }

        }

        private void comboBox7_KeyDown(object sender, KeyEventArgs e)
        {
            State = (e.KeyCode != Keys.Back && e.KeyCode != Keys.Delete);//当按键既不是Back键又不是Delete键时
            comboBox7.DroppedDown = true;//当有按键被按下时显示下拉列表
        }
        */


    }
}
