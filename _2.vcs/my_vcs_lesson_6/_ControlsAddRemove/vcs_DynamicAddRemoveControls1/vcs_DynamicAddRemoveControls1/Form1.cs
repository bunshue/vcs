using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

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

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //動態產生button並且綁定click事件
            DynamicGenerateButton1();
        }

        private void DynamicGenerateButton1()
        {
            int btn_size;

            btn_size = 400 / COLUMNS;

            if ((400 / ROWS) < btn_size)
                btn_size = 400 / ROWS;

            // 設定位置及按鈕寬高值
            int BTN_WIDTH = btn_size;
            int BTN_HEIGHT = btn_size;

            int LEFT_ANCHOR = 20;
            int TOP_ANCHOR = 20;

            richTextBox1.Text += "建立新表單並新增控件於其上\n";
            //當有多個按鈕需要產生時, 如何用loop方式動態產生, 並加入對應的click event
            //產生一個新的form, 並在該form上面產生MxN組的按鈕

            int i;
            int j;
            for (j = 0; j < ROWS; j++)
            {
                for (i = 0; i < COLUMNS; i++)
                {
                    // 實例化按鈕
                    Button btn = new Button();
                    // 設定按鈕參數
                    btn.Left = LEFT_ANCHOR + BTN_WIDTH * i;
                    btn.Top = TOP_ANCHOR + BTN_HEIGHT * j;
                    btn.Width = BTN_WIDTH;
                    btn.Height = BTN_HEIGHT;
                    btn.BackColor = Color.Gray;
                    btn.Tag = "dynamic" + i.ToString("D2") + "_" + j.ToString("D2");
                    btn.Name = "bt" + i.ToString("D2") + "_" + j.ToString("D2");
                    // 加入按鈕事件
                    //btn.Click += new EventHandler(myClick);   //same
                    btn.Click += myClick;
                    // 將按鈕加入表單
                    this.AcceptButton = btn;
                    this.Controls.Add(btn);
                }
            }

            // 實例化按鈕
            pictureBox1.Size = new Size(PICTURE_WIDTH, PICTURE_HEIGHT);
            pictureBox1.BackColor = Color.Pink;

            pictureBox1.Left = 430;
            pictureBox1.Top = 20;

            pictureBox1.Tag = "dynamic";

            // 將按鈕加入表單
            //this.AcceptButton = pictureBox1;
            this.Controls.Add(pictureBox1);
        }

        private void myClick(object sender, EventArgs e)
        {
            //MessageBox.Show(((Button)sender).Text);
            if (((Button)sender).BackColor == Color.Gray)
                ((Button)sender).BackColor = Color.Blue;
            else
                ((Button)sender).BackColor = Color.Gray;


            int i;
            int j;

            string tt = ((Button)sender).Tag.ToString();

            if (tt != null)
            {
                i = int.Parse(tt.Substring(7, 2));
                j = int.Parse(tt.Substring(10, 2));
                richTextBox1.Text += "i = " + i.ToString() + ", j = " + j.ToString() + "\n";

                if (((Button)sender).BackColor == Color.Gray)
                {
                    //((Button)sender).BackColor = Color.Blue;
                    gray[i, j] = 0;
                }
                else
                {
                    //((Button)sender).BackColor = Color.Gray;
                    gray[i, j] = 1;
                }
            }

            richTextBox1.Text += "你按了按鈕 Name : " + ((Button)sender).Name + "\n";

            // 把 sender 轉為 Button 並利用 Button.Name 來判斷是按下哪一個 Button
            string ButtonName = ((Button)sender).Name;
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
        private static void removeAllBtns(Panel panel)
        {
            while (panel.Controls.Count > 0)
            {
                foreach (Control item in panel.Controls.OfType<Button>())
                {
                    Button btn = (Button)item;
                    MessageBox.Show("移除" + btn.Text);
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
                    flag_do_remove = false;
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
                                gray[i, j] = 0;
                            else
                                gray[i, j] = 1;
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


            int i;
            int j;
            richTextBox1.Text += "int[,] gray = new int[,] {\n";
            for (j = 0; j < ROWS; j++)
            {
                richTextBox1.Text += "{ ";
                for (i = 0; i < COLUMNS; i++)
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

        private void button6_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //動態創建按鈕和事件, 創建在richTextBox裡

            int i = 0;
            for (i = 0; i < 10; i++)
            {
                Button btn = new Button();//創建一個新的按鈕
                btn.Name = "button" + i.ToString();//這是我用來區別各個按鈕的辦法
                btn.Text = "button" + i.ToString();
                btn.Size = new Size(80, 45);
                Point p = new Point(100, 50 + i * 50);//創建一個坐標,用來給新的按鈕定位
                btn.Location = p;//把按鈕的位置與剛創建的坐標綁定在一起

                this.richTextBox1.Controls.Add(btn);    //向 某控件 中添加此按鈕

                //動態添加控件的事件,語句:
                //Control.Command += new CommandEventHandler(this.EventFun);
                btn.Click += new System.EventHandler(btn_click);//將按鈕的方法綁定到按鈕的單擊事件中b.Click是按鈕的單擊事件
            }
        }

        private void btn_click(object sender, System.EventArgs e)
        {
            Button b1 = (Button)sender;//將觸發此事件的對象轉換為該Button對象

            richTextBox1.Text += "你按了 " + b1.Name + "\n";
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //動態創建按鈕和事件, 創建在Form裡

            //1.建立Button物件
            Button[] btuArray = new Button[3];
            btuArray[0] = new Button();
            btuArray[1] = new Button();
            btuArray[2] = new Button();

            for (int i = 0; i != btuArray.Length; i++)
            {
                //2.加入控制項
                this.Controls.Add(btuArray[i]);
                btuArray[i].Size = new Size(80, 60);
                btuArray[i].Text = "Dynamic " + i;
                //btuArray[i].Top = 12 + btuArray[i].Height * i;
                //btuArray[i].Left = 13;
                btuArray[i].Location = new Point(550 + i * 90, 500);
                //3.為Click事件註冊
                btuArray[i].Click += new EventHandler(button_Click);
            }
        }

        private void button_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按下 :\t控件種類 : " + sender.ToString() + "\t";
            richTextBox1.Text += "文字 :  " + ((Button)(sender)).Text + "\t";
            richTextBox1.Text += "索引 :  " + ((Button)(sender)).TabIndex.ToString() + "\n";
        }

        private void button9_Click(object sender, EventArgs e)
        {
            int count = 5;
            Button[] btn = new Button[count];
            for (int j = 0; j < count; j++)
            {
                //reader2.Read();
                btn[j] = new Button();
                btn[j].Name = "topic2" + j;
                btn[j].Text = j.ToString();
                btn[j].AutoSize = true;
                btn[j].Location = new Point(100 * j + 20, 440);
                btn[j].Font = new Font("微軟正黑體", 12);
                btn[j].ForeColor = Color.White;
                btn[j].FlatStyle = FlatStyle.Flat;
                btn[j].FlatAppearance.BorderColor = Color.FromArgb(((int)(((byte)(55)))), ((int)(((byte)(65)))), ((int)(((byte)(85)))));
                btn[j].BackColor = Color.FromArgb(((int)(((byte)(55)))), ((int)(((byte)(65)))), ((int)(((byte)(85)))));
            }
            this.Controls.AddRange(btn);

        }

        private void button10_Click(object sender, EventArgs e)
        {
            PictureBox pb_new = new PictureBox();
            pb_new.Size = new Size(250, 250);
            pb_new.Left = 600;
            pb_new.Top = 440;
            pb_new.BackColor = Color.Pink;
            this.Controls.Add(pb_new);

            Button bt_new = new Button();
            this.groupBox1.Controls.Add(bt_new);
            //bt_new.Location = new Point(button10.Location.X, button10.Location.Y + 60);   same
            bt_new.Left = button10.Location.X + 120;
            bt_new.Top = button10.Location.Y + 0;
            bt_new.Size = new Size(100, 40);
            bt_new.BackColor = Color.Red;
            bt_new.Text = "新增控件";
            bt_new.Click += new EventHandler(bt_new_Click);
        }

        private void bt_new_Click(System.Object sender, System.EventArgs e)
        {
            richTextBox1.Text += "你按了這個新控件\n";
        }

        private void button11_Click(object sender, EventArgs e)
        {
            //動態產生button並且綁定click事件
            DynamicGenerateButton2();
        }

        private void DynamicGenerateButton2()
        {
            // 設定位置及按鈕寬高值
            int LEFTANCHOR = 600;
            int TOPANCHOR = 550;
            int BTN_HEIGHT = 80;
            int BTN_WIDTH = 80;

            int i;
            for (i = 0; i < 3; i++)
            {
                // 實例化按鈕
                Button btn = new Button();

                // 設定按鈕參數
                btn.Text = i.ToString();
                btn.Width = BTN_WIDTH;
                btn.Height = BTN_HEIGHT;
                btn.Left = LEFTANCHOR + BTN_WIDTH * i;
                btn.Top = TOPANCHOR + BTN_HEIGHT * 0;

                // 加入按鈕事件
                btn.Click += dynamic_Btn_Click;

                // 將按鈕加入表單
                this.Controls.Add(btn);
            }
        }


        //加入按鈕事件
        private void dynamic_Btn_Click(object sender, EventArgs e)
        {
            // 撰寫事件內容
            //richTextBox1.Text += "XXXXXXXXXXXXXXX\n";

            //MessageBox.Show(((Button)sender).Text);
            richTextBox1.Text += "你按了按鈕 " + ((Button)sender).Text + "\n";

        }
    }
}
