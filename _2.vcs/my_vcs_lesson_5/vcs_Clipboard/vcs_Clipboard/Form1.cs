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

            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            pictureBox1.Image = Image.FromFile(filename);
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
            dx = 200 + 10;
            dy = 60 + 10;

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

            pictureBox1.Size = new Size(450, 560);
            pictureBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);

            groupBox_clipboard.Size = new Size(300, 140);
            groupBox_clipboard.Location = new Point(x_st + dx * 2, y_st + dy * 8 + 10);

            int W = 300;
            int H = 350;
            richTextBox1.Size = new Size(W, H);
            richTextBox1.Location = new Point(x_st + dx * 4 + 50, y_st + dy * 0);
            richTextBox2.Size = new Size(W, H);
            richTextBox2.Location = new Point(x_st + dx * 4 + 50, y_st + dy * 6);

            W = 360;
            H = 200;
            pictureBox_clipboard.Size = new Size(W, H);
            textBox_clipboard.Size = new Size(W, H);
            richTextBoxp_clipboard.Size = new Size(W, H);
            webBrowser_clipboard.Size = new Size(W, H);

            pictureBox_clipboard.Location = new Point(x_st + dx * 6, y_st + dy * 0);
            textBox_clipboard.Location = new Point(x_st + dx * 6, y_st + dy * 3);
            richTextBoxp_clipboard.Location = new Point(x_st + dx * 6, y_st + dy * 6);
            webBrowser_clipboard.Location = new Point(x_st + dx * 6, y_st + dy * 9);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1680, 910);
            this.Text = "vcs_Clipboard";

            //設定執行後的表單起始位置
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((1920 - this.Size.Width) / 2, (1080 - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //檢查剪貼簿內的資料內容 ST
        private void button0_Click(object sender, EventArgs e)
        {
            //讀出剪貼簿內的資料

            richTextBox1.Text += "\n取得系統剪貼簿裏的資料類型:\n";
            IDataObject dataObject = Clipboard.GetDataObject();

            richTextBox1.Text += "取得剪貼簿內容的資料格式 :\n";
            string[] formats = dataObject.GetFormats();
            foreach (string format in formats)
            {
                richTextBox1.Text += "取得 : " + format + "\n";
            }

            if (dataObject.GetDataPresent(DataFormats.Text))
            {
                richTextBox1.Text += "取得文字:\n";
                Console.WriteLine((String)dataObject.GetData(DataFormats.Text));
                //richTextBox1.Text += (string)dataObject.GetData(DataFormats.Text) + "\n";
                richTextBox1.Text += (string)dataObject.GetData(DataFormats.UnicodeText) + "\n";
            }
            else
            {
                MessageBox.Show("目前剪貼簿中數據不可轉換為文本", "錯誤");
            }

            if (dataObject.GetDataPresent(DataFormats.Bitmap))
            {
                richTextBox1.Text += "取得圖片\n";
                Image image1 = (Bitmap)dataObject.GetData(DataFormats.Bitmap);
                //pictureBox1.Image = image1;
            }

            //6060

            pictureBox_clipboard.Image = null;
            textBox_clipboard.Clear();
            richTextBoxp_clipboard.Clear();
            //webBrowser_clipboard.Navigate("about:blank");

            // Image.
            if (Clipboard.ContainsImage() == true)
            {
                pictureBox_clipboard.Image = Clipboard.GetImage();
            }

            // Text.
            if (Clipboard.ContainsText(TextDataFormat.UnicodeText) == true)
            {
                textBox_clipboard.Text = Clipboard.GetText(TextDataFormat.UnicodeText);
            }

            // HTML.
            if (Clipboard.ContainsText(TextDataFormat.Html) == true)
            {
                HtmlDocument doc = webBrowser_clipboard.Document;
                doc.Body.InnerHtml = Clipboard.GetText(TextDataFormat.Html);
            }

            // Rich Text.
            if (Clipboard.ContainsText(TextDataFormat.Rtf) == true)
            {
                richTextBoxp_clipboard.Rtf = Clipboard.GetText(TextDataFormat.Rtf);
            }
        }
        //檢查剪貼簿內的資料內容 SP

        private void button1_Click(object sender, EventArgs e)
        {
            //取得剪貼簿內容的資料格式

            IDataObject dataObject = Clipboard.GetDataObject();    //讀取數據

            richTextBox1.Text += "取得剪貼簿內容的資料格式 :\n";
            string[] formats = dataObject.GetFormats();
            foreach (string format in formats)
            {
                richTextBox1.Text += "取得 : " + format + "\n";
            }

            if (Clipboard.ContainsData(DataFormats.Bitmap) == true)
            {
                richTextBox1.Text += "Bitmap\n";
            }
            if (Clipboard.ContainsData(DataFormats.Text) == true)
            {
                richTextBox1.Text += "Text\n";
            }
            if (Clipboard.ContainsData(DataFormats.UnicodeText) == true)
            {
                richTextBox1.Text += "UnicodeText\n";
            }
            if (Clipboard.ContainsData(DataFormats.FileDrop) == true)
            {
                richTextBox1.Text += "FileDrop\n";
            }



        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "取得剪貼簿內的資料類型:\n";
            IDataObject dataObject1 = Clipboard.GetDataObject();    //讀取數據

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
            }

            if (dataObject3.GetDataPresent(DataFormats.Html))  //HTML類
            {
                richTextBox1.Text += "取得HTML, 內容：\n";
                //取出Text資料, 可做處理
                String str = (String)dataObject3.GetData(DataFormats.Html);
                richTextBox1.Text += str + "\n";
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
            //放小圖到剪貼簿中, 並貼到圖上
            //string filename = @"D:\_git\vcs\_1.data\______test_files1\__pic\chicken.bmp";

            //放進剪貼簿
            //TBD

            Image clipboard_image = GetClipboardImage();

            if (clipboard_image == null)
            {
                return;
            }

            pictureBox1.Image = clipboard_image;

            return;


            // Draw on the image.
            Graphics gr = Graphics.FromImage(pictureBox1.Image);
            Rectangle source_rect = new Rectangle(0, 0, clipboard_image.Width, clipboard_image.Height);
            int x = 50;
            int y = 50;
            Rectangle dest_rect = new Rectangle(x, y, clipboard_image.Width, clipboard_image.Height);
            gr.DrawImage(clipboard_image, dest_rect, source_rect, GraphicsUnit.Pixel);
            pictureBox1.Refresh();
        }

        // Get a PNG from the clipboard if possible.
        // Otherwise try to get a bitmap.
        private Image GetClipboardImage()
        {
            // Try to paste PNG data.
            if (Clipboard.ContainsData("PNG"))
            {
                richTextBox1.Text += "有PNG圖片\n";
                Object png_object = Clipboard.GetData("PNG");
                if (png_object is MemoryStream)
                {
                    MemoryStream png_stream = png_object as MemoryStream;
                    return Image.FromStream(png_stream);
                }
            }

            // Try to paste bitmap data.
            if (Clipboard.ContainsImage() == true)
            {
                return Clipboard.GetImage();
            }

            // We couldn't find anything useful. Return null.
            return null;
        }

        private void button6_Click(object sender, EventArgs e)
        {
        }

        private void button7_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "將圖片放置到剪貼簿中\n";
            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式
            pictureBox1.Image = bitmap1;
            Clipboard.SetImage(bitmap1);//將影像資料放置到剪貼簿中

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "將全螢幕放置到剪貼簿中\n";

            this.Hide();//隱藏當前窗體

            Thread.Sleep(500);//讓線程睡眠一段時間，窗體消失需要一點時間

            //全屏截圖
            Bitmap bitmap2 = new Bitmap(Screen.AllScreens[0].Bounds.Width, Screen.AllScreens[0].Bounds.Height);//新建一個和屏幕大小相同的圖片
            pictureBox1.Image = bitmap2;

            Graphics g = Graphics.FromImage(bitmap2);
            g.CopyFromScreen(new Point(0, 0), new Point(0, 0), new Size(Screen.AllScreens[0].Bounds.Width, Screen.AllScreens[0].Bounds.Height));//保存全屏圖片

            g.DrawRectangle(new Pen(Color.Red, 10), 100, 100, 200, 200);//畫個東西

            //將圖片資料放置到剪貼簿中
            Clipboard.SetImage(bitmap2);//將影像資料放置到剪貼簿中
            this.Show();//重新顯示窗體
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //將文字資料放置到Clipboard中(不累計)

            /*
            richTextBox1.Text += "將文字資料放置到剪貼簿中\n";
            string data = "翠盖龙旗出建章 莺啼百啭柳初黄";
            Clipboard.SetDataObject(data);	//向剪貼簿中放置資料
            */

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            /*
            //複製純文字
            Clipboard.SetText(richTextBox1.Text);

            //複製資料到剪貼簿
            data = "複製資料到剪貼簿\n";
            try
            {
                Clipboard.SetText(data);
                //MessageBox.Show("已成功將文本框內容復制到剪貼簿!");
            }
            catch (Exception)
            {
                MessageBox.Show("Error!");
            }
            */

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //把資料放到系統剪貼簿裏
            //richTextBox1.Text += "按了 複製資料到剪貼簿\n";
            //Clipboard.SetData(DataFormats.Text, richTextBox1.Text + "\n");
            //Clipboard.SetDataObject(richTextBox1.Text + "\n");      //建議用此
            Clipboard.SetDataObject("複製資料到剪貼簿 " + DateTime.Now.ToString() + "\n");      //建議用此  //將poem字串填到Clipboard裏。

            //復制到剪貼簿上，第二個參數表明程序退出時不清空剪貼簿 
            //Clipboard.SetDataObject(dataobj, true);
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //將文字資料放置到Clipboard中(累計)
            //richTextBox1.Text += "按了 累計複製資料到剪貼簿\n";
            //Clipboard.SetData(DataFormats.Text, Clipboard.GetData(DataFormats.Text) + richTextBox1.Text + "\n");
            //Clipboard.SetDataObject(Clipboard.GetText() + richTextBox1.Text + "\n");      //建議用此
            //Clipboard.GetData(DataFormats.Text) 目前剪貼簿內的文字資料
            //Clipboard.GetText() 目前剪貼簿內的文字資料
            Clipboard.SetDataObject(Clipboard.GetText() + "累計複製資料到剪貼簿 " + DateTime.Now.ToString() + "\n");      //建議用此  //將poem字串填到Clipboard裏。
        }

        private void button10_Click(object sender, EventArgs e)
        {
        }

        private void button11_Click(object sender, EventArgs e)
        {
            //剪貼簿中檔名的集合

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

            if ((Clipboard.ContainsFileDropList() == true) && (Clipboard.GetFileDropList().Count > 0))
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

        private void button12_Click(object sender, EventArgs e)
        {
            //剪貼簿 貼上+編碼
            //貼上剪貼簿
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

        private void button13_Click(object sender, EventArgs e)
        {
            Clipboard.Clear();  //清除剪貼簿中的對象
        }

        private void button14_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Clipboard內的影像顯示存檔\t全部\n";
            bool flag = Clipboard.ContainsImage();  //判斷剪貼簿中是否包含圖片資料
            richTextBox1.Text += "Clipboard 是否包含圖片資料 : " + flag.ToString() + "\n";

            if (flag == true)
            {
                Image image1 = Clipboard.GetImage();
                pictureBox_clipboard.Image = image1;
                Bitmap bitmap1 = (Bitmap)image1;
            }
        }

        private void button15_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Clipboard內的影像顯示存檔\t部分\t九宮格之正中\n";

            bool flag = Clipboard.ContainsImage();  //判斷剪貼簿中是否包含圖片資料
            richTextBox1.Text += "Clipboard 是否包含圖片資料 : " + flag.ToString() + "\n";

            if (flag == true)
            {
                Image image1 = Clipboard.GetImage();

                int W = image1.Width;
                int H = image1.Height;
                int x_st = W / 3;
                int y_st = H / 3;
                int w = W / 3;
                int h = H / 3;

                RectangleF rect = new RectangleF(x_st, y_st, w, h);

                // 擷取部份影像，顯示於pictureBox2，區域為(起點x座標, 起點y座標, 寬度, 高度)
                Bitmap bitmap1 = ((Bitmap)image1).Clone(rect, PixelFormat.Format32bppArgb);
                pictureBox_clipboard.Image = bitmap1;
            }
        }

        private void button16_Click(object sender, EventArgs e)
        {
            //從剪貼簿取出圖片然後寫上字保存到文件

            richTextBox1.Text += "取得剪貼簿內的資料類型:\n";
            IDataObject dataObject = Clipboard.GetDataObject();

            Image image1 = (Image)(dataObject.GetData(typeof(Bitmap)));
            if (image1 == null)
            {
                richTextBox1.Text += "無圖片, 不儲存\n";
                return;
            }
            Graphics g = Graphics.FromImage(image1);
            SolidBrush sb = new SolidBrush(Color.Red);
            Font f = new Font("Arial", 10, FontStyle.Bold, GraphicsUnit.Millimeter);
            int x_st = image1.Height - (image1.Height - 25);
            int y_st = 3;

            g.DrawString("剪貼簿上的圖片存檔" + DateTime.Now.ToString(), f, sb, x_st, y_st);

            Image small_image;

            string filename = Application.StartupPath + "\\pic_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";
            string filename_small = Application.StartupPath + "\\pic_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + "_small.jpg";

            small_image = image1.GetThumbnailImage(image1.Width, image1.Height, null, System.IntPtr.Zero);
            small_image.Save(filename_small, ImageFormat.Jpeg);
            image1.Save(filename, ImageFormat.Jpeg);
            image1 = null;
            small_image = null;

            richTextBox1.Text += "已存檔 : " + filename + "\n";
            richTextBox1.Text += "已存檔 : " + filename_small + "\n";
        }

        private void button17_Click(object sender, EventArgs e)
        {
            //取得剪貼簿中的影像資料

            if (Clipboard.ContainsImage() == true)
            {
                richTextBox1.Text += "剪貼簿中 有 影像資料\n";

                Bitmap bitmap2 = (Bitmap)(Clipboard.GetImage().Clone());
                pictureBox1.Image = bitmap2;
            }
            else
            {
                richTextBox1.Text += "剪貼簿中 無 影像資料\n";
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //從剪貼簿獲取圖片
            IDataObject dataObject = null;
            Bitmap bitmap1 = null;

            try
            {
                Application.DoEvents();
                dataObject = Clipboard.GetDataObject();

                if (Clipboard.ContainsImage() == true)
                {
                    bitmap1 = (Bitmap)(Clipboard.GetImage().Clone());
                }

                //return NewBitmap;
                pictureBox_clipboard.Image = bitmap1;
                richTextBox1.Text += "OK\n";
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
                richTextBox1.Text += "無圖片\n";
            }
        }

        private void button18_Click(object sender, EventArgs e)
        {
        }

        private void button19_Click(object sender, EventArgs e)
        {
            //取得剪貼簿中的文字資料

            bool flag = Clipboard.ContainsText();   //判斷剪貼簿中是否包含文字資料
            //richTextBox1.Text += "Clipboard 是否包含文字資料 : " + flag.ToString() + "\n";

            if (flag == true)
            {
                string text = Clipboard.GetText();//取得剪貼簿中的文字資料
                richTextBox1.Text += "取得文字資料 :\n" + text + "\n";
            }
            else
            {
                richTextBox1.Text += "無  文字資料\n";
            }
        }

        private void bt_clipboard0_Click(object sender, EventArgs e)
        {
            // Paste the person from the Clipboard.
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

        private void bt_clipboard1_Click(object sender, EventArgs e)
        {
            // Copy a Person to the Clipboard.
            Person person = new Person() { FirstName = textBox1.Text, LastName = textBox2.Text };
            Clipboard.SetDataObject(person);
            richTextBox1.Text += "已複製類別到剪貼簿\n";
        }
    }

    [Serializable()]    //必要的一行
    class Person
    {
        public string FirstName;
        public string LastName;
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




