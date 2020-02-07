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
        private const int COLUMNS = 10;
        private const int ROWS = 8;
        private const int PICTURE_WIDTH = 500;
        private const int PICTURE_HEIGHT = 400;
        private const int dd = PICTURE_WIDTH / COLUMNS;

        int[,] gray = new int[COLUMNS, ROWS];

        Bitmap bitmap1;
        PictureBox pictureBox1 = new PictureBox();

        public Form1()
        {
            InitializeComponent();

            //動態產生button並且綁定click事件
            DynamicGenerateButton();
        }

        private void DynamicGenerateButton()
        {
            // 設定位置及按鈕寬高值
            int BTN_WIDTH = 400 / COLUMNS;
            int BTN_HEIGHT = 400 / COLUMNS;

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
                    //btn.Text = i.ToString() + ", " + j.ToString();
                    btn.Tag = "dynamic" + (COLUMNS*j+i).ToString("D2");
                    btn.Name = "bt" + (COLUMNS * j + i).ToString("D2");
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

            richTextBox1.Text += "你按了按鈕 Name : " + ((Button)sender).Name + "\n";

            // 把 sender 轉為 Button 並利用 Button.Name 來判斷是按下哪一個 Button
            string ButtonName = ((Button)sender).Name;
            if (ButtonName == "bt00")
            {
                richTextBox1.Text += "你按了bt00\n";
            }
            else if (ButtonName == "bt01")
            {
                richTextBox1.Text += "你按了bt01\n";
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
                //if (strControlTag == "dynamic")
                if (con.Tag != null)
                {
                    if (con.Tag.ToString().Substring(0, 7) == "dynamic")
                    {
                        int index = int.Parse(con.Tag.ToString().Substring(7, 2));
                        /*
                        richTextBox1.Text += "Type:\t" + strControl + "\tName:\t" + strControlName + "\tColor:\t" + con.BackColor + "\t";
                        richTextBox1.Text += "Tag:\t" + con.Tag + "\t";
                        richTextBox1.Text += "Index:\t" + index.ToString() + "\n";
                        */

                        if (con.BackColor == Color.Gray)
                            gray[index % COLUMNS, index / COLUMNS] = 0;
                        else
                            gray[index % COLUMNS, index / COLUMNS] = 1;
                        
                    }
                }

            }

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
                    rr = (byte)(gray[xx / dd, yy / dd] * 255);
                    gg = (byte)(gray[xx / dd, yy / dd] * 255);
                    bb = (byte)(gray[xx / dd, yy / dd] * 255);
                    bitmap1.SetPixel(xx, yy, Color.FromArgb(aa, rr, gg, bb));
                }
            }
            pictureBox1.Image = bitmap1;





        }




    }
}
