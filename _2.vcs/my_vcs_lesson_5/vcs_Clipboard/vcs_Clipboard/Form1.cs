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
using System.Threading;

namespace vcs_Clipboard
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
            webBrowser_clipboard.Navigate("about:blank");
            richTextBox1.Text += "\n";
        }

        void show_item_location()
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

            int offset = 70;
            button15.Location = new Point(x_st + dx * 2 + offset, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 2 + offset, y_st + dy * 6);
            button17.Location = new Point(x_st + dx * 2 + offset, y_st + dy * 7);
            button18.Location = new Point(x_st + dx * 2 + offset, y_st + dy * 8);
            button19.Location = new Point(x_st + dx * 2 + offset, y_st + dy * 9);
            button20.Location = new Point(x_st + dx * 2 + offset, y_st + dy * 10);
            button21.Location = new Point(x_st + dx * 2 + offset, y_st + dy * 11);
            button22.Location = new Point(x_st + dx * 2 + offset, y_st + dy * 12);
            button26.Location = new Point(x_st + dx * 2 + offset, y_st + dy * 13);
            button27.Location = new Point(x_st + dx * 2 + offset, y_st + dy * 14);

            groupBox1.Location = new Point(12, 350);
            y_st = 18;
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button10.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button11.Location = new Point(x_st + dx * 0, y_st + dy * 5);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            richTextBox2.Visible = false;
            pictureBox1.Visible = false;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "\n取得系統剪貼簿裏的資料類型:\n";
            IDataObject dataObject1 = Clipboard.GetDataObject();    //讀取數據 
            int i = 1;
            foreach (string format in dataObject1.GetFormats())
            {
                richTextBox1.Text += (i++).ToString() + "\t" + format + "\n";
            }

            //根據指定的DataFormat獲取數據對象 
            if (Clipboard.ContainsData(DataFormats.UnicodeText) == true)
            {
                richTextBox1.Text += "取得 UnicodeText\n";
                IDataObject dataObject2 = Clipboard.GetDataObject();    //讀取數據 
                string str = dataObject2.GetData(DataFormats.UnicodeText) as string;
                MessageBox.Show(str);
            }

            richTextBox1.Text += "\n把系統剪貼簿裏的資料拿出來, 區分資料類型:\n";
            IDataObject dataObject3 = Clipboard.GetDataObject();   //GetDataObject() 讀取當前剪貼簿中的數據內容
            if (dataObject3.GetDataPresent(DataFormats.Text))  //GetDataPresent()檢測剪貼簿存放的資料類型   //Text純文字類
            {
                richTextBox1.Text += "取得文字, 內容：\n";
                //richTextBox1.Text += dataObject3.GetData(DataFormats.Text).ToString();   //直接顯示在richTextBox裏

                //取出Text資料, 可做處理
                String str = (String)dataObject3.GetData(DataFormats.Text);
                richTextBox1.Text += str + "\n";
            }

            if (dataObject3.GetDataPresent(DataFormats.Bitmap))  //圖片類
            {
                richTextBox1.Text += "取得圖片\n";
                //pictureBox1.Image = (System.Drawing.Image)dataObject3.GetData(DataFormats.Bitmap); //直接顯示在pictureBox裏

                //取出Bitmap資料, 可做處理
                Bitmap bitmap1 = (Bitmap)dataObject3.GetData(DataFormats.Bitmap);  //取得Bitmap資料
                pictureBox1.Image = bitmap1;
                pictureBox1.Visible = true;
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

            if (dataObject3.GetDataPresent(DataFormats.Rtf))  //RTF類
            {
                richTextBox1.Text += "取得RTF, 內容：\n";
                //取出Text資料, 可做處理
                String str = (String)dataObject3.GetData(DataFormats.Rtf);
                richTextBox2.Rtf = Clipboard.GetText(TextDataFormat.Rtf);
                richTextBox2.Visible = true;
            }

            if (dataObject3.GetDataPresent(DataFormats.Html))  //HTML類
            {
                richTextBox1.Text += "取得HTML, 內容：\n";
                //取出Text資料, 可做處理
                String str = (String)dataObject3.GetData(DataFormats.Html);
                richTextBox1.Text += str + "\n";
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //複製純文字
            Clipboard.SetText(richTextBox1.Text);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //貼上純文字
            richTextBox1.Text += Clipboard.GetText();
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

            //復制到剪貼板上，第二個參數表明程序退出時不清空剪貼板 
            //Clipboard.SetDataObject(dataobj, true);
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
            Clipboard.Clear();  //清除剪貼板中的對象
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

        private void button12_Click(object sender, EventArgs e)
        {
            // Copy a Person to the Clipboard.
            Person person = new Person() { FirstName = textBox1.Text, LastName = textBox2.Text };
            Clipboard.SetDataObject(person);
            richTextBox1.Text += "已複製類別到剪貼簿\n";
        }

        // Paste the person from the Clipboard.
        private void button13_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "貼上類別\t";
            IDataObject dataObject = Clipboard.GetDataObject();
            if (dataObject.GetDataPresent("vcs_Clipboard.Person"))
            {
                Person person = (Person)dataObject.GetData("vcs_Clipboard.Person");
                //txtDropFirstName.Text = person.FirstName;
                //txtDropLastName.Text = person.LastName;
                richTextBox1.Text += "取得類別資料 First Name = " + person.FirstName + ", Last Name = " + person.LastName + "\n";
            }
            else
            {
                richTextBox1.Text += "類別資料不存在\n";
            }

        }

        //檢查剪貼簿內的資料內容 ST
        private void button14_Click(object sender, EventArgs e)
        {
            // List the available formats.
            IDataObject dataObject = Clipboard.GetDataObject();

            foreach (string format in dataObject.GetFormats())
            {
                richTextBox1.Text += "取得剪貼簿內的資料格式 : " + format + "\n";
            }
            DisplayData();
        }

        // Display data if possible.
        private void DisplayData()
        {
            pictureBox_clipboard.Image = null;
            textBox_clipboard.Clear();
            richTextBoxp_clipboard.Clear();
            //webBrowser_clipboard.Navigate("about:blank");

            // Image.
            if (Clipboard.ContainsImage())
            {
                pictureBox_clipboard.Image = Clipboard.GetImage();
            }

            // Text.
            if (Clipboard.ContainsText(TextDataFormat.UnicodeText))
            {
                textBox_clipboard.Text = Clipboard.GetText(TextDataFormat.UnicodeText);
            }

            // HTML.
            if (Clipboard.ContainsText(TextDataFormat.Html))
            {
                HtmlDocument doc = webBrowser_clipboard.Document;
                doc.Body.InnerHtml = Clipboard.GetText(TextDataFormat.Html);
            }

            // Rich Text.
            if (Clipboard.ContainsText(TextDataFormat.Rtf))
            {
                richTextBoxp_clipboard.Rtf = Clipboard.GetText(TextDataFormat.Rtf);
            }
        }
        //檢查剪貼簿內的資料內容 SP

        private void button15_Click(object sender, EventArgs e)
        {
            bool flag = Clipboard.ContainsImage();  //判斷Clipboard中是否包含圖片資料
            richTextBox1.Text += "Clipboard 是否包含圖片資料 : " + flag.ToString() + "\n";
        }

        private void button16_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "將圖片資料放置到Clipboard中\n";
            string filename = @"C:\______test_files\picture1.jpg";
            Image img = Image.FromFile(filename);
            Clipboard.SetImage(img);
        }

        private void button17_Click(object sender, EventArgs e)
        {
            bool flag = Clipboard.ContainsText();   //判斷Clipboard中是否包含文字資料
            richTextBox1.Text += "Clipboard 是否包含文字資料 : " + flag.ToString() + "\n";
        }

        private void button18_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "將文字資料放置到Clipboard中\n";
            string data = "翠盖龙旗出建章 莺啼百啭柳初黄";
            Clipboard.SetDataObject(data);	//向Clipboard中放置資料
        }

        private void button19_Click(object sender, EventArgs e)
        {
            bool flag = Clipboard.ContainsText();
            if (flag == true)
            {
                //顯示Clipboard中的文字資料
                string text = Clipboard.GetText();
                richTextBox1.Text += "取得文字資料 :\n" + text + "\n";
            }
            else
            {
                richTextBox1.Text += "無  文字資料\n";
            }
        }

        private void button20_Click(object sender, EventArgs e)
        {
            //Clipboard中檔名的集合

            //Clipboard
            //傳回字串集合，其中包含剪貼簿上已置放檔案的清單。
            System.Collections.Specialized.StringCollection stringCollection = Clipboard.GetFileDropList();
            if (stringCollection != null)
            {
                richTextBox1.Text += "在檔案總管中, 複製 或 剪下的檔案:\n";
                foreach (var item in stringCollection)
                {
                    richTextBox1.Text += "取得檔案 : " + item + "\n";
                }
            }

            richTextBox1.Text += "\n";

            if ((Clipboard.ContainsFileDropList()) && (Clipboard.GetFileDropList().Count > 0))
            {
                int cnt = Clipboard.GetFileDropList().Count;
                int i;
                for (i = 0; i < cnt; i++)
                {
                    richTextBox1.Text += "取得檔案 : " + Path.GetFileName(Clipboard.GetFileDropList()[i]) + "\n";
                }
            }
            richTextBox1.Text += "\n";

            //因為Clipboard是可以複製多個檔案的所有要遍歷獲取
            System.Collections.Specialized.StringCollection sc = Clipboard.GetFileDropList();
            richTextBox1.Text += "在檔案總管中, 複製 或 剪下的檔案:\n";
            foreach (var item in sc)
            {
                richTextBox1.Text += "取得檔案 : " + item + "\n";
            }
        }

        private void button21_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Clipboard內的影像顯示存檔\t全部\n";
            bool flag = Clipboard.ContainsImage();  //判斷Clipboard中是否包含圖片資料
            richTextBox1.Text += "Clipboard 是否包含圖片資料 : " + flag.ToString() + "\n";

            if (flag == true)
            {
                Image img = Clipboard.GetImage();

                pictureBox_clipboard.Image = img;

                string filename = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";

                Bitmap bitmap1 = (Bitmap)img;

                if (bitmap1 != null)
                {
                    try
                    {
                        //bitmap1.Save(@file1, ImageFormat.Jpeg);
                        bitmap1.Save(filename, ImageFormat.Bmp);
                        //bitmap1.Save(@file3, ImageFormat.Png);

                        richTextBox1.Text += "存檔成功\n";
                        richTextBox1.Text += "已存檔 : " + filename + "\n";
                    }
                    catch (Exception ex)
                    {
                        richTextBox1.Text += "xxx錯誤訊息b2 : " + ex.Message + "\n";
                        //show_main_message1("存檔失敗", S_OK, 30);
                        //show_main_message2("存檔失敗 : " + ex.Message, S_OK, 30);
                    }
                }
            }
        }

        private void button22_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Clipboard內的影像顯示存檔\t部分\t九宮格之正中\n";

            bool flag = Clipboard.ContainsImage();  //判斷Clipboard中是否包含圖片資料
            richTextBox1.Text += "Clipboard 是否包含圖片資料 : " + flag.ToString() + "\n";

            if (flag == true)
            {
                Image img = Clipboard.GetImage();

                int W = img.Width;
                int H = img.Height;
                int x_st = W / 3;
                int y_st = H / 3;
                int w = W / 3;
                int h = H / 3;

                RectangleF rect = new RectangleF(x_st, y_st, w, h);

                Bitmap bitmap1;

                try
                {
                    // 擷取部份影像，顯示於pictureBox2，區域為(起點x座標, 起點y座標, 寬度, 高度)
                    bitmap1 = ((Bitmap)img).Clone(rect, PixelFormat.Format32bppArgb);
                    pictureBox_clipboard.Image = bitmap1;

                    string filename = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";

                    if (bitmap1 != null)
                    {
                        try
                        {
                            //bitmap1.Save(@file1, ImageFormat.Jpeg);
                            bitmap1.Save(filename, ImageFormat.Bmp);
                            //bitmap1.Save(@file3, ImageFormat.Png);

                            richTextBox1.Text += "存檔成功\n";
                            richTextBox1.Text += "已存檔 : " + filename + "\n";
                        }
                        catch (Exception ex)
                        {
                            richTextBox1.Text += "xxx錯誤訊息b2 : " + ex.Message + "\n";
                            //show_main_message1("存檔失敗", S_OK, 30);
                            //show_main_message2("存檔失敗 : " + ex.Message, S_OK, 30);
                        }
                    }
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "xxx錯誤訊息p : " + ex.Message + "\t";
                }
            }
        }

        private void button23_Click(object sender, EventArgs e)
        {
            //讀出剪貼簿內的資料
            try
            {
                IDataObject dataObject = Clipboard.GetDataObject();
                if (dataObject.GetDataPresent(DataFormats.Text))
                {
                    //richTextBox1.Text += (string)dataObject.GetData(DataFormats.Text) + "\n";
                    richTextBox1.Text += (string)dataObject.GetData(DataFormats.UnicodeText) + "\n";
                }
                else
                {
                    MessageBox.Show("目前剪貼板中數據不可轉換為文本", "錯誤");
                }
            }
            catch (Exception)
            {
                MessageBox.Show("Error");
            }
        }

        private void button24_Click(object sender, EventArgs e)
        {
            //複製資料到剪貼簿
            string data = "複製資料到剪貼簿\n";
            try
            {
                Clipboard.SetText(data);
                //MessageBox.Show("已成功將文本框內容復制到剪貼板!");
            }
            catch (Exception)
            {
                MessageBox.Show("Error!");
            }

        }

        private void button25_Click(object sender, EventArgs e)
        {
            //累計 複製資料到剪貼簿

        }

        private void button26_Click(object sender, EventArgs e)
        {
            //從剪貼板取出圖片然後寫上字保存到文件

            IDataObject dataObject = Clipboard.GetDataObject();
            Image image = (Image)(dataObject.GetData(typeof(Bitmap)));
            if (image == null)
            {
                richTextBox1.Text += "無圖片, 不儲存\n";
                return;
            }
            Graphics g = Graphics.FromImage(image);
            SolidBrush sb = new SolidBrush(Color.Red);
            Font f = new Font("Arial", 10, FontStyle.Bold, GraphicsUnit.Millimeter);
            int x_st = image.Height - (image.Height - 25);
            int y_st = 3;

            g.DrawString("剪貼簿上的圖片存檔" + DateTime.Now.ToString(), f, sb, x_st, y_st);

            Image small_image;

            string filename = Application.StartupPath + "\\pic_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";
            string filename_small = Application.StartupPath + "\\pic_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + "_small.jpg";

            small_image = image.GetThumbnailImage(image.Width, image.Height, null, System.IntPtr.Zero);
            small_image.Save(filename_small, ImageFormat.Jpeg);
            image.Save(filename, ImageFormat.Jpeg);
            image = null;
            small_image = null;

            richTextBox1.Text += "已存檔 : " + filename + "\n";
            richTextBox1.Text += "已存檔 : " + filename_small + "\n";
        }

        private void button27_Click(object sender, EventArgs e)
        {
            //全屏截圖放置到Clipboard中
            this.Hide();//隱藏當前窗體

            Thread.Sleep(500);//讓線程睡眠一段時間，窗體消失需要一點時間

            //全屏截圖
            Bitmap bitmap1 = new Bitmap(Screen.AllScreens[0].Bounds.Width, Screen.AllScreens[0].Bounds.Height);//新建一個和屏幕大小相同的圖片
            pictureBox1.Image = bitmap1;

            Graphics g = Graphics.FromImage(bitmap1);
            g.CopyFromScreen(new Point(0, 0), new Point(0, 0), new Size(Screen.AllScreens[0].Bounds.Width, Screen.AllScreens[0].Bounds.Height));//保存全屏圖片

            g.DrawRectangle(new Pen(Color.Red, 10), 100, 100, 200, 200);//畫個東西

            //片資料放置到Clipboard中
            Clipboard.SetImage(bitmap1);
            this.Show();//重新顯示窗體
        }
    }

    [Serializable()]    //必要的一行
    class Person
    {
        public string FirstName;
        public string LastName;
    }
}

