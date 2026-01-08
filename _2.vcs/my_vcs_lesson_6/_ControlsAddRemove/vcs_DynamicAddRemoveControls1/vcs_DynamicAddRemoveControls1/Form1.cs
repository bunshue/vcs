using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for Directory

//所有的PNG檔要選屬性/複製到輸出目錄/選 有更新時才複製


//將控件（如按鈕、文字框等）動態加入容器（如 Form、Panel 或 GroupBox）

namespace vcs_DynamicAddRemoveControls1
{
    public partial class Form1 : Form
    {
        private const int COLUMNS = 7;      //1~99
        private const int ROWS = 8;         //1~99
        private const int PICTURE_WIDTH = 50 * COLUMNS;
        private const int PICTURE_HEIGHT = 50 * ROWS;
        private const int DD = PICTURE_WIDTH / COLUMNS;

        int[,] gray = new int[COLUMNS, ROWS];

        Bitmap bitmap1;
        PictureBox pictureBox1 = new PictureBox();
        Label label1 = new Label();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //動態產生button並且綁定click事件
            DynamicGenerateButton1();

            Add_Controls_pictureBox1();//加入控件 pictureBox1
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 370;
            y_st = 600;
            dx = 200 + 5;
            dy = 60 + 5;

            button4.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button5.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button2.Location = new Point(x_st + dx * 1, y_st + dy * 1);

            button7.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button8.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button9.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button10.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button11.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            button12.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            button13.Location = new Point(x_st + dx * 3, y_st + dy * 2);
            button14.Location = new Point(x_st + dx * 3, y_st + dy * 3);
            button30.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            button31.Location = new Point(x_st + dx * 4, y_st + dy * 1);
            button32.Location = new Point(x_st + dx * 4, y_st + dy * 2);
            button33.Location = new Point(x_st + dx * 4, y_st + dy * 3);

            x_st = 10;
            y_st = 600;
            dx = 200 + 5;
            dy = 60 + 5;

            y_st = 20;
            panel1.Size = new Size(280, 220);
            panel1.Location = new Point(1110, y_st + dy * 5);
            lb_panel.Location = new Point(1110, y_st + dy * 5 - 20);
            button31.BackColor = Color.Orange;
            button32.BackColor = Color.Orange;

            richTextBox1.Size = new Size(280, 640);
            richTextBox1.Location = new Point(1400, y_st + dy * 1);
            button18.Location = new Point(1400, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1710, 900);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        int cnt = 1;
        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            Button btn = new Button();

            //設定新控件的名稱和Text屬性，以及產生的位置
            btn.Left = e.X;
            btn.Top = e.Y;
            btn.Name = "Button " + cnt;
            btn.Text = "Button" + cnt;
            btn.Size = new Size(70, 35);

            //為產生的新的Button控件設定事件
            btn.Click += new EventHandler(btn_ClickEvent1);
            this.Controls.Add(btn);//將控件加入 到 表單 容器

            richTextBox1.Text += "新增控件 " + btn.Text + "\n";
            cnt++;
        }

        private void btn_ClickEvent1(object sender, EventArgs e)
        {
            if (sender.GetType() == typeof(Button))
            {
                Button btn = (Button)sender;//將觸發此事件的對象轉換為該Button對象
                richTextBox1.Text += "你按了 " + btn.Text + "\n";
                richTextBox1.Text += "你按了 " + btn.Name + "\n";
                /*
                richTextBox1.Text += "控件種類 : " + sender.ToString() + "\t";
                richTextBox1.Text += "索引 :  " + btn.TabIndex.ToString() + "\n";
                */
            }
        }

        private void btn_MouseEnter(object sender, EventArgs e)
        {
            Button btn = (Button)sender;
            btn.BackColor = Color.Yellow;    //設定按鈕的背景色
        }

        private void btn_MouseLeave(object sender, EventArgs e)
        {
            Button btn = (Button)sender;
            btn.BackColor = System.Drawing.SystemColors.ControlLight;    //設定按鈕的背景色
        }

        private void DynamicGenerateButton1()
        {
            int btn_size;
            int w = 60;
            int h = 60;

            btn_size = 400 / COLUMNS;

            if ((400 / ROWS) < btn_size)
                btn_size = 400 / ROWS;

            w = btn_size;
            h = btn_size;

            int LEFT_ANCHOR = 20;
            int TOP_ANCHOR = 20;

            richTextBox1.Text += "建立新表單並新增控件於其上\n";
            //當有多個按鈕需要產生時, 如何用loop方式動態產生, 並加入對應的click event
            //產生一個新的form, 並在該form上面產生MxN組的按鈕

            for (int j = 0; j < ROWS; j++)
            {
                for (int i = 0; i < COLUMNS; i++)
                {
                    // 實例化按鈕
                    Button btn = new Button();
                    // 設定按鈕參數
                    btn.Left = LEFT_ANCHOR + w * i;
                    btn.Top = TOP_ANCHOR + h * j;
                    btn.Width = w;
                    btn.Height = h;
                    btn.BackColor = Color.Gray;
                    btn.Tag = "dynamic" + i.ToString("D2") + "_" + j.ToString("D2");
                    btn.Name = "bt" + i.ToString("D2") + "_" + j.ToString("D2");
                    //btn.Click += new EventHandler(btn_ClickEvent4);// 加入按鈕事件   //same
                    btn.Click += btn_ClickEvent4;// 加入按鈕事件
                    this.AcceptButton = btn;
                    this.Controls.Add(btn);//將控件加入 到 表單 容器
                }
            }
        }

        void Add_Controls_pictureBox1()
        {
            // 實例化按鈕
            label1.Text = "動態加入pictureBox1";
            label1.AutoSize = true;
            label1.Left = 20;
            label1.Top = 445;
            this.Controls.Add(label1);//將控件加入 到 表單 容器

            pictureBox1.Size = new Size(340, 370);
            pictureBox1.BackColor = Color.Pink;

            pictureBox1.Left = 20;
            pictureBox1.Top = 470;

            pictureBox1.Tag = "dynamic";

            //this.AcceptButton = pictureBox1;
            this.Controls.Add(pictureBox1);//將控件加入 到 表單 容器
        }

        private void btn_ClickEvent4(object sender, EventArgs e)
        {
            Button btn = (Button)sender;
            richTextBox1.Text += "你按了 " + btn.Text + "\n";
            if (btn.BackColor == Color.Gray)
                btn.BackColor = Color.Blue;
            else
                btn.BackColor = Color.Gray;

            string tt = btn.Tag.ToString();

            if (tt != null)
            {
                int i = int.Parse(tt.Substring(7, 2));
                int j = int.Parse(tt.Substring(10, 2));
                richTextBox1.Text += "i = " + i.ToString() + ", j = " + j.ToString() + "\n";

                if (btn.BackColor == Color.Gray)
                {
                    //btn.BackColor = Color.Blue;
                    gray[i, j] = 0;
                }
                else
                {
                    //btn.BackColor = Color.Gray;
                    gray[i, j] = 1;
                }
            }

            richTextBox1.Text += "你按了按鈕 Name : " + btn.Name + "\n";

            // 把 sender 轉為 Button 並利用 Button.Name 來判斷是按下哪一個 Button
            string ButtonName = btn.Name;
            if (ButtonName == "bt00_00")
            {
                richTextBox1.Text += "你按了bt00_00\n";
            }
            else if (ButtonName == "bt01_01")
            {
                richTextBox1.Text += "你按了bt01_01\n";
            }
            else
            {
                richTextBox1.Text += "你按了其他button\n";
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            foreach (Control con in this.Controls)
            {
                System.String strControl = con.GetType().ToString();//获得控件的类型
                System.String strControlName = con.Name.ToString();//获得控件的名称
                //System.String strControlTag = con.Tag.ToString();//获得控件的標籤, 不能用此, 因為不一定有Tag可以ToString

                //richTextBox1.Text += "Type:\t" + strControl + "\tName:\t" + strControlName + "\tColor:\t" + con.BackColor + "\n";

                if (strControl == "System.Windows.Forms.Button")
                {
                    if (con.Tag != null)
                    {
                        if (con.Tag.ToString().Substring(0, 7) == "dynamic")
                        {
                            int i = int.Parse(con.Tag.ToString().Substring(7, 2));
                            int j = int.Parse(con.Tag.ToString().Substring(10, 2));
                            /*
                            richTextBox1.Text += "Type:\t" + strControl + "\tName:\t" + strControlName + "\tColor:\t" + con.BackColor + "\t";
                            richTextBox1.Text += "Tag:\t" + con.Tag + "\t";
                            richTextBox1.Text += "i:\t" + i.ToString() + "\t";
                            richTextBox1.Text += "j:\t" + j.ToString() + "\n";
                            */
                            if (con.BackColor == Color.Gray)
                                gray[i, j] = 0;
                            else
                                gray[i, j] = 1;
                        }
                    }
                }
            }
            draw2D_Array();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            int i;
            int j;
            for (j = 0; j < ROWS; j++)
            {
                for (i = 0; i < COLUMNS; i++)
                {
                    gray[i, j] = 0;
                }
            }

            foreach (Control con in this.Controls)
            {
                System.String strControl = con.GetType().ToString();//获得控件的类型
                System.String strControlName = con.Name.ToString();//获得控件的名称
                //System.String strControlTag = con.Tag.ToString();//获得控件的標籤, 不能用此, 因為不一定有Tag可以ToString

                //richTextBox1.Text += "Type:\t" + strControl + "\tName:\t" + strControlName + "\tColor:\t" + con.BackColor + "\n";
                //if (strControlTag == "dynamic")
                if (con.Tag != null)
                {
                    if (strControl == "System.Windows.Forms.Button")
                    {
                        if (con.Tag.ToString().Substring(0, 7) == "dynamic")
                        {
                            i = int.Parse(con.Tag.ToString().Substring(7, 2));
                            j = int.Parse(con.Tag.ToString().Substring(10, 2));

                            /*
                            richTextBox1.Text += "Type:\t" + strControl + "\tName:\t" + strControlName + "\tColor:\t" + con.BackColor + "\t";
                            richTextBox1.Text += "Tag:\t" + con.Tag + "\t";
                            richTextBox1.Text += "i:\t" + i.ToString() + "\t";
                            richTextBox1.Text += "j:\t" + j.ToString() + "\n";
                            */

                            gray[i, j] = 0;
                            con.BackColor = Color.Gray;
                        }
                    }
                }
            }
            draw2D_Array();
        }

        void draw2D_Array()
        {
            int i;
            int j;
            for (j = 0; j < ROWS; j++)
            {
                for (i = 0; i < COLUMNS; i++)
                {
                    richTextBox1.Text += gray[i, j].ToString() + " ";
                }
                richTextBox1.Text += "\n";
            }

            int xx;
            int yy;
            int width = PICTURE_WIDTH;
            int height = PICTURE_HEIGHT;

            pictureBox1.Size = new Size(width, height);
            bitmap1 = new Bitmap(width, height);

            byte aa = 255;
            byte rr = 0;
            byte gg = 0;
            byte bb = 0;

            for (yy = 0; yy < height; yy++)
            {
                for (xx = 0; xx < width; xx++)
                {
                    //Color p = Color.FromName("SlateBlue");
                    /*
                    Color p ;
                    p.A = (byte)(xx % 255);
                    p.R = (byte)(xx % 127 + 127);
                    p.G = (byte)(xx % 127);
                    p.B = (byte)(xx % 63);
                    */

                    //獲取像素的ＲＧＢ顏色值
                    //srcColor = srcBitmap.GetPixel(x, y);
                    //byte temp = (byte)(srcColor.R * .299 + srcColor.G * .587 + srcColor.B * .114);

                    //byte temp = (byte)((byte)(xx % 255) + (byte)(xx % 127 + 127) + (byte)(xx % 63));

                    //設置像素的ＲＧＢ顏色值
                    rr = (byte)(gray[xx / DD, yy / DD] * 255);
                    gg = (byte)(gray[xx / DD, yy / DD] * 255);
                    bb = (byte)(gray[xx / DD, yy / DD] * 255);
                    bitmap1.SetPixel(xx, yy, Color.FromArgb(aa, rr, gg, bb));
                }
            }
            pictureBox1.Image = bitmap1;
        }

        //移除按鈕部分,  一趟並不會將所有panel上的button回傳, 所以加入while迴圈, 真是神奇驚訝 
        private void DynamicRemoveButtonOnPanel(Panel panel)
        {
            while (panel.Controls.Count > 0)
            {
                foreach (Control item in panel.Controls.OfType<Button>())
                {
                    Button btn = (Button)item;
                    richTextBox1.Text += "移除 " + btn.Text + "\n";
                    panel.Controls.Remove(item);
                }
            }
        }

        //移除按鈕部分,  一趟並不會將所有panel上的button回傳, 所以加入while迴圈, 真是神奇驚訝 
        private void removeAllItems()
        {
            bool flag_do_remove = true;
            while (flag_do_remove == true)
            {
                bool flag_do_remove_this = false;
                richTextBox1.Text += this.Controls.Count.ToString() + " ";

                foreach (Control con in this.Controls)
                {
                    System.String strControl = con.GetType().ToString();//获得控件的类型
                    System.String strControlName = con.Name.ToString();//获得控件的名称
                    //System.String strControlTag = con.Tag.ToString();//获得控件的標籤, 不能用此, 因為不一定有Tag可以ToString

                    //richTextBox1.Text += "Type:\t" + strControl + "\tName:\t" + strControlName + "\tColor:\t" + con.BackColor + "\n";
                    if (con.Tag != null)
                    {
                        if (con.Tag.ToString().Substring(0, 7) == "dynamic")
                        {
                            this.Controls.Remove(con);
                            flag_do_remove_this = true;
                        }
                    }
                }
                if (flag_do_remove_this == false)
                {
                    flag_do_remove = false;
                }
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            removeAllItems();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            removeAllItems();

            //動態產生button並且綁定click事件
            DynamicGenerateButton1();

            foreach (Control con in this.Controls)
            {
                System.String strControl = con.GetType().ToString();//获得控件的类型
                System.String strControlName = con.Name.ToString();//获得控件的名称
                //System.String strControlTag = con.Tag.ToString();//获得控件的標籤, 不能用此, 因為不一定有Tag可以ToString

                //richTextBox1.Text += "Type:\t" + strControl + "\tName:\t" + strControlName + "\tColor:\t" + con.BackColor + "\n";

                if (strControl == "System.Windows.Forms.Button")
                {
                    if (con.Tag != null)
                    {
                        if (con.Tag.ToString().Substring(0, 7) == "dynamic")
                        {
                            int i = int.Parse(con.Tag.ToString().Substring(7, 2));
                            int j = int.Parse(con.Tag.ToString().Substring(10, 2));
                            /*
                            richTextBox1.Text += "Type:\t" + strControl + "\tName:\t" + strControlName + "\tColor:\t" + con.BackColor + "\t";
                            richTextBox1.Text += "Tag:\t" + con.Tag + "\t";
                            richTextBox1.Text += "i:\t" + i.ToString() + "\t";
                            richTextBox1.Text += "j:\t" + j.ToString() + "\n";
                            */
                            if (con.BackColor == Color.Gray)
                            {
                                gray[i, j] = 0;
                            }
                            else
                            {
                                gray[i, j] = 1;
                            }
                        }
                    }
                }
            }
            draw2D_Array();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            int[,] Score = new int[,] {
            { 65, 85, 78, 75, 69 },
            { 66, 55, 52, 92, 47 },
            { 75, 99, 63, 73, 86 },
            { 77, 88, 99, 91, 100 }
            };

            int[,] dddd = new int[,] {
            { 1, 0, 0, 0, 1, 0, 0 },
            { 0, 1, 0, 1, 0, 0, 0 },
            { 0, 0, 1, 0, 0, 0, 0 },
            { 0, 0, 0, 0, 0, 0, 0 },
            { 0, 0, 0, 0, 0, 0, 0 },
            { 0, 0, 0, 0, 0, 0, 0 },
            { 0, 0, 0, 0, 0, 0, 0 },
            { 0, 0, 0, 0, 0, 0, 0 }
            };

            richTextBox1.Text += "int[,] gray = new int[,] {\n";
            for (int j = 0; j < ROWS; j++)
            {
                richTextBox1.Text += "{ ";
                for (int i = 0; i < COLUMNS; i++)
                {
                    richTextBox1.Text += gray[i, j].ToString();
                    if (i == (COLUMNS - 1))
                    {
                        if (j == (ROWS - 1))
                        {
                            richTextBox1.Text += " }\n";
                        }
                        else
                        {
                            richTextBox1.Text += " },\n";
                        }
                    }
                    else
                    {
                        richTextBox1.Text += ", ";
                    }
                }
            }
            richTextBox1.Text += "};\n";
        }

        private void button7_Click(object sender, EventArgs e)
        {
            DynamicGenerateButton2();
        }

        private void DynamicGenerateButton2()
        {
            int x_st = 400;
            int y_st = 10;
            int w = 60;
            int h = 60;
            int count = 3;
            Button[] btn = new Button[count];//建立Button物件, 一維Button陣列
            for (int i = 0; i < count; i++)
            {
                btn[i] = new Button();//實體化Button
                btn[i].Size = new Size(w, h);
                btn[i].BackColor = Color.Yellow;
                btn[i].Text = "Dynamic " + i.ToString();
                btn[i].Name = "btn" + i;
                //btn[i].AutoSize = true;//true:依文字長度改變大小
                btn[i].Location = new Point(x_st + 80 * (i % 3), y_st + 80 * (i / 3));
                btn[i].Font = new Font("微軟正黑體", 12);
                btn[i].ForeColor = Color.White;
                btn[i].FlatStyle = FlatStyle.Flat;
                btn[i].FlatAppearance.BorderColor = Color.FromArgb(255, 65, 85);
                btn[i].BackColor = Color.FromArgb(55, 65, 85);
                btn[i].Click += new EventHandler(btn_ClickEvent1);// 加入按鈕事件
                btn[i].MouseEnter += new EventHandler(btn_MouseEnter);
                btn[i].MouseLeave += new EventHandler(btn_MouseLeave);

                this.Controls.Add(btn[i]);//將控件加入 到 表單 容器
            }
            //this.Controls.AddRange(btn);//將控件批次加入 到 表單 容器

            Button btn2 = new Button();//創建一個新的按鈕
            btn2.Size = new Size(w, h);
            btn2.Name = "NNN";
            btn2.Text = "TTT";
            btn2.Location = new Point(x_st, y_st + 1 * h);
            this.Controls.Add(btn2);//將控件加入 到 表單 容器

            x_st = 400;
            y_st = 150;

            int ss = 40;
            PictureBox pb_new = new PictureBox();
            pb_new.Size = new Size(ss * 3, ss * 3);
            pb_new.Left = x_st;
            pb_new.Top = y_st;
            pb_new.BackColor = Color.Pink;
            this.Controls.Add(pb_new);//將控件加入 到 表單 容器

            Button bt_new = new Button();
            this.Controls.Add(bt_new);//將控件加入 到 表單 容器
            bt_new.BringToFront();
            //bt_new.Location = new Point(button10.Location.X, button10.Location.Y + 60);   same
            bt_new.Left = x_st + ss;
            bt_new.Top = y_st + ss;
            bt_new.Size = new Size(ss, ss);
            bt_new.BackColor = Color.Red;
            bt_new.Text = "新增控件";
            bt_new.Click += new EventHandler(btn_ClickEvent1);// 加入按鈕事件

            x_st = 400;
            y_st = 300;
            w = 60;
            h = 60;
            for (int i = 0; i < 3; i++)
            {
                Button btn3 = new Button();
                btn3.Size = new Size(w, h);
                btn3.Text = i.ToString();
                btn3.Location = new Point(x_st + w * i, y_st);
                btn3.Click += btn_ClickEvent1;// 加入按鈕事件
                this.Controls.Add(btn3);//將控件加入 到 表單 容器
            }

        }

        private void button8_Click(object sender, EventArgs e)
        {
            DynamicGenerateButton3();
        }

        private void DynamicGenerateButton3()
        {
            richTextBox1.Text += "建立新表單並新增控件於其上\n";
            //當有多個按鈕需要產生時, 如何用loop方式動態產生, 並加入對應的click event
            //產生一個新的form, 並在該form上面產生MxN組的按鈕

            int x_st = 700;
            int y_st = 300;
            int i;
            int j;

            for (i = 0; i < m_cols; i++)
            {
                for (j = 0; j < m_rows; j++)
                {
                    Button btn = new Button();
                    this.AcceptButton = btn;
                    this.Controls.Add(btn);//將控件加入 到 表單 容器
                    btn.Left = x_st + m_btnWidth * i;
                    btn.Top = y_st + m_btnHeight * j;
                    btn.Width = m_btnWidth;
                    btn.Height = m_btnHeight;
                    btn.Text = (j + 1).ToString() + ", " + (i + 1).ToString();
                    btn.Click += new EventHandler(btn_ClickEvent1);// 加入按鈕事件
                }
            }
        }

        private void button9_Click(object sender, EventArgs e)
        {
            DynamicGenerateButton4();
        }

        private void DynamicGenerateButton4()
        {
            int x_st = 400;
            int y_st = 220;
            int w = 60;
            int h = 60;
            Button[,] btn = new Button[3, 2];
            Font font = new Font("微軟正黑體", 12);
            for (int x = 0; x < btn.GetLength(0); x++)
            {
                for (int y = 0; y < btn.GetLength(1); y++)
                {
                    btn[x, y] = new Button();
                    btn[x, y].Size = new Size(w, h);
                    btn[x, y].Text = "AA";
                    btn[x, y].Location = new Point(x_st + x * w, y_st + y * h);
                    btn[x, y].Font = font;
                    btn[x, y].Name = "( " + x.ToString() + ", " + y.ToString() + ")";
                    btn[x, y].Click += btn_ClickEvent3;// 加入按鈕事件
                    this.Controls.Add(btn[x, y]);//將控件加入 到 表單 容器
                }
            }
        }

        private void btn_ClickEvent3(object sender, EventArgs e)
        {
            Button btn = sender as Button;
            richTextBox1.Text += "你按了 " + btn.Text + "\n";
            richTextBox1.Text += "你按了 " + btn.Name + "\n";

            if (btn.BackColor != Color.Pink)
                btn.BackColor = Color.Pink;
            else
                btn.BackColor = SystemColors.ControlLight;

            /*
            if (btn.Text == "" && count < 9)
            {
                btn.Text = nowIndex == true ? symbol2 : symbol1;
                nowIndex = !nowIndex;
                label.Text = nowIndex == true ? "玩家二，請選擇。" : "玩家一，請選擇。";
                Check();
                count++;
                if (count == 9)
                {
                    label.Text = "GameOver!";
                    GameOver("GameOver");
                }
                Console.WriteLine(count);
            }
            */
        }

        private void button10_Click(object sender, EventArgs e)
        {
            DynamicGenerateButton5();
        }

        private void DynamicGenerateButton5()
        {
            // Display all of the images in the Buttons folder.
            int x_st = 400;
            int y_st = 440;

            const int w = 40;
            const int h = 40;

            int dx = w + 3;
            int dy = h + 3;

            // Find the images.
            int num = 0;
            foreach (string filename in Directory.GetFiles("Buttons", "*.png"))
            {
                // Make a new Button.
                Button btn = new Button();
                btn.Parent = this;
                btn.Image = new Bitmap(filename);
                btn.Size = new Size(w, h);
                btn.Location = new Point(x_st + dx * (num % 16), y_st + dy * (num / 16));

                num++;

                FileInfo file_info = new FileInfo(filename);
                toolTip1.SetToolTip(btn, file_info.Name);
            }
        }

        private void button11_Click(object sender, EventArgs e)
        {
            DynamicGenerateButton6();
        }

        Color[] colorSet = { Color.Red, Color.Orange, Color.Yellow, Color.Lime };
        Label[] new_label = new Label[100];

        private void DynamicGenerateButton6()
        {
            Panel panel1 = new Panel();
            panel1.Size = new Size(400, 400);
            panel1.BackColor = Color.Pink;
            panel1.Location = new Point(700, 10);
            this.Controls.Add(panel1);//將控件加入 到 表單 容器

            int x_st = 0;
            int y_st = 0;
            int W = 45;
            int H = 45;
            int dx = W + 5;
            int dy = H + 5;
            int not_empty = 0;

            //-----------隨機產生空位
            Random rand = new Random();
            not_empty = rand.Next(1, 100);

            richTextBox1.Text += "not_empty = " + not_empty.ToString() + "\n";

            //動態產生元件並指定屬性與事件
            for (int i = 0; i < new_label.Length; i++)
            {
                new_label[i] = new Label();
                new_label[i].AutoSize = false;//true:依文字長度改變大小, false: 固定大小
                new_label[i].Name = "label" + i.ToString();
                new_label[i].Text = (i + 1).ToString();
                new_label[i].MouseHover += MouseHover_Handler;
                new_label[i].MouseLeave += MouseLeave_Handler;
                new_label[i].Click += btn_ClickEvent2;// 加入按鈕事件
                new_label[i].Location = new Point(x_st, y_st);
                new_label[i].Size = new Size(W, H);
                if (i > not_empty)  //空位
                {
                    new_label[i].Tag = "sample : " + i.ToString() + " is " + "empty";
                    new_label[i].BackColor = Color.Gray;
                }
                else
                {
                    new_label[i].Tag = "sample : " + i.ToString() + " is " + "red";
                    new_label[i].BackColor = Color.Red;
                }
                //this.Controls.Add(new_label[i]);//將控件加入 到 表單 容器
                panel1.Controls.Add(new_label[i]);//將控件加入 到 panel1 容器
                x_st += dx;

                if ((i % 10) == 9)
                {
                    x_st = 0;
                    y_st += dy;
                }
            }
        }

        private void MouseHover_Handler(object sender, EventArgs e)
        {
            //Application.DoEvents();
            ToolTip tooltip = new ToolTip();
            //this.Cursor = Cursors.Hand;
            for (int i = 0; i < new_label.Length; i++)
            {
                if (sender == new_label[i]) // event is from txtBox
                {
                    tooltip.AutoPopDelay = 10000;
                    tooltip.ToolTipIcon = ToolTipIcon.Info;
                    tooltip.ToolTipTitle = "Sample info";
                    tooltip.ShowAlways = true;
                    tooltip.SetToolTip(new_label[i], new_label[i].Tag.ToString());
                }
            }
        }

        private void MouseLeave_Handler(object sender, EventArgs e)
        {
            //this.Cursor = Cursors.Default;
        }

        private void btn_ClickEvent2(object sender, EventArgs e)
        {
            for (int i = 0; i < new_label.Length; i++)
            {
                if (sender == new_label[i])
                {
                    //richTextBox1.Text += "click " + i.ToString() + "\n";
                    setup_next_color(new_label[i]);
                    break;
                }
            }
        }

        void setup_next_color(Label lbl)
        {
            bool flag_match = false;
            //richTextBox1.Text += "old color = " + lbl.BackColor + "\n";
            int i;
            int next = 0;
            for (i = 0; i < colorSet.Length; i++)
            {
                //richTextBox1.Text += colorSet[i].Name.ToString() + "\n";
                if (colorSet[i] == lbl.BackColor)
                {
                    next = (i + 1) % 4;
                    lbl.BackColor = colorSet[next];
                    flag_match = true;
                    break;
                }
            }
            if (flag_match == false)
            {
                lbl.BackColor = Color.Red;
            }
        }

        private void button12_Click(object sender, EventArgs e)
        {
            DynamicGenerateButton7();
        }

        private void DynamicGenerateButton7()
        {
            string foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic\_書畫字圖\_臨江仙";

            int x_st = 400;
            int y_st = 10;

            int w = 64;
            int h = 64;
            int dx = 64 + 6;
            int dy = 64 + 6;

            // Find the images.
            int num = 0;
            foreach (string filename in Directory.GetFiles(foldername, "*.jpeg"))
            {
                // Make a new Button.
                Button btn = new Button();
                btn.Parent = this;
                btn.BackgroundImage = new Bitmap(filename);
                btn.BackgroundImageLayout = ImageLayout.Zoom;
                btn.Size = new Size(w, h);
                btn.Location = new Point(x_st + dx * (num % 10), y_st + dy * (num / 10));
                num++;

                FileInfo file_info = new FileInfo(filename);
                toolTip1.SetToolTip(btn, file_info.Name);
            }
        }

        private void button13_Click(object sender, EventArgs e)
        {
            //清除這些新增的控件
            for (int j = 0; j < 10; j++)
            {
                for (int i = 0; i < this.Controls.Count; i++)
                {
                    if ((this.Controls[i].Name == "button1") || (this.Controls[i].Name == "button2") || (this.Controls[i].Name == "button3") || (this.Controls[i].Name == "button4"))
                    {
                        //richTextBox1.Text += "跳過 : " + this.Controls[i].Name + "\n";
                        continue;
                    }
                    else if (this.Controls[i].Name == "toolTip1")
                    {
                        //richTextBox1.Text += "跳過 : " + this.Controls[i].Name + "\n";
                        continue;
                    }
                    else if (this.Controls[i].Name == "richTextBox1")
                    {
                        //richTextBox1.Text += "跳過 : " + this.Controls[i].Name + "\n";
                        continue;
                    }

                    //richTextBox1.Text += "XXXXXXXX : " + this.Controls[i].Name + "\n";
                    //richTextBox1.Text += "Name: " + this.Controls[i].Name + "\t";
                    //richTextBox1.Text += "Text: " + this.Controls[i].Text + "\t";
                    //richTextBox1.Text += "這項是：" + this.Controls[i].GetType() + "\n";

                    this.Controls.Remove(this.Controls[i]);
                }
            }
        }

        private void button14_Click(object sender, EventArgs e)
        {
            //移除控件
            //this.Controls.Remove(myButton); // 移除特定控制項
            this.Controls.Clear();          // 清空容器內所有控制項
        }

        private void button18_Click(object sender, EventArgs e)
        {
            //單擊視窗的任何地方都會產生Button控件

            this.MouseDown += new MouseEventHandler(Form1_MouseDown);
            button18.Enabled = false;
        }

        private void button30_Click(object sender, EventArgs e)
        {
            DynamicGenerateButton8();
        }

        //groupBox3的
        //C# 動態產生或移除多組按鈕
        int m_cols = 4;
        int m_rows = 3;
        int m_btnWidth = 50;
        int m_btnHeight = 50;

        private void DynamicGenerateButton8()
        {
            richTextBox1.Text += "建立新表單並新增控件於其上\n";
            //當有多個按鈕需要產生時, 如何用loop方式動態產生, 並加入對應的click event
            //產生一個新的form, 並在該form上面產生MxN組的按鈕

            Form frm = new Form();
            frm.Size = new Size(800, 600);
            for (int i = 0; i < m_cols; i++)
            {
                for (int j = 0; j < m_rows; j++)
                {
                    Button btn = new Button();
                    frm.AcceptButton = btn;
                    frm.Controls.Add(btn);
                    btn.Left = m_btnWidth * i;
                    btn.Top = m_btnHeight * j;
                    btn.Width = m_btnWidth;
                    btn.Height = m_btnHeight;
                    btn.Text = (j + 1).ToString() + ", " + (i + 1).ToString();
                    btn.Click += new EventHandler(btn_ClickEvent1);// 加入按鈕事件
                }
            }
            frm.Show();
        }

        //指派一個panel, 在該panels上面產生MxN組的按鈕
        public void DynamicGenerateButtonOnPanel(Panel panel)
        {
            int i;
            int j;

            DynamicRemoveButtonOnPanel(panel);
            for (i = 0; i < m_cols; i++)
            {
                for (j = 0; j < m_rows; j++)
                {
                    Button btn = new Button();
                    panel.Controls.Add(btn);
                    btn.Left = m_btnWidth * i;
                    btn.Top = m_btnHeight * j;
                    btn.Width = m_btnWidth;
                    btn.Height = m_btnHeight;
                    btn.Text = (j + 1).ToString() + ", " + (i + 1).ToString();
                    btn.Click += new EventHandler(btn_ClickEvent1);// 加入按鈕事件
                }
            }
        }

        private void button31_Click(object sender, EventArgs e)
        {
            //動態創建控件和事件 Panel
            richTextBox1.Text += "在panel1上新增控件於其上\n";
            DynamicGenerateButtonOnPanel(panel1);
        }

        private void button32_Click(object sender, EventArgs e)
        {
            //動態移除控件和事件 Panel
            richTextBox1.Text += "移除panel1上的控件\n";
            DynamicRemoveButtonOnPanel(panel1);
        }

        private void button33_Click(object sender, EventArgs e)
        {
            //動態加入控制項( Controls.Add() )

            Label myLabel = new Label();
            myLabel.Text = "Sample Label";

            Panel pp = new Panel();
            pp.Controls.Add(myLabel);
            pp.BackColor = Color.Red;
            pp.BringToFront();
            pp.Location = new Point(600, 300);

            this.Controls.Add(pp);//將控件加入 到 表單 容器
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.DrawRectangle(Pens.Red, 5, 5, this.ClientSize.Width - 10, this.ClientSize.Height - 10);

            int x_st = 400;
            int x_sp = 400 + 700;
            int y_st = 10;
            int y_sp = this.ClientSize.Height - 20;
            for (x_st = 400; x_st <= 1100; x_st += 100)
            {
                e.Graphics.DrawLine(Pens.Red, x_st, y_st, x_st, y_sp);
            }

            x_st = 400;
            x_sp = 400 + 700;
            for (y_st = 10; y_st <= 910; y_st += 100)
            {
                e.Graphics.DrawLine(Pens.Red, x_st, y_st, x_sp, y_st);
            }
            //e.Graphics.DrawRectangle(Pens.Red, 800, 10, 300, this.ClientSize.Height - 20);

            //e.Graphics.DrawRectangle(Pens.Red, 900, 10, 100, this.ClientSize.Height - 20);

            //int x_st = 800;
            //int y_st = 10;
        }
    }
}


//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//------------------------------------------------------------

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

//1515
//---------------  # 15個




/*
調整位置
myButton.BringToFront() 或 myButton.SendToBack() 調整。

                richTextBox1.Text += "在 表單/panel/pictureBox/richtextBox 上動態建立6個按鈕控件\n";
    
                this.Controls.Add(btn[i]);//將控件加入 到 表單 容器
                //panel1.Controls.Add(btn[i]);//將控件加入 到 panel1 容器
                //pictureBox1.Controls.Add(btn[i]);//將控件加入 到 pictureBox1 容器
                //richTextBox1.Controls.Add(btn[i]);//將控件加入 到 richTextBox1 容器

-------------------------
                //動態創建按鈕和事件, 創建在richTextBox裡
                this.richTextBox1.Controls.Add(btn);    //向 某控件 中添加此按鈕

                //動態添加控件的事件,語句:
                //Control.Command += new CommandEventHandler(this.EventFun);
                btn.Click += new System.EventHandler(btn_ClickEvent1);// 加入按鈕事件
*/