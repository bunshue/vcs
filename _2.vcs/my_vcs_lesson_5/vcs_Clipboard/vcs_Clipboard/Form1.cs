using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;                //for Directory
using System.Drawing.Imaging;   //for ImageFormat

namespace vcs_Clipboard
{
    public partial class Form1 : Form
    {
        bool flag_my_PicPick = false;
        int clear_label_count = 0;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            label1.Text = "";
            show_item_location();

            string Path;
            //檢查存d10d的資料夾
            Path = "C:\\dddddddddd";
            if (Directory.Exists(Path) == false)     //確認資料夾是否存在
            {
                Directory.CreateDirectory(Path);
                richTextBox1.Text += "已建立一個新資料夾: " + Path + "\n";
            }
            else
                richTextBox1.Text += "資料夾: " + Path + " 已存在，不用再建立\n";
        }

        void show_item_location()
        {
            if (flag_my_PicPick == true)
            {
                //button1.Visible = false;
                //button2.Visible = false;
                button3.Visible = false;
                button4.Visible = false;
                button5.Visible = false;
                bt_clear.Visible = false;
                groupBox1.Visible = false;
                pictureBox1.Visible = false;
                richTextBox1.Visible = false;

                button1.Text = "截圖存檔";
                button1.Location = new Point(10, 10);
                button1.Size = new Size(60, 50);

                button2.Font = new Font(button2.Font.Name, 14);
                button2.Text = "全螢幕截圖";
                button2.Location = new Point(button1.Location.X + button1.Size.Width + 2, 10);
                button2.Size = new Size(115, 25);

                label1.Location = new Point(75, 40);

                this.Size = new Size(205, 110);

                //設定執行後的表單起始位置, 在螢幕的最右下方
                const int margin = 0;
                int x = Screen.PrimaryScreen.WorkingArea.Right - this.Width - margin;
                int y = Screen.PrimaryScreen.WorkingArea.Bottom - this.Height - margin;
                this.StartPosition = FormStartPosition.Manual;
                this.Location = new Point(x, y);
                //關閉最大化,最小化按鈕, 且固定不能改變表單大小
                //this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedToolWindow;
                this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.Fixed3D;

                //this.ShowInTaskbar = false;     //false : 表單不顯示在 Windows 工作列中
            }
            else
            {
                int x_st;
                int y_st;
                int dx;
                int dy;

                //button
                x_st = 12;
                y_st = 12;
                dx = 130;
                dy = 65;

                button1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
                button2.Location = new Point(x_st + dx * 0, y_st + dy * 1);
                button3.Location = new Point(x_st + dx * 0, y_st + dy * 2);
                button4.Location = new Point(x_st + dx * 0, y_st + dy * 3);
                button5.Location = new Point(x_st + dx * 0, y_st + dy * 4);

                groupBox1.Location = new Point(12, 350);
                y_st = 18;
                button6.Location = new Point(x_st + dx * 0, y_st + dy * 0);
                button7.Location = new Point(x_st + dx * 0, y_st + dy * 1);
                button8.Location = new Point(x_st + dx * 0, y_st + dy * 2);
                button9.Location = new Point(x_st + dx * 0, y_st + dy * 3);
                button10.Location = new Point(x_st + dx * 0, y_st + dy * 4);
                button11.Location = new Point(x_st + dx * 0, y_st + dy * 5);

                bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (flag_my_PicPick == true)
            {
                IDataObject dataObject = Clipboard.GetDataObject();   //GetDataObject() 讀取當前剪貼簿中的數據內容
                if (dataObject.GetDataPresent(DataFormats.Bitmap))  //圖片類
                {
                    richTextBox1.Text += "取得圖片\n";

                    //取出Bitmap資料, 可做處理
                    Bitmap bitmap1 = (Bitmap)dataObject.GetData(DataFormats.Bitmap);  //取得Bitmap資料
                    if (bitmap1 != null)
                    {
                        string filename = "C:\\dddddddddd\\Image_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";
                        try
                        {
                            bitmap1.Save(@filename, ImageFormat.Jpeg);

                            //richTextBox1.Text += "存檔成功\n";
                            //richTextBox1.Text += "已存檔 : " + filename + "\n";
                            label1.Text = "存檔成功";
                            timer1.Enabled = true;
                        }
                        catch (Exception ex)
                        {
                            richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                        }
                    }
                    else
                    {
                        richTextBox1.Text += "無圖可存\n";
                        label1.Text = "無圖可存";
                        timer1.Enabled = true;
                    }
                }
                else
                {
                    richTextBox1.Text += "無圖片\n";
                    label1.Text = "無圖片";
                    timer1.Enabled = true;
                }
            }
            else
            {
                richTextBox1.Text += "\n把系統剪貼簿裏的資料拿出來, 區分資料類型:\n";
                IDataObject dataObject = Clipboard.GetDataObject();   //GetDataObject() 讀取當前剪貼簿中的數據內容
                if (dataObject.GetDataPresent(DataFormats.Text))  //GetDataPresent()檢測剪貼簿存放的資料類型   //Text純文字類
                {
                    richTextBox1.Text += "取得文字, 內容：\n";
                    //richTextBox1.Text += dataObject.GetData(DataFormats.Text).ToString();   //直接顯示在richTextBox裏

                    //取出Text資料, 可做處理
                    String str = (String)dataObject.GetData(DataFormats.Text);
                    richTextBox1.Text += str + "\n";
                }
                else if (dataObject.GetDataPresent(DataFormats.Bitmap))  //圖片類
                {
                    richTextBox1.Text += "取得圖片\n";
                    //pictureBox1.Image = (System.Drawing.Image)dataObject.GetData(DataFormats.Bitmap); //直接顯示在pictureBox裏

                    //取出Bitmap資料, 可做處理
                    Bitmap bitmap1 = (Bitmap)dataObject.GetData(DataFormats.Bitmap);  //取得Bitmap資料
                    pictureBox1.Image = bitmap1;
                    if (bitmap1 != null)
                    {
                        string filename = Application.StartupPath + "\\vcs_Clipboard_" + DateTime.Now.ToString("yyyyMMdd_HHmmss");
                        String filename1 = filename + ".jpg";
                        String filename2 = filename + ".bmp";
                        String filename3 = filename + ".png";

                        try
                        {
                            bitmap1.Save(@filename1, ImageFormat.Jpeg);
                            bitmap1.Save(@filename2, ImageFormat.Bmp);
                            bitmap1.Save(@filename3, ImageFormat.Png);

                            richTextBox1.Text += "存檔成功\n";
                            richTextBox1.Text += "已存檔 : " + filename1 + "\n";
                            richTextBox1.Text += "已存檔 : " + filename2 + "\n";
                            richTextBox1.Text += "已存檔 : " + filename3 + "\n";
                        }
                        catch (Exception ex)
                        {
                            richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                        }
                    }
                    else
                        richTextBox1.Text += "無圖可存\n";
                }
                else if (dataObject.GetDataPresent(DataFormats.Html))  //HTML類
                {
                    richTextBox1.Text += "HTML類\n";
                }
                else
                {
                    richTextBox1.Text += "其他類型資料\n";
                }
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (flag_my_PicPick == true)
            {
                //全螢幕截圖
                //建立空白畫布
                Bitmap bitmap1 = new Bitmap(Screen.PrimaryScreen.Bounds.Width, Screen.PrimaryScreen.Bounds.Height);
                //取得畫布的繪圖物件用以繪圖
                Graphics g = Graphics.FromImage(bitmap1);
                g.CopyFromScreen(new Point(0, 0), new Point(0, 0), new Size(Screen.PrimaryScreen.Bounds.Width, Screen.PrimaryScreen.Bounds.Height));
                IntPtr dc1 = g.GetHdc();
                g.ReleaseHdc(dc1);

                //將裁切出的矩形存成JPG圖檔。
                string filename = "C:\\dddddddddd\\Image_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";
                try
                {
                    bitmap1.Save(@filename, ImageFormat.Jpeg);
                    //richTextBox1.Text += "全螢幕截圖1，存檔檔名：" + filename + "\n";
                    label1.Text = "存檔成功";
                    timer1.Enabled = true;
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
        }

        private void button4_Click(object sender, EventArgs e)
        {
        }

        private void button5_Click(object sender, EventArgs e)
        {
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //把資料放到系統剪貼簿裏
            richTextBox1.Text += "按了 複製資料到剪貼簿\n";
            //Clipboard.SetData(DataFormats.Text, richTextBox1.Text + "\n");
            //Clipboard.SetDataObject(richTextBox1.Text + "\n");      //建議用此
            string poem = "\n唐王翰涼州詞\n葡萄美酒夜光杯，欲飲琵琶馬上催。醉臥沙場君莫笑，古來征戰幾人回。\n";
            Clipboard.SetDataObject("複製資料到剪貼簿" + poem + " " + DateTime.Now.ToString() + "\n");      //建議用此  //將poem字串填到Clipboard裏。
        }

        private void button7_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "按了 累計複製資料到剪貼簿\n";
            //Clipboard.SetData(DataFormats.Text, Clipboard.GetData(DataFormats.Text) + richTextBox1.Text + "\n");
            //Clipboard.SetDataObject(Clipboard.GetText() + richTextBox1.Text + "\n");      //建議用此
            //Clipboard.GetData(DataFormats.Text) 目前剪貼簿內的文字資料
            //Clipboard.GetText() 目前剪貼簿內的文字資料
            Clipboard.SetDataObject(Clipboard.GetText() + "累計複製資料到剪貼簿 " + DateTime.Now.ToString() + "\n");      //建議用此  //將poem字串填到Clipboard裏。
        }

        private void button8_Click(object sender, EventArgs e)
        {
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //C# – 清除剪貼簿
            Clipboard.Clear();
        }

        //Read text from clipboard
        private void button10_Click(object sender, EventArgs e)
        {
            string str = System.String.Empty;
            if (Clipboard.ContainsText())
            {
                str = Clipboard.GetText();
                richTextBox1.Text += str + "\n";
            }
        }

        private void button11_Click(object sender, EventArgs e)
        {
            //C# – 貼上剪貼簿
            richTextBox1.Text += "\n";
            //richTextBox1.Text += Clipboard.GetData(DataFormats.Text);
            richTextBox1.Text += Clipboard.GetText();   //建議用此

            richTextBox1.Text += "\n";
            int len = Clipboard.GetText().Length;
            richTextBox1.Text += "Unicode (Big-Endian), len = " + len.ToString() + "\n";
            int i;
            for (i = 0; i < len; i++)
            {
                //richTextBox1.Text += Clipboard.GetText()[i].ToString() + "\n";
                richTextBox1.Text += ((int)Clipboard.GetText()[i]).ToString("X2") + " ";
            }
            richTextBox1.Text += "\n";
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            clear_label_count++;
            if (clear_label_count == 3)
            {
                clear_label_count = 0;
                label1.Text = "";
                timer1.Enabled = false;
            }

        }

        private void Form1_DoubleClick(object sender, EventArgs e)
        {
            if (flag_my_PicPick == true)
            {
                Application.Exit();
            }
        }

    }
}
