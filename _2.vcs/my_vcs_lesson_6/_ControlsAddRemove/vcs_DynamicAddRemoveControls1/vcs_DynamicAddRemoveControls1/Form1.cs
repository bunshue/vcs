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

//動態加入控制項( Controls.Add() )
//動態移除控制項( Controls.Remove() )

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
        Label label_new = new Label();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //動態產生button並且綁定click事件
            int x_st = 220;
            int y_st = 10;
            DynamicAddControls1(x_st, y_st);

            x_st = 600;
            y_st = 10;
            DynamicAddControls2(x_st, y_st);

            x_st = 600;
            y_st = 110;
            DynamicAddControls3(x_st, y_st);

            x_st = 600;
            y_st = 280;
            DynamicAddControls4(x_st, y_st);

            x_st = 620;
            y_st = 510;
            DynamicAddControls5(x_st, y_st);

            x_st = 620;
            y_st = 710;
            DynamicAddControls6(x_st, y_st);

            x_st = 920;
            y_st = 10;
            DynamicAddControls7(x_st, y_st);

            x_st = 1360;
            y_st = 10;
            DynamicAddControls8(x_st, y_st);

            //動態創建控件和事件 Panel
            richTextBox1.Text += "在panel1上新增控件於其上\n";
            DynamicAddControlsOnPanel(panel1);

        }

        void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;
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
            button10.Location = new Point(x_st + dx * 0, y_st + dy * 10);
            button11.Location = new Point(x_st + dx * 0, y_st + dy * 11);

            button12.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 9);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 10);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 11);

            y_st = 10;

            lb_panel.Location = new Point(1530, y_st + dy * 0);
            panel1.Size = new Size(260, 220);
            panel1.Location = new Point(1530, y_st + dy * 0 + 20);

            richTextBox1.Size = new Size(260, 580);
            richTextBox1.Location = new Point(1530, y_st + dy * 4 - 20);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1820, 900);
            this.Text = "vcs_DynamicAddRemoveControls1";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        private void DynamicAddControls1(int x_st, int y_st)
        {
            int btn_size;
            int w = 60;
            int h = 60;

            btn_size = 400 / COLUMNS;

            if ((400 / ROWS) < btn_size)
                btn_size = 400 / ROWS;

            w = btn_size;
            h = btn_size;
            richTextBox1.Text += "w = " + w.ToString() + ", h = " + h.ToString() + "\n";
            w = 45;
            h = 45;

            int LEFT_ANCHOR = 10;
            int TOP_ANCHOR = 10;

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
                    btn.Left = x_st + LEFT_ANCHOR + w * i;
                    btn.Top = y_st + TOP_ANCHOR + h * j;
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

        private void DynamicAddControls2(int x_st, int y_st)
        {
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
        }

        private void DynamicAddControls3(int x_st, int y_st)
        {
            richTextBox1.Text += "建立新表單並新增控件於其上\n";
            //當有多個按鈕需要產生時, 如何用loop方式動態產生, 並加入對應的click event
            //產生一個新的form, 並在該form上面產生MxN組的按鈕

            for (int i = 0; i < m_cols; i++)
            {
                for (int j = 0; j < m_rows; j++)
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

        private void DynamicAddControls4(int x_st, int y_st)
        {
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

        private void DynamicAddControls5(int x_st, int y_st)
        {
            string foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic\_書畫字圖\_臨江仙";

            int w = 44;
            int h = 44;
            int dx = w + 4;
            int dy = h + 4;

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
                btn.Location = new Point(x_st + dx * (num % 15), y_st + dy * (num / 15));
                num++;

                FileInfo file_info = new FileInfo(filename);
                toolTip1.SetToolTip(btn, file_info.Name);
            }
        }

        private void DynamicAddControls6(int x_st, int y_st)
        {
            // Display all of the images in the Buttons folder.

            int w = 44;
            int h = 44;
            int dx = w + 4;
            int dy = h + 4;

            // Find the images.
            int num = 0;
            foreach (string filename in Directory.GetFiles("Buttons", "*.png"))
            {
                // Make a new Button.
                Button btn = new Button();
                btn.Parent = this;
                btn.Image = new Bitmap(filename);
                btn.Size = new Size(w, h);
                btn.Location = new Point(x_st + dx * (num % 24), y_st + dy * (num / 24));

                num++;

                FileInfo file_info = new FileInfo(filename);
                toolTip1.SetToolTip(btn, file_info.Name);
            }
        }


        Color[] colorSet = { Color.Red, Color.Orange, Color.Yellow, Color.Lime };
        Label[] new_label = new Label[100];

        private void DynamicAddControls7(int xx, int yy)
        {
            Panel panel1 = new Panel();
            panel1.Size = new Size(400, 400);
            panel1.BackColor = Color.Pink;
            panel1.Location = new Point(xx, yy);
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

        private void DynamicAddControls8(int x_st, int y_st)
        {
            //動態加入控件 Controls.Add()

            Label myLabel = new Label();
            myLabel.Text = "Sample Label";
            Panel pp = new Panel();
            pp.Controls.Add(myLabel);
            pp.BackColor = Color.Red;
            pp.BringToFront();
            pp.Size = new Size(150, 100);
            pp.Location = new Point(x_st, y_st);
            this.Controls.Add(pp);//將控件加入 到 表單 容器

            y_st += 120;

            // 實例化按鈕
            label_new.Text = "動態加入pictureBox1";
            label_new.AutoSize = true;
            label_new.Left = x_st;
            label_new.Top = y_st;
            this.Controls.Add(label_new);//將控件加入 到 表單 容器

            y_st += 30;
            pictureBox1.BorderStyle = BorderStyle.Fixed3D;
            pictureBox1.Size = new Size(150, 100);
            pictureBox1.BackColor = Color.Pink;
            pictureBox1.Left = x_st;
            pictureBox1.Top = y_st;
            pictureBox1.Tag = "dynamic";

            //this.AcceptButton = pictureBox1;
            this.Controls.Add(pictureBox1);//將控件加入 到 表單 容器
        }

        //------------------------------------------------------------  # 60個

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
                richTextBox1.Text += "你按了 " + btn.Text + "\t" + btn.Name + "\n";
                /*
                richTextBox1.Text += "控件種類 : " + sender.ToString() + "\t";
                richTextBox1.Text += "索引 :  " + btn.TabIndex.ToString() + "\n";
                */
            }
        }

        private void btn_MouseEnter(object sender, EventArgs e)
        {
            Button btn = (Button)sender;
            btn.BackColor = Color.Yellow;  // 設定按鈕的背景色
        }

        private void btn_MouseLeave(object sender, EventArgs e)
        {
            Button btn = (Button)sender;
            btn.BackColor = Color.FromArgb(55, 65, 85);  // 設定按鈕的背景色
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

        private void button0_Click(object sender, EventArgs e)
        {
            //Reload
            removeAllItems();

            //動態產生button並且綁定click事件
            int x_st = 220;
            int y_st = 10;
            DynamicAddControls1(x_st, y_st);

            foreach (Control con in this.Controls)
            {
                System.String strControl = con.GetType().ToString();  // 获得控件的类型
                System.String strControlName = con.Name.ToString();  // 获得控件的名称
                //System.String strControlTag = con.Tag.ToString();  // 获得控件的標籤, 不能用此, 因為不一定有Tag可以ToString

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
            //1~5
            removeAllItems();
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
            //Array
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

        private void button4_Click(object sender, EventArgs e)
        {
            //Clear
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
                System.String strControl = con.GetType().ToString();  // 获得控件的类型
                System.String strControlName = con.Name.ToString();  // 获得控件的名称
                //System.String strControlTag = con.Tag.ToString();  // 获得控件的標籤, 不能用此, 因為不一定有Tag可以ToString

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

        private void button5_Click(object sender, EventArgs e)
        {
            //動態創建控件和事件9 NewForm
            int x_st = 100;
            int y_st = 100;
            DynamicAddControls9(x_st, y_st);
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //移除控件
            //this.Controls.Remove(myButton); // 移除特定控制項
            this.Controls.Clear();          // 清空容器內所有控制項

            //動態移除控件和事件 Panel
            richTextBox1.Text += "移除panel1上的控件\n";
            DynamicRemoveButtonOnPanel(panel1);
        }

        private void button7_Click(object sender, EventArgs e)
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

        private void button8_Click(object sender, EventArgs e)
        {
            //單擊視窗的任何地方都會產生Button控件

            this.MouseDown += new MouseEventHandler(Form1_MouseDown);
            button11.Enabled = false;
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

        Label label0 = new Label();
        Label label1 = new Label();
        Label label2 = new Label();
        Label label3 = new Label();
        Label label4 = new Label();
        Label label5 = new Label();
        Label label6 = new Label();
        Label label7 = new Label();

        //將 ToolStrip 加入 toolStripContainer1 的 TopToolStripPanel
        //將 toolStripContainer1 加入 表單
        ToolStripContainer toolStripContainer1;
        ToolStrip toolStrip1;

        private void button9_Click(object sender, EventArgs e)
        {
            //建立控件
            //建立控件

            int x_st = 250;
            int y_st = 50;
            int dx = 150;
            int dy = 150;

            //控件一維陣列
            Label[] label_array = new Label[] { label0, label1, label2, label3, label4, label5, label6, label7 };
            for (int i = 0; i < 8; i++)
            {
                label_array[i].BackColor = System.Drawing.SystemColors.ActiveBorder;
                label_array[i].FlatStyle = System.Windows.Forms.FlatStyle.Popup;
                label_array[i].Font = new System.Drawing.Font("微軟正黑體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
                label_array[i].Size = new System.Drawing.Size(72, 90);
                label_array[i].Text = i.ToString();
                label_array[i].Name = "label" + i.ToString();
                label_array[i].TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
                label_array[i].Location = new Point(x_st + dx * (i % 4), y_st + dy * (i / 4));
                this.Controls.Add(label_array[i]);
            }
            for (int i = 0; i < 8; i++)
            {
                richTextBox1.Text += label_array[i].Name + "\n";
            }

            /*
            //控件一維陣列
            TextBox[] textArray = new TextBox[] { numText1a, numText2a, numText3a, numText4a, numText5a, numText6a, numText7a, numText8a };

            for (int i = 0; i < 8; i++)
            {
                //textArray[i].BackColor = SystemColors.Window;
                textArray[i].BackColor = Color.Pink;
                textArray[i].Text = i.ToString();
            }
            */
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //全部更動
            //this.Controls From中的所有元件控制權
            //foreach (Control child in this.Controls)表示每次從this.Controls中取一個元件的控制權
            foreach (Control child in this.Controls)
            {
                //取元件是Label的控制權
                if (child is Label)
                {
                    //做想做的事
                    child.BackColor = Color.SkyBlue;
                    child.Text = "^^";
                    //.................
                    //.................
                }
            }
        }

        private void button11_Click(object sender, EventArgs e)
        {
            //偶數label更動

            int temp = 6;
            foreach (Control child in this.Controls)
            {
                if (child is Label)
                {
                    richTextBox1.Text += "aaaaa : " + child.Name + "\n";
                    if (child.Name == "label" + temp.ToString())
                    {
                        richTextBox1.Text += "取得 : " + child.Name + "\n";
                        temp -= 2;
                        child.BackColor = Color.YellowGreen;
                        child.Text = "QQ";
                    }
                }
            }
        }

        private void button12_Click(object sender, EventArgs e)
        {
            //恢復
            int temp = 0;
            foreach (Control child in this.Controls)
            {
                if (child is Label)
                {
                    temp++;
                    child.BackColor = SystemColors.ActiveBorder;
                    child.Text = temp.ToString();
                }
            }
        }

        private void button13_Click(object sender, EventArgs e)
        {
            //對控件的修改
            foreach (Control x in Controls)
            {
                if (x.GetType().ToString() == "System.Windows.Forms.Button")
                {
                    Button Button = (System.Windows.Forms.Button)x;
                    Button.BackColor = Color.Pink;
                }
            }
        }

        private void button14_Click(object sender, EventArgs e)
        {
            //將 toolStripContainer1 加入 表單
            toolStripContainer1 = new System.Windows.Forms.ToolStripContainer();

            toolStrip1 = new System.Windows.Forms.ToolStrip();
            toolStrip1.Items.Add("新增檔案");
            toolStrip1.Items.Add("開啟檔案");
            toolStrip1.Items.Add("儲存檔案");
            toolStrip1.Items.Add("關閉檔案");
            toolStripContainer1.TopToolStripPanel.Controls.Add(toolStrip1);

            Controls.Add(toolStripContainer1);
        }

        private void button15_Click(object sender, EventArgs e)
        {
            //執行時期 顯示 屬性編輯視窗
            PropertyGrid PG = new PropertyGrid();
            Form PGForm = new Form();
            PGForm.Owner = this;
            PGForm.StartPosition = FormStartPosition.Manual;
            PGForm.Left = this.Left + this.Width;
            PGForm.Top = this.Top;
            PGForm.ShowInTaskbar = false;
            PGForm.Controls.Add(PG);
            PG.Dock = DockStyle.Fill;
            PG.SelectedObject = this.label1;  //選擇要顯示的控件名稱
            PGForm.Text = "Label 屬性編輯視窗";
            PGForm.Show();
        }

        private void button16_Click(object sender, EventArgs e)
        {

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

        //------------------------------------------------------------  # 60個

        //C# 動態產生或移除多組按鈕
        int m_cols = 4;
        int m_rows = 3;
        int m_btnWidth = 50;
        int m_btnHeight = 50;

        private void DynamicAddControls9(int x_st, int y_st)
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
                    btn.Left = x_st + m_btnWidth * i;
                    btn.Top = y_st + m_btnHeight * j;
                    btn.Width = m_btnWidth;
                    btn.Height = m_btnHeight;
                    btn.Text = (j + 1).ToString() + ", " + (i + 1).ToString();
                    btn.Click += new EventHandler(btn_ClickEvent1);// 加入按鈕事件
                }
            }
            frm.Show();
        }

        //指派一個panel, 在該panels上面產生MxN組的按鈕
        public void DynamicAddControlsOnPanel(Panel panel)
        {
            DynamicRemoveButtonOnPanel(panel);
            for (int i = 0; i < m_cols; i++)
            {
                for (int j = 0; j < m_rows; j++)
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

        //------------------------------------------------------------  # 60個

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.DrawRectangle(Pens.Red, 5, 5, this.ClientSize.Width - 10, this.ClientSize.Height - 10);

            int x_st = 220;
            int y_st = 10;
            int x_sp = x_st + 1300;
            int y_sp = y_st + 800;

            for (int xx = x_st; xx <= x_sp; xx += 100)
            {
                e.Graphics.DrawLine(Pens.Red, xx, y_st, xx, y_sp);  // 垂直線
            }
            for (int yy = y_st; yy <= y_sp; yy += 100)
            {
                e.Graphics.DrawLine(Pens.Red, x_st, yy, x_sp, yy);  // 水平線
            }

            x_st = 220;
            y_st = 10;
            e.Graphics.DrawString("1", new Font("標楷體", 20), new SolidBrush(Color.Red), new PointF(x_st, y_st));

            x_st = 600 - 20;
            y_st = 10;
            e.Graphics.DrawString("2", new Font("標楷體", 20), new SolidBrush(Color.Red), new PointF(x_st, y_st));

            x_st = 600 - 20;
            y_st = 110;
            e.Graphics.DrawString("3", new Font("標楷體", 20), new SolidBrush(Color.Red), new PointF(x_st, y_st));

            x_st = 600 - 20;
            y_st = 310;
            e.Graphics.DrawString("4", new Font("標楷體", 20), new SolidBrush(Color.Red), new PointF(x_st, y_st));

            x_st = 620-20;
            y_st = 510;
            e.Graphics.DrawString("5", new Font("標楷體", 20), new SolidBrush(Color.Red), new PointF(x_st, y_st));

            x_st = 620-20;
            y_st = 710;
            e.Graphics.DrawString("6", new Font("標楷體", 20), new SolidBrush(Color.Red), new PointF(x_st, y_st));

            x_st = 920 - 20;
            y_st = 10;
            e.Graphics.DrawString("7", new Font("標楷體", 20), new SolidBrush(Color.Red), new PointF(x_st, y_st));

            x_st = 1360 - 20;
            y_st = 10;
            e.Graphics.DrawString("8", new Font("標楷體", 20), new SolidBrush(Color.Red), new PointF(x_st, y_st));
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

/*
// 加入 TextBox 到 Form
            TextBox tb1 = new TextBox();
            tb1.Name = "tb1";
            tb1.Location = new Point(10, 10);
            this.Controls.Add(tb1);

            // 加入 TextBox 到 GroupBox
            TextBox tb3 = new TextBox();
            tb3.Name = "tb3";
            tb3.Location = new Point(10, 10);
            this.groupBox1.Controls.Add(tb3);
            
            // 加入 TextBox 到 Panel
            TextBox tb4 = new TextBox();
            tb4.Name = "tb4";
            tb4.Location = new Point(10, 10);
            this.panel1.Controls.Add(tb4)
*/






/*

        //清空文本框
        private void btnReset_Click(object sender, EventArgs e)
        {
            foreach (Control ctl in groupBox1.Controls)
            {
                if (ctl.GetType().ToString() == "System.Windows.Forms.TextBox")
                {
                    ctl.Text = "";
                }
            }
            txt_id.Focus();
            cbox_Sex.SelectedIndex = 0;
        }


            //遍歷所有控件, 找出TextBox, 檢查是否為空
            foreach (object ct in Controls)
            {
                if (ct.GetType().ToString() == "System.Windows.Forms.TextBox")
                {
                    TextBox tx = (TextBox)ct;
                    if (tx.Text == "")
                    {
                        MessageBox.Show(tx.Tag.ToString() + "不能為空");
                    }
                }
            }

//------------------------------------------------------------  # 60個

                    ControlInfo(true);
            ControlInfo(false);


        private void ControlInfo(Boolean B)
        {
            foreach (Control ct in this.groupBox1.Controls)
            {
                if (ct is TextBox)
                {
                    if (B)
                    {
                        ct.Enabled = true;
                    }
                    else
                    {
                        ct.Enabled = false;
                    }
                }
            }
        }

//------------------------------------------------------------  # 60個

            ControlInfo(false);
            ControlInfo(false);
            ControlInfo(true);
        private void ControlInfo(Boolean B)
        {
            foreach (Control ct in this.groupBox1.Controls)
            {
                if (ct is TextBox)
                {
                    ct.Text = "";
                    if (B)
                    {
                        ct.Enabled = true;
                    }
                    else
                    {
                        ct.Enabled = false;
                    }
                }
            }
        }


        private Boolean TextClear()
        {
            foreach (Control c in this.groupBox1.Controls)
            {
                if (c is TextBox)
                {
                    if (c.Text == "")
                    {
                        return false;
                    }
                    else
                    {
                        return true;
                    }
                }
            }
            return true;
        }


        private void clearText()
        {
            foreach (Control cl in this.groupBox1.Controls)
            {
                if (cl is TextBox)
                {
                    cl.Text = "";
                }
            }
        }


        private Boolean TextInfo()
        {
            foreach (Control c in groupBox1.Controls)
            {
                if (c is TextBox)
                {
                    if (c.Text == "")
                    {
                        return false;
                    }
                    else
                    {
                        return true;
                    }
                }
            }
            return true;
        }



        private void clearText()
        {
            foreach (Control c in groupBox1.Controls)
            {
                if (c is TextBox)
                {
                    c.Text = "";
                }
            }
            pictureBox1.Image = null;
        }

//------------------------------------------------------------  # 60個



*/


