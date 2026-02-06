



//放大和縮小圖像
//圖像縮放操作
//調整 pbox的大小，來改變圖片大小
//pbox的SizeMode要用Zoom

            pictureBox1.Height = Convert.ToInt32(myImage.Height * Convert.ToSingle(textBox1.Text.Trim()));
            pictureBox1.Width = Convert.ToInt32(myImage.Width * Convert.ToSingle(textBox1.Text.Trim()) * 4 / 3);




private void Form1_Load(object sender, EventArgs e)
{
    //按Enter連動到button1
    this.AcceptButton = button1;	//在表單按Enter, 等於按了button1
    this.AcceptButton = button5;            //在表單按enter就執行button5按鈕的動作
    //按ESC連動到button1
    this.CancelButton = button2;

    //不再TaskBar上顯示程式
    this.ShowInTaskbar = false;
}


/*
//儲存新的影像
string filename = Application.StartupPath + "\\rotate_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";
rotateImage.Save(@filename, ImageFormat.Jpeg);
richTextBox1.Text += "影像旋轉，存檔完成，檔名：" + filename + "\n";
*/

/*
//量測字體大小
            Font f = new Font("標楷體", 40);
            string str = "放大縮小";
            int w = g.MeasureString(str, f).ToSize().Width;
            int h = g.MeasureString(str, f).ToSize().Height;
*/


箭頭的畫法

            Pen p = new Pen(Color.Red, 0);
            p.EndCap = LineCap.ArrowAnchor;





            Console.WriteLine("測試多型（Polymorphism）");
            hi();
            hi("lion-mouse");




            Graphics g;

            //新建圖檔, 初始化畫布
            Bitmap bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            g = Graphics.FromImage(bitmap1);
            g.Clear(Color.White);
            pictureBox1.Image = bitmap1;

            int i;
            double gamma;

            int[] data_in = new int[256];
            int[] data_out = new int[256];
            Point[] curvePoints = new Point[256];    //一維陣列內有 N 個Point


            Pen gammaPen = new Pen(Color.Red, 2);
            /*
                                                        gamma = 2.2;
                                                        //畫出真正的Gamma 2.2曲線
                                                        for (i = 0; i < 256; i++)
                                                        {
                                                            data_in[i] = i;
                                                            data_out[i] = (int)(Math.Pow(((double)data_in[i]) / 255, 1 / gamma) * 255);

                                                            curvePoints[i].X = data_in[i] * 3;
                                                            curvePoints[i].Y = 256 * 2 - 1 - data_out[i] * 2;
                                                        }
                                                        g.DrawLines(gammaPen, curvePoints);   //畫直線
            */






//另存新檔
//SaveBitmapUsingExtension(RotatedBitmap, sfdFile.FileName);


        // Save the file with the appropriate format.
        // Throw a NotSupportedException if the file
        // has an unknown extension.
        public void SaveBitmapUsingExtension(Bitmap bm,
            string filename)
        {
            string extension = Path.GetExtension(filename);
            switch (extension.ToLower())
            {
                case ".bmp":
                    bm.Save(filename, ImageFormat.Bmp);
                    break;
                case ".exif":
                    bm.Save(filename, ImageFormat.Exif);
                    break;
                case ".gif":
                    bm.Save(filename, ImageFormat.Gif);
                    break;
                case ".jpg":
                case ".jpeg":
                    bm.Save(filename, ImageFormat.Jpeg);
                    break;
                case ".png":
                    bm.Save(filename, ImageFormat.Png);
                    break;
                case ".tif":
                case ".tiff":
                    bm.Save(filename, ImageFormat.Tiff);
                    break;
                default:
                    throw new NotSupportedException(
                        "Unknown file extension " + extension);
            }
        }








        private void bt_save_Click(object sender, EventArgs e)
        {
            // Make a copy of the result image.
            using (Bitmap bmp = (Bitmap)pictureBox0.Image.Clone())
            {
                bmp.MakeTransparent(Color.Magenta);

                save_image_to_drive(bmp);
            }
        }

        void save_image_to_drive(Bitmap bitmap1)
        {
            if (bitmap1 != null)
            {
                string filename = Application.StartupPath + "\\IMG_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".png";
                bitmap1.Save(@filename, ImageFormat.Png);

                richTextBox1.Text += "已存檔 : " + filename + "\n";
            }
            else
            {
                richTextBox1.Text += "無圖可存\n";
            }
        }





ImageAttributes的使用
是在畫影像 g.DrawImage(bmp, ....)時，
把影像套用了ImageAttributes的設定，像是gamma, color matrix

所以，並不是bmp被套用設定，是bmp經過設定被畫入畫布

這個新的部分，已經畫在Bitmap上，要用Bitmap.Clone方法取出為新的Bitmap位圖

ImageAttributes ia = new ImageAttributes();
ia.SetGamma
ia.SetGamma(0.6f);
ia.SetColorMatrix(cm, ColorMatrixFlag.Default, ColorAdjustType.Bitmap);
ia.SetColorMatrix(cm, ColorMatrixFlag.Default, ColorAdjustType.Bitmap);same
ia.SetColorMatrices(cm, null);//same


            //int[] gray = new int[220];
            //g.DrawLines(Pens.Red, gray.ToArray());


Binary格式讀出一個檔案到拜列

            FileStream fs = new FileStream(oldpath, FileMode.Open);
            BinaryReader br = new BinaryReader(fs);
            byte[] bytes = br.ReadBytes((int)fs.Length);
            br.Close();
            fs.Close();


/*
記住目前的設定值，下次程式開啟時，可以拿來用。

方案總管/Properties/Settings settings/
加入：
名稱 Argbs
型別 System.Int32[]
範圍 User

目前找不到設定型態的位置，只好到Settings settings檔案改成以下：
<Setting Name="Argbs" Type="System.Int32[]" Scope="User">

*/





可以累計點數，緩慢畫出的方法

Points1 為 已知點數

        //公用變數
        List<PointF> Points1 = new List<PointF>();
        List<PointF> Points2 = new List<PointF>();

                Points1.Add(e.Location);

使用timer

        private void timer2_Tick(object sender, EventArgs e)
        {
            int len = Points1.Count;
            Points2.Add(Points1[cnt]);
            pictureBox2.Invalidate();

            cnt++;
            if (cnt >= len)
            {
                timer2.Enabled = false;

            }
        }
        
呼叫pictureBox2重畫

        private void pictureBox2_Paint(object sender, PaintEventArgs e)
        {
            if (Points2.Count > 1)
            {
                e.Graphics.DrawCurve(Pens.Red, Points2.ToArray());
            }

        }

richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個


Array.Copy(array_data, 0, array_data, offset, array_data.Length - offset);
Array.Copy(array_data, offset, array_data, 0, array_data.Length - offset);

richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

製作透明表單

//Form1屬性的BackColor改成Color.White
//Form1屬性的TransparencyKey改成Color.White

設定表單背景色 與 透明色即可 表單上的影像 畫圖 符合條件的 都會變透明

private void Form1_Load(object sender, EventArgs e)
{
    this.BackColor = Color.White;
    this.TransparencyKey = Color.White;
    this.FormBorderStyle = FormBorderStyle.None;
}

richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

StartPiont = (200, 100)
CutArea = (0,0,300,300)

&lt;pre class="c" name="code">
private Image CutImage(Image SourceImage, Point StartPoint, Rectangle CutArea)
{
    Bitmap NewBitmap = new Bitmap(CutArea.Width, CutArea.Height);
    Graphics tmpGraph = Graphics.FromImage(NewBitmap);
    tmpGraph.DrawImage(SourceImage, CutArea, StartPoint.X, StartPoint.Y, CutArea.Width, CutArea.Height, GraphicsUnit.Pixel);
    tmpGraph.Dispose();
    return NewBitmap;
}


C# PictureBox图片框用法详解（附带实例）

https://c.biancheng.net/view/ply3egf.html

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


this.DoubleBuffered = true;//避免闪烁

Graphics g = e.Graphics;      //定义g为该窗体控件的画布　

// Graphics g = this.CreateGraphics(); //避免使用此方法，会出现闪烁
// Graphics g = this.CreateGraphics(); //避免使用此方法，会出现闪烁

绘制圆润指针、曲线
g.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.HighQuality;//使画出的指针、线条更平滑、高质量


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

            //same
            //Image img = Image.FromFile(filename);
            //pictureBox1.Image = img;

            //same
            //pictureBox1.Image = Image.FromFile(filename); //載入圖檔，由檔案

            //same
            //Bitmap bitmap1 = new Bitmap(filename);
            //pictureBox1.Image = bitmap1;

            //same
            //Image img = Bitmap.FromFile(filename);
            //pictureBox1.Image = img;

            //same
            //Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);
            //pictureBox1.Image = bitmap1;

            //same
            pictureBox1.Image = new Bitmap(filename);

            //pictureBox1.ImageLocation = filename;   //可顯示圖片 但無法抓出圖片的相關資訊

            /*
            int width = pictureBox1.Image.Width;
            int height = pictureBox1.Image.Height;
            pictureBox1.SizeMode = PictureBoxSizeMode.Normal;
            pictureBox1.Size = new Size(width, height);
            */

            Image img = Image.FromFile(filename);
            pictureBox1.Image = img;
            pictureBox1.SizeMode = PictureBoxSizeMode.AutoSize;




richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個



單一圖片模式


            button1.Visible = false;
            richTextBox1.Visible = false;
            //this.FormBorderStyle = FormBorderStyle.None;
            this.AutoSize = true;
            this.AutoSizeMode = AutoSizeMode.GrowAndShrink;     //讓表單大小可以自動隨著圖片大小變化。
            this.TransparencyKey = SystemColors.ControlLight;   //將表單的TransparencyKey設為Control，這樣可以去掉桌面小玩意外圍多餘的部份
            this.ShowInTaskbar = false;
            //this.StartPosition = FormStartPosition.CenterScreen;

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
            this.BackColor = Color.Black;

            //pictureBox1.Dock = DockStyle..Fill;      //停駐於父容器中
            pictureBox1.Location = new Point((this.Width - pictureBox1.Image.Width) / 2, (this.Height - pictureBox1.Image.Height) / 2);






richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個




using System.Diagnostics;           //for Debug
            Debug.Assert(Math.Abs(total) < 0.001f);


 
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //using System.Collections;//for Hashtable

            Hashtable imageList = new Hashtable();

            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Image image1 = Image.FromFile(filename);	//Image.FromFile出來的是Image格式

            string filename2 = @"D:\_git\vcs\_1.data\______test_files1\elephant.jpg";
            Image image2 = Image.FromFile(filename2);	//Image.FromFile出來的是Image格式

            string filename3 = @"D:\_git\vcs\_1.data\______test_files1\bear.jpg";
            Image image3 = Image.FromFile(filename3);	//Image.FromFile出來的是Image格式

            imageList.Add(imageList.Count + 1, image1);
            imageList.Add(imageList.Count + 1, image2);
            imageList.Add(imageList.Count + 1, image3);

            object obj = imageList[1];

            //object obj = imageList[3];

            pictureBox1.Image = (Image)obj;
  

richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個




richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            foreach (int argb in Properties.Settings.Default.Argbs)
            {
                Color color = Color.FromArgb(argb);
                richTextBox1.Text += "get color " + color.ToString() + "\n";
                using (SolidBrush br = new SolidBrush(color))
                {
                    e.Graphics.FillRectangle(br, x, y,
                        PatchWidth, PatchHeight);
                }
                x += PatchWidth + PatchMargin;
                if (x > max_x)
                {
                    x = 0;
                    y += PatchHeight + PatchMargin;
                }
            }


richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

object filename = Application.StartupPath + "\\word_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".doc";
		  Application.StartupPath + "\\test_word_file.doc";
string filename = Application.StartupPath + "\\gif_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".gif";

_filename = Path.GetFullPath(Path.Combine(Application.StartupPath, "..\\..")) + "\\test.png";
filename1 = Path.GetFullPath(Path.Combine(System.Windows.Forms.Application.StartupPath, @"..\..")) + @"\Step.doc";

//string filename = Path.GetFullPath(Path.Combine(Application.StartupPath, @"..\..")) + @"\Step.doc";
//string filename = Path.GetFullPath(Path.Combine(Application.StartupPath, @"..\..")) + @"\bmp_format.docx";
ring doc_filename = Path.GetFullPath(Path.Combine(Application.StartupPath, @"..\..")) + @"\vcs__WORD7.docx";

取得副檔名 包含. .jpg .bmp
string extension = Path.GetExtension(filename);

richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個



button1.PerformClick();	把按鍵按一下



richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個



            pictureBox1.Image = bitmap1; //顯示在 pictureBox1 圖片控制項中
            this.BackgroundImage = bitmap1;//顯示在 表單中




        private void listView1_KeyDown(object sender, KeyEventArgs e)
        {
            //listView接受鍵盤的Delete鍵
            if (e.KeyCode == Keys.Delete)
            {
                if (listView1.SelectedItems.Count > 0)
                {
                    listView1.SelectedItems[0].Remove();
                }
            }
        }
        
        

            string filename = @"../../net/net1.net";

            using (TextReader reader = new StreamReader(filename))
            {
                string line = reader.ReadLine();
                while (line != null)
                {
                    richTextBox1.Text += line + "\n";

                    line = reader.ReadLine();
                }
            }





            //Rectangle 的 Union
            Graphics g = this.pictureBox1.CreateGraphics();

            Rectangle rec1 = new Rectangle(100, 10, 200, 200);
            Rectangle rec2 = new Rectangle(150, 100, 200, 200);
            Rectangle rec3 = new Rectangle(30, 150, 200, 200);
            g.DrawRectangle(Pens.Red, rec1);
            g.DrawRectangle(Pens.Green, rec2);
            g.DrawRectangle(Pens.Blue, rec3);

            Rectangle new_rect = Rectangle.Union(rec1, rec2);
            new_rect = Rectangle.Union(new_rect, rec3);
            g.DrawRectangle(Pens.Magenta, new_rect);




                            string txt = link.Cost.ToString();
                            SizeF txt_size = gr.MeasureString(txt, this.Font);
                            gr.DrawString(txt, this.Font, Brushes.Black,
                                x1 - txt_size.Width / 2,
                                y1 - txt_size.Height / 2);

                string txt = node.Id.ToString();
                SizeF txt_size = gr.MeasureString(txt, this.Font);
                gr.DrawString(txt, this.Font, text_brush,
                    node.Location.X - txt_size.Width / 2,
                    node.Location.Y - txt_size.Height / 2);






        private void pictureBox1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "pictureBox1 ";

            PictureBox pic = sender as PictureBox;
            richTextBox1.Text += pic.Name + " ";
            //MessageBox.Show(pic.Name);
        }
        

        //重寫表單的OnPaint範例 直接寫在此即可
        protected override void OnPaint(PaintEventArgs e)
        {
            e.Graphics.DrawRectangle(Pens.Red, 5, 5, this.Width - 10, this.Height - 10);
        }








            groupBox10.Location = new Point(x_st + dx * 2, y_st + dy * 6 - 40); //listView
            listView1.Location = new Point(5, 10);
            listView1.Size = new Size(360, 120);
            bt3.Location = new Point(370, 10);



        void load_listview_data()
        {
            DateTime dt = DateTime.Now;

            listView1.Items.Add(new ListViewItem(new String[] { "ToLongDateString", "D", dt.ToLongDateString() }));
            listView1.Items.Add(new ListViewItem(new String[] { "ToLongTimeString", "T", dt.ToLongTimeString() }));
            listView1.Items.Add(new ListViewItem(new String[] { "ToShortDateString", "d", dt.ToShortDateString() }));
            listView1.Items.Add(new ListViewItem(new String[] { "ToShortTimeString", "t", dt.ToShortTimeString() }));
            listView1.Items.Add(new ListViewItem(new String[] { "ToString", "G", dt.ToString() }));
        }

        private void bt3_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "c = " + listView1.Items.Count.ToString() + "\n";
            for (int i = 0; i < listView1.Items.Count; i++)
            {
                for (int j = 0; j < listView1.Items[i].SubItems.Count; j++)
                {
                    //richTextBox1.Text += "c2 = " + listView1.Items[i].SubItems.Count.ToString() + "\n";
                    richTextBox1.Text += "i = " + i.ToString() + listView1.Items[i] + "\tj = " + j.ToString() + listView1.Items[i].SubItems[j] + "\n";
                }
            }
        }





textBox 的 KeyPress

        private void textBox2_KeyPress(object sender, KeyPressEventArgs e)
        {
            if ((e.KeyChar < 48 || e.KeyChar > 57) && e.KeyChar != 8 && e.KeyChar != 13)
            {
                e.Handled = true;
            }
            else if (e.KeyChar == 13)
            {
                int textSize = int.Parse(textBox2.Text);
                //ApplyTextSize(textSize);

                e.Handled = true;
                this.richTextBox1.Focus();
            }
        }






richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個



//Cursor myCursor = new Cursor(@"C:\WINDOWS\Cursors\cross_r.cur"); //自定義鼠標 

string location = System.Reflection.Assembly.GetExecutingAssembly().Location;
//string serviceFileName = location.Substring(0, location.LastIndexOf('\\')) + "\\" + serviceName + ".exe";



richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個




richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個


            ListViewItem i1 = new ListViewItem("aaaaaaa");
            ListViewItem.ListViewSubItem sub_i1a = new ListViewItem.ListViewSubItem();
            sub_i1a.Text = "bbbbb";
            i1.SubItems.Add(sub_i1a);
            listView1.Items.Add(i1);


            //設置ListView最後一行可見
            listView1.Items[listView1.Items.Count - 1].EnsureVisible();

richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

splitContainer1
splitContainer1 預設兩個Panel, Panel1 和 Panel2，Dock 選 DockStyle.Fill
放控件至Panel中，Dock 選 DockStyle.Fill


richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個



listView1 屬性 的 ContextMenuStrip 加 contextMenuStrip1


vcs_ListView3_ContextMenuStrip

點選contextMenuStrip1, 在這裡輸入, 項目名稱, 例如 : 取消選擇

使ListView控制元件中的選擇項目以高亮度方式顯示
使ListView控制元件中的選擇項目以高亮度方式顯示


        private void button1_Click(object sender, EventArgs e)
        {
            Graphics g = this.CreateGraphics();
            Size s = this.Size;
            Bitmap bitmap1 = new Bitmap(s.Width, s.Height, g);
            Graphics memoryGraphics = Graphics.FromImage(bitmap1);
            memoryGraphics.CopyFromScreen(this.Location.X, this.Location.Y, 0, 0, s);

            pictureBox1.Image = bitmap1;

            //e.Graphics.DrawImage(memoryImage, 0, 0);
        }


richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個


this.TreeViewFile.Dock = System.Windows.Forms.DockStyle.Fill;


richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個


TreeView 加 圖片icon設定

魏
	曹操
		曹昂
		曹丕	曹叡
		曹彰
		曹植
		曹沖

	司馬懿
		司馬師
		司馬昭	司馬炎
		司馬倫

蜀
	劉備	劉禪、劉永、劉理
	關羽	關平 關興
	張飛	張苞 張紹
吳

	孫堅
		孫策	孫紹
		孫權	孫登
			孫和
			孫休
			孫亮

richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

//把控件當引數傳遞
result = image_processing19(pictureBox1, cx, cy, R, 150F);

//函數部分
public Image image_processing19(string filename, int x, int y, int R, float better)
{
    Bitmap bitmap1 = new Bitmap(Pict.Image, Pict.Image.Width, Pict.Image.Height);//根據圖像實例化Bitmap類
    


richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

String.Format("{0，–10}",text)
//要将字符串向左对齐使用负数，正对齐使用正数，里面的值为当前所占字符的格子。例如:

String aaa = String.Format("{0,-30} | {1,-20} | {2,5}", "a", "b", 3);
String bbb = String.Format("{0,-30} | {1,-20} | {2,5}", "aaaaaaaaaaaaaaaaaaaaaaaa", "b", 3);
String ccc = String.Format("{0,-30} | {1,-20} | {2,5}", "aaaa", "b", 3);


richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

                    Color pt;
                    x_st = WW / 2 - ww / 2 + flag_right_left_cnt * awb_step + flag_right_left_point_cnt;
                    if (x_st < 0)
                        x_st = 0;
                    if ((x_st + ww) > WW)
                        x_st = WW - ww;

                    y_st = HH / 2 - hh / 2 + flag_down_up_cnt * awb_step + flag_down_up_point_cnt;
                    if (y_st < 0)
                        y_st = 0;
                    if ((y_st + hh) > HH)
                        y_st = HH - hh;

                    total_R = 0;
                    total_G = 0;
                    total_B = 0;

                    for (j = 0; j < hh; j++)
                    {
                        for (i = 0; i < ww; i++)
                        {
                            pt = bitmap1.GetPixel(x_st + i, y_st + j);
                            total_R += pt.R;
                            total_G += pt.G;
                            total_B += pt.B;
                        }
                    }

vcs 之 radioButton 可以用Image, Text設為空

richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

SaveBitmapUsingExtension(TheBitmap, sfdImage.FileName);

        public void SaveBitmapUsingExtension(Bitmap bm, string filename)
        {
            string extension = Path.GetExtension(filename);
            switch (extension.ToLower())
            {
                case ".bmp":
                    bm.Save(filename, ImageFormat.Bmp);
                    break;
                case ".exif":
                    bm.Save(filename, ImageFormat.Exif);
                    break;
                case ".gif":
                    bm.Save(filename, ImageFormat.Gif);
                    break;
                case ".jpg":
                case ".jpeg":
                    bm.Save(filename, ImageFormat.Jpeg);
                    break;
                case ".png":
                    bm.Save(filename, ImageFormat.Png);
                    break;
                case ".tif":
                case ".tiff":
                    bm.Save(filename, ImageFormat.Tiff);
                    break;
                default:
                    throw new NotSupportedException(
                        "Unknown file extension " + extension);
            }
        }

vcs
            //撈出一層jpg檔

            string foldername = @"C:\_git\vcs\_1.data\______test_files1\__pic\_書畫字圖\_peony1";
            string[] filenames = Directory.GetFiles(foldername, "*.jpg");

            foreach (string filename in filenames)
            {
                richTextBox1.Text += "取得檔案 : " + filename + "\n";
            }

richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

/*
//圖片檔案 => Image => MemoryStream(ms) => 拜列
//拜列 => MemoryStream(ms) => Image => 圖片檔案
// bmp/png 資料長度 4*W*H + 檔頭54拜
// jpg     資料長度 3*W*H + 檔頭54拜
*/

richTextBox1.Text += byte_data[i].ToString("D03");

# new_image = old_image * 2 - contrast + brightness

 output = image * (contrast / 127 + 1) - contrast + brightness

    //內存法
    public class LockBitmap
    {
        Bitmap bmp = null;
        IntPtr Iptr = IntPtr.Zero;

        public byte[] byte_data { get; set; }
        public int Depth { get; private set; }
        public int Width { get; private set; }
        public int Height { get; private set; }


        /// <summary>
        /// Get the color of the specified pixel
        /// </summary>
        /// <param name="x"></param>
        /// <param name="y"></param>
        /// <returns></returns>
        public Color GetPixel(int x, int y)
        {
            Color clr = Color.Empty;

            // Get color components count
            int cCount = Depth / 8;

            // Get start index of the specified pixel
            int i = ((y * Width) + x) * cCount;

            if (i > byte_data.Length - cCount)
                throw new IndexOutOfRangeException();

            if (Depth == 32) // For 32 bpp get Red, Green, Blue and Alpha
            {
                byte b = byte_data[i];
                byte g = byte_data[i + 1];
                byte r = byte_data[i + 2];
                byte a = byte_data[i + 3]; // a
                clr = Color.FromArgb(a, r, g, b);
            }
            if (Depth == 24) // For 24 bpp get Red, Green and Blue
            {
                byte b = byte_data[i];
                byte g = byte_data[i + 1];
                byte r = byte_data[i + 2];
                clr = Color.FromArgb(r, g, b);
            }
            if (Depth == 8)
            // For 8 bpp get color value (Red, Green and Blue values are the same)
            {
                byte c = byte_data[i];
                clr = Color.FromArgb(c, c, c);
            }
            return clr;
        }

        /// <summary>
        /// Set the color of the specified pixel
        /// </summary>
        /// <param name="x"></param>
        /// <param name="y"></param>
        /// <param name="color"></param>
        public void SetPixel(int x, int y, Color color)
        {
            // Get color components count
            int cCount = Depth / 8;

            // Get start index of the specified pixel
            int i = ((y * Width) + x) * cCount;

            if (Depth == 32) // For 32 bpp set Red, Green, Blue and Alpha
            {
                byte_data[i] = color.B;
                byte_data[i + 1] = color.G;
                byte_data[i + 2] = color.R;
                byte_data[i + 3] = color.A;
            }
            if (Depth == 24) // For 24 bpp set Red, Green and Blue
            {
                byte_data[i] = color.B;
                byte_data[i + 1] = color.G;
                byte_data[i + 2] = color.R;
            }
            if (Depth == 8)
            // For 8 bpp set color value (Red, Green and Blue values are the same)
            {
                byte_data[i] = color.B;
            }
        }
    }


#-----------------------------
    //指針法
    public class PointBitmap
    {
        public Color GetPixel(int x, int y)
        {
            unsafe
            {
                byte* ptr = (byte*)Iptr;
                ptr = ptr + bmpData.Stride * y;
                ptr += Depth * x / 8;
                Color c = Color.Empty;
                if (Depth == 32)
                {
                    int a = ptr[3];
                    int r = ptr[2];
                    int g = ptr[1];
                    int b = ptr[0];
                    c = Color.FromArgb(a, r, g, b);
                }
                else if (Depth == 24)
                {
                    int r = ptr[2];
                    int g = ptr[1];
                    int b = ptr[0];
                    c = Color.FromArgb(r, g, b);
                }
                else if (Depth == 8)
                {
                    int r = ptr[0];
                    c = Color.FromArgb(r, r, r);
                }
                return c;
            }
        }

        public void SetPixel(int x, int y, Color c)
        {
            unsafe
            {
                byte* ptr = (byte*)Iptr;
                ptr = ptr + bmpData.Stride * y;
                ptr += Depth * x / 8;
                if (Depth == 32)
                {
                    ptr[3] = c.A;
                    ptr[2] = c.R;
                    ptr[1] = c.G;
                    ptr[0] = c.B;
                }
                else if (Depth == 24)
                {
                    ptr[2] = c.R;
                    ptr[1] = c.G;
                    ptr[0] = c.B;
                }
                else if (Depth == 8)
                {
                    ptr[2] = c.R;
                    ptr[1] = c.G;
                    ptr[0] = c.B;
                }
            }
        }
    }



那個vcs影像處理

應該改成

do_grayscale1_pixel()

do_grayscale1_marshal()

do_grayscale1_pixel()

函數包起來，這樣要做做1000次量測時間用


richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

/*

            //int i;
            for (i = 0; i < 100; i++)
            {
                richTextBox1.Text += data[i].ToString() + " ";
            }
            richTextBox1.Text += "\n\n";


                    richTextBox1.Text += "aaa" + data[lineIndex + x + 2].ToString() + " " +
    data[lineIndex + x + 1].ToString() + " " +
    data[lineIndex + x + 0].ToString() + "\n";

                    richTextBox1.Text += "bbb" + data[lineIndex + x + 2].ToString() + " " +
    data[lineIndex + x + 1].ToString() + " " +
    data[lineIndex + x + 0].ToString() + "\n";


 *             Bitmap bmp = new Bitmap(@"C:/_git/vcs/_1.data/______test_files1/pic_256X10.bmp");

            pictureBox1.Image = bmp;

            W = bmp.Width;
            H = bmp.Height;

            BitmapData bmpData = bmp.LockBits(new Rectangle(0, 0, W, H), ImageLockMode.ReadOnly, PixelFormat.Format24bppRgb);

            w = bmpData.Width;
            h = bmpData.Height;

            //拷貝出來
            byte[] data = new byte[bmpData.Width * bmpData.Height * 3];
            Marshal.Copy(bmpData.Scan0, data, 0, data.Length); //複製記憶體區塊

            bmp.UnlockBits(bmpData);

            richTextBox1.Text += "------------------------------------------------------------------\n";
*/

        public class EMAFilterRGB2
        {
            private Bitmap emaFrame; // [高度, 寬度, 3]
            private bool initialized = false;
            private readonly float alpha;

            public EMAFilterRGB2(float alpha)
            {
                if (alpha < 0 || alpha > 1)
                    throw new ArgumentException("Alpha 必須介於 0 和 1 之間。");
                this.alpha = alpha;
            }

            public Bitmap Apply(Bitmap currentFrame)
            {
                //int height = currentFrame.GetLength(0);
                //int width = currentFrame.GetLength(1);
                //int channels = currentFrame.GetLength(2);
                int height = currentFrame.Height;
                int width = currentFrame.Width;

                if (!initialized)
                {
                    emaFrame = (Bitmap)currentFrame.Clone();
                }

                Bitmap output = new Bitmap(width, height);
                Color pt1;
                Color pt2;
                Color pt3;

                int total_R = 0;
                int total_G = 0;
                int total_B = 0;

                for (int y = 0; y < height; y++)
                {
                    for (int x = 0; x < width; x++)
                    {
                        pt1 = currentFrame.GetPixel(x, y);
                        pt2 = emaFrame.GetPixel(x, y);
                        total_R = (int)(alpha * pt1.R + (1 - alpha) * pt2.R);
                        total_G = (int)(alpha * pt1.G + (1 - alpha) * pt2.G);
                        total_B = (int)(alpha * pt1.B + (1 - alpha) * pt2.B);
                        
                        pt3 = Color.FromArgb(total_R, total_G, total_B);

                        emaFrame.SetPixel(x, y, pt3);
                    }
                }

                return output;
            }
        }
        

PixelFormat.Format8bppIndexed:
每像素使用 1 个字节（8 位）表示颜色，通常用于索引颜色表的灰度或调色板图像。

PixelFormat.Format16bppRgb555 或 PixelFormat.Format16bppRgb565:
每像素使用 2 个字节（16 位）表示 RGB 颜色。

PixelFormat.Format24bppRgb 或 PixelFormat.Format32bppRgb:
每像素分别使用 3 个字节（24 位）或 4 个字节（32 位，额外字节通常为 0 或填充）表示 RGB 颜色。

PixelFormat.Format32bppArgb 或 PixelFormat.Format32bppPArgb:
每像素使用 4 个字节（32 位）表示 ARGB 颜色，其中 A 代表 Alpha 透明通道。

PixelFormat.Format48bppRgb 或 PixelFormat.Format64bppArgb:
每像素分别使用 6 个字节（48 位）或 8 个字节（64 位）表示高精度 RGB 或 ARGB 颜色。



richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

vcs 使用 macro

#define Use_IndexOf
#define Use_HitTest

        // Display the row and column under the mouse.
        private void listView1_MouseMove(object sender, MouseEventArgs e)
        {
            txtRow.Clear();
            txtColumn.Clear();

#if Use_IndexOf
            // Method 3: Use HitTest and IndexOf.
            ListViewHitTestInfo hti = listView1.HitTest(e.Location);
            if (hti.Item == null) return;
            ListViewItem item = hti.Item;
            txtRow.Text = item.Index.ToString();

            // See which sub-item this is.
            txtColumn.Text = item.SubItems.IndexOf(hti.SubItem).ToString();
#elif Use_HitTest
            // Method 2: Use HitTest.
            ListViewHitTestInfo hti = listView1.HitTest(e.Location);
            if (hti.Item == null) return;
            ListViewItem item = hti.Item;
            txtRow.Text = item.Index.ToString();

            // See which sub-item this is.
            ListViewItem.ListViewSubItem subitem = hti.SubItem;
            for (int i = 0; i < item.SubItems.Count; i++)
            {
                if (item.SubItems[i] == subitem)
                {
                    txtColumn.Text = i.ToString();
                }
            }
#else
            // Method 1: Use the FindListViewRowColumn method.
            int row, column;
            if (listView1.FindListViewRowColumn(e.X, e.Y, out row, out column))
            {
                txtRow.Text = row.ToString();
                txtColumn.Text = column.ToString();
            }
#endif

richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個




richTextBox1.Text += "------------------------------------------------------------\n";  // 60個


richTextBox1.Text += "------------------------------------------------------------\n";  // 60個




richTextBox1.Text += "------------------------------------------------------------\n";  // 60個



            string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_ReadWriteFile\data\excel_20210602_131921.xls";

            richTextBox1.Text += filename + "\n";


richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個


            //string filename = Path.GetFullPath(Path.Combine(Application.StartupPath, @"..\..")) + @"\excel_20210602_131921.xls";



        //將屬標限制在表單內
        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            Cursor.Clip = new Rectangle(this.Location, this.Size); //控制鼠標在窗口範圍內
        }





richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

dgv1
            //// Make the columns autosize.
            //foreach (DataGridViewColumn col in dataGridView1.Columns)
            //    col.AutoSizeMode = DataGridViewAutoSizeColumnMode.AllCells;

------------------------------------------------------------
------------------------------------------------------------

                    axWindowsMediaPlayer1.Ctlcontrols.playItem(playListDict[path]);		playItem ??

指名播放某項
                axWindowsMediaPlayer1.currentMedia = axWindowsMediaPlayer1.currentPlaylist.Item[int.Parse(lvDetail.SelectedItems[0].Text) - 1];

            IWMPMedia currentMedia = axWindowsMediaPlayer1.currentMedia;


        public int index = 1;
        public int listIndex;
        private bool first_in = true;   //是否第一次進入歌詞區域
        private bool showLrc = true;//預設顯示歌詞
        private int index = 0;//播放的圖片下標
														private List<string> imageList;//播放的圖片
        private Point closePoint;//關閉按鈕的位置
        private Size dfSize;//最初的位置


        //聲音
        SoundPlayer player = new SoundPlayer();
        Dictionary<string, string> dic = new Dictionary<string, string>();

        //播放列表
        Dictionary<string, IWMPMedia> playListDict = new Dictionary<string, IWMPMedia>();

						List<string> al = new List<string>(); //當前歌詞時間表     

        IWMPMedia media;


        /// <summary>
        ///  刪除選中的檔案 並停止播放
        private void skinButton2_Click(object sender, EventArgs e)
        {
            try
            {
                ListView.SelectedIndexCollection indexes = this.lvDetail.SelectedIndices;
                if (indexes.Count > 0)
                {
                    int index = indexes[0];
                    string path = this.lvDetail.Items[index].SubItems[4].Text;
					
                    IWMPPlaylist iWMPPlaylist = axWindowsMediaPlayer1.currentPlaylist;
                    //先移除播放列表 再移除listview列表
                    axWindowsMediaPlayer1.currentPlaylist.removeItem(playListDict[path]);
					
                    playListDict.Remove(path);
                    this.lvDetail.Items[index].Remove();
                    dic.Remove(path);
                }
            }
        }
		
------------------------------------------------------------
------------------------------------------------------------

var urlFormat = @"

http://maps.google.com/maps/api/staticmap?center={0},           
 
    {1}&size=640x640&format=jpg&sensor=false&markers=color:red%7Csize:mid%7Clabel:A%7C{0},{1}";
https://maps.googleapis.com/maps/api/staticmap?parameters

------------------------------------------------------------
------------------------------------------------------------

http://maps.google.com/maps/api/staticmap?parameters

https://maps.googleapis.com/maps/api/staticmap?parameters


如何抓取Google Static Map

https://maps.googleapis.com/maps/api/staticmap?center=Brooklyn+Bridge,New+York,NY&zoom=13&size=600x300&maptype=roadmap
&markers=color:blue%7Clabel:S%7C40.702147,-74.015794&markers=color:green%7Clabel:G%7C40.711614,-74.012318
&markers=color:red%7Clabel:C%7C40.718217,-73.998284
&key=AIzaSyDlCB_7UxkHonf782F-MhLa_DmCxfAzSRY




AIzaSyDlCB_7UxkHonf782F-MhLa_DmCxfAzSRY



        private const string mapurl = "http://maps.google.com/mapdata?latitude_e6={0}&longitude_e6={1}&zm={2}&w={3}&h={4}&cc=&min_priority=2";

string.Format(mapurl, this.Latitude, this.Longitude, this.Zoom, this.Width.Value, this.Height.Value)
			
			url : http://maps.google.com/mapdata?latitude_e6=100&longitude_e6=123&zm=200&w=640&h=480&cc=&min_priority=2



------------------------------------------------------------
------------------------------------------------------------

範例網址：
http://maps.google.com/mapdata?Point=b&Point.latitude_e6=23000944&Point.longitude_e6=120180160&Point.iconid=17&Point=e&zm=33900&w=113&h=113&cc=&min_priority=3&client=internal-mobilefe&zl=7

參數說明：
Point=b和Point=e：代表一個點的開始和結尾
Point.latitude_e6：緯度 (無小數點，小數取到第六位)
Point.longitude_e6：經度(無小數點，小數取到第六位)
w：取得的圖片寬度
h：取得的圖片高度
cc：目前好像沒用
min_priority：試著去改過，不過好像沒什麼作用
client：照著輸入即可
zl：縮放比例 (0~17)
zm：應該是Zoom Meter，計算方式為 (zl + 1) * w 




http://maps.google.com/mapdata?latitude_e6=51600117&longitude_e6=
 4293842485&zm=9600&w=600&h=400&cc=&min_priority=2
 
 
------------------------------------------------------------
------------------------------------------------------------





------------------------------------------------------------
------------------------------------------------------------


//C# WinForm窗口最小化到系統托盤2


1.設置WinForm窗體屬性showinTask=false
2.加notifyicon控件notifyIcon1，為控件notifyIcon1的屬性Icon添加一個icon圖標。
3.添加窗體最小化事件(首先需要添加事件引用)：


this.SizeChanged += new System.EventHandler(this.Form1_SizeChanged);
//上面一行是主窗體InitializeComponent()方法中需要添加的引用
private void Form1_SizeChanged(object sender, EventArgs e)
{
if(this.WindowState == FormWindowState.Minimized)
{
this.Hide();
this.notifyIcon1.Visible=true;
}
}

4.添加點擊圖標事件(首先需要添加事件引用)：

private void notifyIcon1_Click(object sender, EventArgs e)
{
this.Visible = true;
this.WindowState = FormWindowState.Normal;
this.notifyIcon1.Visible = false;
}

5.可以給notifyIcon添加右鍵菜單：
主窗體中拖入一個ContextMenu控件NicontextMenu，點中控件，在上下文菜單中添加菜單，notifyIcon1的ContextMenu行為中選中NicontextMenu 作為上下文菜單。
代碼如下：

this.notifyIcon1 = new System.Windows.Forms.NotifyIcon(this.components);
this.NicontextMenu = new System.Windows.Forms.ContextMenu();
this.menuItem_Hide = new System.Windows.Forms.MenuItem();

this.menuItem_Show = new System.Windows.Forms.MenuItem();
this.menuItem_Aubot = new System.Windows.Forms.MenuItem();
this.menuItem_Exit = new System.Windows.Forms.MenuItem();
this.notifyIcon1.ContextMenu = this.NicontextMenu;
this.notifyIcon1.Icon = ((System.Drawing.Icon)(resources.GetObject( "NotifyIcon.Icon ")));
this.notifyIcon1.Text = " ";
this.notifyIcon1.Visible = true;
this.notifyIcon1.DoubleClick += new System.EventHandler(this.notifyIcon1_DoubleClick);
this.notifyIcon1.Click += new System.EventHandler(this.notifyIcon1_Click);
this.NicontextMenu.MenuItems.AddRange(
new System.Windows.Forms.MenuItem[]
{
this.menuItem_Hide,
this.menuItem_Show,
this.menuItem_Aubot,
this.menuItem_Exit
}
);
//
// menuItem_Hide
//
this.menuItem_Hide.Index = 0;
this.menuItem_Hide.Text = "隱藏 ";
this.menuItem_Hide.Click += new System.EventHandler(this.menuItem_Hide_Click);
//
// menuItem_Show
//
this.menuItem_Show.Index = 1;
this.menuItem_Show.Text = "顯示 ";
this.menuItem_Show.Click += new System.EventHandler(this.menuItem_Show_Click);
//
// menuItem_Aubot
//
this.menuItem_Aubot.Index = 2;
this.menuItem_Aubot.Text = "關於 ";
this.menuItem_Aubot.Click += new System.EventHandler(this.menuItem_Aubot_Click);
//
// menuItem_Exit
//
this.menuItem_Exit.Index = 3;
this.menuItem_Exit.Text = "退出 ";
this.menuItem_Exit.Click += new System.EventHandler(this.menuItem_Exit_Click);
protected override void OnClosing(CancelEventArgs e)
{
this.ShowInTaskbar = false;
this.WindowState = FormWindowState.Minimized;
e.Cancel = true;
}
protected override void OnClosing(CancelEventArgs e)
{
//this.ShowInTaskbar = false;
this.WindowState = FormWindowState.Minimized;
e.Cancel = true;
}
private void CloseCtiServer()
{
timer.Enabled = false;
DJ160API.DisableCard();
this.NotifyIcon.Visible = false;
this.Close();
this.Dispose();
Application.Exit();
}
private void HideCtiServer()
{
this.Hide();
}
private void ShowCtiServer()
{
this.Show();
this.WindowState = FormWindowState.Normal;
this.Activate();
}
private void CtiManiForm_Closing(object sender, System.ComponentModel.CancelEventArgs e)
{
this.CloseCtiServer();
}
private void menuItem_Show_Click(object sender, System.EventArgs e)
{
this.ShowCtiServer();
}
private void menuItem_Aubot_Click(object sender, System.EventArgs e)
{
}
private void menuItem_Exit_Click(object sender, System.EventArgs e)
{
this.CloseCtiServer();
}
private void menuItem_Hide_Click(object sender, System.EventArgs e)
{
this.HideCtiServer();
}
private void CtiManiForm_SizeChanged(object sender, System.EventArgs e)
{
if(this.WindowState == FormWindowState.Minimized)
{
this.HideCtiServer();
}
}
private void notifyIcon1_DoubleClick(object sender,System.EventArgs e)
{
this.ShowCtiServer();
}


------------------------------------------------------------
------------------------------------------------------------








把一個ENUM的內容用foreach加到一個combobox裡
點選combobox的項目 套用之

用以測googlemap之各種地圖 圖標



逐步解說：使用 C 撰寫複合控制項#


複合控制項提供可以建立及重複使用自訂圖形介面的方法。 複合控制項基本上是具有視覺表示的元件。 因此，它可能包含一或多個 Windows Forms 控制項、元件或程式碼區塊，可以藉由驗證使用者輸入、修改顯示屬性，或執行作者需要的其他工作來擴充功能。 複合控制項可以放在 Windows Forms 上，與其他控制項的方式相同。 在本逐步解說的第一個部分中，您可以建立簡單的複合控制項，稱為 ctlClock。 在逐步解說的第二個部分中，您透過繼承擴充 ctlClock 的功能。
建立專案

當您建立新的專案時，您會指定其名稱以設定根命名空間、組件名稱和專案名稱，並且確定預設元件將會在正確的命名空間中。
建立 ctlClockLib 控制項程式庫和 ctlClock 控制項



    在 Visual Studio 中，建立新的Windows Forms 控制項程式庫專案，並將它命名為ctlClockLib。

    專案名稱，ctlClockLib，預設也會指派給根命名空間。 根命名空間是用來限定組件中的元件名稱。 例如，如果兩個組件提供元件，名為 ctlClock，您可以使用 ctlClockLib.ctlClock. 指定您的 ctlClock 元件

    在方案總管中，以滑鼠右鍵按一下 [ UserControl1]，然後按一下 [重新命名]。 將檔案名稱變更為 ctlClock.cs。 當系統詢問您是否要重新命名程式碼元素 "UserControl1" 的所有參考時，請按一下 [ 是] 按鈕。




    注意

    依預設，複合控制項繼承自系統提供的 UserControl 類別。 UserControl類別提供所有複合控制項所需的功能，並可執行標準方法和屬性。

    在 [檔案] 功能表上按一下 [全部儲存] 以儲存專案。

將 Windows 控制項和元件新增至複合控制項

視覺化介面是複合控制項不可或缺的一部分。 這個視覺化介面是藉由將一或多個 Windows 控制項新增至設計工具介面來實作。 在下列示範中，您將 Windows 控制項合併到您的複合控制項，並且撰寫程式碼來實作功能。
將標籤和計時器新增至複合控制項

    在方案總管中，以滑鼠右鍵按一下 [ ctlClock]，然後按一下 [視圖設計工具]。

    在 [ 工具箱] 中，展開 [ 通用控制項 ] 節點，然後按兩下 [ 標籤]。

    Label系統會將名 label1 為的控制項新增至設計工具介面上的控制項。

    在設計工具中，按一下 [ label1]。 在 [屬性] 視窗中設定下列屬性。
    屬性 	變更為
    名稱 	lblDisplay
    Text 	(blank space)
    TextAlign 	MiddleCenter
    字型。大小 	14

    在 [工具箱] 中展開 [元件] 節點，然後再按兩下 [計時器]。

    Timer因為是元件，所以在執行時間沒有視覺標記法。 因此，它不會與控制項一起出現在設計工具介面上，而是在 元件設計 工具中 (設計工具介面底部的紙匣) 。

    在元件設計工具中，按一下 [ timer1]，然後將屬性設定為 1000 ，並 Enabled 將屬性設定 Interval 為 true 。

    Interval屬性控制元件刻度的頻率 Timer 。 每次 timer1 走動時，它會執行 timer1_Tick 事件中的程式碼。 間隔代表刻度之間的毫秒數。

    在 元件設計工具中，按兩下 [ timer1 ] 以移至的 timer1_Tick 事件 ctlClock 。

    修改程式碼，使它類似下列程式碼範例。 請確定將存取修飾詞從 private 變更為 protected。
    C#

protected void timer1_Tick(object sender, System.EventArgs e)
{
    // Causes the label to display the current time.
    lblDisplay.Text = DateTime.Now.ToLongTimeString();
}

此程式碼會造成目前時間在 lblDisplay 中顯示。 因為 timer1 的間隔設為 1000，每一千毫秒便會發生此事件，因此每秒會更新目前時間。

修改方法為可使用 virtual關鍵字覆寫。 如需詳細資訊，請參閱以下的「從使用者控制項繼承」一節。
C#

    protected virtual void timer1_Tick(object sender, System.EventArgs e)

    在 [檔案] 功能表上按一下 [全部儲存] 以儲存專案。

將屬性新增至複合控制項

您的時鐘控制項現在會封裝 Label 控制項和 Timer 元件，每個都有自己的一組固有屬性。 雖然這些控制項的個別屬性無法供控制項的後續使用者存取，但是您可以建立並公開自訂屬性，方法是撰寫適當的程式碼區塊。 在下列程序中，您會將屬性新增至控制項，讓使用者變更背景與文字的色彩。
若要將屬性新增至複合控制項

    在方案總管中，以滑鼠右鍵按一下 [ ctlClock]，然後按一下 [視圖程式碼]。

    控制項的程式 代碼編輯器 隨即開啟。

    尋找 public partial class ctlClock 陳述式。 在左大括號 ({) 底下，輸入下列程式碼。
    C#

private Color colFColor;
private Color colBColor;

這些陳述式會建立私用變數，您將用來儲存您即將建立之屬性的值。

在步驟2的變數宣告底下，輸入或貼上下列程式碼。
C#

    // Declares the name and type of the property.
    public Color ClockBackColor
    {
        // Retrieves the value of the private variable colBColor.
        get
        {
            return colBColor;
        }
        // Stores the selected value in the private variable colBColor, and
        // updates the background color of the label control lblDisplay.
        set
        {
            colBColor = value;
            lblDisplay.BackColor = colBColor;
        }
    }
    // Provides a similar set of instructions for the foreground color.
    public Color ClockForeColor
    {
        get
        {
            return colFColor;
        }
        set
        {
            colFColor = value;
            lblDisplay.ForeColor = colFColor;
        }
    }

    上述程式碼會製作兩個自訂屬性，ClockForeColor 和 ClockBackColor，以供此控制項的後續使用者使用。 get 和 set 陳述式提供屬性值的儲存和擷取，以及用來實作適合該屬性之功能的程式碼。

    在 [檔案] 功能表上按一下 [全部儲存] 以儲存專案。

測試控制項

控制項不是獨立應用程式；它們必須裝載在容器中。 測試控制項的執行階段行為，並且使用 UserControl 測試容器執行其屬性。 如需詳細資訊，請參閱如何：測試 UserControl 的執行階段行為。
若要測試控制項

    按 F5 以建立專案，並在 UserControl 測試容器中執行您的控制項。

    在測試容器的屬性方格中，尋找 ClockBackColor 屬性，然後選取屬性以顯示色彩調色盤。

    按一下它以選擇色彩。

    控制項的背景色彩會變更為您所選取的色彩。

    使用類似的一連串事件，確認 ClockForeColor 屬性是否如預期運作。

    在本節和先前的章節中，您已經知道元件和 Windows 控制項如何與程式碼合併並且封裝，以複合控制項的形式提供自訂功能。 您已經了解如何在您的複合控制項中公開屬性，以及如何在完成之後測試您的控制項。 在下一節中，您將學習如何使用 ctlClock 做為基底，建構繼承的複合控制項。

繼承自複合控制項

在先前章節中，您了解如何將 Windows 控制項、元件和程式碼合併成可重複使用的複合控制項。 複合控制項現在可以做為建置其他控制項的基底。 從基底類別衍生類別的處理序稱為「繼承」。 在本節中，您將建立稱為 ctlAlarmClock 的複合控制項。 這個控制項將會從其父控制項 (ctlClock) 衍生。 您將學習藉由覆寫父方法並且新增新方法和屬性，來擴充 ctlClock 的功能。

建立繼承的控制項的第一個步驟是從其父代衍生。 這個動作會建立新的控制項，其中具有父控制項的所有屬性、方法和圖形特性，但是也可以做為基底，以新增新的或修改功能。
若要建立繼承的控制項

    在方案總管中，以滑鼠右鍵按一下 [ ctlClockLib]，指向 [新增]，然後按一下 [使用者控制項]。

    [ 加入新專案 ] 對話方塊隨即開啟。

    選取繼承的使用者控制項範本。

    在 [名稱] 方塊中，輸入 ctlAlarmClock.cs 然後按一下 [新增]。

    [繼承選取器] 對話方塊隨即出現。

    在 [元件名稱] 底下，按兩下 [ctlClock]。

    在方案總管中，流覽目前的專案。

    注意

    名為 ctlAlarmClock.cs 的檔案已新增至目前的專案。

新增警示屬性

屬性會以新增至複合控制項的相同方式，新增至繼承的控制項。 您現在會使用屬性宣告語法將兩個屬性新增至您的控制項︰AlarmTime，它將會儲存警示停止之日期和時間的值，以及 AlarmSet，它將會指示是否已設定警示。
若要將屬性新增至複合控制項

    在方案總管中，以滑鼠右鍵按一下 [ ctlalarmclock]]，然後按一下 [視圖程式碼]。

    尋找 public class 陳述式。 請注意，您的控制項繼承自ctlClockLib.ctlClock。 在左大括號 ({) 陳述式底下，輸入下列程式碼。

    private DateTime dteAlarmTime;
    private bool blnAlarmSet;
    // These properties will be declared as public to allow future
    // developers to access them.
    public DateTime AlarmTime
    {
        get
        {
            return dteAlarmTime;
        }
        set
        {
            dteAlarmTime = value;
        }
    }
    public bool AlarmSet
    {
        get
        {
            return blnAlarmSet;
        }
        set
        {
            blnAlarmSet = value;
        }
    }

加入至控制項的圖形化介面

繼承的控制項具有視覺化介面，與它所繼承的控制項相同。 它擁有與其父控制項相同的組成控制項，但是無法使用組成控制項的屬性，除非特別公開。 您可以使用新增至任何複合控制項的相同方式，新增至繼承的複合控制項的圖形化介面。 若要繼續新增至警示時鐘的視覺化介面，您要新增標籤控制項，該控制項會在警示響起時閃爍。
若要新增標籤控制項

    在方案總管中，以滑鼠右鍵按一下 [ ctlalarmclock]]，然後按一下 [視圖設計工具]。

    ctlAlarmClock 的設計工具隨即在主視窗中開啟。

    按一下控制項的顯示部分，並檢視 [屬性] 視窗。

    注意

    所有屬性顯示時，它們會以灰色顯示。 這表示這些屬性是 lblDisplay 的原生屬性，而且無法修改或在 [屬性] 視窗中存取。 根據預設，包含在複合控制項中的控制項是 private，而且其屬性無法使用任何方法存取。

    注意

    如果您想要讓複合控制項的後續使用者可以存取其內部控制項，請將它們宣告為 public 或 protected。 這可讓您使用適當的程式碼，設定及修改包含在複合控制項中的控制項屬性。

    Label將控制項新增至複合控制項。

    使用滑鼠，將 Label 控制項緊接在 [顯示] 方塊下方。 在 [屬性] 視窗中設定下列屬性。
    屬性 	設定
    名稱 	lblAlarm
    Text 	報警！
    TextAlign 	MiddleCenter
    Visible 	false

新增警示功能

在先前的程序中，您新增屬性和控制項，在您的複合控制項中啟用警示功能。 在此程序中，您將會新增程式碼以比較目前時間與警示時間，如果它們相同，則讓警示閃爍。 藉由覆寫 ctlClock 的 timer1_Tick 方法，並且將額外程式碼新增至其中，您就可以擴充 ctlAlarmClock 的功能，同時保留 ctlClock 的所有固有功能。
若要覆寫 ctlClock 的 timer1_Tick 方法

    在 [程式碼編輯器] 中，尋找 private bool blnAlarmSet; 陳述式。 緊接著在其下新增下列陳述式。

private bool blnColorTicker;

在 [程式碼編輯器] 中，在類別結尾尋找右大括號 (})。 緊接在大括號之前，新增下列程式碼。

    protected override void timer1_Tick(object sender, System.EventArgs e)
    {
        // Calls the Timer1_Tick method of ctlClock.
        base.timer1_Tick(sender, e);
        // Checks to see if the alarm is set.
        if (AlarmSet == false)
            return;
        else
            // If the date, hour, and minute of the alarm time are the same as
            // the current time, flash an alarm.
        {
            if (AlarmTime.Date == DateTime.Now.Date && AlarmTime.Hour ==
                DateTime.Now.Hour && AlarmTime.Minute == DateTime.Now.Minute)
            {
                // Sets lblAlarmVisible to true, and changes the background color based on
                // the value of blnColorTicker. The background color of the label
                // will flash once per tick of the clock.
                lblAlarm.Visible = true;
                if (blnColorTicker == false)
                {
                    lblAlarm.BackColor = Color.Red;
                    blnColorTicker = true;
                }
                else
                {
                    lblAlarm.BackColor = Color.Blue;
                    blnColorTicker = false;
                }
            }
            else
            {
                // Once the alarm has sounded for a minute, the label is made
                // invisible again.
                lblAlarm.Visible = false;
            }
        }
    }

    新增這個程式碼會完成幾項工作。 override 陳述式會指示控制項使用這個方法來取代繼承自基底控制項的方法。 呼叫這個方法時，它會呼叫它藉由叫用 base.timer1_Tick 陳述式覆寫的方法，確保併入原始控制項的所有功能在此控制項中重現。 接著，它會執行其他程式碼以併入警示功能。 發生警示時，閃爍標籤控制項就會出現。

    警示時鐘控制項已接近完成。 唯一剩餘的事項是實作將它關閉的方式。 若要這樣做，您要將程式碼新增至 lblAlarm_Click 方法。

若要實作關閉方法

    在方案總管中，以滑鼠右鍵按一下 [ ctlalarmclock]]，然後按一下 [視圖設計工具]。

    設計工具隨即開啟。

    將按鈕新增至控制項。 將按鈕的屬性設定如下。
    屬性 	值
    名稱 	btnAlarmOff
    Text 	停用警示

    在設計工具中，按兩下 [btnAlarmOff]。

    [程式碼編輯器] 隨即開啟至 private void btnAlarmOff_Click 行。

    修改此方法，使它類似下列程式碼。
    C#

    private void btnAlarmOff_Click(object sender, System.EventArgs e)
    {
        // Turns off the alarm.
        AlarmSet = false;
        // Hides the flashing label.
        lblAlarm.Visible = false;
    }

    在 [檔案] 功能表上按一下 [全部儲存] 以儲存專案。

在表單上使用繼承的控制項

您可以用測試基類控制項的相同方式來測試繼承的控制項，請 ctlClock 按 F5 以建立專案，並在 UserControl 測試容器中執行您的控制項。 如需詳細資訊，請參閱如何：測試 UserControl 的執行階段行為。

若要使用控制項，您必須將它裝載在表單上。 如同標準複合控制項，繼承的複合控制項無法獨立存在，而且必須裝載在表單或其他容器。 由於 ctlAlarmClock 有更深入的功能，需要額外的程式碼來進行測試。 在此程序中，您將撰寫一個簡單的程式來測試 ctlAlarmClock 的功能。 您將撰寫程式碼以設定及顯示 ctlAlarmClock 的 AlarmTime 屬性，然後測試其固有功能。
若要建置控制項並且新增至測試表單

    在方案總管中，以滑鼠右鍵按一下 [ ctlClockLib]，然後按一下 [建立]。

    將新的Windows Forms 應用程式專案加入至方案，並為其命名測試。

    在方案總管中，以滑鼠右鍵按一下測試專案的 [參考] 節點。 按一下 [加入參考]以顯示 [加入參考] 對話方塊。 按一下標籤為 [專案] 的索引標籤。 您的 ctlClockLib 專案會列在 [專案名稱] 底下。 按兩下專案以將參考新增至測試專案。

    在方案總管中，以滑鼠右鍵按一下 [測試]，然後按一下 [建立]。

    在 [工具箱] 中，展開 [ctlClockLib 元件] 節點。

    按兩下 [ctlAlarmClock] 以將 ctlAlarmClock 的複本新增至表單。

    在 [工具箱] 中，找出並按兩下 [ DateTimePicker ]，將控制項新增 DateTimePicker 至表單，然後按兩下 [標籤] 來加入 Label 控制項。

    使用滑鼠將控制項放置在表單上方便的位置。

    以下列方式設定這些控制項的屬性。
    控制 	屬性 	值
    label1 	Text 	(blank space)
    	名稱 	lblTest
    dateTimePicker1 	名稱 	dtpTest
    	格式 	Time

    在設計工具中，按兩下 [dtpTest]。

    [程式碼編輯器] 隨即開啟至 private void dtpTest_ValueChanged。

    修改此程式碼，使它類似下列程式碼。
    C#

    private void dtpTest_ValueChanged(object sender, System.EventArgs e)
    {
        ctlAlarmClock1.AlarmTime = dtpTest.Value;
        ctlAlarmClock1.AlarmSet = true;
        lblTest.Text = "Alarm Time is " +
            ctlAlarmClock1.AlarmTime.ToShortTimeString();
    }

    在方案總管中，以滑鼠右鍵按一下 [測試]，然後按一下 [設定為啟動 Project。

    在 [偵錯] 功能表上，按一下 [開始偵錯] 。

    測試程式隨即啟動。 請注意，目前的時間會在控制項中 ctlAlarmClock 更新，而開始時間則顯示在控制項中 DateTimePicker 。

    DateTimePicker按一下該小時的分鐘顯示位置。

    使用鍵盤，將分鐘值設定為大於 ctlAlarmClock 顯示的目前時間一分鐘。

    警示設定的時間會在 lblTest 中顯示。 等候顯示的時間達到警示設定時間。 當顯示的時間達到警示設定時間，則 lblAlarm 會閃爍。

    按一下 btnAlarmOff 來關閉警示。 您現在可以重設警示。

本文涵蓋了許多重要概念。 您已經了解藉由將控制項和元件合併成複合控制項容器，來建立複合控制項。 您已經了解將屬性新增至您的控制項，以及撰寫程式碼來實作自訂功能。 在最後一節中，您會了解透過繼承擴充指定複合控制項的功能，並且藉由覆寫這些方法來變更主方法的功能。
另請參閱

    各種自訂控制項
    如何：在選擇工具箱項目對話方塊中顯示控制項
    逐步解說：使用 Visual C# 繼承自 Windows Form 控制項

建議的內容

    定義控制項屬性 - Windows Forms .NET Framework

    開發自訂控制項 - Windows Forms .NET Framework

    瞭解 Windows 表單控制項。 具體來說，您將學習如何結合現有的控制項、延伸現有的控制項，以及撰寫您自己的自訂控制項。
    使用 FlowLayoutPanel 排列控制項 - Windows Forms .NET Framework

    學習如何使用 FlowLayoutPanel 控制項和 TableLayoutPanel 控制項，以提供直覺的方式來排列 Windows Forms 專案中的控制項。
    AutoSize 在 TableLayoutPanel 控制項中的行為 - Windows Forms .NET Framework

本文內容

    建立專案
    將 Windows 控制項和元件新增至複合控制項
    將屬性新增至複合控制項
    測試控制項

    舊版文件
    部落格
    參與
    隱私權與 Cookie
    使用規定
    商標
    © Microsoft 2022




------------------------------------------------------------
------------------------------------------------------------





------------------------------------------------------------
------------------------------------------------------------






client.DownloadFile(url, filename);
string data = client1.DownloadString(url_file1);          //抓網頁資料到記憶體
client2.DownloadFile(url_file2, filename_local);          //抓網頁資料到本地檔案
string xml = client3.DownloadString(url_weather);        //抓資料

MemoryStream image_stream = new MemoryStream(client.DownloadData(url));

byte[] bd = client.DownloadData(sURL);






Stream stream = client.OpenRead(URLAddress);


client.Headers.Add("user-agent", "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; .NET CLR 1.0.3705; Combat;)");









using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net;
using System.IO;    //for MemoryStream

namespace vcs_
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // Allow TLS 1.1 and TLS 1.2 protocols for file download.
            //for Sugar     3840 Romeo也可用
            ServicePointManager.SecurityProtocol = Protocols.protocol_Tls11 | Protocols.protocol_Tls12;
            richTextBox1.Text += "SecurityProtocol = " + ((int)(ServicePointManager.SecurityProtocol)).ToString() + "\n";

            //for Romeo and Sugar    3072
            //ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };
            //ServicePointManager.SecurityProtocol = (SecurityProtocolType)3840;
            //richTextBox1.Text += "SecurityProtocol = " + ((int)(ServicePointManager.SecurityProtocol)).ToString() + "\n";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            /*
            //加入這段語法忽略憑證
            ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };
            */

            string url_file1 = @"http://snowball.tartarus.org/otherlangs/english_cpp.txt";
            //string url_file = @"http://antwrp.gsfc.nasa.gov/apod/";

            using ( client1 = new ())     // Create a web client
            {
                try  // Get the response string from the URL.
                {
                    //richTextBox1.Text += data + "\n";
                    richTextBox1.Text += "抓網頁資料到記憶體\tOK\n";
                }
                catch (WebException ex)
                {
                    MessageBox.Show("WebException\t" + ex.Message);
                }
                catch (Exception ex)
                {
                    MessageBox.Show("Unknown error\t" + ex.Message);
                }
            }
            Application.DoEvents();

            string url_file2 = @"http://snowball.tartarus.org/otherlangs/english_cpp.txt";
            //string url_file2 = @"https://apod.nasa.gov/apod/image/2103/VolcanoStars_Vella_1080.jpg";
            using ( client2 = new ())     // Create a web client
            {
                try  // Get the response string from the URL.
                {
                    //string filename_local = Application.StartupPath + "\\txt_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".txt";
                    int pos1 = url_file2.LastIndexOf('/');
                    int pos2 = url_file2.LastIndexOf('.');
                    string filename_local = url_file2.Substring(pos1 + 1, pos2 - pos1 - 1) + DateTime.Now.ToString("_yyyyMMdd_HHmmss") + url_file2.Substring(pos2);
                    richTextBox1.Text += "下載檔案, 本地檔案檔名 : " + filename_local + "\n";

                    richTextBox1.Text += "抓網頁資料到本地檔案\tOK\n";
                }
                catch (WebException ex)
                {
                    MessageBox.Show("WebException\t" + ex.Message);
                }
                catch (Exception ex)
                {
                    MessageBox.Show("Unknown error\t" + ex.Message);
                }
            }
            Application.DoEvents();

            string url_weather = @"http://api.openweathermap.org/data/2.5/weather?q=Hsinchu&mode=xml&units=imperial&APPID=e8edf79325ae8948a635efd0e076a8bc";
            using (  = new ())     // Create a web client
            {
                try  // Get the response string from the URL.
                {
                    // Get the response string from the URL.
                    //richTextBox1.Text += "data\n" + xml + "\n";
                    richTextBox1.Text += "抓網頁查詢資料到記憶體\tOK\n";
                }
                catch (WebException ex)
                {
                    MessageBox.Show("WebException\t" + ex.Message);
                }
                catch (Exception ex)
                {
                    MessageBox.Show("Unknown error\t" + ex.Message);
                }
            }
            Application.DoEvents();

            string img_src_url = @"https://apod.nasa.gov/apod/image/2103/VolcanoStars_Vella_1080.jpg";
            richTextBox1.Text += "圖片所在網址 : " + img_src_url + "\n";
            try
            {
                //圖片下載並存檔
                DownloadImage(img_src_url);
                richTextBox1.Text += "圖片下載並存檔\tOK\n";
                Application.DoEvents();

                //圖片下來並顯示
                Image img = GetPicture(img_src_url);
                pictureBox1.Image = img;
                richTextBox1.Text += "圖片下來並顯示\tOK\n";
                Application.DoEvents();
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "*** Download Error" + "\n";
                richTextBox1.Text += "*** " + ex.Message + "\n";
            }
            Application.DoEvents();


            //下載COVID-19資料

            // Compose the local data file name.
            string filename_covid19a = "state_data" + DateTime.Now.ToString("yyyy_MM_dd") + ".csv";

            // Download today's data.
            string url = "https://covidtracking.com/api/v1/states/daily.csv";

            richTextBox1.Text += "LoadData \tURL : " + url + "\tfile : " + filename_covid19a + "\n";
            Application.DoEvents();

            DownloadFile(url, filename_covid19a);


            richTextBox1.Text += "Loading case data...\n";
            Application.DoEvents();

            // Compose the local data file name.
            string filename_covid19b = "cases" + DateTime.Now.ToString("yyyy_MM_dd") + ".csv";

            // Download today's data.
            url = "https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_confirmed_global.csv&filename=time_series_covid19_confirmed_global.csv";
            DownloadFile(url, filename_covid19b);
        }

        // Download the indicated file.
        private void DownloadImage(string url)
        {
            //richTextBox1.Text += "下載圖片 : " + url + "\n";

            // Make a .
             client = new ();

            /*
            int pos = url.LastIndexOf('/');
            string filename = url.Substring(pos + 1);
            */

            int pos1 = url.LastIndexOf('/');
            int pos2 = url.LastIndexOf('.');
            string filename = url.Substring(pos1 + 1, pos2 - pos1 - 1) + DateTime.Now.ToString("_yyyyMMdd_HHmmss") + url.Substring(pos2);
            richTextBox1.Text += "下載圖片, 本地圖片檔名 : " + filename + "\n";

            // Use one of the following.
            // For .NET Framework 4.5 and later:
            //ServicePointManager.SecurityProtocol =
            //    SecurityProtocolType.Tls12;
            // For .NET Framework 4.0 through 4.4:
            ServicePointManager.SecurityProtocol = (SecurityProtocolType)3072;

            // Download the file.
            client.DownloadFile(url, filename);
        }

        // Download a file from the internet.
        // Get the picture at a given URL.
        private Image GetPicture(string url)
        {
            try
            {
                 client = new ();

                // Use one of the following.
                //ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12;
                ServicePointManager.SecurityProtocol = (SecurityProtocolType)3072;

                MemoryStream image_stream = new MemoryStream(client.DownloadData(url));
                return Image.FromStream(image_stream);
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "Error downloading picture " + url + '\n' + ex.Message + "\n";
                return null;
            }
        }

        private void DownloadFile(string url, string filename)
        {
            try
            {
                // Make a .
                 client = new ();

                // Download the file.
                client.DownloadFile(url, filename);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "Download Error", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
            }
            finally
            {
                if (!File.Exists(filename))
                {
                    richTextBox1.Text += "下載 : " + filename + "\tNG\n";
                }
                else
                {
                    richTextBox1.Text += "下載 : " + filename + "\tOK\n";
                }
            }
        }

    }

    public class Protocols
    {
        public const SecurityProtocolType
            protocol_SystemDefault = 0,
            protocol_Ssl3 = (SecurityProtocolType)48,
            protocol_Tls = (SecurityProtocolType)192,
            protocol_Tls11 = (SecurityProtocolType)768,
            protocol_Tls12 = (SecurityProtocolType)3072;
    }

}




using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net;
using System.IO;    //for MemoryStream

namespace vcs_
{
public partial class Form1 : Form
{
public Form1()
{
InitializeComponent();
}

private void Form1_Load(object sender, EventArgs e)
{
// Allow TLS 1.1 and TLS 1.2 protocols for file download.
//for Sugar     3840 Romeo也可用
ServicePointManager.SecurityProtocol = Protocols.protocol_Tls11 | Protocols.protocol_Tls12;
richTextBox1.Text += "SecurityProtocol = " + ((int)(ServicePointManager.SecurityProtocol)).ToString() + "\n";

//for Romeo and Sugar    3072
//ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };
//ServicePointManager.SecurityProtocol = (SecurityProtocolType)3840;
//richTextBox1.Text += "SecurityProtocol = " + ((int)(ServicePointManager.SecurityProtocol)).ToString() + "\n";
}

private void button1_Click(object sender, EventArgs e)
{
/*
//加入這段語法忽略憑證
ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };
*/

string url_file1 = @"http://snowball.tartarus.org/otherlangs/english_cpp.txt";
//string url_file = @"http://antwrp.gsfc.nasa.gov/apod/";

using ( client1 = new ())     // Create a web client
{
try  // Get the response string from the URL.
{
//richTextBox1.Text += data + "\n";
richTextBox1.Text += "抓網頁資料到記憶體\tOK\n";
}
catch (WebException ex)
{
MessageBox.Show("WebException\t" + ex.Message);
}
catch (Exception ex)
{
MessageBox.Show("Unknown error\t" + ex.Message);
}
}
Application.DoEvents();

string url_file2 = @"http://snowball.tartarus.org/otherlangs/english_cpp.txt";
//string url_file2 = @"https://apod.nasa.gov/apod/image/2103/VolcanoStars_Vella_1080.jpg";
using ( client2 = new ())     // Create a web client
{
try  // Get the response string from the URL.
{
//string filename_local = Application.StartupPath + "\\txt_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".txt";
int pos1 = url_file2.LastIndexOf('/');
int pos2 = url_file2.LastIndexOf('.');
string filename_local = url_file2.Substring(pos1 + 1, pos2 - pos1 - 1) + DateTime.Now.ToString("_yyyyMMdd_HHmmss") + url_file2.Substring(pos2);
richTextBox1.Text += "下載檔案, 本地檔案檔名 : " + filename_local + "\n";

richTextBox1.Text += "抓網頁資料到本地檔案\tOK\n";
}
catch (WebException ex)
{
MessageBox.Show("WebException\t" + ex.Message);
}
catch (Exception ex)
{
MessageBox.Show("Unknown error\t" + ex.Message);
}
}
Application.DoEvents();

string url_weather = @"http://api.openweathermap.org/data/2.5/weather?q=Hsinchu&mode=xml&units=imperial&APPID=e8edf79325ae8948a635efd0e076a8bc";
using (  = new ())     // Create a web client
{
try  // Get the response string from the URL.
{
// Get the response string from the URL.
//richTextBox1.Text += "data\n" + xml + "\n";
richTextBox1.Text += "抓網頁查詢資料到記憶體\tOK\n";
}
catch (WebException ex)
{
MessageBox.Show("WebException\t" + ex.Message);
}
catch (Exception ex)
{
MessageBox.Show("Unknown error\t" + ex.Message);
}
}
Application.DoEvents();

string img_src_url = @"https://apod.nasa.gov/apod/image/2103/VolcanoStars_Vella_1080.jpg";
richTextBox1.Text += "圖片所在網址 : " + img_src_url + "\n";
try
{
//圖片下載並存檔
DownloadImage(img_src_url);
richTextBox1.Text += "圖片下載並存檔\tOK\n";
Application.DoEvents();

//圖片下來並顯示
Image img = GetPicture(img_src_url);
pictureBox1.Image = img;
richTextBox1.Text += "圖片下來並顯示\tOK\n";
Application.DoEvents();
}
catch (Exception ex)
{
richTextBox1.Text += "*** Download Error" + "\n";
richTextBox1.Text += "*** " + ex.Message + "\n";
}
Application.DoEvents();


//下載COVID-19資料

// Compose the local data file name.
string filename_covid19a = "state_data" + DateTime.Now.ToString("yyyy_MM_dd") + ".csv";

// Download today's data.
string url = "https://covidtracking.com/api/v1/states/daily.csv";

richTextBox1.Text += "LoadData \tURL : " + url + "\tfile : " + filename_covid19a + "\n";
Application.DoEvents();

DownloadFile(url, filename_covid19a);


richTextBox1.Text += "Loading case data...\n";
Application.DoEvents();

// Compose the local data file name.
string filename_covid19b = "cases" + DateTime.Now.ToString("yyyy_MM_dd") + ".csv";

// Download today's data.
url = "https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_confirmed_global.csv&filename=time_series_covid19_confirmed_global.csv";
DownloadFile(url, filename_covid19b);
}

// Download the indicated file.
private void DownloadImage(string url)
{
//richTextBox1.Text += "下載圖片 : " + url + "\n";

// Make a Web
 client = new ();

/*
int pos = url.LastIndexOf('/');
string filename = url.Substring(pos + 1);
*/

int pos1 = url.LastIndexOf('/');
int pos2 = url.LastIndexOf('.');
string filename = url.Substring(pos1 + 1, pos2 - pos1 - 1) + DateTime.Now.ToString("_yyyyMMdd_HHmmss") + url.Substring(pos2);
richTextBox1.Text += "下載圖片, 本地圖片檔名 : " + filename + "\n";

// Use one of the following.
// For .NET Framework 4.5 and later:
//ServicePointManager.SecurityProtocol =
//    SecurityProtocolType.Tls12;
// For .NET Framework 4.0 through 4.4:
ServicePointManager.SecurityProtocol = (SecurityProtocolType)3072;

// Download the file.
}

// Download a file from the internet.
// Get the picture at a given URL.
private Image GetPicture(string url)
{
try
{
 client = new ();

// Use one of the following.
//ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12;
ServicePointManager.SecurityProtocol = (SecurityProtocolType)3072;

return Image.FromStream(image_stream);
}
catch (Exception ex)
{
richTextBox1.Text += "Error downloading picture " + url + '\n' + ex.Message + "\n";
return null;
}
}

private void DownloadFile(string url, string filename)
{
try
{
// Make a Web
 client = new ();

// Download the file.
}
catch (Exception ex)
{
MessageBox.Show(ex.Message, "Download Error", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
}
finally
{
if (!File.Exists(filename))
{
richTextBox1.Text += "下載 : " + filename + "\tNG\n";
}
else
{
richTextBox1.Text += "下載 : " + filename + "\tOK\n";
}
}
}

}

public class Protocols
{
public const SecurityProtocolType
protocol_SystemDefault = 0,
protocol_Ssl3 = (SecurityProtocolType)48,
protocol_Tls = (SecurityProtocolType)192,
protocol_Tls11 = (SecurityProtocolType)768,
protocol_Tls12 = (SecurityProtocolType)3072;
}

}


------------------------------------------------------------
------------------------------------------------------------





------------------------------------------------------------
------------------------------------------------------------





------------------------------------------------------------
------------------------------------------------------------








 


richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個


richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個


richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個



richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個



進程

我們可以把計算機中每一個運行的應用程序當作是一個進程



線程

每一個進程是由多個線程組成的。
單線程：讓程序做多件事時，會引發卡死 假死狀態。
多線程：讓一個程序同時處理多個事情，後台運行程序，提高程序的運行效率。
前台線程：只有所有的前台線程都關閉才能完成程序關閉。(winform多窗口時)
後台線程：只要所有的前台線程結束，後台線程自動結束。

 1 //實例化Thread類，並傳入一個指向線程所要運行的方法。（這時線程已經產生，但還沒有運行）
 2 //調用Thread類的Start方法，標記線程可以被CPU執行了，但具體執行事件由CPU決定。
 3 Thread th = new Thread(Test); //創建一個線程去執行這個方法。
 4 th.IsBackground = true; //將線程設置為後台線程，前台關閉後 線程結束。
 5 th.Start(); //標記准備就緒，可以隨意被執行，具體什麼時候執行由CPU決定。
 6 //在.net下是不允許跨線程訪問的。
 7 //有時候需要手動釋放線程 關閉時 判斷線程是否關閉 
 8 if (th != null)
 9 {
10     th.Abort(); //結束這個線程 不能再Start()
11 }
12 Thread.Sleep(3000); //睡眠3秒後執行
13 //線程執行帶參數方法
14 Thread.Start("123")； object類型參數 在start後括號寫參數

//多用於大量數據時，多分一個線程去搜索數據，然後存儲到緩存裡，頁面再用異步獲取緩存中的數據。












BTW, if the HtmlNode has a “ID”, like “<div id='post_list'>value</div>”, call GetElementbyId() is OK for getting the HtmlNode, then get the value by HtmlNode.InnerText or HtmlNode.Attribute.

Please see the following C# code snippet.

Code snippet:

 //get HtmlAgilityPack.HtmlDocument object   
 HtmlDocument doc = new HtmlDocument();  
 //load HTML   
doc.LoadHtml(pageSource);         
//get HtmlNode by ID   
 HtmlNode navNode = doc.GetElementbyId("post_list");	//測這個


 

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Net;
using System.Text.RegularExpressions;
using HtmlAgilityPack;

namespace RegexPractice
{
    class Program
    {
        static void Main(string[] args)
        {
            string pageUrl = "http://top.baidu.com/buzz.php?p=top_keyword";
            WebClient wc = new WebClient();
            byte[] pageSourceBytes = wc.DownloadData(new Uri(pageUrl));
            string pageSource = Encoding.GetEncoding("gb2312").GetString(pageSourceBytes);

            //Regex searchKeyRegex = new Regex("<td class=\"key\">.*?target=\"_blank\">(?<keyWord>.*?)</a></td>");
            //MatchCollection mc = searchKeyRegex.Matches(pageSource);
            //List<string> keyWordList = new List<string>();
            //foreach(Match m in mc)
            //{
            //    keyWordList.Add(m.Groups["keyWord"].Value);
            //}

            HtmlDocument doc = new HtmlDocument();
            doc.LoadHtml(pageSource);

            HtmlNodeCollection keyNodes = doc.DocumentNode.SelectNodes("//td[@class='key']/a[@ target='_blank']");
            List<string> keyWords = new List<string>();
            foreach (HtmlNode keyNode in keyNodes)
            {
                keyWords.Add(keyNode.InnerText);
            }

            //HtmlDocument doc = new HtmlDocument();
            //doc.LoadHtml(pageSource);

            //HtmlNode ulNode = doc.DocumentNode.SelectSingleNode("//ul[@class='hotnews']");

            //HtmlNodeCollection liNodes = ulNode.SelectNodes("li");

            //List<string> topList = new List<string>();
            //List<string> subList = new List<string>();

            //foreach (HtmlNode liNode in liNodes)
            //{
            //    if (liNode.Attributes["class"] != null && liNode.Attributes["class"].Value == "top")
            //    {
            //        topList.Add(liNode.InnerText);
            //    }
            //    else
            //    {
            //        if (subList.Count < topList.Count)
            //        {
            //            subList.Add(liNode.InnerText);
            //        }
            //        else
            //        {
            //            subList[subList.Count - 1] = subList[subList.Count - 1] + liNode.InnerText;
            //        }
            //    }
            //}

            return;

            //Regex hotTopNewsRegex = new Regex("class=\"a3\".*?>(?<hotNews>.*)<");
            //MatchCollection topMc = hotTopNewsRegex.Matches(pageSource);

            //List<string> hotNewsList = new List<string>();
            //foreach (Match m in topMc)
            //{
            //    hotNewsList.Add(m.Groups["hotNews"].Value);
            //}


            //Regex replaceRegex = new Regex("</?font.*?>");
            //for (int i = 0; i < hotNewsList.Count;i++ )
            //{
            //    hotNewsList[i] = replaceRegex.Replace(hotNewsList[i], "");
            //}

            //Regex hotSubNewsRegex = new Regex("(?s)class=\"top\"(?<subNews>.*?)class=\"top\"");
            //MatchCollection subMc = hotSubNewsRegex.Matches(pageSource);
            //int temp = subMc.Count;

            //List<string> subNewsList = new List<string>();
            //foreach (Match m in subMc)
            //{
            //    subNewsList.Add(m.Groups["subNews"].Value);
            //}
        }
    }
}


Another code snippet

Download specified number of pictures from “ http://browse.deviantart.com/customization/wallpaper/widescreen/?order=15” and save to local files.

	using System;  
	using System.Collections.Generic;  
	using System.Linq;  
	using System.Text;  
	using System.Net;  
	using System.Text.RegularExpressions;  
	using HtmlAgilityPack;  
	using System.IO;  
	  
	namespace RegexPractice  
	{  
	    public class Util  
	    {  
	  
	        //Get byte[] format page source    
	        public static byte[] GetPageSourceBytes(string url)  
	        {  
	            WebClient wc = new WebClient();  
	            byte[] pageSourceBytes = wc.DownloadData(new Uri(url));  
	            return pageSourceBytes;  
	        }  
	  
	        //get string format page source    
	        public static string GetPageSource(string url, string encodingType)  
	        {  
	            byte[] pageSourceBytes = GetPageSourceBytes(url);  
	            string pageSource = Encoding.GetEncoding(encodingType).GetString(pageSourceBytes);  
	            return pageSource;  
	        }  
	  
	        //Save image to local file    
	        public static void SavaImagesToFile(string url,string dirPath,string fileName)  
	        {  
	            if(!Directory.Exists(dirPath))  
	            {  
	                Directory.CreateDirectory(dirPath);  
	            }  
	            WebClient wc = new WebClient();  
	            wc.DownloadFile(url, Path.Combine(dirPath, fileName + Guid.NewGuid().ToString()));  
	        }  
	    }  
	  
	    public class ImageInfo  
	    {  
	        public string Title;  
	        public string SrcPath;  
	  
	
	    class Program  
	    {  
	        static void Main(string[] args)  
	        {  
							            int sumCount = 100;  
							            string baseUrl = "http://browse.deviantart.com/customization/wallpaper/widescreen/?order=15";  
							  
							            List<ImageInfo> imageInfoList = new List<ImageInfo>();  
							            imageInfoList = GetSumImageInfoList(sumCount, baseUrl);  
							  
							            foreach (ImageInfo imageInfo in imageInfoList)  
							            {  
							                Util.SavaImagesToFile(imageInfo.SrcPath, @"c:\Images", GetValidFilename(imageInfo.Title));  
							            }  
							  
							            return;  
							        }  
							  
							        static string GetValidFilename(string filename)  
							        {  
							            foreach (char c in Path.GetInvalidFileNameChars())  
							            {  
							                filename = filename.Replace(c, '_');  
							            }  
							            return filename;  
							        }  
							  
							        static List<ImageInfo> GetSumImageInfoList(int sum, string baseUri)  
							        {  
							            List<ImageInfo> resultList = new List<ImageInfo>();  
							            int c = (sum - 1) / 24 + 1;  
							            for (int i = 0; i < c; i++)  
							            {  
							                int offset = i * 24;  
							                string url = string.Format("{0}&offset={1}", baseUri, offset);  
							                List<ImageInfo> curResultList = ImageInfo.GetImageInfoList(url);  
							                foreach (ImageInfo imageInfo in curResultList)  
							                {  
							                    if (resultList.Count < sum)  
							                    {  
							                        resultList.Add(imageInfo);  
							                    }  
							                }  
							            }  
							            return resultList;  
							        }             
	        
	        
	        
	    }  
	 }  


 




richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個


richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個


richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個



richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個




        private void toggleOption(int camIndex, int optionIndex, bool value)
        {
            switch (optionIndex)
            {
                case 0:
                    this.CamMonitor[camIndex].MotionDetection = value;
                    break;
                case 1:
                    this.CamMonitor[camIndex].RecordOnMotion = value;
                    break;
                case 2:
                    this.CamMonitor[camIndex].BeepOnMotion = value;
                    break;
            }
        }


print('------------------------------------------------------------')	#60個

MotionDetection1_CheckedChanged(object sender, EventArgs e)
this.toggleOption(0, 0, true);
this.toggleOption(0, 0, false);

AutoRecord1_CheckedChanged(object sender, EventArgs e)
this.toggleOption(0, 1, true);
this.toggleOption(0, 1, false);

BeepOnMotionCheck1_CheckedChanged(object sender, EventArgs e)
this.toggleOption(0, 2, true);
this.toggleOption(0, 2, false);

print('------------------------------------------------------------')	#60個

        

        public FilterInfoCollection USBWebcams = null;
        public VideoCaptureDevice Cam = null;

        void Init_WebcamSetup()
        {
            //richTextBox1.Text += "重新抓取USB影像\t";
            USBWebcams = new FilterInfoCollection(FilterCategory.VideoInputDevice);
            if (USBWebcams.Count > 0)  // The quantity of WebCam must be more than 0.
            {
                //button12.Enabled = false;
                Cam = new VideoCaptureDevice(USBWebcams[0].MonikerString);  //實例化對象
                Cam.NewFrame += new NewFrameEventHandler(Cam_NewFrame);
                Cam.Start();   // WebCam starts capturing images.
                //richTextBox1.Text += "有影像裝置\n";

                Cam.VideoResolution = Cam.VideoCapabilities[0];

                string webcam_name = string.Empty;

                int ww;
                int hh;
                ww = Cam.VideoCapabilities[0].FrameSize.Width;
                hh = Cam.VideoCapabilities[0].FrameSize.Height;

                webcam_name = USBWebcams[0].Name + " " + Cam.VideoCapabilities[0].FrameSize.Width.ToString() + " X " + Cam.VideoCapabilities[0].FrameSize.Height.ToString() + " @ " + Cam.VideoCapabilities[0].AverageFrameRate.ToString() + " Hz";
                this.Text = webcam_name;

                if (Screen.PrimaryScreen.Bounds.Width == 1920)
                {
                    if (ww >= Screen.PrimaryScreen.Bounds.Width)
                    {
                        pictureBox1.Size = new Size(1920, 1080);
                        pictureBox1.Location = new Point(0, 0);
                        this.FormBorderStyle = FormBorderStyle.None;
                        this.WindowState = FormWindowState.Maximized;
                        //this.Size = new Size(pictureBox1.Size.Width + 200, pictureBox1.Size.Height + 200);
                    }
                    else if (ww < Screen.PrimaryScreen.Bounds.Width)
                    {
                        pictureBox1.Size = new Size(ww, hh);
                        pictureBox1.Location = new Point(140, 60);
                        this.FormBorderStyle = FormBorderStyle.FixedSingle;
                        this.WindowState = FormWindowState.Normal;
                        this.ClientSize = new Size(pictureBox1.Location.X + pictureBox1.Width + 50, pictureBox1.Location.Y + pictureBox1.Height + 50);
                    }
                }
            }
            else
            {
                //button12.Enabled = true;
                //richTextBox1.Text += "無影像裝置\n";
            }


        }


print('------------------------------------------------------------')	#60個


plt.savefig('tmp_event.png', dpi=300) 	# 將圓餅圖出成圖片，檔名為event.png 




            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
            this.pictureBox1.Focus();


#通用
Form1_Load()
Form1_FormClosing()
show_item_location()
bt_clear_Click()
delay()
show_main_message()
timer_display_Tick()
-----------------------------------
#相機一般
Init_WebcamSetup()
Start_Webcam()
Stop_Webcam()
Cam_NewFrame()
save_image_to_drive()
timer_fps_Tick()
-----------------------------------
#相機錄影
do_record()
-----------------------------------
#相機按鈕
bt_start_Click()
bt_stop_Click()
bt_record_start_Click()
bt_record_stop_Click()


print('------------------------------------------------------------')	#60個

            ManagementObjectSearcher searcher = new ManagementObjectSearcher("select * from Win32_Processor");
            foreach (ManagementObject myobject in searcher.Get())
            {
                lblCPU.Text = myobject["LoadPercentage"].ToString() + " %";
                //label2.Text = lblCPU.Text;
                label2.Text = "CPU使用率：" + lblCPU.Text;
                mheight = Convert.ToInt32(myobject["LoadPercentage"].ToString());
                if (mheight == 100)
                    panel3.Height = 100;
                CreateImage();
            }




print('------------------------------------------------------------')	#60個

//vcs最小化錄影

//公用變數
VideoFileWriter writer = new VideoFileWriter();

//開啟檔案
//writer.Open(filename, W, H, fps);

//寫入影格
//writer.WriteVideoFrame(bitmap1);

//關閉檔案
writer.Close();


        private void DoRecord()
        {
            VideoFileWriter writer = new VideoFileWriter();

            writer.Open(RecordingFilename, this.Width, this.Height, 30);


                        Bitmap bitmap1 = frames.Dequeue();
                        writer.WriteVideoFrame(bitmap1);


            writer.Close();
        }

宣告QUEUE

Queue<Bitmap> frames = new Queue<Bitmap>(); // Queue that stores frames to be written by the recorder thread

加入資料
frames.Enqueue((Bitmap)bitmap1.Clone());


取出資料
if (frames.Count > 0)
{
    try
    {
        Bitmap bitmap1 = frames.Dequeue();
        writer.WriteVideoFrame(bitmap1);
    }
    catch (Exception ex)
    {
        Console.WriteLine("xxx錯誤訊息e03 : " + ex.Message);
    }
}



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

            //serialPort2.Write(data, 0, data.Length);
            try
            {   //可能會產生錯誤的程式區段
                serialPort2.Write(data, 0, data.Length);
            }
            catch (Exception ex)
            {   //定義產生錯誤時的例外處理程式碼
                richTextBox1.Text += "xxx錯誤訊息e03 : " + ex.Message + "\n";
            }
            finally
            {
                //一定會被執行的程式區段
            }


WriteToSerialPort2(data, 0, data.Length)


void WriteToSerialPort2(byte[] data, int offset, int count)
{
            //serialPort2.Write(data, offset, count);
            try
            {   //可能會產生錯誤的程式區段
                serialPort2.Write(data, offset, count);
            }
            catch (Exception ex)
            {   //定義產生錯誤時的例外處理程式碼
                richTextBox1.Text += "xxx錯誤訊息e02 : " + ex.Message + "\n";
            }
            finally
            {
                //一定會被執行的程式區段
            }

}




//
        // 摘要:
        //     使用緩衝區中的資料，將指定的位元組數目寫入序列埠。
        //
        // 參數:
        //   buffer:
        //     包含要寫入通訊埠之資料的位元組陣列。
        //
        //   offset:
        //     buffer 參數中以零起始的位元組位移，用來開始將位元組複製到通訊埠。
        //
        //   count:
        //     要寫入的位元組數。
        //
        // 例外狀況:
        //   System.ArgumentNullException:
        //     傳遞的 buffer 為 null。
        //
        //   System.InvalidOperationException:
        //     指定的連接埠未開啟。
        //
        //   System.ArgumentOutOfRangeException:
        //     offset 或 count 參數超出所傳遞之 buffer 的有效區域以外。offset 或 count 小於零。
        //
        //   System.ArgumentException:
        //     offset 加上 count 大於 buffer 的長度。
        //
        //   System.ServiceProcess.TimeoutException:
        //     作業沒有在逾時期間結束之前完成。
        
        
        
        
        
        


        public bool Get_IMS_Data(byte xx, byte yy, byte zz)
        {
            if (get_comport_status() == false)
                return false;

            byte[] data = new byte[5];

            data[0] = 0xAA;
            data[1] = xx;
            data[2] = yy;
            data[3] = zz;
            data[4] = CalcCheckSum(data, 4);

            //richTextBox1.AppendText("[TX] : " + ((int)data[0]).ToString("X2") + " " + ((int)data[1]).ToString("X2") + " " + ((int)data[2]).ToString("X2") + " " + ((int)data[3]).ToString("X2") + " " + ((int)data[4]).ToString("X2") + "\n");

            serialPort2.Write(data, 0, data.Length);
            flag_wait_receive_data = 1;

            return true;
        }


 如需叫用 Just-In-Time (JIT) 偵錯的詳細資料，
請參閱本訊息結尾處 (而非這個對話方塊) 的資訊。

************** 例外狀況文字 **************
System.IO.IOException: 裝置未就緒。

   於 System.IO.Ports.InternalResources.WinIOError(Int32 errorCode, String str)
   於 System.IO.Ports.SerialStream.EndWrite(IAsyncResult asyncResult)
   於 System.IO.Ports.SerialStream.Write(Byte[] array, Int32 offset, Int32 count, Int32 timeout)
   於 System.IO.Ports.SerialPort.Write(Byte[] buffer, Int32 offset, Int32 count)
   於 iMS_Link.Form1.Get_IMS_Data(Byte xx, Byte yy, Byte zz)
   於 iMS_Link.Form1.timer_rtc_Tick(Object sender, EventArgs e)
   於 System.Windows.Forms.Timer.OnTick(EventArgs e)
   於 System.Windows.Forms.Timer.TimerNativeWindow.WndProc(Message& m)
   於 System.Windows.Forms.NativeWindow.Callback(IntPtr hWnd, Int32 msg, IntPtr wparam, IntPtr lparam)


************** 已載入的組件 **************
mscorlib
    組件版本: 4.0.0.0
    Win32 版本: 4.8.9181.0 built by: NET481REL1LAST_C
    程式碼庫: file:///C:/Windows/Microsoft.NET/Framework/v4.0.30319/mscorlib.dll
----------------------------------------
iMS_Link
    組件版本: 1.0.0.0
    Win32 版本: 1.0.0.0
    程式碼庫: file:///C:/Users/070601/Desktop/iMS_Link01/01iMS_AWB_SETUP.exe
----------------------------------------
System.Windows.Forms
    組件版本: 4.0.0.0
    Win32 版本: 4.8.9181.0 built by: NET481REL1LAST_C
    程式碼庫: file:///C:/WINDOWS/Microsoft.Net/assembly/GAC_MSIL/System.Windows.Forms/v4.0_4.0.0.0__b77a5c561934e089/System.Windows.Forms.dll
----------------------------------------
System
    組件版本: 4.0.0.0
    Win32 版本: 4.8.9214.0 built by: NET481REL1LAST_B
    程式碼庫: file:///C:/WINDOWS/Microsoft.Net/assembly/GAC_MSIL/System/v4.0_4.0.0.0__b77a5c561934e089/System.dll
----------------------------------------
System.Drawing
    組件版本: 4.0.0.0
    Win32 版本: 4.8.9037.0 built by: NET481REL1
    程式碼庫: file:///C:/WINDOWS/Microsoft.Net/assembly/GAC_MSIL/System.Drawing/v4.0_4.0.0.0__b03f5f7f11d50a3a/System.Drawing.dll
----------------------------------------
System.Windows.Forms.DataVisualization
    組件版本: 4.0.0.0
    Win32 版本: 4.8.9037.0
    程式碼庫: file:///C:/WINDOWS/Microsoft.Net/assembly/GAC_MSIL/System.Windows.Forms.DataVisualization/v4.0_4.0.0.0__31bf3856ad364e35/System.Windows.Forms.DataVisualization.dll
----------------------------------------
AForge.Video.DirectShow
    組件版本: 2.2.5.0
    Win32 版本: 2.2.5.0
    程式碼庫: file:///C:/Users/070601/Desktop/iMS_Link01/AForge.Video.DirectShow.DLL
----------------------------------------
AForge.Video
    組件版本: 2.2.5.0
    Win32 版本: 2.2.5.0
    程式碼庫: file:///C:/Users/070601/Desktop/iMS_Link01/AForge.Video.DLL
----------------------------------------
System.Configuration
    組件版本: 4.0.0.0
    Win32 版本: 4.8.9037.0 built by: NET481REL1
    程式碼庫: file:///C:/WINDOWS/Microsoft.Net/assembly/GAC_MSIL/System.Configuration/v4.0_4.0.0.0__b03f5f7f11d50a3a/System.Configuration.dll
----------------------------------------
System.Core
    組件版本: 4.0.0.0
    Win32 版本: 4.8.9214.0 built by: NET481REL1LAST_B
    程式碼庫: file:///C:/WINDOWS/Microsoft.Net/assembly/GAC_MSIL/System.Core/v4.0_4.0.0.0__b77a5c561934e089/System.Core.dll
----------------------------------------
System.Xml
    組件版本: 4.0.0.0
    Win32 版本: 4.8.9037.0 built by: NET481REL1
    程式碼庫: file:///C:/WINDOWS/Microsoft.Net/assembly/GAC_MSIL/System.Xml/v4.0_4.0.0.0__b77a5c561934e089/System.Xml.dll
----------------------------------------
System.Windows.Forms.DataVisualization.resources
    組件版本: 4.0.0.0
    Win32 版本: 4.8.9037.0
    程式碼庫: file:///C:/WINDOWS/Microsoft.Net/assembly/GAC_MSIL/System.Windows.Forms.DataVisualization.resources/v4.0_4.0.0.0_zh-Hant_31bf3856ad364e35/System.Windows.Forms.DataVisualization.resources.dll
----------------------------------------
Accessibility
    組件版本: 4.0.0.0
    Win32 版本: 4.8.9037.0 built by: NET481REL1
    程式碼庫: file:///C:/WINDOWS/Microsoft.Net/assembly/GAC_MSIL/Accessibility/v4.0_4.0.0.0__b03f5f7f11d50a3a/Accessibility.dll
----------------------------------------
System.DirectoryServices
    組件版本: 4.0.0.0
    Win32 版本: 4.8.9037.0 built by: NET481REL1
    程式碼庫: file:///C:/WINDOWS/Microsoft.Net/assembly/GAC_MSIL/System.DirectoryServices/v4.0_4.0.0.0__b03f5f7f11d50a3a/System.DirectoryServices.dll
----------------------------------------
HslCommunication
    組件版本: 4.3.2.0
    Win32 版本: 4.3.2.0
    程式碼庫: file:///C:/Users/070601/Desktop/iMS_Link01/HslCommunication.DLL
----------------------------------------
System.Windows.Forms.resources
    組件版本: 4.0.0.0
    Win32 版本: 4.8.9037.0 built by: NET481REL1
    程式碼庫: file:///C:/WINDOWS/Microsoft.Net/assembly/GAC_MSIL/System.Windows.Forms.resources/v4.0_4.0.0.0_zh-Hant_b77a5c561934e089/System.Windows.Forms.resources.dll
----------------------------------------
mscorlib.resources
    組件版本: 4.0.0.0
    Win32 版本: 4.8.9037.0 built by: NET481REL1
    程式碼庫: file:///C:/WINDOWS/Microsoft.Net/assembly/GAC_MSIL/mscorlib.resources/v4.0_4.0.0.0_zh-Hant_b77a5c561934e089/mscorlib.resources.dll
----------------------------------------

************** JIT 偵錯 **************
若要啟用 Just-In-Time (JIT) 偵錯功能，則必須在
此應用程式或電腦的 .config 檔案中，設定
system.windows.forms 區段內的 jitDebugging 值。
且該應用程式也必須在啟用偵錯的狀態下進行
編譯。

例如:

<configuration>
    <system.windows.forms jitDebugging="true" />
</configuration>

當 JIT 偵錯功能啟用後，會將所有未處理的例外狀況
傳送給電腦上已註冊的 JIT 偵錯工具進行處
理，而不是使用這個對話方塊來處理。
      



richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個




                System.Diagnostics.ProcessStartInfo psi = new System.Diagnostics.ProcessStartInfo();
                psi.FileName = @"cmd.exe";
                psi.Arguments = @"/c net use " + Name + " " + Path + "";
                psi.WindowStyle = System.Diagnostics.ProcessWindowStyle.Hidden;
                System.Diagnostics.Process.Start(psi);



        private string[] DirName()
        {
            int j = 0;
            string[] str = new string[26];
            for (int i = 65; i <91;i++ )
            {
                str [j]= Convert.ToChar(i).ToString()+":";
                j++;
            }
            return str;
        }




取得目前本基所有的磁碟機
           this.comboBox2.DataSource = Environment.GetLogicalDrives();



            //checkedListBox1
            // 將chkListLot核取清單方塊所有項目設為不勾選
            for (int i = 0; i < checkedListBox1.Items.Count; i++)
            {
                checkedListBox1.SetItemChecked(i, false);
            }




檔名資料夾名處理 大整理 在 vcs_Mix00

                richTextBox1.Text += "原完整檔名 : " + textBox1.Text + "\n";
                string filename = textBox1.Text;
                filename = filename.Substring(filename.LastIndexOf("\\") + 1, filename.Length - filename.LastIndexOf("\\") - 1);
                richTextBox1.Text += "原簡單檔名 : " + filename + "\n";


取得檔案副檔名:
string extension = Path.GetExtension("C:\\soar.jpg");
string extension = Path.GetExtension(filename);


        
        private string CurrentDir = new DirectoryInfo(Environment.CurrentDirectory).Parent.Parent.FullName;

            richTextBox1.Text += "CurrentDir1 = " + Environment.CurrentDirectory + "\n";
            richTextBox1.Text += "CurrentDir2 = " + new DirectoryInfo(Environment.CurrentDirectory).Parent + "\n";
            richTextBox1.Text += "CurrentDir3 = " + new DirectoryInfo(Environment.CurrentDirectory).Parent.Parent + "\n";
            richTextBox1.Text += "CurrentDir4 = " + new DirectoryInfo(Environment.CurrentDirectory).Parent.Parent.FullName + "\n";
            richTextBox1.Text += "CurrentDir5 = " + CurrentDir + "\n";

            /*
            CurrentDir1 = C:\_git\vcs\_2.vcs\my_vcs_lesson_6\_Network\vcs_GMap\vcs_GMap\bin\Debug
            CurrentDir2 = bin
            CurrentDir3 = vcs_GMap
            CurrentDir4 = C:\_git\vcs\_2.vcs\my_vcs_lesson_6\_Network\vcs_GMap\vcs_GMap
            CurrentDir5 = C:\_git\vcs\_2.vcs\my_vcs_lesson_6\_Network\vcs_GMap\vcs_GMap

            //private string CurrentDir = new DirectoryInfo(Environment.CurrentDirectory).Parent.Parent.FullName;
            */




string[] s = Directory.GetFiles(@"D:\項目\Web\Images\shiji"); //獲得文件夾目錄下所有文件全路徑
string[] s = Directory.GetFiles(@"D:\項目\Web\Images\shiji","*.jpg"); //獲得文件夾目錄下指定後綴名文件全路徑
string[] s = Directory.GetDirectories(@"D:\項目\Web\Images"); //獲得文件夾目錄下的文件夾的全路徑





//附隨檔案的寫法
string filename = Path.GetFullPath(Path.Combine(Application.StartupPath, @"..\..")) + @"\AAAAA.BBBBB";
string filename = Path.GetFullPath(Path.Combine(Application.StartupPath, @"..\..")) + @"\excel_20210602_131921.xls";
string filename = Path.GetFullPath(Path.Combine(Application.StartupPath, @"..\..")) + @"\excel_20210602_131921.xls";

richTextBox1.Text += filename + "\n\n";





注意：Image用后请手动释放pictureBox.Image.Dispose();否则图片大些的话，转转下内存就猛升了（一点经验，敬请笑纳）。









Font設定字型及樣式
                new Font(this.Font, FontStyle.Italic),
                




            //Graphics.DrawImage (Image, Rectangle, Rectangle, GraphicsUnit)
            //四個參數分別是     來源影像 目標區域  來源區域      單位

        Cursor myCursor = new Cursor(@"C:\WINDOWS\Cursors\cross_r.cur"); //自定義鼠標 
                //Cursor.Current = myCursor;




txtFile.Text = Application.ExecutablePath;




            //表單預設參數
            richTextBox1.Text += "AAA = " + SystemInformation.FrameBorderSize.Width.ToString() + "\n";  //8
            richTextBox1.Text += "BBB = " + SystemInformation.FrameBorderSize.Height.ToString() + "\n"; //8
            richTextBox1.Text += "CCC = " + SystemInformation.CaptionHeight.ToString() + "\n";          //23




ScreenSaver最簡版
只要能顯示一張圖 或用label顯示時間

移動滑鼠 或 鍵盤按鍵 離開螢幕保護程式



vcs_bitmap_tmp

0 建立Bitmap
  空白Bitmap
  從圖片建立Bitmap

Bitmap基本特性 Width Height
Setpixel
Getpixel


或許需要一個 Bitmap 與 Image 特性大整理
Bitmap內部資料的排列 及 使用
1. 自建空白 Bitmap
2. 直接從圖片建立Bitmap
3. 自建空白打Bitmap 裡面加入一個小Bitmap
4. 改變Bitmap/Image大小


bitmap.maketransparent

clone語法
            //clone範例
            /*
            在Bitmap中可以找到

            Clone（）方法，該方法有三個重載方法。
            Clone（）
            Clone（Rectangle， PixelFormat）
            Clone（RectangleF， PixelFormat）
            */

            string filename = @"C:\______test_files\picture1.jpg";
            Bitmap bitmap1 = new Bitmap(filename);

            Bitmap bitmap2 = (Bitmap)bitmap1.Clone();

            int w = bitmap1.Width;
            int h = bitmap1.Height;
            Rectangle rect = new Rectangle(w / 2, h / 2, w / 2, h / 2);

            //Bitmap bitmap3 = (Bitmap)bitmap1.Clone(rect, PixelFormat.Format32bppArgb);    //same
            Bitmap bitmap3 = (Bitmap)bitmap1.Clone(rect, bitmap1.PixelFormat);

            pictureBox1.Image = bitmap3;



Bitmap/Image存檔





pikasa            
            this.ShowInTaskbar = false;
            this.MaximizeBox = false;
            this.StartPosition = FormStartPosition.CenterScreen;





              private bool IsValidChar(char input)
              {
                     return(char.IsDigit(input));   //检查是否为数字
              }
              

        				
//--------------------------------------------------------------------------------------------------------------------------



        				
//--------------------------------------------------------------------------------------------------------------------------


            richTextBox1.Text += "找出所有的COM port, ";

            // Get a list of serial port names.
            string[] ports = SerialPort.GetPortNames();

            richTextBox1.Text += " 共有 " + ports.Length + " 個COM port\n";
            // Display each port name to the console.
            foreach (string port in ports)
            {
                richTextBox1.Text += "\t" + port + "\n";
            }
            richTextBox1.Text += "\n";


        				
//--------------------------------------------------------------------------------------------------------------------------


            //獲取屏幕的分辨率
            //獲取屏幕的分辨率，也就是顯示器屏幕的大小。
            int W = SystemInformation.PrimaryMonitorSize.Width;
            int H = SystemInformation.PrimaryMonitorSize.Height;

            richTextBox1.Text += "W = " + W.ToString() + " H = " + H.ToString() + "\n";

            richTextBox1.Text += "取得桌面大小\n";
            richTextBox1.Text += "桌面寬度 : \t" + Screen.PrimaryScreen.WorkingArea.Width.ToString() + "\n";
            richTextBox1.Text += "桌面高度 : \t" + Screen.PrimaryScreen.WorkingArea.Height.ToString() + "\n";




            //取得螢幕解析度資料
            System.Windows.Forms.Screen scr = System.Windows.Forms.Screen.PrimaryScreen;//PrimaryScreen 属性：获取主显示设备
            richTextBox1.Text += "Bounds:\t\t" + scr.Bounds.ToString() + "\n"; //获取屏幕的边界。属性值是一个Rectangle结构的值
            richTextBox1.Text += "DeviceName:\t" + scr.DeviceName.ToString() + "\n"; //获取与显示关联的设备名称
            richTextBox1.Text += "Primary:\t\t" + scr.Primary.ToString() + "\n";   //该值指示某个显示是否为主设备
            richTextBox1.Text += "WorkingArea:\t" + scr.WorkingArea.ToString() + "\n";   //获取显示器的工作区, 属性值是一个Rectangle结构的值
            richTextBox1.Text += "BitsPerPixel:\t" + scr.BitsPerPixel.ToString() + "\n"; //获取与数据的一个像素相关联的内存位数


螢幕解析度 與 可工作區域
            //取得螢幕解析度
            int ScreenWidth = Screen.PrimaryScreen.Bounds.Width;
            int ScreenHeight = Screen.PrimaryScreen.Bounds.Height;

            richTextBox1.Text += "螢幕解析度 : " + ScreenWidth.ToString() + " X " + ScreenHeight.ToString() + "\n";

            //取得可工作區域大小
            int WorkingAreaWidth = Screen.PrimaryScreen.WorkingArea.Width;
            int WorkingAreaHeight = Screen.PrimaryScreen.WorkingArea.Height;

            richTextBox1.Text += "可工作區域大小 : " + WorkingAreaWidth.ToString() + " X " + WorkingAreaHeight.ToString() + "\n";

            foreach (Screen screen in System.Windows.Forms.Screen.AllScreens)
            {
                richTextBox1.Text += "Screen " + screen.DeviceName + "\n";
                richTextBox1.Text += "\tPrimary " + screen.Primary + "\n";
                richTextBox1.Text += "\tBounds: " + screen.Bounds + "\n";
                richTextBox1.Text += "\tWorking Area: " + screen.WorkingArea + "\n";
                richTextBox1.Text += "\tBitsPerPixel: " + screen.BitsPerPixel + "\n";
            }



            //螢幕資訊
            richTextBox1.Text += "AllScreens.Length = " + Screen.AllScreens.Length.ToString() + "\n";

            richTextBox1.Text += "W = " + Screen.AllScreens[0].Bounds.Width.ToString() + ", H = " + Screen.AllScreens[0].Bounds.Height.ToString() + "\n";
            richTextBox1.Text += "Bounds = " + Screen.AllScreens[0].Bounds.Size.ToString() + "\n";
            richTextBox1.Text += "Rank = " + Screen.AllScreens.Rank.ToString() + "\n";

            richTextBox1.Text += "DeviceName = " + Screen.PrimaryScreen.DeviceName + "\n";
            richTextBox1.Text += "BitsPerPixel = " + Screen.PrimaryScreen.BitsPerPixel.ToString() + "\n";
            richTextBox1.Text += "Bounds = " + Screen.PrimaryScreen.Bounds.ToString() + "\n";
            richTextBox1.Text += "WorkingArea = " + Screen.PrimaryScreen.WorkingArea.ToString() + "\n";



            Rectangle WorkArea = Screen.GetWorkingArea(this);//屏幕顯示區域
            int W = WorkArea.Width; //屏幕寬度
            int H = WorkArea.Height; //屏幕高度
            richTextBox1.Text += "W = " + W.ToString() + "\n";
            richTextBox1.Text += "H = " + H.ToString() + "\n";


        				
//--------------------------------------------------------------------------------------------------------------------------

DateTime

        // Parse a dater with format 20200517.
        private DateTime ParseDate(string date_text)
        {
            int year = int.Parse(date_text.Substring(0, 4));
            int month = int.Parse(date_text.Substring(4, 2));
            int day = int.Parse(date_text.Substring(6));
            return new DateTime(year, month, day);
        }

        // Return a value from the CSV file.
        private int ParseValue(object value)
        {
            if (value == null) return 0;
 
            int result;
            if (int.TryParse(value.ToString(), out result)) return result;
            return 0;
        }

可能可以拿來改成分析西元前年份的部分
        // Parse a dater with format 20200517.
        private DateTime ParseDate(string date_text)
        {
            int year = int.Parse(date_text.Substring(0, 4));
            int month = int.Parse(date_text.Substring(4, 2));
            int day = int.Parse(date_text.Substring(6));
            return new DateTime(year, month, day);
        }



"-123年4月5日"
先自己解看看
若是年份是負的 先反相再交DateTime.Parse()來解
解出來的結果 再反相

                          
                    
				
//--------------------------------------------------------------------------------------------------------------------------

            string namespaceName = Assembly.GetExecutingAssembly().GetName().Name.ToString();   //獲取前文檔命名空間的名稱
            richTextBox1.Text += namespaceName + "\n";





        				
//--------------------------------------------------------------------------------------------------------------------------







           

//============================================================================================================================





  

//============================================================================================================================


            






//============================================================================================================================





            richTextBox1.Text += "取得網頁資料\n";
            string strUrl = "https://www.google.com.tw/"; //獲得IP的網址了

            Uri uri = new Uri(strUrl);
            System.Net.WebRequest wr = System.Net.WebRequest.Create(uri);
            Stream s = wr.GetResponse().GetResponseStream();
            StreamReader sr = new StreamReader(s, Encoding.Default);
            string all = sr.ReadToEnd(); //讀取網站的數據
            richTextBox1.Text += all + "\n";






//============================================================================================================================




//如何取得網路上的圖片並顯示 
            string url = @"https://upload.wikimedia.org/wikipedia/commons/0/0f/Ic-photo-intel-D4004.png";
            this.pictureBox1.Image = ReadImageFromUrl(url);

        private Image ReadImageFromUrl(string urlImagePath)
        {
            Uri uri = new Uri(urlImagePath);
            WebRequest webRequest = WebRequest.Create(uri);
            Stream stream = webRequest.GetResponse().GetResponseStream();
            Image res = Image.FromStream(stream);
            return res;

        }




//============================================================================================================================




 
 
//提取HTML代碼中文字的C#函數

/// <summary>
  /// 去除HTML標記
  /// </summary>
  /// <param name="strHtml">包括HTML的源碼 </param>
  /// <returns>已經去除後的文字</returns>
  public static string StripHTML(string strHtml)
  {
   string [] aryReg ={
          @"<script[^>]*?>.*?</script>",

          @"<(\/\s*)?!?((\w+:)?\w+)(\w+(\s*=?\s*(([""'])(\\[""'tbnr]|[^\7])*?\7|\w+)|.{0})|\s)*?(\/\s*)?>",
          @"([\r\n])[\s]+",
          @"&(quot|#34);",
          @"&(amp|#38);",
          @"&(lt|#60);",
          @"&(gt|#62);", 
          @"&(nbsp|#160);", 
          @"&(iexcl|#161);",
          @"&(cent|#162);",
          @"&(pound|#163);",
          @"&(copy|#169);",
          @"&#(\d+);",
          @"-->",
          @"<!--.*\n"

         };

   string [] aryRep = {
           "",
           "",
           "",
           "\"",
           "&",
           "<",
           ">",
           " ",
           "\xa1",//chr(161),
           "\xa2",//chr(162),
           "\xa3",//chr(163),
           "\xa9",//chr(169),
           "",
           "\r\n",
           ""
          };

   string newReg =aryReg[0];
   string strOutput=strHtml;
   for(int i = 0;i<aryReg.Length;i++)
   {
    Regex regex = new Regex(aryReg[i],RegexOptions.IgnoreCase );
    strOutput = regex.Replace(strOutput,aryRep[i]);
   }

   strOutput.Replace("<","");
   strOutput.Replace(">","");
   strOutput.Replace("\r\n","");


   return strOutput;
  }


 
 

 











//============================================================================================================================


//C#chart之PieChart

                void CreateChart()
        {
            string[] xValues = { "0-20", "20-30", "30-40", "40-50", "50-60", "> 60", "unknow" };
            int[] yValues = {5, 18, 45, 17, 2, 1, 162 };

            //ChartAreas,Series,Legends 基本設定-------------------------------------------------
            Chart Chart1 = new Chart();
            Chart1.ChartAreas.Add(ChartArea1); //圖表區域集合
            Chart1.Legends.Add(Legends1); //圖例集合說明
            Chart1.Series.Add(Series1); //數據序列集合

            //設定 Chart-------------------------------------------------------------------------
            Chart1.Width = 770;
            Chart1.Height = 400;
            Title title = new Title();
            title.Text = "titleStr";
            title.Alignment = ContentAlignment.MiddleCenter;
            title.Font = new System.Drawing.Font("Trebuchet MS", 14F, FontStyle.Bold);
            Chart1.Titles.Add(title);

            //設定 ChartArea1--------------------------------------------------------------------
            Chart1.ChartAreas[ChartArea1].Area3DStyle.Enable3D = is3D;
            Chart1.ChartAreas[0].AxisX.Interval = 1;

            //設定 Legends-------------------------------------------------------------------------                
            //Chart1.Legends[Legends1].DockedToChartArea = ChartArea1; //顯示在圖表內
            //Chart1.Legends[Legends1].Docking = Docking.Bottom; //自訂顯示位置
            //背景色
            Chart1.Legends[Legends1].BackColor = Color.FromArgb(235, 235, 235); 
            //斜線背景
            Chart1.Legends[Legends1].BackHatchStyle = ChartHatchStyle.DarkDownwardDiagonal; 
            Chart1.Legends[Legends1].BorderWidth = 1;
            Chart1.Legends[Legends1].BorderColor = Color.FromArgb(200, 200, 200);

            //設定 Series1-----------------------------------------------------------------------
            Chart1.Series[Series1].ChartType = SeriesChartType.Pie;
            //Chart1.Series[Series1].ChartType = SeriesChartType.Doughnut;
            Chart1.Series[Series1].Points.DataBindXY(xValues, yValues);
            Chart1.Series[Series1].LegendText = "Aaaaaa";   //#VALX:    [ #PERCENT{P1} ]; //X軸 + 百分比
            Chart1.Series[Series1].Label = "bbbb";  //#VALX#PERCENT{P1}; //X軸 + 百分比
            //Chart1.Series[Series1].LabelForeColor = Color.FromArgb(0, 90, 255); //字體顏色
            //字體設定
            Chart1.Series[Series1].Font = new System.Drawing.Font("Trebuchet MS", 10, System.Drawing.FontStyle.Bold); 
            Chart1.Series[Series1].Points.FindMaxByValue().LabelForeColor = Color.Red;
            //Chart1.Series[Series1].Points.FindMaxByValue().Color = Color.Red;
            //Chart1.Series[Series1].Points.FindMaxByValue()[Exploded] = true;
            Chart1.Series[Series1].BorderColor = Color.FromArgb(255, 101, 101, 101);
            
            //Chart1.Series[Series1][DoughnutRadius] = 80; // ChartType為Doughnut時，Set Doughnut hole size
            //Chart1.Series[Series1][PieLabelStyle] = Inside; //數值顯示在圓餅內
            Chart1.Series[Series1][PieLabelStyle] = Outside; //數值顯示在圓餅外
            //Chart1.Series[Series1][PieLabelStyle] = Disabled; //不顯示數值
            //設定圓餅效果，除 Default 外其他效果3D不適用
            Chart1.Series[Series1][PieDrawingStyle] = Default; 
            //Chart1.Series[Series1][PieDrawingStyle] = SoftEdge;
            //Chart1.Series[Series1][PieDrawingStyle] = Concave;

            //Random rnd = new Random();  //亂數產生區塊顏色
            //foreach (DataPoint point in Chart1.Series[Series1].Points)
            //{
            //    //pie 顏色
            //    point.Color = Color.FromArgb(150, rnd.Next(0, 255), rnd.Next(0, 255), rnd.Next(0, 255)); 
            //}
            this.Controls.Add(Chart1);
        }
      




//============================================================================================================================




//--------------------------------------------------------------------------------------------------------------------------







//--------------------------------------------------------------------------------------------------------------------------


//--------------------------------------------------------------------------------------------------------------------------

            //取得顯示設備相關資訊
            ManagementObjectSearcher mos = new ManagementObjectSearcher("select * from win32_VideoController");//聲明一個用于檢索設備管理信息的對象
            foreach (ManagementObject mo in mos.Get())//循環遍歷WMI實例中的每一個對象
            {
                richTextBox1.Text += "顯示設備名稱 : " + mo["name"].ToString() + "\n";  //在文本框中顯示顯示設備的名稱
                richTextBox1.Text += "PNPDeviceID : " + mo["PNPDeviceID"].ToString() + "\n"; //在文本框中顯示顯示設備的PNPDeviceID

                richTextBox1.Text += "最大更新率 : " + mo["MaxRefreshRate"].ToString() + "\n"; //在當前文本框中顯示最大刷新率
                richTextBox1.Text += "最小更新率 : " + mo["MinRefreshRate"].ToString() + "\n"; //在當前文本框中顯示最小刷新率
                richTextBox1.Text += "目前更新率 : " + mo["CurrentRefreshRate"].ToString() + "\n"; //在當前文本框中顯示當前刷新率

                richTextBox1.Text += "顯示模式 : " + mo["VideoModeDescription"].ToString() + "\n"; //在文本框中顯示設備的當前顯示模式
            }


				
//--------------------------------------------------------------------------------------------------------------------------

            //取得計算機的顯示設備訊息
            ManagementObjectSearcher mos = new ManagementObjectSearcher("select * from Win32_VideoController");
            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += "顯示設備訊息\n";
                richTextBox1.Text += "顯示設備名稱：" + mo["Name"].ToString() + "\n";//顯示設備名稱
                richTextBox1.Text += "顯示設備PNPDeviceID：" + mo["PNPDeviceID"].ToString() + "\n";//顯示設備的PNPDeviceID
                richTextBox1.Text += "顯示設備驅動程序文件：" + mo["InstalledDisplayDrivers"].ToString() + "\n";//顯示設備的驅動程序文件
                richTextBox1.Text += "顯示設備驅動版本號：" + mo["DriverVersion"].ToString() + "\n";//顯示設備的驅動版本號
                richTextBox1.Text += "顯示設備的顯示處理器：" + mo["VideoProcessor"].ToString() + "\n";//顯示設備的顯示處理器
                richTextBox1.Text += "顯示設備的最大更新率：" + mo["MaxRefreshRate"].ToString() + "\n";//顯示設備的最大更新率
                richTextBox1.Text += "顯示設備的最小更新率：" + mo["MinRefreshRate"].ToString() + "\n";//顯示設備的最大更新率
                richTextBox1.Text += "顯示設備目前顯示模式：" + mo["VideoModeDescription"].ToString() + "\n";//顯示設備目前顯示模式
            }




//--------------------------------------------------------------------------------------------------------------------------

            //取得音效設備相關資訊
            ManagementObjectSearcher mos = new ManagementObjectSearcher("select * from Win32_SoundDevice");//聲明一個用于檢索設備管理信息的對象
            foreach (ManagementObject mo in mos.Get())//循環遍歷WMI實例中的每一個對象
            {
                richTextBox1.Text += "音效設備名稱 : " + mo["ProductName"].ToString() + "\n"; //在當前文本框中顯示聲音設備的名稱
                richTextBox1.Text += "PNPDeviceID : " + mo["PNPDeviceID"].ToString() + "\n";//在當前文本框中顯示聲音設備的PNPDeviceID
            }





//--------------------------------------------------------------------------------------------------------------------------

            //取得映射驅動器路徑
            //映射驅動器 = 網路芳鄰硬碟的連結

            SelectQuery selectQuery = new SelectQuery("select * from win32_logicaldisk");
            ManagementObjectSearcher searcher = new ManagementObjectSearcher(selectQuery);
            int i = 0;
            foreach (ManagementObject disk in searcher.Get())
            {
                string DriveType;
                DriveType = disk["DriveType"].ToString();

                richTextBox1.Text += "磁盤名稱：" + disk["Name"].ToString() + "\n";
                //獲得硬盤的可用空間

                long mb = 1048576;
                double free = 0;
                double use = 0;
                double total = 0;
                free = Convert.ToInt64(disk["FreeSpace"]) / mb;
                //獲得硬盤的已用空間
                use = (Convert.ToInt64(disk["Size"]) - Convert.ToInt64(disk["FreeSpace"])) / mb;
                //獲得硬盤的合計空間
                total = Convert.ToInt64(disk["Size"]) / mb;
                richTextBox1.Text += " 總計：" + total.ToString() + "MB\n";
                richTextBox1.Text += "已用空間：" + use.ToString() + "MB\n";
                richTextBox1.Text += "可用空間：" + free.ToString() + "MB\n";

                if (DriveType == "4")
                {
                    richTextBox1.Text += "取得 : " + disk["Name"].ToString() + "\n";
                }
                i++;
            }





//--------------------------------------------------------------------------------------------------------------------------






//--------------------------------------------------------------------------------------------------------------------------








//--------------------------------------------------------------------------------------------------------------------------


//Properties Save ST

            this.SetBounds(
                Properties.Settings.Default.Left,
                Properties.Settings.Default.Top,
                Properties.Settings.Default.Width,
                Properties.Settings.Default.Height);

            txtScale.Text = Properties.Settings.Default.Scale;

        // Save parameters.
        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            Properties.Settings.Default.Left = this.Left;
            Properties.Settings.Default.Top = this.Top;
            Properties.Settings.Default.Width = this.Width;
            Properties.Settings.Default.Height = this.Height;

            Properties.Settings.Default.Directory = txtDirectory.Text;
            Properties.Settings.Default.Scale = txtScale.Text;

            Properties.Settings.Default.Save();
        }






有需要存檔的資料
1. 最後存取的路徑
2. 視窗大小
3. 最後選取的設定項目


若是我的筆記本

properties.save
還要儲存字型 大小 前景色背景色
表單大小位置 

//Properties Save SP



//--------------------------------------------------------------------------------------------------------------------------






//--------------------------------------------------------------------------------------------------------------------------






//--------------------------------------------------------------------------------------------------------------------------






//--------------------------------------------------------------------------------------------------------------------------






//--------------------------------------------------------------------------------------------------------------------------





//--------------------------------------------------------------------------------------------------------------------------

MD5/SHA1說明大集合


異名同義字
 
            MD5 md5 = MD5.Create();    //創建MD5對象
            MD5 md5 = MD5CryptoServiceProvider.Create();    //創建MD5對象
            MD5 md5 = new MD5CryptoServiceProvider();
            MD5CryptoServiceProvider md5 = new MD5CryptoServiceProvider();
            HashAlgorithm md5 = new MD5CryptoServiceProvider(); // or SHA1CryptoServiceProvider();
            HashAlgorithm md5 = MD5.Create();


            MD5 md5 = MD5.Create();    //創建MD5對象
            //MD5 md5 = MD5CryptoServiceProvider.Create();    //創建MD5對象
            //MD5 md5 = new MD5CryptoServiceProvider();
            //MD5CryptoServiceProvider md5 = new MD5CryptoServiceProvider();
            //HashAlgorithm md5 = new MD5CryptoServiceProvider(); // or SHA1CryptoServiceProvider();
            //HashAlgorithm md5 = MD5.Create();



byte[] input = Encoding.Default.GetBytes(str);	//字串轉拜列  111
byte[] input = Encoding.UTF8.GetBytes(key + str); //字串轉拜列
byte[] input = Encoding.UTF8.GetBytes(str); //字串轉拜列
byte[] input = Encoding.UTF8.GetBytes(str); //字串轉拜列   222
byte[] input = Encoding.Unicode.GetBytes(str);  //字串轉拜列
byte[] input = Encoding.ASCII.GetBytes(str);
byte[] input = Encoding.Unicode.GetBytes(str);
byte[] input = Encoding.UTF8.GetBytes(key + str); //字串轉拜列
byte[] input = Encoding.Unicode.GetBytes(str);  //字串轉拜列
byte[] input = Encoding.UTF8.GetBytes(str); //字串轉拜列
byte[] input = Encoding.Unicode.GetBytes(str);  //字串轉拜列
byte[] input = Encoding.UTF8.GetBytes(str); //字串轉拜列
byte[] input = Encoding.UTF8.GetBytes(str); //字串轉拜列
byte[] input = Encoding.UTF8.GetBytes(str); //字串轉拜列
byte[] input = Encoding.Unicode.GetBytes(str); //字串轉拜列

byte[] input = ASCIIEncoding.ASCII.GetBytes(str); //字串轉拜列
byte[] input = ASCIIEncoding.ASCII.GetBytes(str);
byte[] input = new UnicodeEncoding().GetBytes(str);   //字串轉拜列
byte[] input = Encoding.Unicode.GetBytes(str); //字串轉拜列
byte[] input = UTF8Encoding.UTF8.GetBytes(str); //字串轉拜列
byte[] input = UTF8Encoding.UTF8.GetBytes(str); //字串轉拜列


UTF8Encoding.Default.GetBytes(str)


        private byte[] GetKeyByteArray(string str)
        {
            int tmpStrLen = str.Length;
            byte[] input = input = new ASCIIEncoding().GetBytes(str);
            return input;
        }

        //byte[] input = Encoding.Default.GetBytes(str);  //字串轉拜列




string md5Result = Encoding.Default.GetString(md5Hash); //Hash轉字串






各種拜列轉字串

            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < md5Hash.Length; i++)
            {
                sb.Append(md5Hash[i].ToString("X2"));
            }
            md5Result = sb.ToString();






            //Hash轉字串
            for (int i = 0; i < md5Hash.Length; i++)
            {
                md5Result = md5Result + md5Hash[i].ToString("X2");
            }






            //Hash轉字串
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < md5Hash.Length; i++)
            {
                sb.Append(md5Hash[i].ToString("X2"));
                //sb.AppendFormat("{0:X2}", md5Hash[i]);    //same
            }
            md5Result = sb.ToString();


            //Hash轉字串
            StringBuilder sb = new StringBuilder();
            foreach (byte b in md5Hash)
            {
                sb.Append(b.ToString("X2"));
            }
            md5Result = sb.ToString();

            for (int i = 0; i < md5Hash.Length; i++)
            {
                md5Result += md5Hash[i].ToString("X2");
            }


            //Hash轉字串
            md5Result = Encoding.Default.GetString(md5Hash);

            //Hash轉字串
            md5Result = GetStringValue(md5Hash);



            //Hash轉字串
            for (int i = 0; i < md5Hash.Length; i++)
            {
                md5Result += md5Hash[i].ToString("X2");
            }



            for (int i = 0; i < md5Hash.Length - 1; i++)//遍歷Byte數組
            {
                md5Result += md5Hash[i].ToString("X2").PadLeft(2, '0');//對遍歷到的Byte進行加密
            }


            for (int i = 0; i < md5Hash.Length; i++)
            {
                md5Result = md5Result + md5Hash[i].ToString("X2");
            }




            foreach (byte b in md5Hash)
            {
                md5Result += b.ToString("X2");
            }



            //Hash轉字串
            StringBuilder sb = new StringBuilder(16);
            for (int i = 0; i < md5Hash.Length; i++)
            {
                sb.Append((md5Hash[i]).ToString("X2", System.Globalization.CultureInfo.InvariantCulture));
            }
            md5Result = sb.ToString();





            /*
            //Hash轉字串
            StringBuilder sb = new StringBuilder(32);
            for (int i = 0; i < md5Hash.Length; i++)
            {
                sb.Append(md5Hash[i].ToString("X2").PadLeft(2, '0'));
            }
            md5Result = sb.ToString();
            */



            //md5Result = BitConverter.ToString(md5Hash).Replace("-", "");
            //md5Result = Encoding.Default.GetString(md5Hash);

            //Hash轉字串
            //將加密後的數組轉化為字段(普通加密)  
            //string testResult = Encoding.Unicode.GetString(md5Hash);    //不正確

            //作為密碼方式加密
            //需要改用.NetFramework4.0 且 參考/加入參考 .NET /System.Web
            //md5Result = System.Web.Security.FormsAuthentication.HashPasswordForStoringInConfigFile(str, "MD5");




            /*
            //Hash轉字串
            foreach (byte b in md5Hash)
            {
                md5Result += b.ToString("X2");
            }
            */



















MD5 File 線上工具
HTML5 File Hash Online Calculator
https://md5file.com/calculator
				

            //MD5加密是不可以逆的，只能將字串轉為MD5值，不能將MD5值轉回字串。

            //這裡Hash算法用MD5算法為例，MD5加密是不可逆的，所以只有加密沒有解密。


        //C#實現MD5加密
        /*
        MD5的全稱是message-digest algorithm 5(信息-摘要算法，在90年代初由mit laboratory for computer science和rsa data security inc的ronald l. rivest開發出來， 經md2、md3和md4發展而來。
        MD5具有很好的安全性(因為它具有不可逆的特征,加過密的密文經過解密後和加密前的東東相同的可能性極小)
        */



            /*
            MD5簡介： 
            MD5的全稱是Message-Digest Algorithm 5，在90年代初由MIT的計算機科學實驗室和RSA Data Security Inc發明，
            經MD2、MD3和MD4發展而來。MD5將任意長度的“字節串”變換成一個128bit的大整數，並且它是一個不可逆的字符串變換算法。
            換句話說就是，即使你看到源程序和算法描述，也無法將一個MD5的值變換回原始的字符串，
            從數學原理上說，是因為原始的字符串有無窮多個，這有點象不存在反函數的數學函數。
            */







    Cryptography測試

資料來源: [C#] 使用MD5、SHA-1、SHA-2(SHA-256、SHA-384、SHA-512) 加密資料


文中提到一些常見的加密演算法目的及c#範例, 方便有需要的人取用!!!

1. 使用者輸入密碼, Hash後寫入資料庫, 因此即使資料庫被入侵, 有心人士也無法得知原始的密碼為何!

2. 爾後使用者登錄輸入密碼, 同樣Hash後跟資料庫進行比對驗證





首先,先簡單介紹一下MD5

MD5的全稱是message-digest algorithm 5(信息-摘要算法，在90年代初由mit laboratory for computer science和rsa data security inc的ronald l. rivest開發出來， 經md2、md3和md4發展而來。

MD5具有很好的安全性(因為它具有不可逆的特征,加過密的密文經過解密後和加密前的東東相同的可能性極小) 


//而C#默認的是16位的字節數組，需要略加修改，轉為32個字節的字符串，

//C# MD5 校驗32位的字符串






C#計算文件的MD5值實例


　　MD5 是 Message Digest Algorithm 5（信息摘要算法）的縮寫，MD5 一種散列(Hash)技術，普遍用於加密、解密、數據簽名和數據完整性校驗等方面。任何一個文件，不管是可執行程序、圖像文件、臨時文件或者其餘任何類型的文件，也無論它體積多大，均可以計算出一個MD5值，若是文件被修改過，就算只改動了一個字節，其 MD5 值也會變得徹底不一樣。所以，咱們能夠經過對比同一文件的 MD5 值，來校驗這個文件是否被「篡改」過。算法




由於MD5是不可逆的，所以加密之後就無法解密，取用戶名和密碼時候，需要再加密一邊用戶輸入的數據與數據庫中已加密的數據進行比對。
如果比對結果一致，則可以判定登錄成功


            //MD5   32位
            //MD5驗證 32 位元
            //使用Md5Sum算出32位的校驗碼字符串
            //MD5 校驗默認為32位的字符串， 而C#默認的是16位的字節數組，需要略加修改，轉為32個字節的字符串，




    //C#計算文件的MD5值實例
    /*
在C#中，數據的Hash以MD5或SHA1的方式實現，MD5與SHA1都是Hash算法，MD5輸出是128位的，SHA1輸出是160位的，MD5比SHA1快，SHA1比MD5強度高。
1.1 SHA-1和MD5的比較

因為二者均由MD4導出，SHA-1和MD5彼此很相似。相應的，他們的強度和其他特性也是相似，但還有以下幾點不同：

    對強行攻擊的安全性：最顯著和最重要的區別是SHA-1摘要比MD5摘要長32 位。使用強行技術，產生任何一個報文使其摘要等於給定報摘要的難度對MD5是2128數量級的操作，而對SHA-1則是2160數量級的操作。這樣，SHA-1對強行攻擊有更大的強度。
    對密碼分析的安全性：由於MD5的設計，易受密碼分析的攻擊，SHA-1顯得不易受這樣的攻擊。
    速度：在相同的硬件上，SHA-1的運行速度比MD5慢。

1.2 SHA-1和MD5在C#中的實現
*/

    /*
    MD5 是 Message Digest Algorithm 5（信息摘要算法）的縮寫，MD5 一種散列(Hash)技術，廣泛用於加密、解密、數據簽名和數據完整性校驗等方面。任何一個文件，無論是可執行程序、圖像文件、臨時文件或者其他任何類型的文件，也不管它體積多大，都可以計算出一個MD5值，如果文件被修改過，就算只改動了一個字節，其 MD5 值也會變得完全不同。因此，我們可以通過對比同一文件的 MD5 值，來校驗這個文件是否被“篡改”過。C# 可以方便的計算出文件的 MD5 值：
    \\計算文件的MD5值
    */




//C# MD5摘要算法、哈希算法，
//MD5即Message-Digest Algorithm 5（信息-摘要算法5），用於確保信息傳輸完整一致。是計算機廣泛使用的雜湊算法之一（又譯摘要算法、哈希算法）

//C#計算文件的MD5值實例
//MD5 是 Message Digest Algorithm 5（信息摘要算法）的縮寫，MD5 一種散列(Hash)技術，廣泛用於加密、解密、數據簽名和數據完整性校驗等方面。



        //MD5，SHA1，SHA256，SHA512 ST

        /**/
        /// <summary>
        /// 使用DES加密（Added by niehl 2005-4-6）
        /// </summary>
        /// <param name="originalValue">待加密的字符串</param>
        /// <param name="key">密鑰(最大長度8)</param>
        /// <param name="IV">初始化向量(最大長度8)</param>
        /// <returns>加密後的字符串</returns>
        public string DESEncrypt(string originalValue, string key, string IV)
        {
            //將key和IV處理成8個字符
            key += "12345678";
            IV += "12345678";
            key = key.Substring(0, 8);
            IV = IV.Substring(0, 8);
            SymmetricAlgorithm sa;
            ICryptoTransform ct;
            MemoryStream ms;
            CryptoStream cs;
            byte[] byt;
            sa = new DESCryptoServiceProvider();
            sa.Key = Encoding.UTF8.GetBytes(key);
            sa.IV = Encoding.UTF8.GetBytes(IV);
            ct = sa.CreateEncryptor();
            byt = Encoding.UTF8.GetBytes(originalValue);
            ms = new MemoryStream();
            cs = new CryptoStream(ms, ct, CryptoStreamMode.Write);
            cs.Write(byt, 0, byt.Length);
            cs.FlushFinalBlock();
            cs.Close();
            return Convert.ToBase64String(ms.ToArray());
        }

        public string DESEncrypt(string originalValue, string key)
        {
            return DESEncrypt(originalValue, key, key);
        }

        /**/
        /// <summary>
        /// 使用DES解密（Added by niehl 2005-4-6）
        /// </summary>
        /// <param name="encryptedValue">待解密的字符串</param>
        /// <param name="key">密鑰(最大長度8)</param>
        /// <param name="IV">m初始化向量(最大長度8)</param>
        /// <returns>解密後的字符串</returns>
        public string DESDecrypt(string encryptedValue, string key, string IV)
        {
            //將key和IV處理成8個字符
            key += "12345678";
            IV += "12345678";
            key = key.Substring(0, 8);
            IV = IV.Substring(0, 8);
            SymmetricAlgorithm sa;
            ICryptoTransform ct;
            MemoryStream ms;
            CryptoStream cs;
            byte[] byt;
            sa = new DESCryptoServiceProvider();
            sa.Key = Encoding.UTF8.GetBytes(key);
            sa.IV = Encoding.UTF8.GetBytes(IV);
            ct = sa.CreateDecryptor();
            byt = Convert.FromBase64String(encryptedValue);
            ms = new MemoryStream();
            cs = new CryptoStream(ms, ct, CryptoStreamMode.Write);
            cs.Write(byt, 0, byt.Length);
            cs.FlushFinalBlock();
            cs.Close();
            return Encoding.UTF8.GetString(ms.ToArray());
        }

        public string DESDecrypt(string encryptedValue, string key)
        {
            return DESDecrypt(encryptedValue, key, key);
        }




//--------------------------------------------------------------------------------------------------------------------------






richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個



richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個



vcs標準版大集合
TBGBMBKB
轉出與全部轉出
儲存圖檔
移動控件mousedown-mousemove-mouseup




準備自建函式庫用
        Bitmap color_to_gray(Bitmap bitmap1)
        {
            //SetPixel 彩色轉灰階
            int xx;
            int yy;

            for (yy = 0; yy < bitmap1.Height; yy++)
            {
                for (xx = 0; xx < bitmap1.Width; xx++)
                {
                    byte rrr = bitmap1.GetPixel(xx, yy).R;
                    byte ggg = bitmap1.GetPixel(xx, yy).G;
                    byte bbb = bitmap1.GetPixel(xx, yy).B;

                    int Gray = (rrr * 299 + ggg * 587 + bbb * 114 + 500) / 1000;
                    Color zz = Color.FromArgb(255, Gray, Gray, Gray);

                    bitmap1.SetPixel(xx, yy, zz);
                }
            }
            return bitmap1;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //SetPixel 彩色轉灰階
            string filename = @"C:\______test_files\picture1.jpg";

            Bitmap bitmap1 = new Bitmap(filename);
            Bitmap bitmap2 = color_to_gray(bitmap1);

            pictureBox1.Image = bitmap2;

        }





vcs
listBox1.Items.Count > 0);

            if (listBox1.SelectedItems.Count > 0)


移除多選的項目
            while (listBox1.SelectedIndices.Count > 0)
            {
                listBox1.Items.RemoveAt(listBox1.SelectedIndices[0]);
            }
            

listBox屬性
            listBox1.SelectionMode = SelectionMode.MultiExtended;
            listBox1.HorizontalScrollbar = true;






—index of hemoglobin (IHb) imaging



excel/excel7_item.xlsx  新舊有何不同\


 public void ShowTxt(string a)
 {
 this.textBox1.AppendText(DateTime.Now.ToString() + | + a + );
  
   } 
 
 

整理搜尋關鍵字
DataTable



pictureCrop 標準版

2006/03/11
		相距 XXX 天
2022/07/07






WebClient不能處理特定於任何協議的任何特性，例如Cookie等。如果需要使用這些特性，需要使用.net中的HttpWebRequest類。


The Sacred Geometry of the Yin Yang


MyScreenSaver.rar
C#制作簡易屏保，
http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/184114.html

https://www.cnblogs.com/Scl891004X/p/6242805.html


ProgressBar類是密封(sealed)的，不能再被繼承。



pictureBox圖像直接存檔
pictureBox1.Image.Save(filename);


寫圖片至檔案
            //write image
            bitmap1.Save("C:\\Output.png");
            
            pictureBox1.Image.Save(filename);



存圖 
                    FileStream fs = (FileStream)saveFileDialog1.OpenFile();
                    switch (saveFileDialog1.FilterIndex)    		//選擇保存文件類型
                    {
                        case 1:
                            this.pictureBox1.Image.Save(fs, ImageFormat.Jpeg); 		//保存為jpeg文件
                            break;
                        case 2:
                            this.pictureBox1.Image.Save(fs, ImageFormat.Bmp);
                            break;
                        case 3:
                            this.pictureBox1.Image.Save(fs, ImageFormat.Gif);
                            break;
                    }
                    fs.Close();         					//關閉文件流









            //跟隨鼠標在 pictureBox 的圖片上畫矩形
            pictureBox1.MouseDown += new MouseEventHandler(pictureBox1_MouseDown);
            pictureBox1.MouseMove += new MouseEventHandler(pictureBox1_MouseMove);
            pictureBox1.MouseUp += new MouseEventHandler(pictureBox1_MouseUp);


        private int intStartX = 0;
        private int intStartY = 0;
        private bool isMouseDraw = false;
        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            isMouseDraw = true;
            intStartX = e.X;
            intStartY = e.Y;
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (isMouseDraw)
            {
                try
                {
                    //Image tmp = Image.FromFile("1.png");

                    Graphics g = this.pictureBox1.CreateGraphics();

                    //清空上次畫下的痕跡

                    g.Clear(this.pictureBox1.BackColor);

                    Brush brush = new SolidBrush(Color.Red);

                    Pen pen = new Pen(brush, 1);

                    pen.DashStyle = DashStyle.Solid;

                    g.DrawRectangle(pen, new Rectangle(intStartX > e.X ? e.X : intStartX, intStartY > e.Y ? e.Y : intStartY, Math.Abs(e.X - intStartX), Math.Abs(e.Y - intStartY)));

                    g.Dispose();

                    //this.pictureBox_Src.Image = tmp;
                }

                catch (Exception ex)
                {
                    ex.ToString();
                }
            }
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            isMouseDraw = false;

            intStartX = 0;

            intStartY = 0;
        }





[C#] 使用 Regex.Match 從 String 中提出英文或數字
正規表示式

[abc]： 字元集合
[^a-z]： 非a-z
\d ：  數字
\D ：  非數字
\s ： 一個空白字元
\S：  非空白字元
\w：  單詞字元(a-z,A-Z,0-9,_)
\W：  非單詞字元


無法嵌入互操作類型“Microsoft.Office.Interop.Excel.ApplicationClass”。請改用適用的接口，interop.excel
把Microsoft.Office.Interop.Excel.DLL的嵌入互操作類型改為ture就可以了






如何把一個大Bitmap直接縮成一個小Bitmap
例如原本300X300的Bitmap要如何變成一個100X100的Bitmap?



非1080p的，要標注出來


標準版轉出程式：
用一個結構陣列List儲存最終資料

richtextbox 直接貼上簡中 會出現亂碼  why?

別人的vcs程式也會這樣嗎？


從一個資料夾中撈出所有檔案 標準版
1. 包含/不包含 子目錄
2. 不排序、依檔名排序、依檔案大小排序、依時間排序





//本地緩存+在線服務
            this.gMapControl1.Manager.Mode = AccessMode.ServerAndCache;
//在線服務
            this.gMapControl1.Manager.Mode = AccessMode.ServerOnly;
//本地緩存
            this.gMapControl1.Manager.Mode = AccessMode.CacheOnly;


盡量要把dropbox的文件 搬到 git 裏

            

啟動一個外部程序: [html]   using System;   using System.Collections.Generic;   using System.Linq;   using System.Text;         /* 創建一個進程，並為進程傳入需要的參數    * 或者說是啟動一個外部程序，並為其傳入參數    * 等待退出或者強制關閉   */   namespace ConsoleApplication1   {       class Program       {           static void Main(string[] args)           {                      ////////////聲明一個程序信息類，指定啟動進程是的參數信息                   System.Diagnostics.ProcessStartInfo  Info  =  new  System.Diagnostics.ProcessStartInfo();                      //設置外部程序名                   Info.FileName  =  "notepad.exe";                      //設置外部程序的啟動參數（命令行參數）為test.txt                   Info.Arguments  =  "test.txt";                      //設置外部程序工作目錄為  C:\                   Info.WorkingDirectory  =  "C:\\";                      ///////////聲明一個程序類,也就是創建一個進程                   System.Diagnostics.Process  Proc  ;                      try                   {                   //                   //啟動外部程序                   //                   Proc  =  System.Diagnostics.Process.Start(Info);                   }                   catch(System.ComponentModel.Win32Exception  e)                   {                   Console.WriteLine("系統找不到指定的程序文件。\r{0}",  e);                   return;                   }                      //打印出外部程序的開始執行時間                   Console.WriteLine("外部程序的開始執行時間：{0}",  Proc.StartTime);                      //等待3秒鐘                   Proc.WaitForExit(3000);                      //如果這個外部程序沒有結束運行則對其強行終止                   if(Proc.HasExited  ==  false)                   {                   Console.WriteLine("由主程序強行終止外部程序的運行！");                   Proc.Kill();                   }                   else                   {  www.2cto.com                 Console.WriteLine("由外部程序正常退出！");                   }                   Console.WriteLine("外部程序的結束運行時間：{0}",  Proc.ExitTime);                   Console.WriteLine("外部程序在結束運行時的返回值：{0}",  Proc.ExitCode);           }       }   }     


AcdSee2.4 Serial: 
Name:Unregistered 
Code:422301873421327 


PictureBox 好像不能旋轉方向～～～～～～～～～～～～
若做成Picasa效果 可能不行


參考
C:\_git\vcs\_2.vcs\my_vcs_lesson_5\vcs_StackOrder

讀一個資料夾內的圖片檔
用controls add 造出幾個 picturebox 顯示這些圖 zoom模式
Randomly任意位置顯示 及方向

圖片按左鍵把圖片拉到最上層
圖片按右鍵把圖片推到最下層
也可以無邊框移動圖片





車諾比核事故

，是烏克蘭的一座已經停止使用的核電廠；1986年4月26日四號機因核事故而停止使用，從2015年4月開始1至3號機組已陸續進入退役狀態[1]。而1986年電站的四號機組發生爆炸，引發車諾比核事故。 



將一個資料夾中的所有圖片檔案撈出來編號 每隔1分鐘更換一張桌面底圖 寫上時間 循環播放

記住上次程式關閉時的中心位置 及顯示圖片狀態 給下次程式啟動實用



//要將視頻升級到1080p，請輸入：
//ffmpeg -i input.mp4 -vf scale = 1920x1080：flags = lanczos output_1080p.mp4

//要升級到4K視頻，請輸入：
//ffmpeg -i input.mp4 -vf scale = 3840x2560：flags = lanczos -c：v libx264 -preset slow -crf 21 output_compress_4k.mp4

pie.mp4


ffmpeg -i pie.mp4 -vf scale = 1920x1080：flags = lanczos pie222.mp4



C:\______test_files\_exe\ffmpeg>
C:\______test_files\_exe\ffmpeg>ffmpeg.exe -i pie.mp4 -vf scale=1920x1080 pie222.mp4
C:\______test_files\_exe\ffmpeg>



灰階 與 亮度 的差異

黑白圖片 講 灰階, 最黑是0, 最亮是255, 只有黑白兩色
彩色圖片 講 亮度, 最暗是0, 最亮是255, 有各種顏色

灰階 和 亮度(Y) 在黑白圖片上 是一樣的
彩色圖片只有亮度(Y) 

黑白圖片的每一個點 R=G=B=Y
彩色圖片上 RGBY都是不一樣的

剛剛做了實驗

彩色圖片經過適當的轉換成黑白照片 彩色圖片的亮度Y 會等於 轉換之後黑白照片的RGBY的值

但是 這跟轉換公式有關 轉換公式不同 就不是以上結果

如果轉換公式可靠的話 確實是可以把 亮度 拿來當 灰階 用的

晚些時候 我再寄個圖給你看
 
  

如附圖

左邊是原本彩色 中間是RGBY值

彩色經過某轉轉換成黑白 畫在右邊

你再用工具去量右邊黑白圖片的亮度 是不是等於彩色時的亮度Y

所以

只要能確保轉換公式可靠

彩色的亮度 = 黑白的灰階








獲取遠端圖片 這樣可以節省抓取衛星雲圖的程式碼

桌布程式  可以選擇 置中 shrink zoom........

做成桌面圖的程式

應加上圖形顯示模式 是 zoom stretch shrink .......


衛星雲圖可選其他氣象局的圖



C:\_git\vcs\_2.vcs\my_vcs_lesson_6\_Player\vcs_MP3Cutter
應改成 AudioVideo 轉換程式


目前是 mp3 切割程式

改成
 + mp4 切割程式
 mp3/mp4 info
 mp3 <-> wav 轉換
 mp3合併
  
 除切割程式外 簡單就好 做成範例就好
 做成FFMPEG全部應用


vcs_mp3cutter
應該為vcs_FFMPEG大集合








C:\_git\vcs\_2.vcs\my_vcs_lesson_6_picture_image
和
C:\_git\vcs\_2.vcs\my_vcs_lesson_6\_Screen
裡面的有些混用到listBox的  應分離出來使用


多層次ContextMenuStrip
ContextMenuStrip 選取項目 按右鍵 編輯DropDownItems(E)



//關於c#在DataTable中根據條件刪除某一行，

我們經常會將數據源放在DataTable裡面,但是有時候也需要移除不想要的行,下面的代碼告訴你們

　　　　　　DataTable dts；
                DataRow[] foundRow;
                foundRow = dts.Select("ID=99", "");
                foreach (DataRow row in foundRow)
                {
                    dts.Rows.Remove(row);
                }

其實就是用DataTable的Select方法

上面就是如何Datatable中某一行的id為99，就移除這一行,id為字段名


//C# DataTable 相關操作


///判斷DataTable中某列是否包含某值
/// <summary>
    /// 判斷DataTable中是否包含某值
    /// </summary>
    /// <param name="dt">DataTable</param>
    /// <param name="columnName">列名</param>
    /// <param name="fieldData">值</param>
    /// <returns></returns>
    public Boolean IsColumnIncludeData(DataTable dt, String columnName, string fieldData)
    {
        if (dt == null)
        {
            return false;
        }
        else
        {
            DataRow[] dataRows = dt.Select(columnName + "='" + fieldData + "'");
            if (dataRows.Length.Equals(1))
            {
                return true;
            }
            else
            {
                return false;
            }
        }

    }

 

向DataTable中添加數據

DataTable dt = null;

        dt = handle.ExecuteDataTable(sql, true);

        #region

        DataRow dr;

        for (int i = 0; i < code.Length; i++)
        {
            if (IsColumnIncludeData(dt, "SystemCode", code[i]) == false)
            {
                dr = dt.NewRow();
                dr[0] = name[i];
                dr[1] = code[i];
                dr[2] = 0;
                dt.Rows.Add(dr);
            }
        }
        
        #endregion










        //從沒被用到過
        bool IsInELP(Point Cusorpostion, Point ElpCenter, int radius)
        {
            int elpX = ElpCenter.X;
            int elpY = ElpCenter.Y;
            int csX = Cusorpostion.X;
            int csY = Cusorpostion.Y;
            if (!((elpX - csX) * (elpX - csX) + (elpY - csY) * (elpY - csY) >= radius * radius))
            {
                richTextBox1.Text += "真";
                return true;
            }
            else
            {
                richTextBox1.Text += "假";
                return false;
            }
        }





        private DrawingMode drawingMode = DrawingMode.None;


drawingMode = DrawingMode.None;


namespace GMapDrawTools
{
    public enum DrawingMode
    {
        None,
        Circle,
        Rectangle,
        Polygon,
        Route,
        Line
    }
}



            this.MapControl.CanDragMap = false;
        }

        private void Deactive()
        {
            this.MapControl.CanDragMap = true;



test 下載

源码及Demo下载地址：http://www.chungen90.com/?news_2/

完整代码下载地址：http://pan.baidu.com/s/1o8Lkozw
https://pan.baidu.com/s/1o8Lkozw?errmsg=Auth+Login+Params+Not+Corret&errno=2&ssnerror=0#list/path=%2F



EMGU讀取WebCam
Image<Bgr, Byte> image = cap.QueryFrame(); // Query WebCam 的畫面
EMGU讀取圖片檔案
//Image<Bgr, Byte> image = cap.QueryFrame(); // Query WebCam 的畫面
string filename = @"C:\______test_files\ims01.bmp";
Image<Bgr, Byte> image = new Image<Bgr, byte>(filename);

            

高德地圖
https://www.amap.com/



https://www.cnblogs.com/wpwen/archive/2009/01/01/1366719.html

 自绘进度条的其余代码…

				

C# 以MP3的格式將錄製的音頻數據寫入文件流
https://www.twblogs.net/a/5f02b56e9644181341a1b6e0



    class UtilityFunctions
    {
        /// <summary>
        /// Removes a directory, including all the files in it.
        /// </summary>
        /// <param name="pPath">The directory to remove</param>
        /// <returns>A blank string upon success, or a warning upon error.  If the directory does not exist, that is not an error.</returns>
        public static String DeleteDir(String pPath)
        {
            String retval = "";

            if (Directory.Exists(pPath))
            {
                try
                {
                    // Delete all the files
                    String[] filenames = Directory.GetFiles(pPath);
                    foreach (String filename in filenames)
                        File.Delete(filename);
                    // Delete the directory
                    Directory.Delete(pPath, true);
                }
                catch (System.Exception exc)
                {
                    retval = exc.Message;
                }
            }

            return retval;
        }
    }






        				
//--------------------------------------------------------------------------------------------------------------------------
               





                        GMapMarker marker = new GMarkerGoogle(point, GMarkerGoogleType.green);
                        marker.ToolTipText = place.Value.Address;
                        marker.ToolTipMode = MarkerTooltipMode.Always;
                        markersOverlay.Markers.Add(marker);
                        

對類中得所有成員有五種訪問權限：

· “public” 可以被所有代碼訪問；
· “protected” 只可以被繼承類訪問；
· “internal” 只可以被同一個項目的代碼訪問;
· “protected internal”只可以被同一個項目的代碼或繼承類訪問；
· “private” 只可以被本類中的代碼訪問。
缺省狀態是“private”。






//是否是指名serial port讀取長度 未達目的決不罷休?
serial.Read(bytData, 0, bytData.Length, Timeout.Infinite);




Beep

        [DllImport("kernel32.dll")]
        public static extern bool Beep(int freq, int duration);
        private void button2_Click(object sender, EventArgs e)
        {
            Beep(800, 3000);

        }



https://www.zhangshengrong.com/p/yOXD5ejR1B/





            //抓網頁
            string url = @"https://tw.dictionary.search.yahoo.com/";
            HttpWebRequest httpWebRequest = (HttpWebRequest)HttpWebRequest.Create(url);
            httpWebRequest.ContentType = "application/x-www-form-urlencoded; charset=UTF-8";
            httpWebRequest.Method = "POST";
            var data = Encoding.UTF8.GetBytes(string.Format("{0}", "tiger"));

            using (Stream stream = httpWebRequest.GetRequestStream())
            {
                stream.Write(data, 0, data.Length);
                stream.Close();
            }
            data = null;
            //Result result = new Result();
            string result;

            try
            {
                HttpWebResponse webResponse = httpWebRequest.GetResponse() as HttpWebResponse;
                using (StreamReader stream = new StreamReader(webResponse.GetResponseStream()))
                {
                    //result = Newtonsoft.Json.JsonConvert.DeserializeObject<Result>(stream.ReadToEnd());
                    richTextBox1.Text += stream.ReadToEnd();
                }
                httpWebRequest = null;
                webResponse.Close();
                webResponse = null;
            }
            catch { }
            //result.billInfo.consNo = consNo.ToString();
            //Write(result);




 C# 透過Win32取得滑鼠位置 GetCursorPos

        [DllImport("User32")]
        internal extern static bool GetCursorPos(out MousePoint point);

        internal struct MousePoint {
            public int x;
            public int y;
        };

        public Form1()
        {
            InitializeComponent();
            MousePoint point;
            GetCursorPos(out point);
            Console.WriteLine(point.x + "," + point.y);
        }
    }
}


移動鼠標



        [DllImport("User32")]
        public static extern void mouse_event(
            int dwFlags,
            int dx,
            int dy,
            int dwData,
            int dwExtraInfo
        );

        const int MOUSEEVENTF_ABSOLUTE = 0x8000;
        const int MOUSEEVENTF_LEFTDOWN = 0x0002;
        const int MOUSEEVENTF_LEFTUP = 0x0004;
        const int MOUSEEVENTF_MIDDLEDOWN = 0x0020;
        const int MOUSEEVENTF_MIDDLEUP = 0x0040;
        const int MOUSEEVENTF_MOVE = 0x0001;
        const int MOUSEEVENTF_RIGHTDOWN = 0x0008;
        const int MOUSEEVENTF_RIGHTUP = 0x0010;
        const int MOUSEEVENTF_WHEEL = 0x0800;
        const int MOUSEEVENTF_XDOWN = 0x0080;
        const int MOUSEEVENTF_XUP = 0x1000;
        const int MOUSEEVENTF_HWHEEL = 0x01000;



            int dx = 100;
            int dy = 100;
            mouse_event(MOUSEEVENTF_MOVE, dx, dy, 0, 0);
        
        


　/// 應用程序的主入口點。

　///

　[STAThread]

　static void Main(string[] args)

　{

　　if(args.Length==1)

　　　if(args[0].Substring(0,2).Equals("/c"))

　　　{

　　　　MessageBox.Show("沒有設置項功能","C# Screen Saver");

　　　　Application.Exit();

　　　}

　　　else if(args[0]=="/s")

　　　Application.Run(new screen());

　　else if(args[0]=="/a")

　　{

　　　MessageBox.Show("沒有口令功能","C# Screen saver");

　　　Application.Exit();

　　}

　　else

　　Application.Run(new screen());

　}
　　最後運行該程序，把screen_saver.exe改為screen_saver.scr，拷入Windows系統目錄中，這樣就可以運行該屏幕保護程序。

        
        



    .NET 4.6 內建支援且預設使用 TLS 1.2
    .NET 4.5 內建支援，但需透過 ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12 設為預設協定
    .NET 4 本身不支援，但安裝 .NET 4.5 後即可使用 TLS 1.2，指定 TLS 1.2 的寫法為 ServicePointManager.SecurityProtocol = (SecurityProtocolType)3072; 
    


            //WebBrowser 轉 RichTextBox
            
            string testString = @"<FONT face=Verdana><FONT face=Verdana> 
<P><FONT face=Verdana>測試內容：</FONT></P> 
<P><FONT face=Verdana>    哈哈       <BR>    吃飯啦<BR>     下班啦   <BR>     回家<BR>     睡覺       </FONT></P> 
<P><FONT face=Verdana>呵呵呵<BR>神馬</FONT></P> 
<P><FONT face=Verdana><BR></FONT> </P></FONT> 
<P><FONT face=Verdana><BR></FONT> </P></FONT>";

            webBrowser1.DocumentText = testString;
            webBrowser1.Document.Write(testString);

            webBrowser1.Refresh();

            using (WebBrowser webBrowser = new WebBrowser())
            {
                webBrowser.Visible = false;

                webBrowser.DocumentText = testString;

                webBrowser.Document.Write(testString);

                richTextBox1.Text = webBrowser.Document.Body.OuterText;
            } 



\\圖片格式轉換



vcs helper的  根據副檔名 決定檔案儲存格式

        public void SaveBitmapUsingExtension(Bitmap bm, string filename)
        {
            string extension = Path.GetExtension(filename);
            switch (extension.ToLower())
            {
                case ".bmp":
                    bm.Save(filename, ImageFormat.Bmp);
                    break;
                case ".exif":
                    bm.Save(filename, ImageFormat.Exif);
                    break;
                case ".gif":
                    bm.Save(filename, ImageFormat.Gif);
                    break;
                case ".jpg":
                case ".jpeg":
                    bm.Save(filename, ImageFormat.Jpeg);
                    break;
                case ".png":
                    bm.Save(filename, ImageFormat.Png);
                    break;
                case ".tif":
                case ".tiff":
                    bm.Save(filename, ImageFormat.Tiff);
                    break;
                default:
                    throw new NotSupportedException(
                        "Unknown file extension " + extension);
            }
        }




        public void ImageFormatter(string sourcePath, string filename, string format) {
            System.Drawing.Bitmap bitmap = new System.Drawing.Bitmap(sourcePath);
            switch (format.ToLower()) {
                case "bmp":
                    bitmap.Save(filename, ImageFormat.Bmp);
                    break;
                case "emf":
                    bitmap.Save(filename, ImageFormat.Emf);
                    break;
                case "gif":
                    bitmap.Save(filename, ImageFormat.Gif);
                    break;
                case "ico":
                    bitmap.Save(filename, ImageFormat.Icon);
                    break;
                case "jpg":
                    bitmap.Save(filename, ImageFormat.Jpeg);
                    break;
                case "png":
                    bitmap.Save(filename, ImageFormat.Png);
                    break;
                case "tif":
                    bitmap.Save(filename, ImageFormat.Tiff);
                    break;
                case "wmf":
                    bitmap.Save(filename, ImageFormat.Wmf);
                    break;
                default: throw new Exception("無法轉換此格式！");
            }
        }

    


 
\\圖片格式轉換

        public void ImageFormatter(string sourcePath, string distationPath, string format) {
            System.Drawing.Bitmap bitmap = new System.Drawing.Bitmap(sourcePath);
            switch (format.ToLower()) {
                case "bmp":
                    bitmap.Save(distationPath, System.Drawing.Imaging.ImageFormat.Bmp);
                    break;
                case "emf":
                    bitmap.Save(distationPath, System.Drawing.Imaging.ImageFormat.Emf);
                    break;
                case "gif":
                    bitmap.Save(distationPath, System.Drawing.Imaging.ImageFormat.Gif);
                    break;
                case "ico":
                    bitmap.Save(distationPath, System.Drawing.Imaging.ImageFormat.Icon);
                    break;
                case "jpg":
                    bitmap.Save(distationPath, System.Drawing.Imaging.ImageFormat.Jpeg);
                    break;
                case "png":
                    bitmap.Save(distationPath, System.Drawing.Imaging.ImageFormat.Png);
                    break;
                case "tif":
                    bitmap.Save(distationPath, System.Drawing.Imaging.ImageFormat.Tiff);
                    break;
                case "wmf":
                    bitmap.Save(distationPath, System.Drawing.Imaging.ImageFormat.Wmf);
                    break;
                default: throw new Exception("無法轉換此格式！");
            }
        }






            Bitmap bitmap1 = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bitmap1);

            //重置背景顏色,可以自定義
            g.Clear(Color.White);

            g.SmoothingMode = SmoothingMode.AntiAlias;//消除鋸齒
            g.CompositingQuality = CompositingQuality.HighQuality;
            g.InterpolationMode = InterpolationMode.HighQualityBicubic;




//c#中接收16進制串口數據(com), 在textbox顯示

static int buffersize = 18;   //十六進制數的大小（假設為6Byte）
byte[] buffer = new Byte[buffersize];   //創建緩沖區

private void button1_Click(object sender, EventArgs e)
{
    serialPort1.Read(buffer, 0, buffersize);
    string ss;
    ss = byteToHexStr(buffer); //用到函數byteToHexStr
    textBox2.Text = ss;
    serialPort1.Close();
    MessageBox.Show("數據接收成功！", "系統提示");
}

//字節數組轉16進制字符串
public static string byteToHexStr(byte[] bytes)
{
    string returnStr = "";
    if (bytes != null)
    {
        for (int i = 0; i < bytes.Length; i++)
        {
            returnStr += bytes[i].ToString("X2");
        }
    }
    return returnStr;
}

//========================================================================================


            Image<Bgr, byte> image1 = capture.QueryFrame();
            image1 = capture.QueryFrame();
            ImageViewer viewer = new ImageViewer();
            viewer.Image = image1;
            viewer.ShowDialog();




cap.SetCaptureProperty(Emgu.CV.CvEnum.CAP_PROP.CV_CAP_PROP_FOURCC, 4);


int codec = Emgu.CV.CvInvoke.CV_FOURCC('P', 'I', 'M', '1');







VideoFileWriter	
AForge用的 vcs_VideoFileWriter OK 但是在WebCam上有些問題 總是Memory不足


VideoWriter
EMGU用的 在sugar使用OK

 


            if (File.ReadAllText("setting.txt") != null)
            {
                folderPath = File.ReadAllText("setting.txt");
            }
            else
            {

                    File.WriteAllText(@"setting.txt", folderPath);





測試out 語法

C#通過POP3協議驗證 Email 賬號

static bool ValidateEmailAccount(string server, int port, string userName, string password, out string ErrorMessage) 
        { 
            ErrorMessage = ""; 
            //create a tcp connection 
            TcpClient _server = new TcpClient(server, port); 
            //prepare  
            NetworkStream netStream = _server.GetStream(); 
            StreamReader reader = new StreamReader(_server.GetStream()); 
            if (!reader.ReadLine().Contains("+OK")) 
           { 
                //失敗 
                ErrorMessage = "server鏈接失敗"; 
                return false; 
            } 
            string data; 
            byte[] charData; 
            string CRLF = "\r\n"; 
            //login 
            data = "USER " + userName + CRLF; 
            charData = Encoding.ASCII.GetBytes(data); 
            netStream.Write(charData, 0, charData.Length); 
            if (!reader.ReadLine().Contains("+OK")) 
            { 
                //賬戶錯誤 
                ErrorMessage = "賬戶錯誤"; 
                return false; 
            } 
            data = "PASS " + password + CRLF; 
            charData = Encoding.ASCII.GetBytes(data); 
            netStream.Write(charData, 0, charData.Length); 
            if (!reader.ReadLine().Contains("+OK")) 
            { 
                //密碼錯誤 
                ErrorMessage = "密碼錯誤"; 
                return false; 
            } 
            return true; 
        } 
 調用

string errorMessage; 

bool isContains = ValidateEmailAccount("pop3.163.com", 110, "wise_sandy@XXX.com", "************", out errorMessage); 

 

Console.WriteLine(isContains ? "用戶存在" : errorMessage); 

 






string thumb = fpath + fn.Replace(CodecExtension, ".jpg");


                /*
                Supported Formats:
                    Raw	        Raw (uncompressed) video.
	                MPEG2	    MPEG-2 part 2.
	                FLV1	    Flash Video (FLV) / Sorenson Spark / Sorenson H.263.
	                H263P	    H.263+ / H.263-1998 / H.263 version 2.
	                MSMPEG4v3	MPEG-4 part 2 Microsoft variant version 3.
	                MSMPEG4v2	MPEG-4 part 2 Microsoft variant version 2.
	                WMV2	    Windows Media Video 8.
	                WMV1	    Windows Media Video 7.
	                MPEG4	    MPEG-4 part 2.
	                Default	    Default video codec, which FFmpeg library selects for the specified file format.
                    missing : H264        
                */



            // as long as we're recording
            // we dequeue the BitMaps waiting in the Queue and write them to the file
            while (IsRecording)
            {
                if (frames.Count > 0)
                {
                    Bitmap bmp = frames.Dequeue();
                    writer.WriteVideoFrame(bmp);
                    bmp.Dispose();
                }
            }
            writer.Close();



                                using (MemoryStream ms = new MemoryStream(solImage.ImageData))
                                using (Bitmap bitmap = (Bitmap)Image.FromStream(ms))
                                {
                                    if (bitmap.Width == videoWriter.Width && bitmap.Height == videoWriter.Height)
                                    {
                                        using (Bitmap newBitmap = new Bitmap(bitmap.Width, bitmap.Height))
                                        using (Graphics g = Graphics.FromImage(newBitmap))
                                        {
                                            g.DrawImage(bitmap, 0, 0);
                                            g.DrawString(String.Format("{0} - Sol: {1}", solImage.Cam, solImage.Sol), new Font(FontFamily.GenericSansSerif, 30, FontStyle.Bold), Brushes.White, new PointF(10, 10));

                                            for (int i = 0; i < 4; i++)
                                            {
                                                videoWriter.WriteVideoFrame(newBitmap);
                                            }



Example #25
0
File: Camera.cs Project: alienwow/CSharpProjects

        private void Video_Player_NewFrame(object sender, ref Bitmap image)
        {
            //录像
            Graphics g = Graphics.FromImage(image);

            SolidBrush drawBrush = new SolidBrush(Color.Red);

            Font drawFont = new Font("Arial", 4, FontStyle.Italic, GraphicsUnit.Millimeter);
            int xPos = image.Width - (image.Width - 15);
            int yPos = 10;
            //写到屏幕上的时间
            drawDate = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss");

            g.DrawString(drawDate, drawFont, drawBrush, xPos, yPos);
            if (!Directory.Exists(videoPath))
                Directory.CreateDirectory(videoPath);

            //开始录像
            if (createNewFile)
            {
                //videoFileName = DateTime.Now.ToString("yyyy-MM-dd-HH-mm-ss") + ".flv";
                videoFileName = "wuwh.flv";
                videoFileFullPath = videoPath + "/" + videoFileName;
                createNewFile = false;
                if (videoWriter != null)
                {
                    videoWriter.Close();
                    videoWriter.Dispose();
                }
                videoWriter = new VideoFileWriter();
                //这里必须是全路径，否则会默认保存到程序运行根据录下了
                videoWriter.Open(videoFileFullPath, image.Width, image.Height, frameRate, VideoCodec.FLV1);
                videoWriter.WriteVideoFrame(image);

                VideoFileSource videoFileSource = new VideoFileSource(videoFileFullPath);

            }
            else
            {
                videoWriter.WriteVideoFrame(image);
            }
        }









Image ImgOrnek = (Image.FromFile(pic_filename) as Bitmap).Clone() as Image;
int width = ImgOrnek.Width;
int height = ImgOrnek.Height;
ImgOrnek.Dispose();
VideoFileWriter writer = new VideoFileWriter();
writer.Open(filename, width, height, this.Videofps, VideoCodec.MPEG4);




                image = (Bitmap)Image.FromFile("C:\\Users\\Halil\\Desktop\\newframes\\image" + i + ".jpg");
                writer.WriteVideoFrame(image);
                
                




要輸入帳號密碼的 WebClient
                        // Upload the file to the server.
                        WebClient myWebClient = new WebClient();
                        NetworkCredential myCredentials = new NetworkCredential("snijhof", "MKD7529s09");
                        myWebClient.Credentials = myCredentials;
                        byte[] responseArray = myWebClient.UploadFile("ftp://student.aii.avans.nl/GRP/42IN11EWd/Videos/" + fileName, filePath);

                        String temp = Encoding.ASCII.GetString(responseArray);

                        // Decode and display the response.
                        Console.WriteLine("\nResponse Received.The contents of the file uploaded are:\n{0}", Encoding.ASCII.GetString(responseArray));


            textBox1.ShortcutsEnabled = false;   // 不啟用快速鍵, 限制 TextBox 上不使用快速鍵與滑鼠右鍵表單
            textBox5.ShortcutsEnabled = false;   // 不啟用快速鍵, 限制 TextBox 上不使用快速鍵與滑鼠右鍵表單


        private void textBox1_KeyPress(object sender, KeyPressEventArgs e)
        {
            // 限制 TextBox只能輸入十六進位碼、Backspace、Enter
            // e.KeyChar == (Char)48 ~ 57 -----> 0~9
            // e.KeyChar == (Char)8 -----------> Backspace
            // e.KeyChar == (Char)13-----------> Enter            
            if ((e.KeyChar >= (Char)48 && e.KeyChar <= (Char)57) || ((e.KeyChar >= 'A') && (e.KeyChar <= 'F')) || ((e.KeyChar >= 'a') && (e.KeyChar <= 'f')) || (e.KeyChar == (Char)13) || (e.KeyChar == (Char)8))
            {
                e.Handled = false;
            }
            else
            {
                e.Handled = true;
            }
        }


        private void textBox5_KeyPress(object sender, KeyPressEventArgs e)
        {
            // 限制 TextBox只能輸入十進位碼、Backspace、Enter
            // e.KeyChar == (Char)48 ~ 57 -----> 0~9
            // e.KeyChar == (Char)8 -----------> Backspace
            // e.KeyChar == (Char)13-----------> Enter            
            if ((e.KeyChar >= (Char)48 && e.KeyChar <= (Char)57) || (e.KeyChar == (Char)13) || (e.KeyChar == (Char)8))
            {
                e.Handled = false;
            }
            else
            {
                e.Handled = true;
            }
        }
        
        
        
        public double hex2dec(string hex_data)
        {
            byte value = 0;
            double dec_value = 0;
            //MessageBox.Show("data = " + hex_data);
            for (int i = 0; i < hex_data.Length; i++)
            {
                if ((hex_data[i] >= (Char)48 && hex_data[i] <= (Char)57))
                {
                    value = (byte)(hex_data[i] - 48);

                }
                else if ((hex_data[i] >= 'A') && (hex_data[i] <= 'F'))
                {
                    value = (byte)(hex_data[i] - 'A' + 10);
                }
                else if ((hex_data[i] >= 'a') && (hex_data[i] <= 'f'))
                {
                    value = (byte)(hex_data[i] - 'a' + 10);
                }
                dec_value = dec_value * 16 + value;
                //MessageBox.Show("data : " + hex_data[i] + " value : " + value);
            }
            return dec_value;
        }
        
        
        


有一點注意事項就是在你關閉From2的時候一定要在關閉窗體前把主程序終止,也就是在Form2_FormClosed事件中執行Application.Exit();


webBrowser1 空白頁
this.webBrowser1.Navigate("about:blank");


<a> 超連結 如何取得文字 :

Name = htmlNode.InnerText

<a> 超連結 如何取得連結 :

Url = htmlNode.GetAttributeValue("href", "")








十六、運行時顯示自己定義的圖標：
//load icon and set to form
System.Drawing.Icon ico = new System.Drawing.Icon(@c: empapp.ico);
this.Icon = ico;





----------------vcs +++ ST----------------

找一些標準icon  放在vcs裏
開啟檔案 儲存檔案 新增檔案 關閉檔案........


vcs_test_all_00_Usually +
開新表單範例



usually + 繪圖基本範例
bitmap -> graphics -> pictureBox1



vcs_MyToolbox+
日曆功能
年月日星期
農曆

vcs_HtmlAgility+
氣象 水 電 空氣 covid-19
博客來

vcs_MyLibrary
1. 三角函數
2. 檔案屬性參數 檔案大小時間影片大小長度
3. drawcircle fillcircle
WebCam Comport使用
若要讀取info 回傳一個string即可

MyPlayer3
		1. 取消最上層顯示
4. 做個地方可以做筆記, 筆記可存檔

操作類:
	按ctrl+上下	小量的加減速
	按shift+上下	大量的加減速
	Backspace	跳到檔頭
	PageUp/PageDown 同資料夾、依檔名排序的上一個、下一個檔案
	
----------------vcs +++ SP----------------



HtmlAgilityPack 訊息


            WebClient wc = new WebClient();
            wc.BaseAddress = "http://www.juedui100.com/";
            wc.Encoding = Encoding.UTF8;
            HtmlAgilityPack.HtmlDocument doc = new HtmlAgilityPack.HtmlDocument();
            string html = wc.DownloadString("aaaa.html");
            doc.LoadHtml(html);
            HtmlNode node = doc.DocumentNode.SelectSingleNode("/html/body/div[4]/div[1]/div[2]/ul[1]");     //根据XPath查找节点，跟XmlNode差不多
            Console.WriteLine(node.InnerText);  //输出节点内容      年龄：21～30之间 婚史：未婚 ......      与InnerHtml的区别在于，它不会输出HTML代码
            Console.WriteLine(node.InnerHtml);  //输出节点Html <li>年龄：21～30之间</li> <li>婚史：未婚</li> ....
            Console.WriteLine(node.Name);       //输出 ul    Html元素名 




Name　　　　　　　　　　　　　　  Html元素名
Id　　　　　　　　　　　　　　　　 获取该节点的Id属性
InnerHtml　　　　　　　　　　　　 获取该节点的Html代码
InnerText　　　　　　　　　　　　 获取该节点的内容，与InnerHtml不同的地方在于它会过滤掉Html代码，而InnerHtml是连Html代码一起输出
NodeType　　　　　　　　　　　　  获取该节点的节点类型




静态属性

public static Dictionary<string, HtmlElementFlag> //ElementsFlags;获取集合的定义为特定的元素节点的特定行为的标志。表包含小写标记名称作为键和作为值的 HtmlElementFlags 组合 DictionaryEntry 列表。
public static readonly string HtmlNodeTypeNameComment;　　//获取一个注释节点的名称。实际上，它被定义为 '#comment
public static readonly string HtmlNodeTypeNameDocument;　  //获取文档节点的名称。实际上，它被定义为 '#document'
public static readonly string HtmlNodeTypeNameText;　　　　  //获取一个文本节点的名称。实际上，它被定义为 '#text'

二、属性

Attributes 　　　　　　　　　　　　获取节点的属性集合
ChildNodes　　　　　　　　　　　　获取子节点集合(包括文本节点)
Closed　　　　　　　　　　　　　　该节点是否已关闭(</xxx>)
ClosingAttributes　　　　　　　　  在关闭标签的属性集合
FirstChild　　　　　　　　　　　　  获取第一个子节点
HasAttributes　　　　　　　　　　  判断该节点是否含有属性
HasChildNodes　　　　　　　　　　判断该节点是否含有子节点
HasClosingAttributes　　　　　　  判断该节点的关闭标签是否含有属性(</xxx class="xxx">)
LastChild　　　　　　　　　　　　  获取最后一个子节点
Line　　　　　　　　　　　　　　　 获取该节点的开始标签或开始代码位于整个HTML源代码的第几行(行号)
LinePosition　　　　　　　　　　　 获取该节点位于第几列
NextSibling　　　　　　　　　　　　获取下一个兄弟节点
OriginalName　　　　　　　　　　　获取原始的未经更改的元素名
OuterHtml　　　　　　　　　　　　 整个节点的代码
OwnerDocument　　　　　　　　　节点所在的HtmlDocument文档
ParentNode　　　　　　　　　　　　获取该节点的父节点
PreviousSibling　　　　　　　　　　获取前一个兄弟节点
StreamPosition　　　　　　　　　　该节点位于整个Html文档的字符位置
XPath　　　　　　　　　　　　　　  根据节点返回该节点的XPath



http://bsubramanyamraju.blogspot.com/2019/03/htmlagilitypack-html-parsing-in.html
https://github.com/SubramanymRajuB/Xamarin.Forms/tree/master/HtmlParsing


c# - C#htmlagilitypack Node.InnerHTML不正确区分大小写，如何拉正确大小写 





  
  
  var response1 = await http.GetByteArrayAsync("http://www.nsfund.ir/news?"+link);
                String source1 = Encoding.GetEncoding("utf-8").GetString(response1, 0, response1.Length - 1);
                source1 = WebUtility.HtmlDecode(source1);
                HtmlDocument resultat1 = new HtmlDocument();
                resultat1.LoadHtml(source1);
               var val = resultat1.DocumentNode.SelectSingleNode("//div[@class='news_content_container']").InnerText;
               
               
               
               
               
               
               
               
               

            

dll檔案選sapi.dll

參考出現SpeechLib

引用要寫 using SpeechLib;
 
                SpeechVoiceSpeakFlags spFlags = SpeechVoiceSpeakFlags.SVSFlagsAsync;
                SpVoice voice = new SpVoice();
                
                    voice.Speak(this.textBox1.Text, spFlags);

            
            
            

可以錄影的那個webcam版本 x86可用的
用的AForge是比較舊的版本
目前會認版本
只能使用特定舊的AForge版本

要不要做一個極簡化AForge/EMGU版本的WebCam







1.對於那種明知道跨線程調用不會帶來錯誤的，可以設置Form控件不檢查跨線程調用錯誤，這樣就不報錯了。
在Form1構造方法中：
C#代碼 
CheckForIllegalCrossThreadCalls = false; 




2 C#圖像處理的基本方法

C#處理圖像有三種方法:像素法、內存法和指針法。
像素法應用GDI+中的方法,易於理解,方法簡單,但運行速度慢;
內存法把圖像復制到內存中,直接對內存中的數據進行處理,運行速度比像素法快得多,程序難度也不大;
指針法直接利用指針來對圖像進行處理,速度最快。

但C#建議不使用指針,因為使用指針,代碼不僅難以編寫和調試,而且無法利用CRL的內存類型安全檢查,不能發揮C#的特長。

下面介紹用內存法對圖像處理的基本方法。

首先在處理圖像的窗體類中定義一個字符串(圖像文件名)和一個Bitmap類型的數據成員(圖像對象),然後可以利用OpenFileDialog選擇圖像文件並讀取文件名,再使用Image.FromFile創建圖形對象。比如:


Image.FromFile可開啟影像檔:
 "*.jpg,*.jpeg,*.bmp,*.gif,*.ico,*.png,*.tif,*.wmf|*.jpg;*.jpeg;*.bmp;*.gif;*.ico;*.png;*.tif;*.wmf";

//--------------------------------------------------------------------------------------------------------------------------


//--------------------------------------------------------------------------------------------------------------------------

讀取文件到一個List

用法
// 讀取cs文件內容
                List<String> rcq = ReaderLine(e.FullName);
 // 遍歷cs文件代碼行
                foreach (String q in rcq)
                {
                    if (!StringHandle.isNote(q)) continue;// 判斷是否是注釋

                    string note = StringHandle.GetNoteValue(q);// 獲取注釋內容

                    if (string.IsNullOrWhiteSpace(note)) continue;
                    :
                    :

		}                
                
/// <summary>
        /// 讀取文件
        /// </summary>
        /// <param name="path"></param>
        /// <returns></returns>
        public List<String> ReaderLine(string path)
        {
            StreamReader sr = new StreamReader(path, Encoding.Default);
            List<String> lines = new List<string>();
            string line;
            while ((line = sr.ReadLine()) != null)
            {
                lines.Add(line);
            }
            sr.Close();
            return lines;
        }
        
//--------------------------------------------------------------------------------------------------------------------------


//--------------------------------------------------------------------------------------------------------------------------

                

//--------------------------------------------------------------------------------------------------------------------------






//============================================================================================================================






//============================================================================================================================





微軟 SAPI.SpVoice C# 使用方法 + 實例
http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/192842.html



//============================================================================================================================



List 與 DataTable的比較

綁定的顯示控件？
DataGridView??


List比較像陣列
DataTable可以加標題 比較像EXCEL表單




//============================================================================================================================


                
            //comport訊息
            if (serialPort2.IsOpen)
            {
                richTextBox1.Text += "BaudRate = " + serialPort2.BaudRate.ToString() + "\n";
                richTextBox1.Text += "StopBits = " + serialPort2.StopBits.ToString() + "\n";
                richTextBox1.Text += "DataBits = " + serialPort2.DataBits.ToString() + "\n";
                richTextBox1.Text += "Parity = " + serialPort2.Parity.ToString() + "\n";
                richTextBox1.Text += "ReadTimeout = " + serialPort2.ReadTimeout.ToString() + "\n";



            }



private PlayState _palystate = PlayState.Closed;

     public enum PlayState
     {
         Opne,
         Playing,
         Paused,
         Stopped,
         Closed,
         None,
         Error
     }
     
     


public class User  
{  
    private int userID = 0;  
  
    private string userName = string.Empty;  
  
    public int UserID  
    {  
        get  
        {  
            return this.userID;  
        }  
    }  
  
    public string UserName  
    {  
        get  
        {  
            return this.userName;  
        }  
    }  
  
    public User(int userID, string userName)  
    {  
        this.userID = userID;  
  
        this.userName = userName;  
    }  
}  

P2P，英文Peer-to-Peer的縮寫，中譯為對等互聯或點對點技術。


                saveFileDialog1.CreatePrompt = true;	//如果指定不存在的文件，提示允許創建該文件
                saveFileDialog1.OverwritePrompt = true;//如果用戶指定的文件名已存在，顯示警告


        				
//---Assembly 用法 ST-----------------------------------------------------------------------------------------------------------------------
       
using System.Reflection;
	Assembly asm = Assembly.GetExecutingAssembly();
	string name = asm.GetName().Name;
	richTextBox1.Text += "name : " + name + "\n";


private void AboutBox_Load(object sender, EventArgs e)
{
	AssemblyInfoClass myAssembly = new AssemblyInfoClass();
	labelProductName.Text = "產品名稱：" + myAssembly.Product;
	labelVersion.Text = "版本：" + myAssembly.Version;
	labelCopyright.Text = "版權宣告：" + myAssembly.Copyright;
	labelCompanyName.Text = "公司名稱：" + myAssembly.Company;
	textBoxDescription.Text = "細部描述：" +
	myAssembly.Description;
}

                string location = Assembly.GetExecutingAssembly().Location;
                string serviceFileName = location.Substring(0, location.LastIndexOf('\\')) + "\\" + serviceName + ".exe";

一、獲取程序集版本
label版本.Text = Assembly.GetExecutingAssembly().GetName().Version.ToString();





            //獲取本代碼所在的文件作為臨時文件，用於獲取屬性列表
            string tempFile = Assembly.GetExecutingAssembly().FullName;




C#讀取exe版本號

	using System.Reflection;
	using System.IO;
	...
	
	Assembly currentAssembly = Assembly.LoadFile(currentAssemblyPath);
	Assembly updatedAssembly = Assembly.LoadFile(updatedAssemblyPath);
	
	AssemblyName currentAssemblyName = currentAssembly.GetName();
	AssemblyName updatedAssemblyName = updatedAssembly.GetName();
	
	// 比較版本號
	if (updatedAssemblyName.Version.CompareTo(currentAssemblyName.Version) <= 0)
	{
	    // 不需要更新
	    return;
	}
	
	using System.Reflection;
	using System.IO;
	...
	
	AssemblyName currentAssemblyName = AssemblyName.GetAssemblyName(currentAssemblyPath);
	AssemblyName updatedAssemblyName = AssemblyName.GetAssemblyName(updatedAssemblyPath);
	
	// 比較版本
	if (updatedAssemblyName.Version.CompareTo(currentAssemblyName.Version) <= 0)
	{
	    // 不需要更新
	    return;
	}
	
	// 更新
	File.Copy(updatedAssemblyPath, currentAssemblyPath, true);
	

            
using System.Reflection;
            //取得 namespaceName
            string namespaceName = Assembly.GetExecutingAssembly().GetName().Name.ToString();

            richTextBox1.Text += namespaceName + "\n";

            richTextBox1.Text += Assembly.GetExecutingAssembly().Location + "\n";


一、獲取程序集版本
label版本.Text = Assembly.GetExecutingAssembly().GetName().Version.ToString();





使用資源檔的圖片

屬性/資源/加入資源/加入現有檔案/ 選取檔案 picture1.jpg
此時, Resources 會出現 picture1.jpg
點選picture1.jpg, 屬性
建置動作 改成 內嵌資源


using System.Reflection;    //for Assembly
using System.IO;    //for Stream

            Assembly asm = this.GetType().Assembly;
            Stream stream = asm.GetManifestResourceStream("vcs_test.Resources.picture1.jpg");
            this.BackgroundImage = new Bitmap(stream);






//---Assembly 用法 SP-----------------------------------------------------------------------------------------------------------------------




鼠標相關的事件大致有六種，分別是 ：
"MouseHover"、"MouseLeave"、"MouseEnter"、"MouseMove"、"MouseDown"和"MouseUp"。


對於上述的前三個事件，是用以下語法來定義的：
"組件名稱"."事件名稱"+= new System.EventHandler（"事件名稱"）；
下面是程序中具體實現代碼：
button1.MouseLeave += new Syetem.EvenHandler（button1_MLeave）；


其中，getSubNode為一方法，用於獲取子目錄，以創建目錄樹節點，參數：PathName為獲取的子目錄在此節點下創建子節點，參數isEnd：結束標志,true則結束。

private void getSubNode(TreeNode PathName,bool isEnd)

vcs_Splitter

然後，添加TreeView控件，命名為treeView，Dock屬性設為Left，再添加Splitter控件，同樣將Dock屬性設為Left。最後添加ListView控件，命名為listView，Dock屬性設為Fill。
　　　Splitter(用於允許用戶調整TreeView和ListView的大小)；




            //顯示詳細信息
            listView1.View = View.Details;

            //選中整行
            listView1.FullRowSelect = true;

            //顯示checkbox
            listView1.CheckBoxes = true;

                //添加項
                listView1.Items.Add(zhuxiang);

            if (listView1.SelectedItems.Count > 0)
            {
                MessageBox.Show(listView1.SelectedItems[0].Text);
            }

            string s = "";

            foreach (ListViewItem item in listView1.CheckedItems)
            {
                s += item.Text + "--";
            }

            MessageBox.Show(s);


        //實現控件中捕獲按鍵 只要補上這個函數就好
        protected override bool ProcessCmdKey(ref Message msg, Keys keyData)
        {
            const int WM_KEYDOWN = 0x100;
            const int WM_SYSKEYDOWN = 0x104;
            if ((msg.Msg == WM_KEYDOWN) || (msg.Msg == WM_SYSKEYDOWN))
            {
                switch (keyData)
                {
                    case Keys.Down:
                        this.Text = "向下鍵已經被捕捉";
                        break;
                    case Keys.Up:
                        this.Text = "向上鍵已經被捕捉";
                        break;
                    case Keys.Left:
                        this.Text = "向左鍵已經被捕捉";
                        break;
                    case Keys.Right:
                        this.Text = "向右鍵已經被捕捉";
                        break;
                    case Keys.Home:
                        this.Text = "Home 鍵已經被捕捉";
                        break;
                    case Keys.End:
                        this.Text = "End 鍵已經被捕捉";
                        break;
                }
            }
            return base.ProcessCmdKey(ref msg, keyData);
        }





停止一個線程

Thread.Sleep 方法能夠在一個固定周期類停止一個線程

thread.Sleep(); 
 
設定線程優先級
線程類中的ThreadPriority 屬性是用來設定一個ThreadPriority的優先級別。線程優先級別包括Normal, AboveNormal, BelowNormal, Highest, and Lowest幾種。
	
thread.Priority = ThreadPriority.Highest; 

掛起一個線程
調用線程類的Suspend()方法將掛起一個線程直到使用Resume()方法喚起她。在掛起一個線程起前應該判斷線程是否在活動期間。

if (thread.ThreadState = ThreadState.Running )
{
thread.Suspend();
} 

喚起一個線程

通過使用Resume()方法可以喚起一個被掛起線程。在掛起一個線程起前應該判斷線程是否在掛起期間，如果
線程未被掛起則方法不起作用。


if (thread.ThreadState = ThreadState.Suspended )
{
thread.Resume();
} 







//------------------------------------------------------


Thread.Join()用法的理解


指在一線程裡面調用另一線程join方法時，表示將本線程阻塞直至另一線程終止時再執行  
  比如  

 1using System;
 2
 3namespace TestThreadJoin
 4{
 5    class Program
 6    {
 7        static void Main()
 8        {
 9            System.Threading.Thread x = new System.Threading.Thread(new System.Threading.ThreadStart(f1));
10            x.Start();
11            Console.WriteLine("This is Main.{0}", 1);
12            x.Join();
13            Console.WriteLine("This is Main.{0}", 2);
14            Console.ReadLine();
15        }
16        static void f1()
17        {
18            System.Threading.Thread y = new System.Threading.Thread(new System.Threading.ThreadStart(f2));
19            y.Start();
20            y.Join();
21            Console.WriteLine("This is F1.{0}",1);
22        }
23
24        static void f2()
25        {
26            Console.WriteLine("This is F2.{0}", 1);
27        }
28    }
29}


這兒有三個線程在處理(包括主線程),大家可看看執行結果.
結果:
This is Main.1
This is F2.1
This is F1.1
This is Main.2

如果: 注釋//  x.Join();
結果:
This is Main.1
This is Main.2
This is F2.1
This is F1.1
 



EXIF，是英文Exchangeable Image File









哪些事需要快捷鍵??
全螢幕截圖
計算機
我的時鐘、倒數計時鐘、
Drap



vcs
非強制回應 Modeless
強制回應 Modal

非強制回應表單	Form2 f2 = new Form2();	f2.Show();

Form1關閉Form2   f2.Close();
Form1隱藏Form2   f2.Hide();


強制回應表單	Form2 f2 = new Form2();	f2.ShowDialog();
可以取得回應
if(f3.DialogResult == DialogREsult.OK)
  ....
  

        private void button12_Click(object sender, EventArgs e)
        {
            //html轉txt
            //http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/184774.html
        }

        /// C#過濾html標簽
        /// 用正則表達式來做html轉txt
        public static string Html2Text(string htmlStr)
        {
            if (String.IsNullOrEmpty(htmlStr))
            {
                return "";
            }
            string regEx_style = "<style[^>]*?>[\\s\\S]*?<\\/style>"; //定義style的正則表達式
            string regEx_script = "<script[^>]*?>[\\s\\S]*?<\\/script>"; //定義script的正則表達式
            string regEx_html = "<[^>]+>"; //定義HTML標簽的正則表達式
            htmlStr = Regex.Replace(htmlStr, regEx_style, "");//刪除css
            htmlStr = Regex.Replace(htmlStr, regEx_script, "");//刪除js
            htmlStr = Regex.Replace(htmlStr, regEx_html, "");//刪除html標記
            htmlStr = Regex.Replace(htmlStr, "\\s*|\t|\r|\n", "");//去除tab、空格、空行
            htmlStr = htmlStr.Replace(" ", "");
            htmlStr = htmlStr.Replace("\"", ""); //去除異常的引號" " "
            htmlStr = htmlStr.Replace("\"", ""); //去除異常的引號" " "
            return htmlStr.Trim();
        }


　　
            	//讀取一檔
                FileStream fs = new FileStream(targetPath, FileMode.Open, FileAccess.Read);
                BinaryReader br = new BinaryReader(fs);
                br.BaseStream.Seek(0, SeekOrigin.Begin); //將指針設到開頭
                while (br.BaseStream.Position < br.BaseStream.Length)
                {
                    try
                    {
                        Console.WriteLine(br.ReadString());
                    }
                    catch (EndOfStreamException e)
                    {
                        Console.WriteLine("已經到了結尾 {0}", e.ToString());
                    }
                }
                br.Close();
                fs.Close();


讀取網頁 回傳資料 看看是甚麼樣子 xml? html?
http://lbsyun.baidu.com/index.php?title=webapi/guide/webservice-geocoding

 
                     

使用icon
this.Icon = new Icon(@"C:\______test_files\_icon\唐.ico");


使用鼠標
this.Cursor = new Cursor(xxxxxx);





try by sugar
C#如何獲取遠程磁盤上的剩余空間
http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/191690.html



C# 條形碼操作【源碼下載】

http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/185924.html


網站的標識圖片怎麼修改？


放favicon.ico在網站更目錄或者單獨頁面用link標簽指定圖標也行

 <link rel="SHORTCUT ICON" href="/xxx/xx.ico"/>



C# 網頁抓取類

//--需要引用 using System.Net 以及 using System.IO;
private string GetContentFromUrll(string _requestUrl)
        {
            string _StrResponse ="";
            HttpWebRequest _WebRequest = ( HttpWebRequest )WebRequest.Create( _requestUrl );
            _WebRequest.Method = "GET";
            WebResponse _WebResponse = _WebRequest.GetResponse();
            StreamReader _ResponseStream = new StreamReader( _WebResponse.GetResponseStream(), Encoding.GetEncoding("gb2312"));
            _StrResponse = _ResponseStream.ReadToEnd();
            _WebResponse.Close(); 
            _ResponseStream.Close();
            return _StrResponse;        
        }
        

systemsystem
//獲取文件的版本信息:
FileVersionInfo myFileVersionInfo1 = FileVersionInfo.GetVersionInfo("D:\\TEST.DLL");
textBox1.Text="版本號: " + myFileVersionInfo1.FileVersion;


首先准備一個畫板:

創建一個畫板主要有3種方式:

A: 在窗體或控件的Paint事件中直接引用Graphics對象

B: 利用窗體或某個控件的CreateGraphics方法

C: 從繼承自圖像的任何對象創建Graphics對象



在C＃環境下的多態就是重載和覆寫。
在一個類中，兩個以上的方法有著相同的名字，不同的參數類型，但是返回值可以不相同，

覆寫就是子類為了實現某一個功能而重復定義父類的某個方法，覆寫方法比重載方法要更加嚴格：只有虛方法和抽象方法才可以被覆寫，同時覆寫時必須滿足一下幾個條件：相同的方法名字，參數列表和返回值類型，缺一不可。


　　18、把字符轉為數字，查代碼點，注意是單引號。

　　(int)'字符'

　　如：

Response.Write((int)'中'); //結果為中字的代碼：20013

　　19、把數字轉為字符，查代碼代表的字符：(char)代碼

　　如：

Response.Write((char)22269); //返回“國”字。

　　26、在字串左（或右）加空格或指定char字符，使字串達到指定長度：PadLeft()、PadRight() ，如：

＜%
string str1="中國人";
str1=str1.PadLeft(10,'1'); //無第二參數為加空格
Response.Write(str1); //結果為“1111111中國人” ， 字串長為10
%＞

　　C#用多種修飾符來表達類的不同性質。根據其保護級C#的類有五種不同的限制修飾符：
    public可以被任意存取；
    protected只可以被本類和其繼承子類存取；
    internal只可以被本組合體（Assembly）內所有的類存取，組合體是C#語言中類被組合後的邏輯單位和物理單位，其編譯後的文件擴展名往往是“.DLL”或“.EXE”。
    protected internal唯一的一種組合限制修飾符，它只可以被本組合體內所有的類和這些類的繼承子類所存取。
    private只可以被本類所存取。
    

　　如果不是嵌套的類，命名空間或編譯單元內的類只有public和internal兩種修飾。

　　new修飾符只能用於嵌套的類，表示對繼承父類同名類型的隱藏。

abstract用來修飾抽象類，表示該類只能作為父類被用於繼承，而不能進行對象實例化。抽象類可以包含抽象的成員，但這並非必須。abstract不能和new同時用。

sealed用來修飾類為密封類，阻止該類被繼承。同時對一個類作abstract和sealed的修飾是沒有意義的，也是被禁止的。




	
	







//C# 播放聲音
﻿﻿

1.播放系統事件聲音
　　 System.Media.SystemSounds.Asterisk.Play();
　　 System.Media.SystemSounds.Beep.Play();
　　 System.Media.SystemSounds.Exclamation.Play();
　　 System.Media.SystemSounds.Hand.Play();
　　 System.Media.SystemSounds.Question.Play();

2.使用System.Media.SoundPlayer播放.wav格式聲音
　　 SoundPlayer player = new SoundPlayer();
player.SoundLocation = Application.StartupPath + "\\" + "sounds/WallHit.wav";
player.Load(); //同步加載聲音
player.Play(); //啟用新線程播放
//player.PlayLooping(); //循環播放模式
//player.PlaySync(); //UI線程播放

3.利用Windows Media Player

加載COM組件:ToolBox->Choose Items->COM Components->Windows Media Player

把Windows Media Player控件拖放到Winform窗體中，把axWindowsMediaPlayer1中URL屬性設置為MP3或是AVI的文件路徑。


4.MCI Command String多媒體設備的程序接口

using System.Runtime.InteropServices;
　　public static uint SND_ASYNC = 0x0001;
　　public static uint SND_FILENAME = 0x00020000;
　　[DllImport("winmm.dll")]
　　public static extern uint mciSendString(string lpstrCommand,
　　string lpstrReturnString, uint uReturnLength, uint hWndCallback);
　　public void Play()
　　{
　　　　mciSendString(@"close temp_alias", null, 0, 0);
　　　　mciSendString(@"open " "路徑.mp3"" alias temp_alias", null, 0, 0);
　　　　mciSendString("play temp_alias repeat", null, 0, 0);
　　}

關於MCI Command String多媒體設備的程序接口的詳細資料，可以參看http://blog.csdn.net/psongchao/article/details/1487788

  
  



用WMI查serial port可否知道是ims的comport，
若可以知道，直接連線看看～～～




ListView添加內容範例
        /// <summary>
        /// listview1 顯示搜索主機
        /// </summary>
        private void listLanHost()
        {
            listView1.View = View.List;

            ListViewItem aa;
            for (int i = 0; i < 255; i++)
            {
                if (LanHost[i, 0] != "")
                {
                    aa = new ListViewItem();
                    aa.Text = LanHost[i, 1];
                    aa.Tag = LanHost[i, 0];
                    listView1.Items.Add(aa);
                }
            }

        }


        				
//--------------------------------------------------------------------------------------------------------------------------







Graphics g = Graphics.FromImage(ThumbNail);

// 設置畫布的描繪質量
g.CompositingQuality = CompositingQuality.HighSpeed;
g.CompositingQuality = CompositingQuality.HighQuality;
g.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.HighQuality;
g.SmoothingMode = SmoothingMode.HighSpeed;
g.SmoothingMode = SmoothingMode.AntiAlias;	//反鋸齒
g.SmoothingMode = SmoothingMode.HighQuality;
g.InterpolationMode = InterpolationMode.HighQualityBicubic;
g.InterpolationMode = InterpolationMode.HighQualityBilinear;




//--------------------------------------------------------------------------------------------------------------------------




drawdraw

　　本文將介紹在．Net中如何使用代碼畫圖表，就像用MS Excel產生的圖表一樣。也可以畫像DataGrid一樣的表格。
　　在．Net中，微軟給我們提供了畫圖類（System.Drawing.Imaging），在該類中畫圖的準系統都有。比如：直線、折線、矩形、多邊形、橢圓形、扇形、曲線等等，因此一般的圖形都可以直接通過代碼畫出來。接下來介紹一些畫圖函數：
Bitmap bMap=new Bitmap(500,500)　//定義映像大小；
bMap.Save(Stream,ImageCodecInfo) //將映像儲存到指定的輸出資料流；
Graphics gph //定義或建立GDI繪圖對像；
PointF cPt　//定義二維平面中x,y座標；
DrawString(string,Font,Brush,PonitF) //用指定的Brush和Font對像在指定的矩形或點繪製指定的字串；
DrawLine(Pen,Ponit,Ponit) //用指定的筆(Pen)對像繪製指定兩點之間直線；
DrawPolygon(Pen,Ponit[]) //用指定的筆(Pen)對像繪製指定多邊形，比如三角形，四邊形等等；
FillPolygon(Brush,Ponit[]) //用指定的刷子(Brush)對像填充指定的多邊形；
DrawEllipse(Pen,x,y,Width,Height) //用指定的筆繪製一個邊框定義的橢圓；
FillEllipse(Brush,x,y,Width,Height) //用指定的刷子填充一個邊框定義的橢圓；
DrawRectangle(Pen,x,y,Width,Height) //用指定的筆繪製一個指定座標點、寬度、高度的矩形；
DrawPie(Pen,x,y,Width,Height,startAngle,sweepAngle) //用指定的筆繪製一個指定座標點、寬度、高度以及兩條射線組成的扇形；





    




//--------------------------------------------------------------------------------------------------------------------------






       

MemoryStream 可以seek
                    MemoryStream ms = new MemoryStream();
                    XmlWt = new XmlTextWriter(ms, Encoding.Unicode);
                    //獲取ds中的數據
                    dt.WriteXml(XmlWt);
                    int count = (int)ms.Length;
                    byte[] temp = new byte[count];
                    ms.Seek(0, SeekOrigin.Begin);
                    ms.Read(temp, 0, count);
                    //返回Unicode編碼的文本

                        ms.Close();
                        ms.Dispose();
                        
     MemoryStream stream = null;
     XmlTextWriter writer = null;
     try
     {
         stream = new MemoryStream();
         writer = new XmlTextWriter(stream, Encoding.Default);
         xmlDS.WriteXml(writer);
         int count = (int)stream.Length;
         byte[] arr = new byte[count];
         stream.Seek(0, SeekOrigin.Begin);
         stream.Read(arr, 0, count);
         UTF8Encoding utf = new UTF8Encoding();
         return utf.GetString(arr).Trim();
         

         /// <summary>
        /// 實現bitmap到ico的轉換
        /// </summary>
        /// <param name="bitmap">原圖</param>
        /// <returns>轉換後的指定大小的圖標</returns>
        private Icon ConvertBitmap2Ico(Bitmap bitmap)
        {
            Bitmap icoBitmap = new Bitmap(bitmap, size);//創建制定大小的原位圖

            //獲得原位圖的圖標句柄
            IntPtr hIco = icoBitmap.GetHicon();
            //從圖標的指定WINDOWS句柄創建Icon
            Icon icon = Icon.FromHandle(hIco);

            return icon;
        }
        
        

    
            

先使用無符號字節數組存放數據庫對應的數據集中表的image類型字段的值。例如：

byte[] bytes= (byte[]) image類型字段值



//在C#中調用windows API函數

using System.Runtime.InteropServices;

/// <summary>
/// 打開和關閉CD托盤.
/// </summary>
[DllImport("winmm.dll" , EntryPoint="mciSendString", CharSet=CharSet.Auto)]
public static extern int mciSendString (string lpstrCommand,string lpstrReturnstring ,int uReturnLength,int hwndCallback);

/// <summary>
/// 顯示和隱藏鼠標指針.
/// </summary>
[DllImport("user32.dll", EntryPoint="ShowCursor", CharSet=CharSet.Auto)]
public static extern int ShowCursor(int bShow);

/// <summary>
/// 清空回收站.
/// </summary>
[DllImport("shell32.dll", EntryPoint="SHEmptyRecycleBin", CharSet=CharSet.Auto)]
public static extern long SHEmptyRecycleBin(IntPtr hwnd, string pszRootPath, long dwFlags);

/// <summary>
/// 打開浏覽器
/// </summary>
[DllImport("shell32.dll", EntryPoint="ShellExecute", CharSet=CharSet.Auto)]
public static extern int ShellExecute(IntPtr hwnd,string lpOperation,string lpFile,string lpParameters,string lpDirectory,int nShowCmd);

/// <summary>
/// 最大化窗口，最小化窗口，正常大小窗口；
/// </summary>
[DllImport("user32.dll", EntryPoint="ShowWindow", CharSet=CharSet.Auto)]
public static extern int ShowWindow(IntPtr hwnd,int nCmdShow);



//打開CD托盤：
long lngReturn = ApiCalls.mciSendString("set CDAudio door open", strReturn, 127, 0);
//關閉CD托盤：
long lngReturn = ApiCalls.mciSendString("set CDAudio door closed", strReturn, 127, 0);
//在應用程序窗體中顯示鼠標指針：
ApiCalls.ShowCursor(1);
//在應用程序窗體中隱藏鼠標指針：
ApiCalls.ShowCursor(0);
//清空回收站：
ApiCalls.SHEmptyRecycleBin(Form.ActiveForm.Handle,"",0x00000000);
//打開浏覽器窗口，textBox1.Text中表示要訪問的URL地址：
Long lngReturn= ApiCalls.ShellExecute(Form.ActiveForm.Handle,"Open",textBox1.Text,"","",1);
//最大化窗口：
ApiCalls.ShowWindow(Form.ActiveForm.Handle,3);
//最小化窗口：
ApiCalls.ShowWindow(Form.ActiveForm.Handle,2);
//恢復正常大小窗口：
ApiCalls.ShowWindow(Form.ActiveForm.Handle,1);
 


ADO.Net方面的：
八、連接Access數據庫：
using System;
using System.Data;
using System.Data.OleDb;

class TestADO
{
    static void Main(string[] args)
    {
        string strDSN = Provider=Microsoft.Jet.OLEDB.4.0;Data Source=c:\test.mdb;
        string strSQL = SELECT * FROM employees ;

        OleDbConnection conn = new OleDbConnection(strDSN);
        OleDbCommand cmd = new OleDbCommand( strSQL, conn );
        OleDbDataReader reader = null;
        try
        {
            conn.Open();
            reader = cmd.ExecuteReader();
            while (reader.Read() )
            {
                Console.WriteLine(First Name:{0}, Last Name:{1}, reader[FirstName], reader[LastName]);
            }
        }
        catch (Exception e)
        {
            Console.WriteLine(e.Message);
        }
        finally
        {
            conn.Close();
        }
    }
} 

九、連接SQL Server數據庫：
using System;
using System.Data.SqlClIEnt;

public class TestADO
{
    public static void Main()
    {
        SqlConnection conn = new SqlConnection(Data Source=localhost; Integrated Security=SSPI; Initial Catalog=pubs);

SqlCommand  cmd = new SqlCommand(SELECT * FROM employees, conn);
        try
        {        
            conn.Open();

            SqlDataReader reader = cmd.ExecuteReader();            
            while (reader.Read())
            {
                Console.WriteLine(First Name: {0}, Last Name: {1}, reader.GetString(0), reader.GetString(1));
            }
        
            reader.Close();
            conn.Close();
        }
        catch(Exception e)
        {
            Console.WriteLine(Exception Occured -->> {0},e);
        }        
    }
}

十、從SQL內讀數據到XML：
using System;
using System.Data;
using System.XML;
using System.Data.SqlClIEnt; 
using System.IO; 

public class TestWriteXML
{ 
    public static void Main()
    { 

        String strFileName=c:/temp/output.XML;

        SqlConnection conn = new SqlConnection(server=localhost;uid=sa;pwd=;database=db);

        String strSql = SELECT FirstName, LastName FROM employees; 

        SqlDataAdapter adapter = new SqlDataAdapter(); 

        adapter.SelectCommand = new SqlCommand(strSql,conn);

        // Build the DataSet
        DataSet ds = new DataSet();

        adapter.Fill(ds, employees);

        // Get a FileStream object
        FileStream fs = new FileStream(strFileName,FileMode.OpenOrCreate,FileAccess.Write);

        // Apply the WriteXml method to write an XML document
        ds.WriteXML(fs);

        fs.Close();

    }
}

十一、用ADO添加數據到數據庫中：
using System;
using System.Data;   
using System.Data.OleDb;   

class TestADO
{  
    static void Main(string[] args)  
{  
        string strDSN = Provider=Microsoft.Jet.OLEDB.4.0;DataSource=c: est.mdb;  
        string strSQL = INSERT INTO Employee(FirstName, LastName) VALUES(''FirstName'', ''LastName'') ;  
                   
        // create Objects of ADOConnection and ADOCommand   
        OleDbConnection conn = new OleDbConnection(strDSN);  
        OleDbCommand cmd = new OleDbCommand( strSQL, conn );  
        try  
        {  
            conn.Open();  
            cmd.ExecuteNonQuery();  
        }  
        catch (Exception e)  
        {  
            Console.WriteLine(Oooops. I did it again: {0}, e.Message);  
        }  
        finally  
        {  
            conn.Close();  
        }          
    } 
}  

十 二、使用OLEConn連接數據庫：
using System;
using System.Data;   
using System.Data.OleDb;   

class TestADO
{  
    static void Main(string[] args)  
    {  
        string strDSN = Provider=Microsoft.Jet.OLEDB.4.0;DataSource=c: est.mdb;  
        string strSQL = SELECT * FROM employee ;  

        OleDbConnection conn = new OleDbConnection(strDSN);
        OleDbDataAdapter cmd = new OleDbDataAdapter( strSQL, conn ); 

        conn.Open();
        DataSet ds = new DataSet();
        cmd.Fill( ds, employee );
        DataTable dt = ds.Tables[0];

        foreach( DataRow dr in dt.Rows )
        {
            Console.WriteLine(First name: + dr[FirstName].ToString() + Last name: + dr[LastName].ToString());
        }
        conn.Close();  
    } 
}  
十三、讀取表的屬性：

using System;
using System.Data;   
using System.Data.OleDb;   

class TestADO
{  
    static void Main(string[] args)  
    {  
        string strDSN = Provider=Microsoft.Jet.OLEDB.4.0;DataSource=c: est.mdb;  
        string strSQL = SELECT * FROM employee ;  

        OleDbConnection conn = new OleDbConnection(strDSN);
        OleDbDataAdapter cmd = new OleDbDataAdapter( strSQL, conn ); 

        conn.Open();
        DataSet ds = new DataSet();
        cmd.Fill( ds, employee );
        DataTable dt = ds.Tables[0];

        Console.WriteLine(FIEld Name DataType Unique AutoIncrement AllowNull);
        Console.WriteLine(==================================================================);
        foreach( DataColumn dc in dt.Columns )
        {
            Console.WriteLine(dc.ColumnName+ , +dc.DataType + ,+dc.Unique + ,+dc.AutoIncrement+ ,+dc.AllowDBNull );
        }
        conn.Close();  
    } 
} 

網絡方面的：
十八、取得IP地址：
using System;
using System.Net;

class GetIP
{
     public static void Main()
     {
         IPHostEntry ipEntry = Dns.GetHostByName (localhost);
         IPAddress [] IpAddr = ipEntry.AddressList;
         for (int i = 0; i < IpAddr.Length; i++)
         { 
             Console.WriteLine (IP Address {0}: {1} , i, IpAddr.ToString ());
         }
    }
}
十九、取得機器名稱：
using System;
using System.Net;

class GetIP
{
    public static void Main()
    {
          Console.WriteLine (Host name : {0}, Dns.GetHostName());
    }
}

十一、根據IP地址得出機器名稱：
using System;
using System.Net;

class ResolveIP
{
     public static void Main()
     {
         IPHostEntry ipEntr.Resolve(172.29.9.9);
         Console.WriteLine (Host name : {0}, ipEntry.HostName);         
     }
}



Web Service方面的：
二十五、一個Web Service的小例子：
<% @WebService Language=C# Class=TestWS %>

using System.Web.Services;

public class TestWS : System.Web.Services.WebService
{
    [WebMethod()]
    public string StringFromWebService()
    {
        return This is a string from web service.;
    }
} 


//-------------------------------------------------------------


emule
http://www.ed2k.online/tushu/jsjwl/16725.html


ed2k://|file|[www.ed2k.online][C#%E5%85%A8%E8%83%BD%E9%80%9F%E6%9F%A5%E5%AE%9D%E5%85%B8].%E6%98%8E%E6%97%A5%E7%A7%91%E6%8A%80%E7%AD%89.%E6%89%AB%E6%8F%8F%E7%89%88.pdf|255157709|83403adcb05aaf95a0a0ef19846a00aa|h=pk25dcx3grk63emqyukmuh2eb6zuhpg5|/







fullscreenfullscreen

    2. 接下來為了方便在這之上進行截圖，有一個很重要的設計實現方式：用全屏幕窗體代替現有真實屏幕，這樣就可以把截圖過程的所有操作都在那個窗體上實現（該窗體設置成無邊框，高寬等於屏幕大小即可），另外為了顯示掩蔽效果（只能正常顯示選擇的部分屏幕內容，而其實部分用一個如半透明層覆蓋），就添加一層半透明位置位圖。具體代碼如下：

    public partial class FullScreenForm : Form
    {
	    private Rectangle rectSelected = Rectangle.Empty;
	
	    private bool isClipping = false;
	
	    private Bitmap screen;
	
	    private Bitmap coverLayer = null;
	
	    private Color coverColor;
	
	    private Brush rectBrush = null;
	
	    private Bitmap resultBmp = null;
	
	    public FullScreenForm(Bitmap screen)
	    {
		    InitializeComponent();
		
		    int width = Screen.PrimaryScreen.Bounds.Width;
		
		    int height = Screen.PrimaryScreen.Bounds.Height;
		
		    coverLayer = new Bitmap(width, height);
		
		    coverColor = Color.FromArgb(50, 200, 0, 0);
		
		    rectBrush = new SolidBrush(coverColor);
		
		    using (Graphics g = Graphics.FromImage(coverLayer)) {
		
		    g.Clear(coverColor);
	    }
	
	    this.Bounds = new Rectangle(0, 0, width, height);
	
	    this.screen = screen;
	
	    this.DoubleBuffered = true;
    }

    protected override void OnMouseDown(MouseEventArgs e)
    {
	    if (e.Button == MouseButtons.Left)
	    {
		    isClipping = true;
		    rectSelected.Location = e.Location;
	    }
	    else if (e.Button == MouseButtons.Right)
	    {
	    	this.DialogResult = DialogResult.OK;
	    }
    }

    protected override void OnMouseMove(MouseEventArgs e)
    {
	    if (e.Button == MouseButtons.Left & & isClipping)
	    {
		    rectSelected.Width = e.X - rectSelected.X;
		    rectSelected.Height = e.Y - rectSelected.Y;
		    this.Invalidate();
	    }
    }

    protected override void OnMouseUp(MouseEventArgs e)
    {
	    if (e.Button == MouseButtons.Left && isClipping)
	    {
		    rectSelected.Width = e.X - rectSelected.X;
		    rectSelected.Height = e.Y - rectSelected.Y;
		    this.Invalidate();
		    resultBmp = new Bitmap(rectSelected.Width, rectSelected.Height);
		    using (Graphics g = Graphics.FromImage(resultBmp))
		    {
		    	g.DrawImage(screen,new Rectangle(0, 0, rectSelected.Width, rectSelected.Height), rectSelected, GraphicsUnit.Pixel);
		    }
		    this.DialogResult = DialogResult.OK;
	    }
    }

    protected override void OnPaint(PaintEventArgs e)
    {
	    Graphics g = e.Graphics;
	    g.DrawImage(screen, 0, 0);
	    g.DrawImage(coverLayer, 0, 0);
	    PaintRectangle();
    }

    protected override void OnPaintBackground(PaintEventArgs e)
    {
    }

    protected override void OnKeyDown(KeyEventArgs e)
    {
	    if (e.KeyCode == Keys.Escape)
	    {
	    	this.DialogResult = DialogResult.Cancel;
	    }
    }

    private void PaintRectangle()
    {
	    using (Graphics g = Graphics.FromImage(coverLayer))
	    {
		    g.Clear(coverColor);
		    GraphicsPath path = new GraphicsPath();
		    path.AddRectangle(this.Bounds);
		    path.AddRectangle(rectSelected);
		    g.FillPath(rectBrush, path);
		    g.DrawRectangle(Pens.Blue, rectSelected);
	    }
    }

    public Bitmap ResultBitmap
    {
    	get { return resultBmp; }
    }
}



byte[]與Image Image與 byte[] 之間的轉換

/// <summary>
/// 將byte[]轉換為Image
/// </summary>
/// <param name="bytes">字節數組</param>
/// <returns>Image</returns>
public Image ReadImage(byte[] bytes)
{
     MemoryStream ms=new MemoryStream(bytes,0,bytes.Length);
     BinaryFormatter bf = new BinaryFormatter();
     object obj=bf.Deserialize(ms);  
　　ms.Close();
　　return (Image)obj;
}
/// <summary>
/// 將Image轉換為byte[]
/// </summary>
/// <param name="image">Image</param>
/// <returns>byte[]</returns>
public byte[] ConvertImage(Image image)
{
     MemoryStream ms=new MemoryStream();
     BinaryFormatter bf = new BinaryFormatter();
     bf.Serialize(ms,(object)image);
     ms.Close();
     return ms.ToArray();
}




C# GUID介紹和的使用，

GUID（全局統一標識符）是指在一台機器上生成的數字，它保證對在同一時空中的所有機器都是唯一的。通常平台會提供生成GUID的API。生成算法很有意思，用到了以太網卡地址、納秒級時間、芯片ID碼和許多可能的數字。GUID的唯一缺陷在於生成的結果串會比較大。

GUID永遠是方便的; 對於程序開發的各個方面，.NET Framework簡化了建立和處理GUID數值的過程。在.NET程序需要的地方，這一功能很容易地生成唯一的數值。

 

1. 一個GUID為一個128位的整數(16字節)，在使用唯一標識符的情況下，你可以在所有計算機和網絡之間使用這一整數。

2. GUID 的格式為“xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx”，其中每個 x 是 0-9 或 a-f 范圍內的一個十六進制的數字。例如：337c7f2b-7a34-4f50-9141-bab9e6478cc8 即為有效的 GUID 值。

3. 世界上（Koffer注：應該是地球上）的任何兩台計算機都不會生成重復的 GUID 值。GUID 主要用於在擁有多個節點、多台計算機的網絡或系統中，分配必須具有唯一性的標識符。

4. 在 Windows 平台上，GUID 應用非常廣泛：注冊表、類及接口標識、數據庫、甚至自動生成的機器名、目錄名等。





GUID（全局統一標識符）是指在一台機器上生成的數字，它保證對在同一時空中的所有機器都是唯一的。GUID的唯一缺陷在於生成的結果串會比較大。

      對於程序開發的各個方面，.NET Framework簡化了建立和處理GUID數值的過程。在.NET程序需要的地方，這一功能很容易地生成唯一的數值。

1、Guid.NewGuid().ToString("N") 結果為：
         38bddf48f43c48588e0d78761eaa1ce6
2、Guid.NewGuid().ToString("D") 結果為：
            57d99d89-caab-482a-a0e9-a0a803eed3ba
3、Guid.NewGuid().ToString("B") 結果為：
            {09f140d5-af72-44ba-a763-c861304b46f8}
4、Guid.NewGuid().ToString("P") 結果為：
            (778406c2-efff-4262-ab03-70a77d09c2b5)
            
可見默認的為第2種效果

        其中：N、D、B、P分別代表一種輸出格式

小注：在個人使用中，主要是在數據中某列在沒有輸入值的情況下，用於生成內碼（NOT NULL PRIMARY KEY）。
EG:       string str = "insert into 表名(NM,BH,MC) values('" + Guid.NewGuid().ToString("N") + "','" + textBox_bh.Text + "','" + textBox_mc.Text + "')";
            
            




//拜列轉字串(16進制)

	static int buffersize = 18;   //十六進制數的大小（假設為6Byte）
	byte[] buffer = new Byte[buffersize];   //創建緩沖區
	
	private void button1_Click(object sender, EventArgs e)
	{
	    serialPort1.Read(buffer, 0, buffersize);
	    string ss;
	    ss = byteToHexStr(buffer); //用到函數byteToHexStr
	    textBox2.Text = ss;
	    serialPort1.Close();
	    MessageBox.Show("數據接收成功！", "系統提示");
	}
	
	//字節數組轉16進制字符串
	public static string byteToHexStr(byte[] bytes)
	{
	    string returnStr = "";
	    if (bytes != null)
	    {
	        for (int i = 0; i < bytes.Length; i++)
	        {
	            returnStr += bytes[i].ToString("X2");
	        }
	    }
	    return returnStr;
	}
	

c#畫三角形、並填充顏色
目前知道有兩種方法：畫多邊形、GraphicsPath。但是用畫多邊形的方式畫三角形不太好。老畫不正的，截圖放大就明顯了。

	Point point1 = new Point(0, 0);
	Point point2 = new Point(11, 0);
	Point point3 = new Point(5, 8);
	Point[] pntArr = {point1, point2, point3};
	
	e.Graphics.FillPolygon(Brushes.Red, pntArr);


//c#記事本實現代碼




目前大部分數碼相機都將所拍照的圖像保存成JPG格式，
而像拍照日期這樣的 信息統稱為EXIF信息。
EXIF是英文ExchangeableImageFile(可交換圖像文件)的 縮寫


new vcs data

不寫注釋是流氓，名字瞎起是扯淡

C#對注冊表的操作

C#中提供的與注冊表相關的最主要的是兩個類：

Registry 和 RegistryKey，這兩個類屬於Microsoft.Win32命名空間

 

Registry類包含5個公共的靜態域，分別代表5個基本主鍵分別是：

Registry.ClassesRoot

Registry.CurrentUser

Registry.LocalMachine

Registry.Users

Registry.Current Config

這5個類分別對應注冊表的第二級目錄的五個預定義主鍵

 

RegistryKey類中提供了對注冊表操作的方法

CreateSubKey //建立一個子鍵

OpenSubKey //打開一個子鍵

DeleteKey //刪除一個子鍵

DeleteKeyTree//刪除一個鍵及其下的全部鍵

GetValue //獲取鍵值

SetValue //設置鍵值



檢測 USB 設備撥插的 C# 類庫：USBClassLibrary

private void USBPort_USBDeviceAttached(objectsender, USBClass.USBDeviceEventArgs e)
{
	if (!MyUSBDeviceConnected)
	{
		if(USBClass.GetUSBDevice(MyDeviceVID, MyDevicePID, ref USBDeviceProperties, false))
		{
			//My Device is connected
			MyUSBDeviceConnected = true;
		}
	}
}

private void USBPort_USBDeviceRemoved(objectsender, USBClass.USBDeviceEventArgs e)
{
	if(!USBClass.GetUSBDevice(MyDeviceVID, MyDevicePID, ref USBDeviceProperties, false))
	{
		//My Device is removed 
		MyUSBDeviceConnected = false;
	}
}



C# TabControl標簽的隱藏
	當你想要隱藏的時候
	
	if (this.tabMain.TabPages[ "tabpageThePage "] != null)
	
	{
	
	this.tabMain.TabPages.Remove(tabpageThePage);
	
	}
	
	當你想要顯示的時候
	
	if (this.tabMain.TabPages[ "tabpageThePage "] == null)
	
	{
	
	this.tabMain.TabPages.Add(tabpageThePage);
	
	}


c#畫三角形、並填充顏色

Point point1 = new Point(0, 0);
Point point2 = new Point(11, 0);
Point point3 = new Point(5, 8);
Point[] pntArr = {point1, point2, point3};
e.Graphics.FillPolygon(Brushes.Red, pntArr);


int len = 10;                       
int x = 0;
int y = 0;
Point[] pntArr = new Point[3];
pntArr[0] = new Point(x, y);
pntArr[1] = new Point(x - len, y);
pntArr[2] = new Point(x - len / 2, (int)(len * Math.Sqrt(3) / 2 + y));


        protected override void OnPaintBackground(PaintEventArgs e)
        {
            //不進行背景的繪制
        }



//字符串轉數組
string mystring="this is a string"
char[] mychars=mystring.ToCharArray();

//foreach循環處理char數組
foreach(char mychar in mystring)
{
Console.WriteLine(mychar);
}
mystring.Length //獲取元素的個數 


        
        

c# 控件閃爍處理方法
如果你在Form中繪圖的話，不論是不是采用的雙緩存，都會看到圖片在更新的時候都會不斷地閃爍，解決方法就是在這個窗體的構造函數中增加以下三行代碼：

請在構造函數裡面底下加上如下幾行：
SetStyle(ControlStyles.UserPaint, true);
SetStyle(ControlStyles.AllPaintingInWmPaint, true); // 禁止擦除背景.
SetStyle(ControlStyles.DoubleBuffer, true); // 雙緩沖
參數說明：

UserPaint
如果為 true，控件將自行繪制，而不是通過操作系統來繪制。此樣式僅適用於派生自 Control 的類。

AllPaintingInWmPaint
如果為 true，控件將忽略 WM_ERASEBKGND 窗口消息以減少閃爍。僅當 UserPaint 位設置為 true 時，才應當應用該樣式。

DoubleBuffer
如果為 true，則繪制在緩沖區中進行，完成後將結果輸出到屏幕上。雙重緩沖區可防止由控件重繪引起的閃爍。要完全啟用雙重緩沖，還必須將 UserPaint 和 AllPaintingInWmPaint 樣式位設置為 true。


//初始化加載皮膚 
            skinEngine1.SkinFile = "MacOS.ssk"; 

 skinEngine1.SkinFile = "PageColor.ssk"; 


objStreamWriter = new StreamWriter(objFileStream, Encoding.Unicode); 



   private DataSet ReadExcel(string strFileName, string sheetName)//使用OLE操作數據庫的方法讀取excel數據，導入到系統 
        { 
            if (strFileName == string.Empty) 
            { 
                return null; 
            } 
            else 
            { 
                string strConnection = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source = " + strFileName + ";Extended Properties = Excel 8.0"; 
                OleDbConnection oleConnection = new OleDbConnection(strConnection); 
                oleConnection.Open(); 
                DataSet dsRead = new DataSet(); 
                OleDbDataAdapter oleAdper = new OleDbDataAdapter(" SELECT *  FROM [" + sheetName + "$]", oleConnection); 
                oleAdper.Fill(dsRead, "result"); 
                oleConnection.Close(); 
                return dsRead;  
            }                                      
        } 
        
        
        
        
        
        
        
        

C#:判斷當前程序是否通過管理員運行，

public bool IsAdministrator()
{
WindowsIdentity current = WindowsIdentity.GetCurrent();
WindowsPrincipal windowsPrincipal = new WindowsPrincipal(current);
return windowsPrincipal.IsInRole(WindowsBuiltInRole.Administrator);
}


C# 文件創建時間，修改時間，

FileInfo fi = new FileInfo(@"D:\site\EKECMS\skin\Grey\default#.html");
Response.Write("修改時間：" + fi.LastWriteTime.ToString() + "<br>");
Response.Write("創建時間：" + fi.CreationTime.ToString() + "<br>");

//在代碼中設置控件的padding 設置Label的字體
如果要在代碼中設置margin，可以使用如下代碼：
this.label1.Padding = new Padding(20,8,20,8);
或者=new Padding(20);

設置Label的字體代碼：
this.label1.Font = new Font(label1.Font.FontFamily,10f);

設置Label的背景色代碼：
this.label1.BackColor = Color.FromArgb(((int)(((byte)(226)))), ((int)(((byte)(238)))), ((int)(((byte)(255)))));



在不設置Cookie、PostData的情況下要獲得一個頁面 的HTML的方法很簡單：

public static string GetHtml(string URL)
　 　　　{
　　　　　　WebRequest wrt;
　　　　　　wrt = WebRequest.Create(URL);
　　　　　　wrt.Credentials = CredentialCache.DefaultCredentials;
　　　　　　WebResponse wrp;
　　　 　　　wrp = wrt.GetResponse();
　　　　　　return new StreamReader (wrp.GetResponseStream(), Encoding.Default).ReadToEnd();
　　　　} 



地支時間與現在時間的對應關系：

【子時】夜半，又名子夜、中夜：十二時辰的第一個時辰。（23時至次日01時）。

【丑時】雞鳴，又名荒雞：十二時辰的第二個時辰。（01時至03時）。

【寅時】平旦，又稱黎明、早晨、日旦等：時是夜與日的交替之際。（03時至05時）。

【卯時】日出，又名日始、破曉、旭日等：指太陽剛剛露臉，冉冉初升的那段時間。（05 時至07時）。

【辰時】食時，又名早食等：古人“朝食”之時也就是吃早飯時間，（07時至 09時）。

【巳時】隅中，又名日禺等：臨近中午的時候稱為隅中。（09時至11時）。

【午時】日中，又名日正、中午等：（11時至13時）。

【未時】日昳，又名日跌、日央等：太陽偏西為日跌。（13時至15時）。

【申時】哺時，又名日鋪、夕食等：（15時至17時）。

【酉時】日入，又名日落、日沉、傍晚：意為太陽落山的時候。（17時至19時）。　

【戌時】黃昏，又名日夕、日暮、日晚等：此時太陽已經落山，天將黑未黑。天地昏黃，萬物朦胧 ，故稱黃昏。（19時至21時）。

【亥時】人定，又名定昏等：此時夜色已深，人們也已經停止活動，安歇睡眠了。人定也就是人靜 。（21時至23時）。




開關檔案 使用指定的編碼
StreamWriter outStream = new StreamWriter(filepath, false, Encoding.GetEncoding(950));
using (StreamReader sr = new StreamReader(filepath, Encoding.GetEncoding(936)))



用C＃實現在客戶區拖動窗體


C#調用默認浏覽器打開網頁的幾種方法




方法一：從注冊表中讀取默認浏覽器可執行文件路徑

 

        private void button1_Click(object sender, EventArgs e)
        {
            //從注冊表中讀取默認浏覽器可執行文件路徑
            RegistryKey key = Registry.ClassesRoot.OpenSubKey(@httpshellopencommand);
            string s = key.GetValue().ToString();

            //s就是你的默認浏覽器，不過後面帶了參數，把它截去，不過需要注意的是：不同的浏覽器後面的參數不一樣！
            //D:Program Files (x86)GoogleChromeApplicationchrome.exe -- %1
            System.Diagnostics.Process.Start(s.Substring(0, s.Length - 8), http://blog.csdn.net/testcs_dn);
        }
方法二：
        private void button2_Click(object sender, EventArgs e)
        {
            //調用系統默認的浏覽器 
            System.Diagnostics.Process.Start(explorer.exe, http://blog.csdn.net/testcs_dn);
        }
方法三：
        private void button3_Click(object sender, EventArgs e)
        {
            //調用系統默認的浏覽器 
            System.Diagnostics.Process.Start(http://blog.csdn.net/testcs_dn);
        }

方法四：調用IE浏覽器


從原理上來講，方法二和方法三應該是一樣的，不過方法三的代碼更短一點。 




命令行msinfo32


三、添加office相關引用
Microsoft.Office.Interop.Word 12.0.0.0





using System.Data.OleDb;
using System.Data.SqlClient;
using System.IO;
using Microsoft.Office.Core;
using Word=Microsoft.Office.Interop.Word;
using System.Reflection;



求取字母的ASCII值

            Console.Write("輸入一個字符："); 
            char c = Console.ReadKey().KeyChar; 
            Console.WriteLine("\r\n字符{0}的ASCII值是：{1}", c, (int)c); 
            Console.ReadKey(false); 



DataGridView 指定欄位排序

// 根據 資料行1 (Name) 做 大到小 排序
dataGridView1.Sort(dataGridView1.Columns[1], System.ComponentModel.ListSortDirection.Descending); 

// 根據 資料行1 (Name) 做 小到大 排序 
dataGridView1.Sort(dataGridView1.Columns[1], System.ComponentModel.ListSortDirection.Ascending); 



    
    
            //                    來源位置             目的位置      要傳輸的區域大小  判斷在像素複製作業中來源色彩如何與目的色彩結合以產生最後的色彩
            //g.CopyFromScreen(new Point(x_st, y_st), new Point(0, 0), new Size(w, h), CopyPixelOperation.SourceInvert);
            //g.CopyFromScreen(new Point(x_st, y_st), new Point(0, 0), new Size(w, h));
            g.CopyFromScreen(new Point(pt.X - w / 2, pt.Y - h / 2), new Point(0, 0), new Size(w, h));



 C# 修改啟始Form [複製鏈接]
打開program.cs，修改Application.Run(new Form1());，將Form1改為要啟始的頁面即可!


網際網路時間伺服器，
從原來的 time.windows.com 改為 time.nist.gov，





3. 如何为一个窗体设置一个默认按钮？（How to set the default button for a form?）

form1.AcceptButton = button1;

4. 如何为一个窗体设置一个取消按钮？（How to set the Cancel button for a form?）

form1.CancelButton = button1;

5. 如何阻止一个窗体标题显示在任务栏上？（How to prevent a form from being shown in the taskbar?）

设置窗体的ShowIntaskbar属性为False

9. 如何获取应用程序当前执行的路径？（How to get the path to my running EXE?）

string appPath = Application.ExecutablePath; 

23. 如何使Windows Form上的Panel或者Label控件半透明？（How to make a Panel or Label semi-transparent on a Windows Form? ）

通过设置控件背景色的alpha值
panel1.BackColor = Color.FromA#41ccd4;
注意：在设计时手动输入这些值，不要用颜色选取


        //執行時期 顯示 屬性編輯視窗
        private void Form1_Load(object sender, EventArgs e)
        {
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






陣列
一群資料型態相同的變數集合在一起

反向運算子



要顯示 & 以 ＆amp;取代
要顯示 < 以 ＆lt;取代
要顯示 > 以 ＆gt;取代
要顯示 " 以 ＆quot;取代
要顯示 ' 以 ＆apos;取代

Unicode中文字碼（CJK Unified Ideographs；中日韓統一表意文字）的範圍落在0x4E00至0x9FFF（UTF-32），但迄今（Unicode v11.0）最末的0x9FF0～0x9FFF這16個字仍是空白。


#define abs(a, b)	(((a) > (b)) ? (a - b) : (b - a))

printf("function: %s:%s(%d) debug message\r\n",__FILE__,__func__,__LINE__);
       

內建函式

if(isprint(ch))
系統時間

函式 abs dec2hex hex2dec print9X9_Table

VC#
資料型態	string(字串) bool(布耳)
各種控件	button richTextBox pictureBox timer


colsole mode的scanf        
        
            // 宣告字串資料型別ProductName變數，用來存放品名
            string ProductName;
            // 宣告整數資料型別Price變數，用來存放單價
            int Price;
            Console.Write("請輸入品名：");        // 印出 "請輸入品名："
            // 由鍵盤輸入品名資料並按 [Enter]鍵，即將品名存放至ProductName變數
            ProductName = Console.ReadLine();
            Console.Write("請輸入單價：");         // 印出 "請輸入單價："
            // 由鍵盤輸入單價並按 [Enter]鍵，將單價轉成整數之後
            // 再將單價放至Price變數
            Price = int.Parse(Console.ReadLine());
            Console.WriteLine("品名：{0}　單價：{1}　這筆記錄儲存成功",ProductName, Price);
            Console.Read();

console mode讀取double數字
            double netIncome;
            int taxRate;

            Console.Write("請輸入全年綜合所得淨額(單位:萬元) : ");
            netIncome = double.Parse(Console.ReadLine());

console mode讀取字串
            // 宣告Ans字串變數用來存放使用者由鍵盤輸入的答案
            string Ans = Console.ReadLine();
                        
       
#include <stdio.h>
int main(int argc,char* argv[])
{



    /*
	int i;

	time_t time_ptr;

	printf("david: This is a c template.\n");

	printf("function: %s:%s(%d) debug message\r\n",__FILE__,__func__,__LINE__);


	time(&time_ptr);

	printf("現在時間 : %s\n", asctime(localtime(&time_ptr)));
*/


    time_t t1 = time(NULL);
    struct tm *nPtr = localtime(&t1);
    char *now = asctime(nPtr);

    printf("現在時間 : %s\n", now);
    printf("len = %d\n",sizeof(now));

    int i;

    for(i=0;i<sizeof(now);i++)
    {
        printf("%c\n", now[i]);


    }



    //srand(123);
    srand(now[0]);

    for(i=0;i<10;i++)
    {
        printf("%c\n", 'A' + rand() % 26);

    }

	return 0;
}
        
        
        
        



Display_Cam1

            //pictureBox1.Image = (Bitmap)eventArgs.Frame.Clone();
            bm = (Bitmap)eventArgs.Frame.Clone();
            //bm.RotateFlip(RotateFlipType.RotateNoneFlipY);    //反轉
            pictureBox1.Image = bm;

            GC.Collect();       //回收資源

//--------------------------

            //录像
            //pictureBox1.Image = (Bitmap)eventArgs.Frame.Clone();
            bm = (Bitmap)eventArgs.Frame.Clone();
            //bm.RotateFlip(RotateFlipType.RotateNoneFlipY);    //反轉
			
            Graphics g = Graphics.FromImage(image);
			
			
										SolidBrush drawBrush = new SolidBrush(Color.Yellow);

										Font drawFont = new Font("Arial", 6, System.Drawing.FontStyle.Bold, GraphicsUnit.Millimeter);
										int xPos = image.Width - (image.Width - 15);
										int yPos = 10;
										//写到屏幕上的时间
										string drawDate = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss");

										g.DrawString(drawDate, drawFont, drawBrush, xPos, yPos);

            ////创建文件路径
            string fileFullPath = videoPath + "V1" + DateTime.Now.ToString("yyyy-MM-dd-HH-mm-ss");

            if (stopREC)
            {
                stopREC = true;
                createNewFile = true;  //这里要设置为true表示要创建新文件
                if (videoWriter != null)
                    videoWriter.Close();
            }
            else
            {
										//开始录像
										if (createNewFile)
										{

											createNewFile = false;
											if (videoWriter != null)
											{
												videoWriter.Close();
												videoWriter.Dispose();
											}
											richTextBox1.Text += "開啟檔案 : " + fileFullPath + "\n";

											videoWriter = new VideoFileWriter();
											//这里必须是全路径，否则会默认保存到程序运行根据录下了
											videoWriter.Open(fileFullPath, image.Width, image.Height, 30, VideoCodec.MPEG4);
											videoWriter.WriteVideoFrame(image);
										}
										else
										{
											videoWriter.WriteVideoFrame(image);
										}
            }



fileFullPath : C:\_git\vcs\_2.vcs\my_vcs_lesson_c_example\_video\OperateCamera\bin\Debug\V12021-08-20-15-39-07



關掉AForge的VSP
        // Close currently open camera if any
        private void CloseCamera()
        {
            if (videoSource != null)
            {
                videoSourcePlayer.VideoSource = null;

                videoSource.SignalToStop();
                videoSource.WaitForStop();
                videoSource = null;
            }
        }		


在 C# 中使用 File.ReadAllText() 方法將檔案讀取為字串
string text = File.ReadAllText(@"C:\File\file.txt");
Console.WriteLine(text);

在 C# 中使用 StreamReader.ReadToEnd() 方法將檔案讀取為字串
StreamReader fileReader = new StreamReader(@"C:\File\file.txt");
string text = fileReader.ReadToEnd();
Console.WriteLine(text);			



使用 C# 中的 FileInfo.Length 屬性獲取檔案大小
FileInfo fileinfo = new FileInfo("dark.jpg");
Console.WriteLine(fileinfo.Length);
FileInfo 類提供了用於在 C# 中建立，開啟，複製，刪除和移動檔案的方法。



//打开注册表
string regeditstr = Environment.GetEnvironmentVariable("WinDir");//WinDir系统环境变量的名称
Process.Start(regeditstr + "\\regedit.exe");//打开注册表




//開啟檔案總管到指定的目錄
string Path = @"C:\dddddddddd";
Process.Start("explorer.exe", Path);

Process.Start(textBox1.Text);//打开文件夹进行查看

MainMenu選了之後會有打勾記號

        // On Size menu item popup
        private void sizeItem_Popup(object sender, System.EventArgs e)
        {
            normalSizeItem.Checked = (pictureBox.SizeMode == PictureBoxSizeMode.Normal);
            stretchedSizeItem.Checked = (pictureBox.SizeMode == PictureBoxSizeMode.StretchImage);
            centeredSizeItem.Checked = (pictureBox.SizeMode == PictureBoxSizeMode.CenterImage);
        }




        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "檢查IP合法性\n";
            string[] lines = new string[4];
            string s = ".";
            string ip = "192.168.0.123";

            lines = ip.Split(s.ToCharArray(), 4);

            for (int i = 0; i < 4; i++)
            {
                if (Convert.ToInt32(lines[i]) >= 255)
                {
                    richTextBox1.Text += "不合法\n";
                    return;
                }
            }
            richTextBox1.Text += "合法\n";
			

        }




如何清除播放清單

顯示播放清單的內容

播放清單移除特定檔案






        public override string show()
        {
            return base.show() +
                   ": 寬 = " + width +
                   ", 高 = " + height;
        }
		
        public string listing()
        {
            string res = "";

            for (int i = 0; i < count; i++)
            {   // polymorphism
                Shape s = shapeArray[i];
                res += s.show() + ", 面積 = " + s.area() +
                       "\r\n-----------------------\r\n";
            }

            return res;
        }




計算程式執行的時間

int URms = System.Environment.TickCount;

XXXXXXXXX

Console.WriteLine("花費 {0} ms 完成!!!", Environment.TickCount - URms);




				

做一個我的 Transform範例

角度-180~+180
正弦值 -1~+1

xmin = -180;
xmax = 180;
ymin = -1;
ymax = 1;
xmargin = 10;
ymargin = 0.2;

顯示區域寬度W  if 720
顯示區域高度H  if 360

xratio = W/(xmax-xmin+xmargin*2);     //2 倍
yratio = H/(ymax-ymin+ymargin*2);     //180 倍

x=xmin:1:xmax;
y=sind(x);

先不考慮margin  把圖畫在中間

畫x時 每點相距 2 pixel

畫y時 要放大180倍

for(i=0; i<360;i++)
{
 x_new = x_old*2;
 y_new = y_old*180;
}


            e.Graphics.Clear(picGraph.BackColor);
            if (Balance.Count < 2) return;

            // Scale to make the data fit.
            float xmin = -1;
            float xmax = Contributions.Count + 1;
            float ymax = Balance.Max(pt => pt.Y);
            float ymin = -ymax * 0.05f;
            RectangleF rect = new RectangleF(xmin, ymin, xmax - xmin, ymax - ymin);
            PointF[] pts =
            {
                new PointF(0, picGraph.ClientSize.Height),
                new PointF(picGraph.ClientSize.Width, picGraph.ClientSize.Height),
                new PointF(0, 0),
            };
            Transform = new Matrix(rect, pts);
            e.Graphics.Transform = Transform;




        string drap_setup_filename = "drap_setup.ini";

        void update_setup_file()
        {
            richTextBox2.Text += "update_setup_file ST\n";
            richTextBox2.Text += "length of old_search_path = " + old_search_path.Count.ToString() + "\n";

            {
                StreamWriter sw = File.CreateText(drap_setup_filename);
                string content = "";
                //定義系統版本
                Version ver = Environment.OSVersion.Version;
                //Major主版本號,Minor副版本號
                if (ver.Major == 6 && ver.Minor == 1)
                {
                    //Windows7
                    content += "\"C:\\Program Files\\DAUM\\PotPlayer\\PotPlayerMini.exe\"\n";
                }
                else
                {
                    //Windows10
                    content += "\"C:\\Program Files (x86)\\DAUM\\PotPlayer\\PotPlayerMini.exe\"\n";
                }
                content += "\"C:\\Program Files (x86)\\AIMP\\AIMP.exe\"\n";
                content += "\"C:\\Program Files (x86)\\ACDSee32\\ACDSee32.exe\"\n";
                content += "\"C:\\Program Files (x86)\\IDM Computer Solutions\\UltraEdit-32\\uedit32.exe\"\n";
                content += SelectedLanguage.ToString() + "\n";
                content += comboBox1.SelectedIndex.ToString() + "\n";
                if (cb_video_only.Checked == true)
                    content += "1\n";
                else
                    content += "0\n";
                if (cb_video_l.Checked == true)
                    content += "1\n";
                else
                    content += "0\n";
                if (cb_video_m.Checked == true)
                    content += "1\n";
                else
                    content += "0\n";
                if (cb_video_s.Checked == true)
                    content += "1\n";
                else
                    content += "0\n";
                if (cb_file_size.Checked == true)
                    content += "1\n";
                else
                    content += "0\n";
                if (cb_file_l.Checked == true)
                    content += "1\n";
                else
                    content += "0\n";
                if (cb_file_m.Checked == true)
                    content += "1\n";
                else
                    content += "0\n";
                if (cb_file_s.Checked == true)
                    content += "1\n";
                else
                    content += "0\n";
                if (cb_generate_text.Checked == true)
                    content += "1\n";
                else
                    content += "0\n";

                /*
                //Major主版本號,Minor副版本號
                if (ver.Major == 6 && ver.Minor == 1)
                {
                    //Windows7
                    video_player_path = @"C:\Program Files\DAUM\PotPlayer\PotPlayerMini.exe";
                }
                else
                {
                    //Windows10
                    video_player_path = @"C:\Program Files (x86)\DAUM\PotPlayer\PotPlayerMini.exe";
                }
                audio_player_path = @"C:\Program Files (x86)\AIMP\AIMP.exe";
                picture_viewer_path = @"C:\Program Files (x86)\ACDSee32\ACDSee32.exe";
                text_editor_path = @"C:\Program Files (x86)\IDM Computer Solutions\UltraEdit-32\uedit32.exe";
                */

                richTextBox2.Text += "目前共有 " + listBox1.Items.Count.ToString() + " 條搜尋路徑\n";

                if (listBox1.Items.Count == 0)
                {
                    content += "C:\\______test_files\n";
                    old_search_path.Add("C:\\______test_files");
                }
                else
                {
                    for (int i = 0; i < listBox1.Items.Count; i++)
                    {
                        richTextBox2.Text += listBox1.Items[i] + "\n";
                        content += listBox1.Items[i] + "\n";
                    }
                }
                content += "\n";

                sw.WriteLine(content, Encoding.UTF8);
                sw.Close();
            }
        }

        void Read_Setup_File()
        {
            int i;
            int tmp;
            if (File.Exists(drap_setup_filename) == false)
            {
                richTextBox2.Text += "檔案 " + drap_setup_filename + " 不存在，製作一個。\n";
                update_setup_file();
            }
            else
            {
                richTextBox2.Text += "檔案 " + drap_setup_filename + " 存在, 開啟，並讀入設定\n";
                string line;
                StreamReader sr = new StreamReader(drap_setup_filename, Encoding.UTF8);
                i = 0;
                while (!sr.EndOfStream)
                {               // 每次讀取一行，直到檔尾
                    line = sr.ReadLine().Trim();            // 讀取文字到 line 變數
                    richTextBox2.Text += "第 " + i.ToString() + " 行資料 : " + line + "\n";
                    switch (i)
                    {
                        case 0:
                            video_player_path = line;
                            break;
                        case 1:
                            audio_player_path = line;
                            break;
                        case 2:
                            picture_viewer_path = line;
                            break;
                        case 3:
                            text_editor_path = line;
                            break;
                        case 4:
                            SelectedLanguage = int.Parse(line);
                            break;
                        case 5:
                            tmp = int.Parse(line);
                            comboBox1.SelectedIndex = tmp;
                            break;
                        case 6:
                            tmp = int.Parse(line);
                            if (tmp == 1)
                                cb_video_only.Checked = true;
                            else
                                cb_video_only.Checked = false;
                            break;
                        case 7:
                            tmp = int.Parse(line);
                            if (tmp == 1)
                                cb_video_l.Checked = true;
                            else
                                cb_video_l.Checked = false;
                            break;
                        case 8:
                            tmp = int.Parse(line);
                            if (tmp == 1)
                                cb_video_m.Checked = true;
                            else
                                cb_video_m.Checked = false;
                            break;
                        case 9:
                            tmp = int.Parse(line);
                            if (tmp == 1)
                                cb_video_s.Checked = true;
                            else
                                cb_video_s.Checked = false;
                            break;
                        case 10:
                            tmp = int.Parse(line);
                            if (tmp == 1)
                                cb_file_size.Checked = true;
                            else
                                cb_file_size.Checked = false;
                            break;
                        case 11:
                            tmp = int.Parse(line);
                            if (tmp == 1)
                                cb_file_l.Checked = true;
                            else
                                cb_file_l.Checked = false;
                            break;
                        case 12:
                            tmp = int.Parse(line);
                            if (tmp == 1)
                                cb_file_m.Checked = true;
                            else
                                cb_file_m.Checked = false;
                            break;
                        case 13:
                            tmp = int.Parse(line);
                            if (tmp == 1)
                                cb_file_s.Checked = true;
                            else
                                cb_file_s.Checked = false;
                            break;
                        case 14:
                            tmp = int.Parse(line);
                            if (tmp == 1)
                                cb_generate_text.Checked = true;
                            else
                                cb_generate_text.Checked = false;
                            break;
                        case 15:
                            search_path = line;
                            break;
                        default:
                            break;
                    }
                    if (i >= 15)
                    {
                        if (line.Length > 0)
                        {
                            richTextBox2.Text += "加入路徑 : " + line + "\n";
                            old_search_path.Add(line);
                        }
                        else
                        {
                            richTextBox2.Text += "空行\n";
                        }
                    }
                    i++;
                }
                sr.Close();
            }
        }


        				
//--------------------------------------------------------------------------------------------------------------------------



//--------------------------------------------------------------------------------------------------------------------------
//較完整 可一段一段貼上範例程式
//--------------------------------------------------------------------------------------------------------------------------


//C#獲取硬盤序列號

using System;
using System.Runtime.InteropServices;

namespace ArLi.CommonPrj {

#region how use this?
/*
string sVol = getvol.GetVolOf("C");
*/
#endregion

public class getvol{

[DllImport("kernel32.dll")]
private static extern int GetVolumeInformation(
string lpRootPathName,
string lpVolumeNameBuffer,
int nVolumeNameSize,
ref int lpVolumeSerialNumber,
int lpMaximumComponentLength,
int lpFileSystemFlags,
string lpFileSystemNameBuffer,
int nFileSystemNameSize
);

public static string GetVolOf(string drvID){
const int MAX_FILENAME_LEN = 256;
int retVal = 0;
int a =0;
int b =0;
string str1 = null;
string str2 = null;


int i = GetVolumeInformation(
drvID + @":\",
str1,
MAX_FILENAME_LEN,
ref retVal,
a,
b,
str2,
MAX_FILENAME_LEN
);

return retVal.ToString("x");
}
}
}




//--------------------------------------------------------------------------------------------------------------------------



//--------------------------------------------------------------------------------------------------------------------------




        				
//--------------------------------------------------------------------------------------------------------------------------



正則表達式

用於字符串處理、表單驗證等。
var regx = "^[a-zA-Z0-9]{6,20}$";
if ( ! Regex.IsMatch("abcdef;sd123",regex)
{
    //長度必須6-20，字母和數字
}
^  匹配一行的開始 例如正則表達式 ^when 能夠匹配到 ”when in the“ 的開始，但不能匹配到 ”what and when in the“ 
$ 匹配一行的結束。 例如正則表達式 food$ 能夠匹配到 “he's  food” 的末尾 
.點 匹配任何單個字符，例如正則表達式 r.t 能夠匹配 “rat、rut、r t”，但是不能匹配root 
*  匹配0或多個正好在它之前的那個字符，例如 .* 能夠匹配任意數量的任何字符。 
[] 匹配匹配一個出現在[]中的字符 
|  或 敏感詞 ab|cd|ed|df
() 提高優先級 a(bc) 實現分組
+ 緊跟在+前面的字符出現任意次，至少1次
? 緊跟在?前面的字符出現或不出現
{n} {n,} {n,m} 匹配一定范圍個數 {1,} 相當與+ {0,} 相當於*
\d 代表 [0-9] \D 代表 [^0-9] 非0-9
\i 代表 [a-z]
\u 代表 [A-Z]
\a 代表 [A-Za-z]
\w 代表 [a-zA-Z0-9] 
常用表達式
匹配身份證：\d{15}|\d{18}
匹配中國郵政編碼：[1-9]\d{5}(?!\d)
匹配騰訊QQ號：[1-9][0-9]{4,}
匹配國內電話號碼：\d{3}-\d{8}|\d{4}-\d{7}
匹配帳號是否合法(字母開頭，允許5-16字節，允許字母數字下劃線)：^[a-zA-Z][a-zA-Z0-9_]{4,15}$
匹配網址URL的正則表達式：[a-zA-z]+://[^\s]*
匹配Email地址的正則表達式：\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*
匹配首尾空白字符的正則表達式：^\s*|\s*$
匹配HTML標記的正則表達式：<(\S*?)[^>]*>.*?</\1>|<.*? />
匹配中文字符的正則表達式： [\u4e00-\u9fa5]
限制網頁表單裡的文本框輸入內容：
只能輸入中文：<input type="text" onkeyup="value=value.replace(/[^\u4E00-\u9FA5]/g,'')" onbeforepaste="clipboardData.setData('text',clipboardData.getData('text').replace(/[^\u4E00-\u9FA5]/g,''))" />
只能輸入數字：<input type="text" onkeyup="value=value.replace(/[^\d]/g,'') " onbeforepaste="clipboardData.setData('text',clipboardData.getData('text').replace(/[^\d]/g,''))" />
只能輸入數字和英文：<input type="text" onkeyup="value=value.replace(/[\W]/g,'') " onbeforepaste="clipboardData.setData('text',clipboardData.getData('text).replace(/[^\d]/g,''))" />





//--------------------------------------------------------------------------------------------------------------------------




//--------------------------------------------------------------------------------------------------------------------------






//--------------------------------------------------------------------------------------------------------------------------





typedef double point[3];

point v[] =
{
    {0.0, 0.0, 1.0},
    {0.0, 0.942809, -0.33333},
    {-0.816497, -0.471405, -0.333333},
    {0.816497, -0.471405, -0.333333}
};

    point v1, v2, v3;
        normal(v1);


/* normalize a vector */
void normal(point p)
{
    double d = 0.0;
    int i;
    for (i = 0; i < 3; i++)
    {
        d += p[i] * p[i];
    }
    d = sqrt(d);
    if (d > 0.0)
    {
        for (i = 0; i < 3; i++)
        {
            p[i] /= d;
        }
    }
}






            string dir1 = @"C:\______test_files\compare1";

            string[] file_names1 = Directory.GetFiles(dir1);
            for (int i = 0; i < file_names1.Length; i++)
            {
                richTextBox1.Text += "i = " + i.ToString() + "\t" + file_names1[i] + "\n";
                file_names1[i] = file_names1[i].Replace(dir1, "");
                richTextBox1.Text += "i = " + i.ToString() + "\t" + file_names1[i] + "\n";
            }
            Array.Sort(file_names1);

            List<string> name_list = new List<string>();
            for (int i = 0; i < file_names1.Length; i++)
            {
                richTextBox1.Text += "i = " + i.ToString() + "\t" + file_names1[i] + "\n";
                name_list.Add(file_names1[i]);

            }


            DirectoryInfo dir1_info = new DirectoryInfo(dir1);
            FileInfo[] fi = dir1_info.GetFiles();

            int len = fi.Length;
            richTextBox1.Text += "len = " + len.ToString() + "\n";

            for (int i = 0; i < len; i++)
            {
                richTextBox1.Text += fi[i].Name + "\n";

            }




//以下未預設值, 寫不寫都一樣
//gluOrtho2D(-1.0, 1.0, -1.0, 1.0);   //窗口座標範圍2D, 顯示範圍 : X軸(-1.0 ~ 1.0) Y軸(-1.0 ~ 1.0), 左下為原點



/* Address in MSF format */
struct cdrom_msf0
{
	__u8	minute;
	__u8	second;
	__u8	frame;
};

/* Address in either MSF or logical format */
union cdrom_addr
{
	struct cdrom_msf0	msf;
	int			lba;
};



typedef struct {
    int data;
    int audio;
    int cdi;
    int xa;
    long error;
} tracktype;





---------util.h---------
// Define Data type

typedef unsigned int       INT32U;
typedef unsigned short int INT16U;
typedef unsigned char      INT8U;
typedef int                INT32;
typedef short int          INT16;
typedef char               INT8;
typedef unsigned char      BOOLEAN;
#define true               (1 == 1)
#define false              (0 == 1)
#define OK                 true
#define NG                 false
// macro definition
#define READ_REG_INT32U(Addr)        *((INT32U*)(Addr))
#define WRITE_REG_INT32U(Addr,Value) *((INT32U*)(Addr))=Value
#define READ_REG_INT8U(Addr)         *((INT8U*)(Addr))
#define WRITE_REG_INT8U(Addr,Value)  *((INT8U*)(Addr))=Value



bool animate = true;

        animate ^= 1;


// display image to the screen as textured quad
void displayImage(GLuint texture)
{
    glBindTexture(GL_TEXTURE_2D, texture);	//綁定紋理
    glEnable(GL_TEXTURE_2D);
    glDisable(GL_DEPTH_TEST);
    glDisable(GL_LIGHTING);
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE);

    glMatrixMode(GL_PROJECTION);
    glPushMatrix();
    glLoadIdentity();	//設置單位矩陣
    glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0);

    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();	//設置單位矩陣

    glViewport(0, 0, window_width, window_height);

    // if the texture is a 8 bits UI, scale the fetch with a GLSL shader

    glBegin(GL_QUADS);
    glTexCoord2f(0.0, 0.0);
    glVertex3f(-1.0, -1.0, 0.5);
    glTexCoord2f(1.0, 0.0);
    glVertex3f(1.0, -1.0, 0.5);
    glTexCoord2f(1.0, 1.0);
    glVertex3f(1.0, 1.0, 0.5);
    glTexCoord2f(0.0, 1.0);
    glVertex3f(-1.0, 1.0, 0.5);
    glEnd();

    glMatrixMode(GL_PROJECTION);
    glPopMatrix();

    glDisable(GL_TEXTURE_2D);

    SDK_CHECK_ERROR_GL();
}


void runAutoTest(int argc, char** argv, const char* filename, int kernel_param)
{



//這邊擷取出來讀取bmp的部分

    const char* image_path = sdkFindFilePath("portrait_noise.bmp", argv[0]);

    if (image_path == NULL)
    {
        printf(
            "imageDenoisingGL was unable to find and load image file "
            "<portrait_noise.bmp>.\nExiting...\n");
        exit(EXIT_FAILURE);
    }

    LoadBMPFile(&h_Src1, &imageW, &imageH, image_path);
    printf("Data init done.\n");

    checkCudaErrors(CUDA_MallocArray(&h_Src1, imageW, imageH));

    TColor* d_dst = NULL;
    unsigned char* h_dst = NULL;
    checkCudaErrors(cudaMalloc((void**)&d_dst, imageW * imageH * sizeof(TColor)));
    h_dst = (unsigned char*)malloc(imageH * imageW * 4);

    {
        g_Kernel = kernel_param;
        printf("[AutoTest]: %s <%s>\n", sSDKsample, filterMode[g_Kernel]);

        checkCudaErrors(cudaDeviceSynchronize());

        checkCudaErrors(cudaMemcpy(h_dst, d_dst, imageW * imageH * sizeof(TColor),
            cudaMemcpyDeviceToHost));
        sdkSavePPM4ub(filename, h_dst, imageW, imageH);
    }

    checkCudaErrors(CUDA_FreeArray());
    free(h_Src1);

    checkCudaErrors(cudaFree(d_dst));
    free(h_dst);

    printf("\n[%s] -> Kernel %d, Saved: %s\n", sSDKsample, kernel_param, filename);

    exit(g_TotalErrors == 0 ? EXIT_SUCCESS : EXIT_FAILURE);
}







    glDeleteTextures(1, &texture);
    if (imgBuf)
    {
        delete[] imgBuf;
        imgBuf = nullptr;
    }






/** CUDA Runtime API Version */
#define CUDART_VERSION  11070


#if CUDART_VERSION >= 2020

    if (!deviceProp.canMapHostMemory)
    {
        fprintf(stderr, "Device %d does not support mapping CPU host memory!\n", idev);

        exit(EXIT_SUCCESS);
    }

    checkCudaErrors(cudaSetDeviceFlags(cudaDeviceMapHost));
#else
    fprintf(stderr,
        "CUDART version %d.%d does not support "
        "<cudaDeviceProp.canMapHostMemory> field\n",
        , CUDART_VERSION / 1000, (CUDART_VERSION % 100) / 10);

    exit(EXIT_SUCCESS);
#endif





// Device code: 送入GPU執行的部分

__global__ void VecAdd(float* A, float* B, float* C)
{
:
:
}
            
// Host code: 送入CPU執行的部分

int main()
{
:
:



	// 動態分配位於"host(CPU) 記憶體" 的向量
	float* h_A = (float*)malloc(size);
	// 隨機初始化輸入向量
	for(i = 0; i < N; i++){
		h_A[i] = (float)rand() / (float)RAND_MAX;
	}

	// 動態分配位於"device(GPU) 記憶體"的向量
	float* d_A;
	cudaMalloc(&d_A, size); // cudaError_t cudaMalloc ( void** devPtr, size_t size )
	
	
	// 將向量從 CPU 複製到 GPU
	cudaMemcpy(d_A, h_A, size, cudaMemcpyHostToDevice);
	

	// 將 device code 送入 GPU 並執行，執行時一個 Grid 只有一個 block ，一個 block 有 N 個 thread
	VecAdd<<<1, N>>>(d_A, d_B, d_C);	


	// 將算好的向量從 GPU 複製到 CPU
	cudaMemcpy(h_C, d_C, size, cudaMemcpyDeviceToHost);

	// 印出運算結果
	printf("%f ", h_C[i]);


	// 釋放 GPU 記憶體
	cudaFree(d_A);
	cudaFree(d_B);
	cudaFree(d_C);
 
	// 釋放 CPU 記憶體
    free(h_A);
	free(h_B);
	free(h_C);
	

    


#if __CUDA_ARCH__ < 700
        return *(volatile unsigned char*)arrived;
#else
        unsigned int result;
        asm volatile("ld.acquire.sys.global.u8 %0, [%1];"
            : "=r"(result)
            : "l"(arrived)
            : "memory");
        return result;
#endif








//--------------------------------------------------------------------------------------------------------------------------

gluLookAt

   gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
1. gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0);

相當于我們的腦袋位置在(0.0,0.0,5.0)處，
眼睛望向(0.0,0.0,0.0),即原點。
后面的三個參數(0.0,1.0,0.0),y軸為1，其余為0，表示腦袋朝上，就是正常的情況。
壺嘴在右，壺柄在坐，壺底在下，壺蓋在上。
 
2.將gluLookAt的后三個參數設置為（0.0,-1.0,0.0）,即y軸為-1,其余為0。這樣表示腦袋向下，即人眼倒著看



3.修改gluLookAt的后三個參數為（1.0,0.0,0.0）;
x軸為1，其余為0.
即人的腦袋像右歪90度來看，即順時針轉90度（換個角度思考就是壺逆時針轉90度）
，猜想看到的結果應該是壺嘴在上，壺蓋在右，壺底在左，壺柄在下。如下圖：

 
 
gluLookAt的參數，
前三個參數表示的是腦袋的位置，
中間三個參數是人眼的朝向，
后三個位置表示的是腦袋朝向的方向。

 
在默認情況下，照相機位于原點，指向z軸的負方向，朝上向量為(0,1,0)。
 
可以修改原來的代碼。把視圖變換函數gluLookAt()函數，改為模型變換函數glTranslatef(),并使用參數(0.0,0.0,-5.0)。這個函數的效果和使用gluLookAt()函數的效果是完全相同的，原因：


gluLookAt()函數是通過移動照相機（使用試圖變換）來觀察這個立方體，
glTranslatef()函數是通過移動茶壺（使用模型變換）。

//--------------------------------------------------------------------------------------------------------------------------

選單範例


openGL
最小化可用之openGL
有視窗之範例
有讀寫檔案之範例


			


//------------------------------------------------------------------------------








//------------------------------------------------------------------------------







//------------------------------------------------------------------------------







//------------------------------------------------------------------------------






//------------------------------------------------------------------------------



   



        				
//--------------------------------------------------------------------------------------------------------------------------




//--------------------------------------------------------------------------------------------------------------------------





//--------------------------------------------------------------------------------------------------------------------------





//--------------------------------------------------------------------------------------------------------------------------








        				
//--------------------------------------------------------------------------------------------------------------------------




//--------------------------------------------------------------------------------------------------------------------------





//--------------------------------------------------------------------------------------------------------------------------


//C#檢查url鏈接是否有效
//檢查url地址是否能訪問,代碼如下:   

     /// <summary>
    /// 檢查url鏈接是否有效
     /// </summary>
    /// <param name="strUri"></param>
    /// <returns></returns>
    public static bool CheckUri(string strUri)
    {
        try
        {
            System.Net.HttpWebRequest.Create(strUri).GetResponse();
            return true;
        }
        catch
        {
            return false;
        }
    }
    
    

.net(C#)從html中提取中文字（正則表達式）
用正則表達式提取html中的純文本,代碼實現如下: 

using System.Text.RegularExpressions;      

 private string StripHT(string strHtml)  //從html中提取純文本
        {
            Regex regex = new Regex("<.+?>", RegexOptions.IgnoreCase);
            string strOutput = regex.Replace(strHtml, "");//替換掉"<"和">"之間的內容
            strOutput = strOutput.Replace("<", "");
            strOutput = strOutput.Replace(">", "");
            strOutput = strOutput.Replace("&nbsp;", "");
            return strOutput;
        }
    
    




//--------------------------------------------------------------------------------------------------------------------------









        				
//-----wmp---------------------------------------------------------------------------------------------------------------------


//添加列表
WC = new WMPLib.WindowsMediaPlayerClass();
MC = WC.newMedia(str);
this.axWindowsMediaPlayer1.currentPlaylist.appendItem(MC);
richTextBox1.Text += "add " + str + "\n";




C# WindowsMediaPlayer 的一些用法

播放單首歌曲

                player.URL = 

添加多首歌曲到播放列表

            IWMPPlaylist playList = player.playlistCollection.newPlaylist(); 
 (DataRow drItem = player.newMedia(drItem[].ToString()); 
=

 或者直接在當前列表上添加

 (DataRow drItem = player.newMedia(drItem[].ToString()); 


設置播放器音量

 player.settings.volume=;


 設置循環播放

player.settings.setMode(, );

 

設置隨機播放


  player.settings.setMode(, );





richTextBox1.Text += "測試使用WindowsMediaPlayerClass\n";
WindowsMediaPlayerClass c;
IWMPMedia m;

c = new WindowsMediaPlayerClass();
m = c.newMedia(mp3_filename);
richTextBox1.Text += "歌手名:\t" + m.getItemInfo("Author") + "\n" + "歌  名:\t" + m.getItemInfo("Title") + "\n";


getItemInfo Author Title

// Store the current media object.
var cm = Player.currentMedia;

// Get the number of attributes for the current media. 
var atCount = cm.attributeCount;

// Loop through the attribute list.
for(var i=0; i < atCount; i++){

   // Print each attribute index and name.   
   myText.value += "Attribute " + i +": ";
   myText.value += cm.getAttributeName(i);
   myText.value += "\n";
}








//C#中如何禁止WindowsMediaPlayer双击全屏显示


private void AxWindowsMediaPlayer1_MouseDownEvent(object sender, AxWMPLib._WMPOCXEvents_MouseDownEvent e)
{
    if (axWindowsMediaPlayer1.fullScreen)
        axWindowsMediaPlayer1.fullScreen = false;
} 











axWindowsMediaPlayer1


uiMode	//播放器介面模式
//Full, 有影像, 完整播放器介面
axWindowsMediaPlayer1.uiMode = "full";

//Mini, 有影像, 簡約播放器介面
axWindowsMediaPlayer1.uiMode = "mini";

//None, 有影像, 無播放器介面
axWindowsMediaPlayer1.uiMode = "none";

//Invisible, 無影像, 有無播放器介面
axWindowsMediaPlayer1.uiMode = "invisible";


在視頻播放之後,可以通過如下方式讀取源視頻的寬度和高度,然後設置其還原爲原始的大小.
         private void ResizeOriginal()
         {
             int intWidth = axWindowsMediaPlayer1.currentMedia.imageSourceWidth;
             int intHeight = axWindowsMediaPlayer1.currentMedia.imageSourceHeight;
             axWindowsMediaPlayer1.Width = intWidth + 2;
             axWindowsMediaPlayer1.Height = intHeight + 2;
         }

可能因爲媒體文件的打開需要一定時間，這裏等待媒體文件的打開

顯示文件播放長度。

則顯示結果很可能爲0，因此，這時候很可能獲取不到文件的播放時間長度，容易出錯。所以在利用的時候可以加一個timer控件：

從WMP8開始就不支持mms/rtsp協議了，所用wmp.URL="mms://xxxx";是不行的了。點此處見詳情，而mms這個協議現在還在廣泛使用。鬱悶。因此，我們不能使用wmp來看網絡電視了。




媒體播放器包括如下元素：
Video Display Panel：視頻顯示面板；
Video Border：視頻邊框；
Closed Captioning Display Panel；字幕顯示面板；
Track Bar；搜索欄；
Control Bar with Audio and Position Controls：帶有聲音和位置控制的控制欄；
Go To Bar：轉到欄；
Display Panel：顯示面板；
Status Bar：狀態欄；

　　就是這麼幾個部分，網上有資料說控件提供方法控制它們顯示與否，但是我在sdk中並沒有找到它們。唯一可以粗略控制它們的就是uiMode屬性。它的取值前面有。


　　七、像暴風有字幕相關信息的設置，wmp控件有這個功能嗎？
　　當然有。就是AxWindowsMediaPlayer.closedCaption。它是IWMPClosedCaption的實例。

label4.Text = axMediaPlayer1.Volume.ToString();    //音量
axMediaPlayer1.FileName = @"mms://218.98.101.164/vod/jingwei.wma";//文件路徑
axMediaPlayer1.Play(); //開始播放


nResL = axRealAudio1.GetPosition(); //獲得當前影片 的播放進度
label1.Text = axRealAudio1.GetTitle();   //獲得影片的標題
label2.Text = "當前的帶寬: " + axRealAudio1.GetBandwidthCurrent() / 1024 + "KB";//當前影片的當前的帶寬              
label3.Text = "連接的帶寬: " + axRealAudio1.GetConnectionBandwidth() / 1024 + "KB"; //當前的連接的帶寬

AxWindowsMediaPlayer媒體文件主要方法屬性
屬性/方法名︰ 說明︰ 
[基本屬性]  
URL:String; 指定媒體位置，本機或網絡地址 

playState:integer; 播放狀態，1=停止，2=暫停，3=播放，6=正在緩沖，9=正在連接，10=準備就緒 
enableContextMenu:Boolean; 啟用/禁用右鍵菜單 


//播放器基本控製 

Ctlcontrols.next; 下一曲 
Ctlcontrols.previous; 上一曲 

[settings] wmp.settings //播放器基本設置 
settings.volume:integer; 音量，0-100 
settings.autoStart:Boolean; 是否自動播放 
settings.mute:Boolean; 是否靜音 
settings.playCount:integer; 播放次數 

[currentMedia] wmp.currentMedia //當前媒體屬性 
currentMedia.duration:double; 媒體總長度 
currentMedia.durationString:string; 媒體總長度，字符串格式。如“03:24” 
currentMedia.getItemInfo(const string); 獲取當前媒體信息"Title"=媒體標題，"Author"=藝術家，"Copyright"=版權信息，"Description"=媒體內容描述， "Duration"=持續時間（秒），"FileSize"=文件大小，"FileType"=文件類型，"sourceURL"=原始地址 
currentMedia.setItemInfo(const string); 通過屬性名設置媒體信息 
currentMedia.name:string; 同 currentMedia.getItemInfo("Title") 

[currentPlaylist] wmp.currentPlaylist //當前播放列表屬性 
currentPlaylist.count:integer; 當前播放列表所包含媒體數 
currentPlaylist.Item[integer]; 獲取或設置指定項目媒體信息，其子屬性同wmp.currentMedia 


在視頻播放之後,可以通過如下方式讀取源視頻的寬度和高度,然後設置其還原為原始的大小.
         private void ResizeOriginal()
         {
							             int intWidth = axWindowsMediaPlayer1.currentMedia.imageSourceWidth;
							             int intHeight = axWindowsMediaPlayer1.currentMedia.imageSourceHeight;
							             axWindowsMediaPlayer1.Width = intWidth + 2;
							             axWindowsMediaPlayer1.Height = intHeight + 2;
         }






//--------------------------------------------------------------------------------------------------------------------------





//--------------------------------------------------------------------------------------------------------------------------






//--------------------------------------------------------------------------------------------------------------------------








        				
//--------------------------------------------------------------------------------------------------------------------------



//--------------------------------------------------------------------------------------------------------------------------





//--------------------------------------------------------------------------------------------------------------------------





//--------------------------------------------------------------------------------------------------------------------------





//--------------------------------------------------------------------------------------------------------------------------








        				
//--------------------------------------------------------------------------------------------------------------------------




//--------------------------------------------------------------------------------------------------------------------------


//--------------------------------------------------------------------------------------------------------------------------



        				
//--------------------------------------------------------------------------------------------------------------------------




//--------------------------------------------------------------------------------------------------------------------------





//--------------------------------------------------------------------------------------------------------------------------


        public class ImageInfo
        {
            private string image_path;
            private int image_width;
            private int image_height;

            public string ImagePath
            {
                get { return image_path; }
                set { image_path = value; }
            }

            public int ImageWidth
            {
                get { return image_width; }
                set { image_width = value; }
            }

            public int ImageHeight
            {
                get { return image_height; }
                set { image_height = value; }
            }

            public ImageInfo(string ImagePath, int ImageWidth, int ImageHeight)
            {
                this.ImagePath = ImagePath;
                this.ImageWidth = ImageWidth;
                this.ImageHeight = ImageHeight;
            }

            public Bitmap GetBitmap()
            {
                //WebPageBitmap Shot = new WebPageBitmap(this.ImagePath, this.ImageWidth, this.ImageHeight);
                //Shot.GetIt();
                //Bitmap Pic = Shot.DrawBitmap(this.ImageHeight, this.ImageWidth);
                //return Pic;
                return null;
            }
        }
        
        
        
        
        



//--------------------------------------------------------------------------------------------------------------------------




            //DesktopLocation的用法

            richTextBox1.Text += "DesktopLocation = " + this.DesktopLocation.ToString() + "\n";
            richTextBox1.Text += "DesktopLocation = " + this.DesktopLocation.X.ToString() + "\n";
            richTextBox1.Text += "DesktopLocation = " + this.DesktopLocation.Y.ToString() + "\n";


            Point p = new Point(this.DesktopLocation.X - 1, this.DesktopLocation.Y);

            this.DesktopLocation = p;



            //取得某一控件的參數
            //獲取傳入對象的所有屬性名稱
            Type types = button1.GetType();
            foreach (var p in types.GetProperties())
            {
                richTextBox1.Text += "Type : \t" + p.PropertyType + "\tName : \t" + p.Name + "\n";
            }



//指定視窗出現的地方
            Point p = new Point(600, 240);

            this.DesktopLocation = p;




            //C#啟動另外一個C#程序，並傳遞參數
            string filename = @"C:\______test_files\aaaaa4.txt";
            System.Diagnostics.Process.Start("notepad.exe", filename);









//--------------------------------------------------------------------------------------------------------------------------




//--------------------------------------------------------------------------------------------------------------------------




        				
//--------------------------------------------------------------------------------------------------------------------------




//--------------------------------------------------------------------------------------------------------------------------








        				
//--------------------------------------------------------------------------------------------------------------------------




//--------------------------------------------------------------------------------------------------------------------------








        				
//--------------------------------------------------------------------------------------------------------------------------





//--------------------------------------------------------------------------------------------------------------------------





//--------------------------------------------------------------------------------------------------------------------------








        				
//--------------------------------------------------------------------------------------------------------------------------





//--------------------------------------------------------------------------------------------------------------------------





//--------------------------------------------------------------------------------------------------------------------------








        				
//--------------------------------------------------------------------------------------------------------------------------





//--------------------------------------------------------------------------------------------------------------------------





//--------------------------------------------------------------------------------------------------------------------------








        				
//--------------------------------------------------------------------------------------------------------------------------




//--------------------------------------------------------------------------------------------------------------------------


            Cursor.Hide();  //隱藏光標
            Cursor.Show();  //顯示光標




//--------------------------------------------------------------------------------------------------------------------------


          
            
            
                    




        				
//--------------------------------------------------------------------------------------------------------------------------





//--------------------------------------------------------------------------------------------------------------------------








        				
//--------------------------------------------------------------------------------------------------------------------------





//--------------------------------------------------------------------------------------------------------------------------





//--------------------------------------------------------------------------------------------------------------------------








        				
//--------------------------------------------------------------------------------------------------------------------------





//--------------------------------------------------------------------------------------------------------------------------





//--------------------------------------------------------------------------------------------------------------------------







        				
//--------------------------------------------------------------------------------------------------------------------------




//--------------------------------------------------------------------------------------------------------------------------



//--------------------------------------------------------------------------------------------------------------------------



        				
//--------------------------------------------------------------------------------------------------------------------------






//--------------------------------------------------------------------------------------------------------------------------




        				
//--------------------------------------------------------------------------------------------------------------------------





//--------------------------------------------------------------------------------------------------------------------------





//--------------------------------------------------------------------------------------------------------------------------


            int[,] pbox = new int[9, 2];    //[Col,Row]
            richTextBox1.Text += "COLUMN = " + pbox.GetLength(0).ToString() + "\n";    //9
            richTextBox1.Text += "ROW = " + pbox.GetLength(1).ToString() + "\n";    //2






        				
//--------------------------------------------------------------------------------------------------------------------------


Graphics.GetHdc 方法 可以 獲得關聯的設備上下文的句柄
但不知有什麼用途
 
public class GDI
{
    [System.Runtime.InteropServices.DllImport("gdi32.dll")]
    internal static extern bool Rectangle(
       IntPtr hdc,
       int ulCornerX, int ulCornerY,
       int lrCornerX, int lrCornerY);
}
private void Form1_Paint(object sender, PaintEventArgs e)
{
    // Create pen.
    Pen redPen = new Pen(Color.Red, 1);

    // Draw rectangle with GDI+.
    e.Graphics.DrawRectangle(redPen, 10, 10, 100, 50);

    // Get handle to device context.
    IntPtr hdc = e.Graphics.GetHdc();

    // Draw rectangle with GDI using default pen.
    GDI.Rectangle(hdc, 10, 70, 110, 120);

    // Release handle to device context.
    e.Graphics.ReleaseHdc(hdc);
}




//--------------------------------------------------------------------------------------------------------------------------



利用线程的方法 做延时 不卡界面

Thread t = new Thread(o => Thread.Sleep(500));
                    t.Start(this);
                    while (t.IsAlive)
                    {
                        Application.DoEvents();
                    }


 不用线程 也可以这样不卡界面 

public static void Delay(int mm)
        {
            DateTime current = DateTime.Now;
            while (current.AddMilliseconds(mm) > DateTime.Now)
            {
                Application.DoEvents();
            }
            return;
        } 




//--------------------------------------------------------------------------------------------------------------------------


//线程常用的方法

/// <summary>
/// 一个示例方法 - 无参数
/// </summary>
private void TestMethod()
{
    Console.WriteLine("我是测试线程");
}
//无参数线程的创建
Thread Thd = new Thread(TestMethod);

/// <summary>
/// 一个示例方法 - 有参数
/// </summary>
private void TestMethod(int Obj)
{
    Console.WriteLine("我是测试线程");
}
//有参数线程的创建
int Obj = 0;
Thread Thd = new Thread(() => TestMethod(Obj));

//如果要设置线程为MTA模型
Thd.SetApartmentState(ApartmentState.MTA);

//如果设置线程为后台线程（有人说这个就是MTA模型的线程，不过未经考证）
Thd.IsBackground = true;

//设置这个线程的名字
Thd.Name = "MyThread";

//线程激活
Thd.Start();

//线程挂起（类似线程暂停）
Thd.Suspend();

//线程恢复（将挂起线程恢复运行状态）
Thd.Resume();

//线程强制终止（强制退出）
Thd.Abort();
//为了保证线程被终止，要加入一句Join
Thd.Join();

//得到当前线程的名字
string MyThreadName = Thread.CurrentThread.Name;

//判断线程是否存活
if (Thd.IsAlive)
{
    //如果存活，则执行....
}







        				
//--------------------------------------------------------------------------------------------------------------------------

寫日誌範例 : 
2022-04-14 10:03:13 INFO  :VirtualHere Client 5.2.9 starting (Compiled: Feb 14 2022 07:50:45)
2022-04-14 10:03:13 INFO  :Client OS is Windows 10 (build 19044), 64-bit edition
2022-04-14 10:03:13 INFO  :Using config at C:\Users\070601\AppData\Roaming\vhui.ini
2022-04-14 10:03:13 INFO  :IPC available at \\.\pipe\vhclient
2022-04-14 10:03:13 INFO  :Auto-find (Bonjour) on
2022-04-14 10:03:13 INFO  :Auto-find (Bonjour SSL) on
2022-04-14 10:03:15 INFO  :Drivers are up-to-date
2022-04-14 10:03:15 INFO  :Connected to the VirtualHere Client Driver (Version 2)
2022-04-14 10:26:13 ERROR :Data stream corruption, compressedSize=2810554238, uncompressedSize=2827462782
2022-04-14 10:26:25 INFO  :Server ping timeout, shutting down connection 1...





//C# 寫日志文件

public static void WriteLog(string txt)

        {

            try

            {

                string path = Application.StartupPath + @"\log\" + DateTime.Now.ToString("yyyy-MM-dd") + @"\";

                if (!Directory.Exists(path))

                {

                    Directory.CreateDirectory(path);

                }

                path +=  DateTime.Now.ToString("yyyyMMdd") + "-" + DateTime.Now.ToString("HH") + ".txt";

                if (!File.Exists(path))

                {

                    File.Create(path);

                }

                FileStream fs;

                StreamWriter sw;

                fs = new FileStream(path, FileMode.Append);

                sw = new StreamWriter(fs, Encoding.Default);

                sw.Write(DateTime.Now.ToString("HH:mm:ss") + " " + txt + "\r\n");

                sw.Close();

                fs.Close();

            }

            catch (Exception ex)

            {

                WriteLog("程序發生異常（WriteLog）。詳情：" + ex.Message);

            }

        }




//--------------------------------------------------------------------------------------------------------------------------


//如何將List轉換為DataTable

public static DataTable ToDataTable(List<NetworkAdapterInformation> list)
{
	DataTable result = new DataTable();
	if (list.Count > 0)
	{
		PropertyInfo[] propertys = list[0].GetType().GetProperties();
		foreach (PropertyInfo pi in propertys)
		{
			result.Columns.Add(pi.Name, pi.PropertyType);
		}
		for (int i = 0; i < list.Count; i++)
		{
			ArrayList tempList = new ArrayList();
			foreach (PropertyInfo pi in propertys)
			{
				object obj = pi.GetValue(list[i], null);
				tempList.Add(obj);
			}
			object[] array = tempList.ToArray();
			result.LoadDataRow(array, true);
		}
	}
	return result;
}





//--------------------------------------------------------------------------------------------------------------------------

randomrandom




使用 Random 方法產生不重複亂數 

//取得非常random的數字
Random rd = new Random((int)DateTime.Now.Ticks);





/// <summary> 
 /// 生成隨機字符串 
 /// </summary> 
 private class RandomStringGenerator 
 { 
     static readonly Random r = new Random(); 
     const string _chars = "0123456789"; 
     public static string GetRandomString() 
     { 
         char[] buffer = new char[5]; 
         for (int i = 0; i < 5; i++) 
         { 
             buffer[i] = _chars[r.Next(_chars.Length)]; 
          } 
          return new string(buffer); 
      } 
 }





        public static string GetRandomString2(int length)
        {
            var str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
            //var next = new Random();
            Random Rnd = new Random(); //加入Random，產生的數字不會重覆
            var builder = new StringBuilder();
            for (var i = 0; i < length; i++)
            {
                builder.Append(str[Rnd.Next(0, str.Length)]);
            }
            return builder.ToString();
        }



//應該效果不太好
            //Random rnd = new Random();  //亂數產生區塊顏色
            //foreach (DataPoint point in Chart1.Series[Series1].Points)
            //{
            //    //pie 顏色
            //    point.Color = Color.FromArgb(150, rnd.Next(0, 255), rnd.Next(0, 255), rnd.Next(0, 255)); 
            //}


        				
//--------------------------------------------------------------------------------------------------------------------------



直接把DataTable的資料貼到DataGridView上

	//C#之界面上依次出現表格（DataTable和DataGridView提高）
	
	C#之界面上依次出現表格（DataTable和DataGridView提高）
	
	效果圖：
	
	在textBox控件中輸入信息，點擊增加
	
	\
	
	出現如圖：
	
	\
	
	繼續：
	
	\
	
	代碼（沒用csdn插入代碼功能是插入的代碼增刪改不能選中，特別費事，所以下面代碼可能會看的有點亂）：
	
	//創建坡口形式選擇數據表
	dt = new DataTable();
	
	//建九列
	
	dt.Columns.Add("name", typeof(System.String));
	dt.Columns.Add("sex", typeof(System.String));
	dt.Columns.Add("age", typeof(System.String));
	
	//將MongoDB中數據插入到該一行對應的各列中（我這裡是數據存入MongoDB中，在之前取出bson,然後foreach）
	foreach (BsonDocument result in resultList)
	{
	//建一行
	DataRow dr = dt.NewRow();
	//行信息
	dr[0] = 你的數據
	dr[1] = 你的數據
	dr[2] = 你的數據
	//將上述該行加入DataTable中
	dt.Rows.Add(dr);
	
	//綁定在sorce上
	dataGridView1.DataSource = dt;




//--------------------------------------------------------------------------------------------------------------------------





//--------------------------------------------------------------------------------------------------------------------------



C#_把dataTable數據導出到CSV,XLS文件
http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/190579.html
https://blog.csdn.net/happmaoo/article/details/83814604


        				
//--------------------------------------------------------------------------------------------------------------------------


ffmpeg的用法

//從開始分割600秒視頻命令如下：

//從開始的第1分鐘擷取3分鐘影片出來
ffmpeg.exe -ss 00:01:00 -i sample.mp4 -c copy -t 180 cut.mp4
or
ffmpeg.exe -i sample.mp4 -ss 00:01:00 -t 00:03:00 -acodec copy -vcodec copy cut.mp4

//-y : 強制覆蓋檔案
//-i : 要擷取的原始檔案
//-ss : 起始時間
//-t : 擷取長度, -t sec 或 -t hh:mm:ss
//-acodec copy : 音訊編碼格式和來源檔案相同
//-vcodec copy : 影像編碼格式和來源檔案相同



//查看視頻文件的音視頻編解碼格式，視頻時長，比特率等，如下：
ffmpeg.exe -i sample.mp4


ffmpeg.exe -i xxx.mp4 -f mp3 -vn xxx.mp3并回車。
參數解釋：-i表示input，-f表示format，-vn表示video not

//多個mp3文件合并成一個mp3文件
一種方法是連接到一起
ffmpeg64.exe -i "concat:123.mp3|124.mp3" -acodec copy output.mp3
解釋：-i代表輸入參數
          contact:123.mp3|124.mp3代表著需要連接到一起的音頻文件
           -acodec copy output.mp3 重新編碼并復制到新文件中
另一種方法是混合到一起
ffmpeg64.exe -i 124.mp3 -i 123.mp3 -filter_complex amix=inputs=2:duration=first:dropout_transition=2 -f mp3 remix.mp3
解釋：-i代表輸入參數
           -filter_complex ffmpeg濾鏡功能，非常強大，詳細請查看文檔
           amix是混合多個音頻到單個音頻輸出
           inputs=2代表是2個音頻文件，如果更多則代表對應數字
           duration 確定最終輸出文件的長度
               longest(最長)|shortest（最短）|first（第一個文件）
            dropout_transition
The transition time, in seconds, for volume renormalization when an input stream ends. The default value is 2 seconds.
            -f mp3  輸出文件格式
音頻文件截取指定時間部分
ffmpeg64.exe -i 124.mp3 -vn -acodec copy -ss 00:00:00 -t 00:01:32 output.mp3
解釋：-i代表輸入參數
          -acodec copy output.mp3 重新編碼并復制到新文件中
           -ss 開始截取的時間點
           -t 截取音頻時間長度
           
音頻文件格式轉換
ffmpeg64.exe -i null.ape -ar 44100 -ac 2 -ab 16k -vol 50 -f mp3 null.mp3
解釋：-i代表輸入參數
           -acodec aac（音頻編碼用AAC） 
          -ar 設置音頻采樣頻率
          -ac  設置音頻通道數
          -ab 設定聲音比特率
           -vol <百分比> 設定音量



        				
//--------------------------------------------------------------------------------------------------------------------------



    /// <summary>
    /// 图片处理
    /// http://www.cnblogs.com/wu-jian/
    /// 
    /// 吴剑 2011-02-20 创建
    /// 吴剑 2012-08-08 修改
    /// </summary>
    public class Image
    {
        #region 正方型裁剪并缩放

        /// <summary>
        /// 正方型裁剪
        /// 以图片中心为轴心，截取正方型，然后等比缩放
        /// 用于头像处理
        /// </summary>
        /// <remarks>吴剑 2012-08-08</remarks>
        /// <param name="fromFile">原图Stream对象</param>
        /// <param name="fileSaveUrl">缩略图存放地址</param>
        /// <param name="side">指定的边长（正方型）</param>
        /// <param name="quality">质量（范围0-100）</param>
        public static void CutForSquare(Stream fromFile, string fileSaveUrl, int side, int quality)
        {
            //创建目录
            string dir = Path.GetDirectoryName(fileSaveUrl);
            if (!Directory.Exists(dir))
                Directory.CreateDirectory(dir);

            //原始图片（获取原始图片创建对象，并使用流中嵌入的颜色管理信息）
            System.Drawing.Image initImage = System.Drawing.Image.FromStream(fromFile, true);

            //原图宽高均小于模版，不作处理，直接保存
            if (initImage.Width <= side && initImage.Height <= side)
            {
                initImage.Save(fileSaveUrl, System.Drawing.Imaging.ImageFormat.Jpeg);
            }
            else
            {
                //原始图片的宽、高
                int initWidth = initImage.Width;
                int initHeight = initImage.Height;

                //非正方型先裁剪为正方型
                if (initWidth != initHeight)
                {
                    //截图对象
                    System.Drawing.Image pickedImage = null;
                    System.Drawing.Graphics pickedG = null;

                    //宽大于高的横图
                    if (initWidth > initHeight)
                    {
                        //对象实例化
                        pickedImage = new System.Drawing.Bitmap(initHeight, initHeight);
                        pickedG = System.Drawing.Graphics.FromImage(pickedImage);
                        //设置质量
                        pickedG.InterpolationMode = System.Drawing.Drawing2D.InterpolationMode.HighQualityBicubic;
                        pickedG.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.HighQuality;
                        //定位
                        Rectangle fromR = new Rectangle((initWidth - initHeight) / 2, 0, initHeight, initHeight);
                        Rectangle toR = new Rectangle(0, 0, initHeight, initHeight);
                        //画图
                        pickedG.DrawImage(initImage, toR, fromR, System.Drawing.GraphicsUnit.Pixel);
                        //重置宽
                        initWidth = initHeight;
                    }
                    //高大于宽的竖图
                    else
                    {
                        //对象实例化
                        pickedImage = new System.Drawing.Bitmap(initWidth, initWidth);
                        pickedG = System.Drawing.Graphics.FromImage(pickedImage);
                        //设置质量
                        pickedG.InterpolationMode = System.Drawing.Drawing2D.InterpolationMode.HighQualityBicubic;
                        pickedG.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.HighQuality;
                        //定位
                        Rectangle fromR = new Rectangle(0, (initHeight - initWidth) / 2, initWidth, initWidth);
                        Rectangle toR = new Rectangle(0, 0, initWidth, initWidth);
                        //画图
                        pickedG.DrawImage(initImage, toR, fromR, System.Drawing.GraphicsUnit.Pixel);
                        //重置高
                        initHeight = initWidth;
                    }

                    //将截图对象赋给原图
                    initImage = (System.Drawing.Image)pickedImage.Clone();
                    //释放截图资源
                    pickedG.Dispose();
                    pickedImage.Dispose();
                }

                //缩略图对象
                System.Drawing.Image resultImage = new System.Drawing.Bitmap(side, side);
                System.Drawing.Graphics resultG = System.Drawing.Graphics.FromImage(resultImage);
                //设置质量
                resultG.InterpolationMode = System.Drawing.Drawing2D.InterpolationMode.HighQualityBicubic;
                resultG.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.HighQuality;
                //用指定背景色清空画布
                resultG.Clear(Color.White);
                //绘制缩略图
                resultG.DrawImage(initImage, new System.Drawing.Rectangle(0, 0, side, side), new System.Drawing.Rectangle(0, 0, initWidth, initHeight), System.Drawing.GraphicsUnit.Pixel);

                //关键质量控制
                //获取系统编码类型数组,包含了jpeg,bmp,png,gif,tiff
                ImageCodecInfo[] icis = ImageCodecInfo.GetImageEncoders();
                ImageCodecInfo ici = null;
                foreach (ImageCodecInfo i in icis)
                {
                    if (i.MimeType == "image/jpeg" || i.MimeType == "image/bmp" || i.MimeType == "image/png" || i.MimeType == "image/gif")
                    {
                        ici = i;
                    }
                }
                EncoderParameters ep = new EncoderParameters(1);
                ep.Param[0] = new EncoderParameter(System.Drawing.Imaging.Encoder.Quality, (long)quality);

                //保存缩略图
                resultImage.Save(fileSaveUrl, ici, ep);

                //释放关键质量控制所用资源
                ep.Dispose();

                //释放缩略图资源
                resultG.Dispose();
                resultImage.Dispose();

                //释放原始图片资源
                initImage.Dispose();
            }
        }

        #endregion

        #region 自定义裁剪并缩放

        /// <summary>
        /// 指定长宽裁剪
        /// 按模版比例最大范围的裁剪图片并缩放至模版尺寸
        /// </summary>
        /// <remarks>吴剑 2012-08-08</remarks>
        /// <param name="fromFile">原图Stream对象</param>
        /// <param name="fileSaveUrl">保存路径</param>
        /// <param name="maxWidth">最大宽(单位:px)</param>
        /// <param name="maxHeight">最大高(单位:px)</param>
        /// <param name="quality">质量（范围0-100）</param>
        public static void CutForCustom(Stream fromFile, string fileSaveUrl, int maxWidth, int maxHeight, int quality)
        {
            //从文件获取原始图片，并使用流中嵌入的颜色管理信息
            System.Drawing.Image initImage = System.Drawing.Image.FromStream(fromFile, true);

            //原图宽高均小于模版，不作处理，直接保存
            if (initImage.Width <= maxWidth && initImage.Height <= maxHeight)
            {
                initImage.Save(fileSaveUrl, System.Drawing.Imaging.ImageFormat.Jpeg);
            }
            else
            {
                //模版的宽高比例
                double templateRate = (double)maxWidth / maxHeight;
                //原图片的宽高比例
                double initRate = (double)initImage.Width / initImage.Height;

                //原图与模版比例相等，直接缩放
                if (templateRate == initRate)
                {
                    //按模版大小生成最终图片
                    System.Drawing.Image templateImage = new System.Drawing.Bitmap(maxWidth, maxHeight);
                    System.Drawing.Graphics templateG = System.Drawing.Graphics.FromImage(templateImage);
                    templateG.InterpolationMode = System.Drawing.Drawing2D.InterpolationMode.High;
                    templateG.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.HighQuality;
                    templateG.Clear(Color.White);
                    templateG.DrawImage(initImage, new System.Drawing.Rectangle(0, 0, maxWidth, maxHeight), new System.Drawing.Rectangle(0, 0, initImage.Width, initImage.Height), System.Drawing.GraphicsUnit.Pixel);
                    templateImage.Save(fileSaveUrl, System.Drawing.Imaging.ImageFormat.Jpeg);
                }
                //原图与模版比例不等，裁剪后缩放
                else
                {
                    //裁剪对象
                    System.Drawing.Image pickedImage = null;
                    System.Drawing.Graphics pickedG = null;

                    //定位
                    Rectangle fromR = new Rectangle(0, 0, 0, 0);//原图裁剪定位
                    Rectangle toR = new Rectangle(0, 0, 0, 0);//目标定位

                    //宽为标准进行裁剪
                    if (templateRate > initRate)
                    {
                        //裁剪对象实例化
                        pickedImage = new System.Drawing.Bitmap(initImage.Width, (int)System.Math.Floor(initImage.Width / templateRate));
                        pickedG = System.Drawing.Graphics.FromImage(pickedImage);

                        //裁剪源定位
                        fromR.X = 0;
                        fromR.Y = (int)System.Math.Floor((initImage.Height - initImage.Width / templateRate) / 2);
                        fromR.Width = initImage.Width;
                        fromR.Height = (int)System.Math.Floor(initImage.Width / templateRate);

                        //裁剪目标定位
                        toR.X = 0;
                        toR.Y = 0;
                        toR.Width = initImage.Width;
                        toR.Height = (int)System.Math.Floor(initImage.Width / templateRate);
                    }
                    //高为标准进行裁剪
                    else
                    {
                        pickedImage = new System.Drawing.Bitmap((int)System.Math.Floor(initImage.Height * templateRate), initImage.Height);
                        pickedG = System.Drawing.Graphics.FromImage(pickedImage);

                        fromR.X = (int)System.Math.Floor((initImage.Width - initImage.Height * templateRate) / 2);
                        fromR.Y = 0;
                        fromR.Width = (int)System.Math.Floor(initImage.Height * templateRate);
                        fromR.Height = initImage.Height;

                        toR.X = 0;
                        toR.Y = 0;
                        toR.Width = (int)System.Math.Floor(initImage.Height * templateRate);
                        toR.Height = initImage.Height;
                    }

                    //设置质量
                    pickedG.InterpolationMode = System.Drawing.Drawing2D.InterpolationMode.HighQualityBicubic;
                    pickedG.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.HighQuality;

                    //裁剪
                    pickedG.DrawImage(initImage, toR, fromR, System.Drawing.GraphicsUnit.Pixel);

                    //按模版大小生成最终图片
                    System.Drawing.Image templateImage = new System.Drawing.Bitmap(maxWidth, maxHeight);
                    System.Drawing.Graphics templateG = System.Drawing.Graphics.FromImage(templateImage);
                    templateG.InterpolationMode = System.Drawing.Drawing2D.InterpolationMode.High;
                    templateG.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.HighQuality;
                    templateG.Clear(Color.White);
                    templateG.DrawImage(pickedImage, new System.Drawing.Rectangle(0, 0, maxWidth, maxHeight), new System.Drawing.Rectangle(0, 0, pickedImage.Width, pickedImage.Height), System.Drawing.GraphicsUnit.Pixel);

                    //关键质量控制
                    //获取系统编码类型数组,包含了jpeg,bmp,png,gif,tiff
                    ImageCodecInfo[] icis = ImageCodecInfo.GetImageEncoders();
                    ImageCodecInfo ici = null;
                    foreach (ImageCodecInfo i in icis)
                    {
                        if (i.MimeType == "image/jpeg" || i.MimeType == "image/bmp" || i.MimeType == "image/png" || i.MimeType == "image/gif")
                        {
                            ici = i;
                        }
                    }
                    EncoderParameters ep = new EncoderParameters(1);
                    ep.Param[0] = new EncoderParameter(System.Drawing.Imaging.Encoder.Quality, (long)quality);

                    //保存缩略图
                    templateImage.Save(fileSaveUrl, ici, ep);
                    //templateImage.Save(fileSaveUrl, System.Drawing.Imaging.ImageFormat.Jpeg);

                    //释放资源
                    templateG.Dispose();
                    templateImage.Dispose();

                    pickedG.Dispose();
                    pickedImage.Dispose();
                }
            }

            //释放资源
            initImage.Dispose();
        }
        #endregion

        #region 等比缩放

        /// <summary>
        /// 图片等比缩放
        /// </summary>
        /// <remarks>吴剑 2012-08-08</remarks>
        /// <param name="fromFile">原图Stream对象</param>
        /// <param name="savePath">缩略图存放地址</param>
        /// <param name="targetWidth">指定的最大宽度</param>
        /// <param name="targetHeight">指定的最大高度</param>
        /// <param name="watermarkText">水印文字(为""表示不使用水印)</param>
        /// <param name="watermarkImage">水印图片路径(为""表示不使用水印)</param>
        public static void ZoomAuto(Stream fromFile, string savePath, System.Double targetWidth, System.Double targetHeight, string watermarkText, string watermarkImage)
        {
            //创建目录
            string dir = Path.GetDirectoryName(savePath);
            if (!Directory.Exists(dir))
                Directory.CreateDirectory(dir);

            //原始图片（获取原始图片创建对象，并使用流中嵌入的颜色管理信息）
            System.Drawing.Image initImage = System.Drawing.Image.FromStream(fromFile, true);

            //原图宽高均小于模版，不作处理，直接保存
            if (initImage.Width <= targetWidth && initImage.Height <= targetHeight)
            {
                //文字水印
                if (watermarkText != "")
                {
                    using (System.Drawing.Graphics gWater = System.Drawing.Graphics.FromImage(initImage))
                    {
                        System.Drawing.Font fontWater = new Font("黑体", 10);
                        System.Drawing.Brush brushWater = new SolidBrush(Color.White);
                        gWater.DrawString(watermarkText, fontWater, brushWater, 10, 10);
                        gWater.Dispose();
                    }
                }

                //透明图片水印
                if (watermarkImage != "")
                {
                    if (File.Exists(watermarkImage))
                    {
                        //获取水印图片
                        using (System.Drawing.Image wrImage = System.Drawing.Image.FromFile(watermarkImage))
                        {
                            //水印绘制条件：原始图片宽高均大于或等于水印图片
                            if (initImage.Width >= wrImage.Width && initImage.Height >= wrImage.Height)
                            {
                                Graphics gWater = Graphics.FromImage(initImage);

                                //透明属性
                                ImageAttributes imgAttributes = new ImageAttributes();
                                ColorMap colorMap = new ColorMap();
                                colorMap.OldColor = Color.FromArgb(255, 0, 255, 0);
                                colorMap.NewColor = Color.FromArgb(0, 0, 0, 0);
                                ColorMap[] remapTable = { colorMap };
                                imgAttributes.SetRemapTable(remapTable, ColorAdjustType.Bitmap);

                                float[][] colorMatrixElements = { 
                                   new float[] {1.0f,  0.0f,  0.0f,  0.0f, 0.0f},
                                   new float[] {0.0f,  1.0f,  0.0f,  0.0f, 0.0f},
                                   new float[] {0.0f,  0.0f,  1.0f,  0.0f, 0.0f},
                                   new float[] {0.0f,  0.0f,  0.0f,  0.5f, 0.0f},//透明度:0.5
                                   new float[] {0.0f,  0.0f,  0.0f,  0.0f, 1.0f}
                                };

                                ColorMatrix wmColorMatrix = new ColorMatrix(colorMatrixElements);
                                imgAttributes.SetColorMatrix(wmColorMatrix, ColorMatrixFlag.Default, ColorAdjustType.Bitmap);
                                gWater.DrawImage(wrImage, new Rectangle(initImage.Width - wrImage.Width, initImage.Height - wrImage.Height, wrImage.Width, wrImage.Height), 0, 0, wrImage.Width, wrImage.Height, GraphicsUnit.Pixel, imgAttributes);

                                gWater.Dispose();
                            }
                            wrImage.Dispose();
                        }
                    }
                }

                //保存
                initImage.Save(savePath, System.Drawing.Imaging.ImageFormat.Jpeg);
            }
            else
            {
                //缩略图宽、高计算
                double newWidth = initImage.Width;
                double newHeight = initImage.Height;

                //宽大于高或宽等于高（横图或正方）
                if (initImage.Width > initImage.Height || initImage.Width == initImage.Height)
                {
                    //如果宽大于模版
                    if (initImage.Width > targetWidth)
                    {
                        //宽按模版，高按比例缩放
                        newWidth = targetWidth;
                        newHeight = initImage.Height * (targetWidth / initImage.Width);
                    }
                }
                //高大于宽（竖图）
                else
                {
                    //如果高大于模版
                    if (initImage.Height > targetHeight)
                    {
                        //高按模版，宽按比例缩放
                        newHeight = targetHeight;
                        newWidth = initImage.Width * (targetHeight / initImage.Height);
                    }
                }

                //生成新图
                //新建一个bmp图片
                System.Drawing.Image newImage = new System.Drawing.Bitmap((int)newWidth, (int)newHeight);
                //新建一个画板
                System.Drawing.Graphics newG = System.Drawing.Graphics.FromImage(newImage);

                //设置质量
                newG.InterpolationMode = System.Drawing.Drawing2D.InterpolationMode.HighQualityBicubic;
                newG.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.HighQuality;

                //置背景色
                newG.Clear(Color.White);
                //画图
                newG.DrawImage(initImage, new System.Drawing.Rectangle(0, 0, newImage.Width, newImage.Height), new System.Drawing.Rectangle(0, 0, initImage.Width, initImage.Height), System.Drawing.GraphicsUnit.Pixel);

                //文字水印
                if (watermarkText != "")
                {
                    using (System.Drawing.Graphics gWater = System.Drawing.Graphics.FromImage(newImage))
                    {
                        System.Drawing.Font fontWater = new Font("宋体", 10);
                        System.Drawing.Brush brushWater = new SolidBrush(Color.White);
                        gWater.DrawString(watermarkText, fontWater, brushWater, 10, 10);
                        gWater.Dispose();
                    }
                }

                //透明图片水印
                if (watermarkImage != "")
                {
                    if (File.Exists(watermarkImage))
                    {
                        //获取水印图片
                        using (System.Drawing.Image wrImage = System.Drawing.Image.FromFile(watermarkImage))
                        {
                            //水印绘制条件：原始图片宽高均大于或等于水印图片
                            if (newImage.Width >= wrImage.Width && newImage.Height >= wrImage.Height)
                            {
                                Graphics gWater = Graphics.FromImage(newImage);

                                //透明属性
                                ImageAttributes imgAttributes = new ImageAttributes();
                                ColorMap colorMap = new ColorMap();
                                colorMap.OldColor = Color.FromArgb(255, 0, 255, 0);
                                colorMap.NewColor = Color.FromArgb(0, 0, 0, 0);
                                ColorMap[] remapTable = { colorMap };
                                imgAttributes.SetRemapTable(remapTable, ColorAdjustType.Bitmap);

                                float[][] colorMatrixElements = { 
                                   new float[] {1.0f,  0.0f,  0.0f,  0.0f, 0.0f},
                                   new float[] {0.0f,  1.0f,  0.0f,  0.0f, 0.0f},
                                   new float[] {0.0f,  0.0f,  1.0f,  0.0f, 0.0f},
                                   new float[] {0.0f,  0.0f,  0.0f,  0.5f, 0.0f},//透明度:0.5
                                   new float[] {0.0f,  0.0f,  0.0f,  0.0f, 1.0f}
                                };

                                ColorMatrix wmColorMatrix = new ColorMatrix(colorMatrixElements);
                                imgAttributes.SetColorMatrix(wmColorMatrix, ColorMatrixFlag.Default, ColorAdjustType.Bitmap);
                                gWater.DrawImage(wrImage, new Rectangle(newImage.Width - wrImage.Width, newImage.Height - wrImage.Height, wrImage.Width, wrImage.Height), 0, 0, wrImage.Width, wrImage.Height, GraphicsUnit.Pixel, imgAttributes);
                                gWater.Dispose();
                            }
                            wrImage.Dispose();
                        }
                    }
                }

                //保存缩略图
                newImage.Save(savePath, System.Drawing.Imaging.ImageFormat.Jpeg);

                //释放资源
                newG.Dispose();
                newImage.Dispose();
                initImage.Dispose();
            }
        }

        #endregion

        #region 其它

        /// <summary>
        /// 判断文件类型是否为WEB格式图片
        /// (注：JPG,GIF,BMP,PNG)
        /// </summary>
        /// <param name="contentType">HttpPostedFile.ContentType</param>
        /// <returns></returns>
        public static bool IsWebImage(string contentType)
        {
            if (contentType == "image/pjpeg" || contentType == "image/jpeg" || contentType == "image/gif" || contentType == "image/bmp" || contentType == "image/png")
            {
                return true;
            }
            else
            {
                return false;
            }
        }

        #endregion

    }//end class





        				
//--------------------------------------------------------------------------------------------------------------------------




old 暫存一下
        private void button5_Click(object sender, EventArgs e)
        {
            //广东省深圳市福田区华强北路1002号

            string address = "广东省深圳市福田区华强北路1002号";

            if (!string.IsNullOrEmpty(address))
            {
                richTextBox1.Text += "你按了 地址解析 之 查詢\t地址 : " + address + "\n";

                this.routeOverlay.Markers.Clear();
                Placemark placemark = new Placemark(address);

                richTextBox1.Text += "初始化就給值 Text : " + placemark.Address + "\n";

                //placemark.CityName = currentCenterCityName;   //useless

                //richTextBox1.Text += "currentCenterCityName : " + currentCenterCityName + "\n";   尚未給值

                if (currentAreaPolygon != null)
                {
                    placemark.CityName = currentAreaPolygon.Name;
                }

                //richTextBox1.Text += "placemark.CityName : " + placemark.CityName + "\n"; 無資料

                List<PointLatLng> points = new List<PointLatLng>();
                //GeoCoderStatusCode statusCode = SoSoMapProvider.Instance.GetPoints(placemark, out points);
                GeoCoderStatusCode statusCode = AMapProvider.Instance.GetPoints(placemark, out points);

                //richTextBox1.Text += "Text : " + placemark.Address + "\n";

                if (statusCode == GeoCoderStatusCode.G_GEO_SUCCESS)
                {
                    richTextBox1.Text += "查詢資料成功, 共有" + points.Count.ToString() + " 筆資料\n";
                    foreach (PointLatLng point in points)
                    {
                        richTextBox1.Text += "取得地圖資料 地理座標 " + point.ToString() + "\n";
                        GMarkerGoogle marker = new GMarkerGoogle(point, GMarkerGoogleType.red_dot);

                        marker.ToolTipText = placemark.Address;
                        this.routeOverlay.Markers.Add(marker);
                        this.gMapControl1.Position = point;

                        richTextBox1.Text += "Text1 : " + placemark.Address + "\n";

                        /*  除了第一項，全無資料
                        richTextBox1.Text += "Text2 : " + placemark.AdministrativeAreaName + "\n";
                        richTextBox1.Text += "Text3 : " + placemark.CityName.ToString() + "\n";
                        richTextBox1.Text += "Text4 : " + placemark.CountryName + "\n";
                        richTextBox1.Text += "Text5 : " + placemark.DistrictName + "\n";
                        richTextBox1.Text += "Text6 : " + placemark.HouseNo.ToString() + "\n";
                        richTextBox1.Text += "Text7 : " + placemark.LocalityName + "\n";
                        richTextBox1.Text += "Text8 : " + placemark.Name.ToString() + "\n";
                        richTextBox1.Text += "Text9 : " + placemark.Neighborhood + "\n";
                        richTextBox1.Text += "Text10 : " + placemark.ProvinceName.ToString() + "\n";

                        richTextBox1.Text += "Text9 : " + placemark.StreetNumber.ToString() + "\n";
                        richTextBox1.Text += "Text9 : " + placemark.SubAdministrativeAreaName + "\n";
                        richTextBox1.Text += "Text9 : " + placemark.Tel.ToString() + "\n";
                        richTextBox1.Text += "Text9 : " + placemark.ThoroughfareName + "\n";
                        */
                    }
                }
                else
                {
                    richTextBox1.Text += "查詢資料失敗\n";
                }
            }
            else
            {
                richTextBox1.Text += "地址無資料\n";
            }
        }






        				
//--------------------------------------------------------------------------------------------------------------------------






        				
//--------------------------------------------------------------------------------------------------------------------------









        				
//--------------------------------------------------------------------------------------------------------------------------






        				
//--------------------------------------------------------------------------------------------------------------------------









        				
//--------------------------------------------------------------------------------------------------------------------------






        				
//--------------------------------------------------------------------------------------------------------------------------










        				
//--------------------------------------------------------------------------------------------------------------------------






        				
//--------------------------------------------------------------------------------------------------------------------------











        				
//--------------------------------------------------------------------------------------------------------------------------






        				
//--------------------------------------------------------------------------------------------------------------------------








richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個


richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個


richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個



.net 4.5中新增了async和await這一對用於異步編程的關鍵字。




            string filename = @"C:\______test_files\_case1\pic1.jpg";
            FileStream fs = File.OpenRead(filename); //OpenRead[二進位讀檔]
            int filelength = 0;
            filelength = (int)fs.Length; //獲得檔長度
            Byte[] image = new Byte[filelength]; //建立一個位元組陣列
            fs.Read(image, 0, filelength); //按位元組流讀取
            System.Drawing.Image result = System.Drawing.Image.FromStream(fs);
            fs.Close();

            //pictureBox1.Image = (Image)image;




.Net 知識家
https://dotblogs.com.tw/hung-chin



vcs的textBox、richTextBox顯示文字都是用Unicode顯示，這樣才可以顯示各種編碼文字
也可利用打印unicode編碼打印出各種特殊文字

可指明其他編碼打印文字





經緯度距離計算
http://m4.hhlink.com/%E7%BB%8F%E7%BA%AC%E5%BA%A6

r=6371;
2*pi*r/360

平均半徑	6,371.0 km（3,958.8 mi）
赤道半徑	6,378.1 km（3,963.2 mi）
極半徑	6,356.8 km（3,949.9 mi）
扁率	0.0033528
1/298.257222101（ETRS89）
周長	40,075.017 km（24,901.461 mi）赤道
40,007.86 km（24,859.73 mi）子午線


vcs進行圖像處理的幾種方法
C#進行圖像處理的幾種方法（bitmap，bitmapData,IntPtr）
https://www.twblogs.net/a/5b8a94922b71775d1ce7e03d


JPG 檔案：開頭 Byte 為 FF D8

BMP 檔案：開頭 Byte 為 42 4D

GIF 檔案：開頭 Byte 為 47 49 46

PNG 檔案：開頭 Byte 為 89 50 4E 47 0D 0A 1A 0A

Encoding.GetEncoding big5 gb2312 shift_jis UTF-8 unicode

test write
StreamWriter swAcqflg = new StreamWriter(strFilePath + strFileName, false, System.Text.Encoding.GetEncoding("big5"));


StreamWriter sw = new StreamWriter(fs, Encoding.GetEncoding("utf-8"));   //指名編碼格式 the same
StreamWriter sw = new StreamWriter(fs, Encoding.GetEncoding("UTF-8"));    //指名編碼格式
StreamWriter sw = new StreamWriter(fs, Encoding.GetEncoding("unicode"));   //指名編碼格式
StreamWriter sw = new StreamWriter(fs, Encoding.UTF8);    //指名編碼格式


byte[] unknow = Encoding.GetEncoding("Big5").GetBytes(strBig5);  // 繁體中文 (Big5) 
return Encoding.GetEncoding("gb2312").GetString(unknow); // 簡體中文 (GB2312) 
StreamReader(fs, Encoding.GetEncoding("gb2312"));	    //

byte[] unknow = Encoding.GetEncoding("Big5").GetBytes(strBig5);  // 繁體中文 (Big5) 
return Encoding.GetEncoding("gb2312").GetString(unknow); // 簡體中文 (GB2312) 
byte[] bytes = Encoding.GetEncoding("GB2312").GetBytes(word);

Encoding enc = Encoding.GetEncoding("BIG5");
Encoding enc = Encoding.GetEncoding("GB2312");


大小寫不拘

//StreamWriter sw = new StreamWriter(File.Open(filename, FileMode.Create), Encoding.GetEncoding("UTF-8"));    //指名編碼格式
            var hopefullyRecovered = Encoding.GetEncoding(1252).GetBytes(badstringFromDatabase);
            StreamWriter sw = new StreamWriter(fs, System.Text.Encoding.GetEncoding("unicode"));   //指名編碼格式

打印字串的編碼值

            int i;
            for (i = 0; i < Info.Length; i++)
            {
                //richTextBox1.Text += Info[i].ToString() + "\n";
                //richTextBox1.Text += ((int)Info[i]).ToString("X2") + " ";
            }

                string filename = "02 渡り鳥仁義(1984.07.01-候鳥仁義).mp3";
                for (i = 0; i < filename.Length; i++)
                {
                    //richTextBox1.Text += filename[i].ToString() + "\n";
                    richTextBox1.Text += ((int)filename[i]).ToString("X2") + " ";
                }
        

            string tmp_string = "春花秋月何時了";
            richTextBox1.Text += button18.Text + "\n";
            richTextBox1.Text += tmp_string + "\n";
            Graphics g2 = richTextBox1.CreateGraphics();
            Size sss = g2.MeasureString(tmp_string, richTextBox1.Font).ToSize();
            richTextBox1.Text += "size W = " + sss.Width.ToString() + "\n";
            richTextBox1.Text += "size H = " + sss.Height.ToString() + "\n";

            f = new Font("Arial", 128);
            g.DrawString("A", f, sb, new PointF(0, 0));

            //Graphics g2 = richTextBox1.CreateGraphics();
            sss = g.MeasureString("A", f).ToSize();
            richTextBox1.Text += "size f = " + f.Size.ToString() + "\t";
            richTextBox1.Text += "size W = " + sss.Width.ToString() + "\t";
            richTextBox1.Text += "size H = " + sss.Height.ToString() + "\n";

'




vcs
https://www.itread01.com/content/1549838013.html




vcs可否取得Windows的安裝時間
vcs可否達到systeminfo之資訊 
 



無論上下次序，TextBox/RichTextBox會吃到方向鍵


網頁加密驗證協定TLS (Transport Layer Security) 1.0及1.1版	停止支援

DateTime 是一個結構型態的實值型別，是用來表示日期和時間的物件，具有以下幾個特性：
1. 可記錄範圍：0001/1/1 12:00:00 AM ～ 9999/12/31 11:59:59 PM
2. 時間值是以刻度（Tick）為最小單位，每個 Tick 等於 100 奈秒。
3. Tick 值由 0001/1/1 12:00:00 AM 開始累加計算，每 100 奈秒，Tick 值加一。
所以內建的DateTime無法處理西元前的時間

String to DateTime
1. Parse ：將指定的日期時間字串，轉換成相對應的 DateTime 型別。若轉換失敗會產生 FormatException 。
2. TryParse ：將指定的日期時間字串，轉換成相對應的 DateTime 型別，回傳值表示轉換是否成功。
3. ParseExact ：將指定的日期時間字串，轉換成相對應的 DateTime 型別，字串表示的格式必須完全符合指定的格式，否則會擲回例外狀況。
4. TryParseExact ：將指定的日期時間字串，轉換成相對應的 DateTime 型別，字串表示的格式必須完全符合指定的格式，回傳值表示轉換是否成功。





Windows Task Scheduler). I am currently using Process.Start() to launch the file (or exe) required by th



Process myProcess = Process.Start("param1", "param2");
if (myProcess != null && !myProcess.HasExited)
  newProcess.Kill();
  
            if ((myProcess != null) && (!myProcess.HasExited))
                myProcess.Kill();


process.start加參數

  
  proc = Process.Start("C:\Program Files\Windows Media Player\wmplayer.exe", filename)

Then you can kill it normally.

proc.Kill()
  
  
  
		richTextBox1.Text += "系統啟動後經過的時間： " + (Environment.TickCount / 1000).ToString() + "秒" + "\n";

richTextBox1.Text += "程式啟動時間: " + start_time.ToString() + " 秒\n";




timer中斷中
如果把Focus()改成若非Focused再Focus()
看這樣會不會比較順


vcs


如何得知richtextbox當時的游標位置

這樣才可以從特定點開始搜尋，不用總是從頭開始搜尋


richtextbox範例 for 搜尋

load一檔
從頭搜尋到尾 搜尋到的字串變色。

 








this.close() ; //關閉視窗
Application.Exit() ; //結束程序

現在都習慣直接強制離開
Environment.Exit(0);



LargeImageList

這個屬性包含ImageList,而ImageList包含大影象。這些影象可以在View屬性為LargeIcon時使用。


SmallImageList

當View屬性為SmaillIcon時,這個屬性包含了ImageList,其中ImageList包含了要使用的影象



LabelWrap

為True時,標籤會自動換行,以顯示所有文字

LabelEdit

為True時,使用者可以在Details檢視下編輯第一列的內容


MultiSelect

可以多選

Scrollabel

顯示滾動條



View

列表檢視可以用4種不同的模式顯示其選項:

LargeIcon:所有選項都在其旁邊顯示一個大圖示(32*32)和一個標籤

SamllIcon:所有選項都在其旁邊顯示一個小圖示(32*16)和一個標籤

List:只顯示一列。該列可以包含一個圖示和一個標籤

Details:可以顯示任意數量的列。只有第一列可以包含圖示

Tile:(只用於WindowsXp和較新的Windwos平臺)顯示一個大圖示和一個標籤,在圖示的右邊顯示子項資訊


BeginUpdate

開始更新,直到呼叫EndUpdate為止。當一次插入多個選項使用這個方法很有用,因為它會禁止檢視閃爍,並可以大大提高速度
EndUpdate

結束更新





C# listview中顯示imagelist中的圖片
https://www.itread01.com/content/1546725619.html





vcs參考code

IsDigit
                    for (int i = 0; i < BytesToRead_tmp; i++)
                    {
                        if (char.IsDigit((char)receive_buffer_tmp[i]) == true)
                        {
                            richTextBox1.Text += receive_buffer_tmp[i] + " ";
                        }
                        else
                            richTextBox1.Text += ". ";
                    }


        //C# 獲取MP3 資訊
            //所以，我們只要把MP3檔的最後128個位元組分段讀出來並保存到該結構裡就可以了。函式定義如下：
            private byte[] getLast128(string FileName)
            {
                FileStream fs = new FileStream(FileName, FileMode.Open, FileAccess.Read);
                Stream stream = fs;
                stream.Seek(-128, SeekOrigin.End);
                const int seekPos = 128;
                int rl = 0;
                byte[] Info = new byte[seekPos];
                rl = stream.Read(Info, 0, seekPos);
                fs.Close();
                stream.Close();
                return Info;
            }





C#中如何獲取一個二維陣列的兩維長度，即行數和列數？


int[,] array = new int[,] {{1,2,3},{4,5,6},{7,8,9}};//定義一個3行3列的二維陣列
int row = array.Rank;//獲取行數
int col = array.GetLength(1);//獲取指定維中的元 個數，這裡也就是列數了。（1表示的是第二維，0是第一維）
int col = array.GetUpperBound(0)+1;//獲取指定維度的上限，在 上一個1就是列數
int num = array.Length;//獲取整個二維陣列的長度，即所有元 的個數






1，Tag这个属性是留给程序员自己用的，也就是说你可以自己做点标记   

比如说一个窗体上有N个控件，你让TextBox1.Tag   =   "123";   Button1.Tag   =   "123";   
将来你可以遍历窗体的控件，如果某个控件的Tag   =   "123";，你就可以做点事情，比如把他们都禁用，所以说他们就像是给你留的一个标记

2，我的习惯是把一个对象赋值给tag。比如文本框显示员工姓名，那么这个文本框的tag就是   
那个员工对象，这样我就很容易知道名字是谁的。

 tag本身是“标签”的意思，顾名思义，就是给控件打上标签。
当项目中有很多类型名称各不相同的控件时，可以将这些控件打上相同的标签，即，将控件的tag值设置为同一个值，如，hide、TLB等等，然后用一段代码，进行相应的操作，如下：




vcs_Oscilloscope



圖表解決方案【Microsoft Chart Controls】


Microsoft Visual Studio (2008版本以上)

Microsoft Chart Controls (For .Net FrameWork3.5，若專案使用.Net FrameWork 4.0 以上不須安裝，專案設定引用反而會出錯，原因是後續的版本已經內含了，額外引用會造成抓取元件衝突)


.Net 讀取、修改、複製 照片資訊 EXIF 使用 ExifLibrary
https://www.ez2o.com/Blog/Post/csharp-Read-Image-EXIF-ExifLibrary

參考/加入參考/ExifLibrary.dll


C# 呼叫 Matlab Function
要新版的Matlab 2015a才可以 + VS2015
http://oblivious9.pixnet.net/blog/post/215744828-c%23-%e5%91%bc%e5%8f%ab-matlab-function



 MouseWheel事項不會出現在IDE的事件中。必需自己手動加進來。
this.tcResult.MouseWheel += new MouseEventHandler(tcResult_MouseWheel);
而且PictureBox及TabPage無法收到MouseWheel的事件。 	


列舉系統的所有Color並以ComboBox顯示

comboBox自行繪制顯示的內容，在這邊需要將comboBox中的屬性'DrawMode'設為'OwnerDrawFixed'，並新的DrawItem事件





#region 是 C# 預處理器指令。
#region 是一個分塊預處理命令，它主要是用於編輯器代碼的分塊，在編譯時會被自動刪除。




C# Debug的方法，可以將debug msg在『輸出』視窗觀看


using System.Diagnostics;
 
Debug.Print("欲輸出訊息");

"即時運算視窗"

勾選 
【工具】→【選項】→【偵錯】→【將所有輸出視窗文字重新導向到即時運算視窗】


vcs_MyPaint
            int xx;
            int yy;
            for (yy = 0; yy < bitmap1.Height; yy++)
            {
                for (xx = 0; xx < bitmap1.Width; xx++)
                {
                    byte rrr = bitmap1.GetPixel(xx, yy).R;
                    byte ggg = bitmap1.GetPixel(xx, yy).G;
                    byte bbb = bitmap1.GetPixel(xx, yy).B;


                    int Gray = (rrr * 299 + ggg * 587 + bbb * 114 + 500) / 1000;
                    Color zz = Color.FromArgb(255, Gray, Gray, Gray);

                    bitmap1.SetPixel(xx, yy, zz);
                }
            }

            pictureBox2.Image = bitmap1;







[C#]將指定的檔案刪除並送到資源回收桶


參考/加入參考/.NET/Microsoft.VisualBasic

FileSystem.DeleteFile(openFileDialog1.FileName,
		UIOption.OnlyErrorDialogs,
		RecycleOption.SendToRecycleBin);


.Dll加入參考。


            if (flag_search_place == false)
                flag_search_place = true;
            else
                flag_search_place = false;



[C#] 圖片檔讀取：非鎖定檔方法 [Image.FromFile 釋放]

content from http://jashliao.pixnet.net/blog/post/223534989


FileStream fs = File.OpenRead(StrDestFilePath); //OpenRead[二進位讀檔]
int filelength = 0;
filelength = (int)fs.Length; //獲得檔長度
Byte[] image = new Byte[filelength]; //建立一個位元組陣列
fs.Read(image, 0, filelength); //按位元組流讀取
System.Drawing.Image result = System.Drawing.Image.FromStream(fs);
fs.Close();


    [C#] 幾個常用的取路徑及檔名的方法

分享: facebook PLURK twitter 
 

string file = @"d:\abc\123.txt"

Path.GetFileNameWithoutExtension(file) 取得檔案名,不包含副檔名,本例得到123

Path.GetExtension(file) 取得副檔名txt

Path.GetPathRoot(file) 取得根目錄

Path.GetFullPath(file) 取得路徑


[C#] 觀察程式執行時間 StopWatch


Stopwatch loadingWatch = new Stopwatch();
loadingWatch.Start();

XXXXXXXXX

loadingWatch.Stop();

Console.WriteLine(loadingWatch.ElapsedMilliseconds);

可以使用Reset()來重置計算時間.









待測
//File.AppendAllText("E:\\Time\\新建文檔夾 (2)"+"/"+strname,DateTime.Now+"\r\n");



根據時間建立文件
File.Create("C:\\______test_files\\" + DateTime.Now.ToString("yyyyMMddhhmmss") + ".jpg");//建立文件


windows media player
// 播放歌曲
            axWMP.URL = @"D:\Music\02.AVRIL LAVIGNE 酷到骨子裡 MY HAPPY ENDING.mp3";
            // 設定重複播放
            //axWMP.settings.setMode("loop", true);
            // 設定隨機播放
            //axWMP.settings.setMode("shuffle", true);
            
C# - 如何讀取特定位置Registry Key
https://barryhungmvp.pixnet.net/blog/post/88133155-c%23---%E5%A6%82%E4%BD%95%E8%AE%80%E5%8F%96%E7%89%B9%E5%AE%9A%E4%BD%8D%E7%BD%AEregistry-key

加一個讀取RegistryKey的範例

        private void button4_Click(object sender, EventArgs e)
        {
            RegistryKey mreg;
            mreg = Registry.LocalMachine;
            mreg = mreg.CreateSubKey("software\\Microsoft\\Internet Explorer");
            string IEVersion = "目前IE瀏覽器的版本訊息：" + (String)mreg.GetValue("Version");
            mreg.Close();
            richTextBox1.Text += IEVersion + "\n";

        }

桌布存放位置 win7 romeo
C:\Users\Administrator\AppData\Roaming\Microsoft\Windows\Themes\TranscodedWallpaper.jpg

如何找到Windows 10桌面背景图片的位置
http://www.xstui.com/read/446



 C# 根據桌面大小調整視窗大小 
 
 private void Form1_Load(object sender, EventArgs e)
        {
            int DeskWidth = Screen.PrimaryScreen.WorkingArea.Width; //PrimaryScreen為取得主顯示器，WorkingArea可取得顯示器的工作區(不包含工作列…等)
            int DeskHeight = Screen.PrimaryScreen.WorkingArea.Height;
            this.Width = Convert.ToInt32(DeskWidth * 0.8);
            this.Height = Convert.ToInt32(DeskHeight * 0.8);
        }
 

Ray's Working Note 
http://ray19841984.blogspot.com/

'





字體做陰影效果 同樣字往右下寫一遍 顏色不同

            string test_string = "金陵圖";
            bmp = new Bitmap(500, 500);     //initial W, H
            g = Graphics.FromImage(bmp);

            font_type = "標楷體";
            font_size_default = 200;
            
            f = new Font(font_type, font_size_default);

            g.DrawString(test_string, f, new SolidBrush(Color.Pink), new PointF(0, 0));


            font_size_default = 200;

            f = new Font(font_type, font_size_default);

            g.DrawString(test_string, f, new SolidBrush(Color.Red), new PointF(5, 5));
            
            
            pictureBox1.Image = bmp;


picturebox + keydown
https://zhidao.baidu.com/question/495903236489591124.html


vcs
https://jojosula001.pixnet.net/blog/category/2297573







 27. 設定兩個或兩個以上的字型樣式 (例如一段文字設定粗體加斜體)。

假如要將一段文字，同時設定 粗體文字 FontStyle.Bold 與 斜體文字 FontStyle.Italic，則需透過 FontFamily 類別，透過 | 做連結

	// 將RichTextBox中選取的文字，透過 FontFamily 類別 
// 同時設定 粗體文字 FontStyle.Bold 與 斜體文字 FontStyle.Italic 
Font MyFont = new Font(new FontFamily("標楷體"), 10, FontStyle.Bold | FontStyle.Italic); 
this.richTextBox1.SelectionFont = MyFont;





33. String 轉為 Byte 序列與 Byte 序列轉為 String。

使用 System.Text.Encoding 類別中的這兩個方法，須注意編碼方式 :

Encoding.GetBytes 方法 : 將字元集編碼成位元組序列。

Encoding.GetString 方法 : 將位元組序列解碼成字串。

程式碼

	String strOrg = "12345";
            // Encoding.GetBytes方法，將 String 轉為 Byte 序列
            byte[] stringConvByte = Encoding.Default.GetBytes(strOrg);
            // Encoding.GetString方法，將 Byte 序列 轉為 String
            string byteConvStrig = Encoding.Default.GetString(stringConvByte);


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
            

不用richTextBox的debug方法            

寫
System.Diagnostics.Debug.WriteLine("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX");

到【輸出】視窗看輸出資料

先到專案/右鍵/屬性/建置 勾選 定義DEBUG常數





 C# byte 轉 文字
byte轉char或 byte轉string

Convert.ToChar是把hex轉成相對應ascii code
像a的ascii code是0x61

byte[] b = new byte[2] { 0x61,0x62 };
string s=Convert.ToChar(b[0]); => s="a";
string s=Convert.ToChar(b[1]); => s="b";

如果你要把byte code轉成"字面上"的數值 應該這樣寫

byte[] b = new byte[2] { 0x61,0x62 };
string s=b[0].ToString("X2"); => s="61";
string s=b[1].ToString("X2"); => s="62";

ToString("X2")這個格式化字串還蠻好用的 一下就可以把byte轉成相對應的文字
以前我要把byte轉成文字都是用下面這方法

byte[] b = new byte[2] { 0x03,0x04 };
string s= Convert.ToString(b[1], 16);
if (s.Length == 1) //不滿2位要補一個零
{
s= "0"+s;
}
===> s="03";

太麻煩了 那麼多行直接用b[0].ToString("X2")一行就可以取代 還不用自己判斷前面要不要補零 




變更滑鼠鼠標圖案 ( 有效範圍在Form內 )。
this.Cursor = new Cursor("C:\\test.ico"); // "C:\\test.ico" 改成您的圖檔，接受的影像格式為cur與ico






[ C# ] WinForm 顯示於延伸螢幕之方法
https://georgiosky2000.wordpress.com/2014/03/19/c-winform-%e9%a1%af%e7%a4%ba%e6%96%bc%e5%bb%b6%e4%bc%b8%e8%9e%a2%e5%b9%95%e4%b9%8b%e6%96%b9%e6%b3%95/


        Graphics g;
        Pen p;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            p = new Pen(Color.Red, 6);

        }

        private void button1_Click(object sender, EventArgs e)
        {
            g = this.CreateGraphics();
            g.DrawString("驗證完成", new Font("標楷體", 60), new SolidBrush(Color.Blue), new PointF(20, 20));

        }




richTextBox1.Text += "year = " + year.ToString("00") + "\n";
richTextBox1.Text += "month = " + month.ToString("00") + "\n";
richTextBox1.Text += "mday = " + mday.ToString("0000") + "\n";
richTextBox1.Text += "wday = " + wday.ToString() + "\n";
richTextBox1.Text += "hour = " + hour.ToString("00") + "\n";
richTextBox1.Text += "minutes = " + minutes.ToString("00") + "\n";
richTextBox1.Text += "seconds = " + seconds.ToString("00") + "\n";
richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行


richTextBox1.Text += receive_buffer_tmp[i].ToString("X2") + " ";

string drawDate = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss");
string filename = "imsLink_log.long." + DateTime.Now.ToString("yyyy.MMdd.HHmm.ss") + 

string drawDate = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss");


lb_time1.Text = "PC時間 : " + DateTime.Now.ToString("yyyy" + '/' + "MM" + '/' + "dd ") + weekday + DateTime.Now.ToString(" HH" + ':' + "mm" + ':' + "ss");


string filename = "imsLink_log." + DateTime.Now.ToString("yyyy.MMdd.HHmm.ss") + ".txt";


                    else if (Comport_Mode == 2)  //hex mode
                    {
                        input = "";
                        for (int i = 0; i < BytesToRead; i++)
                        {
                            input += ((int)receive_buffer[i]).ToString("X2") + " ";
                        }
                        richTextBox1.AppendText(input);     //打印一般文字訊息
                        richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
                    }
48 65 78 20 6D 6F 64 65 986F 793A 5167 5BB9 0A 






string和byte[]的轉換 (C#)

string類型轉成byte[]：

byte[] byteArray = System.Text.Encoding.Default.GetBytes ( str );

反過來，byte[]轉成string：

string str = System.Text.Encoding.Default.GetString ( byteArray );

其它編碼方式的，如System.Text.UTF8Encoding，System.Text.UnicodeEncoding class等；例如：

string類型轉成ASCII byte[]：（"01" 轉成 byte[] = new byte[]{ 0x30, 0x31}）

byte[] byteArray = System.Text.Encoding.ASCII.GetBytes ( str );

ASCII byte[] 轉成string：（byte[] = new byte[]{ 0x30, 0x31} 轉成 "01"）

string str = System.Text.Encoding.ASCII.GetString ( byteArray );








string text = "是不是漢字，ABC，keleyi.com";
for (int i = 0; i < text.Length; i++)
{
	if (Regex.IsMatch(text[i].ToString(), @"[\u4e00-\u9fbb]+{1}quot;))
		Console.WriteLine("是漢字");
	else
	Console.WriteLine("不是漢字");
}

3400～4DFFh：中日韓認同表意文字擴充A區，總計收容6,582個中日韓漢字。
	4E00～9FFFh：中日韓認同表意文字區，總計收容20,902個中日韓漢字。
A000～A4FFh：彝族文字區，收容中國南方彝族文字和字根。
AC00～D7FFh：韓文拼音組合字區，收容以韓文音符拼成的文字。
F900～FAFFh：中日韓兼容表意文字區，總計收容302個中日韓漢字。
FB00～FFFDh：文字表現形式區，收容組合拉丁文字、希伯來文、阿拉伯文、中日韓直式標點、小符號、半角符號、全角符號等。

Hexadecimal value of 基 is 57FA
Hexadecimal value of 本 is 672C
Hexadecimal value of 運 is 904B
Hexadecimal value of 算 is 7B97
Hexadecimal value of 制 is 5236
Hexadecimal value of 作 is 4F5C
Hexadecimal value of U is 0055
Hexadecimal value of S is 0053
Hexadecimal value of B is 0042
Hexadecimal value of ? is 542F
Hexadecimal value of ? is 52A8
Hexadecimal value of ? is 76D8
Hexadecimal value of ? is 30A6
Hexadecimal value of ? is 30A3
Hexadecimal value of ? is 30AD
Hexadecimal value of ? is 30DA
Hexadecimal value of ? is 30C7
Hexadecimal value of ? is 30A3
Hexadecimal value of ? is 30A2
Hexadecimal value of ? is 003F
Hexadecimal value of ? is 003F
Hexadecimal value of ? is 003F
Hexadecimal value of 世 is 4E16
Hexadecimal value of ? is 003F
Hexadecimal value of 生 is 751F
Hexadecimal value of ? is 003F
Hexadecimal value of ? is 003F
Hexadecimal value of ? is 003F
Hexadecimal value of ? is 003F
Hexadecimal value of ? is 003F
Hexadecimal value of 概 is 6982
Hexadecimal value of ? is 003F
Hexadecimal value of 表 is 8868
Hexadecimal value of ? is 003F
Hexadecimal value of ? is 003F
Hexadecimal value of ? is 003F
Hexadecimal value of ? is 003F



'

vcs
http://cs0.wikidot.com/introduction
https://jjnnykimo.pixnet.net/blog/category/1324785/9

Simple way to Zip files with C# .NET (Framework 4.5 /4.6)
https://coderwall.com/p/hgotua/simple-way-to-zip-files-with-c-net-framework-4-5-4-6
C# UNIX Timestamp Creation
https://coderwall.com/p/6mrs5a/c-unix-timestamp-creation

【c#】 emgucv 設定
https://debbiedbaby.pixnet.net/blog/post/426657881-%E3%80%90c%23%E3%80%91-emgucv-%E8%A8%AD%E5%AE%9A

如何自訂右鍵工具選單
http://davidhsu666.com/archives/context_menu/



c# Delay 1秒鐘寫法

using System.Threading;
Thread.Sleep(1000); //Delay 1秒，不好用，因為這段時間會卡住


codepage
http://www.lingoes.net/en/translator/codepage.htm


C# 提供了許多方法給string使用

方法				說明 					格式
Length				取得字串長度長度			x.Length
IndexOf('關鍵字')		搜尋該關鍵字所在起始位置的索引值	x.IndexOf("H")
Insert(索引, '關鍵字')		將關鍵字插入指定索引位置		x.Insert(3,"Hello")
Remove(索引)			清除索引位置之後的字串			x.Remove(2)
Replace('原字串', '新字串')	將原字串取代為新字串			x.Replace("Hi","Hello")
Substring(索引, 長度)		從指定索引位置取得指定長度的字串	x.Substring(3,10)
Contains('關鍵字')		判斷是否包含該關鍵字			x.Contains("Build")


            string x = "My name is Tom";

            int j = x.Length;
            Console.WriteLine(j);//14

            int p = x.IndexOf("me");
            Console.WriteLine(p);//5

            string k = x.Insert(0, "Hello! ");
            Console.WriteLine(k);//Hello! My name is Tom

            string l = x.Remove(10);
            Console.WriteLine(l);//My name is

            string m = x.Replace("Tom", "John");
            Console.WriteLine(m);//My name is John

            string i = x.Substring(3, 7);
            Console.WriteLine(i);//name is

            if (x.Contains("Tom"))
            {
                Console.WriteLine("Yes! You are Tom");
            }else
            {
                Console.WriteLine("Who are you?");
            }//Yes! You are Tom
            

另外，string跟array一樣，索引的起始值也是0
因此，可以直接操作索引來取得字元
範例

string x = "Hello world";
Console.WriteLine(x[4]); //o






改變各種滑鼠屬標

            pictureBox1.Cursor = Cursors.Cross;  //移到控件上，改變鼠標
            pictureBox1.Cursor = Cursors.Help;
            pictureBox1.Cursor = Cursors.HSplit;
            pictureBox1.Cursor = Cursors.No;
            
            this.Cursor = System.Windows.Forms.Cursors.Help;
            this.Cursor = Cursors.Help; 
            
            this.Cursor = Cursors.WaitCursor;	//等待標記
            this.Cursor = Cursors.Default;	//預設
            

自定義滑鼠屬標
this.Cursor = new Cursor("icon.ico");
icon.ico要放在bin之下

不用製作游標檔的做法:
this.Cursor = new Cursor(new Bitmap(@"C:\______test_files\reuse.bmp").GetHicon());


[C#] webBrowser如何判斷網頁是否讀取完成


在Windows Mobile 6 上用C# 讀取圖片(如jpg)貼在畫面上 	畫上一圖
Graphics g = this.CreateGraphics();

//選擇您要貼的畫面的圖片位置
Bitmap br = new Bitmap("My Documents\\我的圖片\\Waterfall.jpg");

//放置您所指定的圖片
//並指定圖片要放置的位置，(X,Y) = (0,0)
g.DrawImage(br, 0, 0);



在Windows Mobile 6 上用C# 畫點與點之間的線段，方法有二! 

 方法一：(兩點之間的線段)
      Graphics g = this.CreateGraphics();
      Pen pen = new Pen(Color.Blue, 2);     

      //10, 10 為起始位置，20, 20 終點位置
      g.DrawLine(pen, 10, 10, 20, 20);

 

方法二：(多點之間的線段)
      Graphics g = this.CreateGraphics();
      Pen pen = new Pen(Color.Blue, 2);      

      //定義一個陣列有三個點
      //分別為(10,10)、(20,20)、(30,30)
      Point[] points = 
      {
            new Point(10, 10),
            new Point(20, 20),
            new Point(30, 30)
      };

      g.DrawLines(pen, points);




在Windows Mobile 6 上用C# 畫實心圓圈，就是把圈圈填滿，方法有二!


方法一：(用圖片填滿圓圈)
      Graphics g = this.CreateGraphics();
      TextureBrush tb = new TextureBrush(new Bitmap(@"Program Files\\drawImage\\point.jpg"));
     
      //20, 20 為座標位置，10, 10 為圓的大小
      g.FillEllipse(tb, 20, 20, 10, 10);

 

方法二：(用筆刷填滿圓圈)
      Graphics g = this.CreateGraphics();
      SolidBrush sb = new SolidBrush(Color.Blue);
      
      //20, 20 為座標位置，10, 10 為圓的大小
      g.FillEllipse(sb, 20, 20, 10, 10);




在Windows Mobile 6 平臺上的PDA 寫一個抓取無線AP(無線區域網路)訊號強弱的小程式(使用C#在.NET Compact Framework 2.0上) 

https://dreamtails.pixnet.net/blog/post/22318000




韓戰
1950年6月25日－1953年7月27日[註 19]
（3年1個月又2天）



記得在((TextBox)sender).SelectAll();後邊加上一句e.SuppressKeyPress = true;

否則鍵盤消息還會繼續傳遞到基礎控件，傳出難听的“叮”一聲





  uiMode:String; 播放器界面模式，可?Full, Mini, None, Invisible 
  
  
  
  
  
  
  
  
   [C#]開啟EXE檔並輸入EXE檔的參數
先USING System.Diagnostics;

在程式裡放入下列程式
System.Diagnostics.Process.Start("路徑", "參數"); 



c# 首字母大寫 方法
s.Substring(0,1).ToUpper()+s.Substring(1);






DateTime類型中 DayOfWeek時的英文如何轉換成中文

1.這是一种最笨的方法 

Code highlighting produced by Actipro CodeHighlighter (freeware)http://www.CodeHighlighter.com/-->int   i=(int)DateTime.Today.DayOfWeek;  
 switch(i)  
 {  
          case   0:  
                      txtDate.Text="星期天"；  
                      break；  
          case   1:  
                      txtDate.Text="星期一"；  
                      break；  
          case   2:  
                      txtDate.Text="星期二"；  
                      break；  
          case   3:  
                      txtDate.Text="星期三"；  
                      break；  
          case   4:  
                      txtDate.Text="星期四"；  
                      break；  
          case   5:  
                      txtDate.Text="星期五"；  
                      break；  
          case   6:  
                      txtDate.Text="星期六"；  
                      break；  
          ……  
 }
 
 
 
2.聰明的方法：
string strWeek = "星期"+"日一二三四五六".Substring((int)System.DateTime.Now.DayOfWeek,1); 


3.最好的方法： 
string dateString = System.DateTime.Today.ToString("yyyy-M-d dddd", new System.Globalization.CultureInfo("zh-CN")); 







用方向鍵移動picturebox在form上的位置

        private void Form1_Load(object sender, EventArgs e)
        {
            this.pictureBox1.KeyDown += new KeyEventHandler(pictureBox1_KeyDown);
        }

        bool bIsEnterKeyPressed = false;
        private void pictureBox1_KeyDown(object sender, KeyEventArgs e)
        {

            if (e.KeyCode == Keys.Enter)
            {
                bIsEnterKeyPressed = true;
            }
            if (!bIsEnterKeyPressed)
            {
                int x = pictureBox1.Location.X;
                int y = pictureBox1.Location.Y;

                {
                    if (e.KeyCode == Keys.Right) x += 50;
                    else if (e.KeyCode == Keys.Left) x -= 50;
                    else if (e.KeyCode == Keys.Up) y -= 50;
                    else if (e.KeyCode == Keys.Down) y += 50;
                    pictureBox1.Location = new Point(x, y);
                }
            }
        }



	//C# 取得資料夾下的所有檔案(包括子目錄)
	//顯示每個檔案的資訊
        private void button1_Click(object sender, EventArgs e)
        {
            string path = String.Empty;
            string filetype = String.Empty;
            filetype = "*.*";

            //path = @"D:\_DATA2\_VIDEO_全為備份\百家??_清十二帝疑案";
            path = @"C:\______test_files";

            //C# 取得資料夾下的所有檔案(包括子目錄)
            string[] files = System.IO.Directory.GetFiles(path, filetype, System.IO.SearchOption.AllDirectories);
            foreach (string filename in files)
            {
                richTextBox1.Text += "原撈到的檔案 : " + filename + "\n";
                FileInfo fi = new FileInfo(filename);
                richTextBox1.Text += "Name :" + fi.Name + "\n";
                richTextBox1.Text += "FullName :" + fi.FullName + "\n";
                richTextBox1.Text += "Directory :" + fi.Directory + "\n";
                richTextBox1.Text += "DirectoryName :" + fi.DirectoryName + "\n";
                richTextBox1.Text += "Extension :" + fi.Extension + "\n";
                richTextBox1.Text += "Length :" + fi.Length.ToString() + "\n";
                //C# 取得檔案建立日期,及最後修改日期 
                richTextBox1.Text += "檔案建立日期" + fi.CreationTime.ToString() + "\n";
                richTextBox1.Text += "檔案最後修改日期" + fi.LastWriteTime.ToString() + "\n";
                //C# 取得檔案路徑、副檔名、檔案大小
                richTextBox1.Text += "檔案路徑： " + filename.ToString() + "\n";
                richTextBox1.Text += "副檔名： " + filename.Substring(filename.LastIndexOf(".") + 1, filename.Length - filename.LastIndexOf(".") - 1) + "\n";    //取得副檔名
                richTextBox1.Text += "檔案大小： " + File.Open(filename, FileMode.Open).Length.ToString() + " 位元組\n";
                richTextBox1.Text += "\n";
            }

        }




除去換行符號
            //置換換行符號為空白，讓messagebox秀出輸入的字串
            String a = textBox1.Text;
            a = a.Replace("\r\n", "");
            a = a.Replace("\n", "");
            a = a.Replace("\r", "");
            MessageBox.Show(a);
        
        
        
 C# 根據桌面大小調整視窗大小 
             int DeskWidth = Screen.PrimaryScreen.WorkingArea.Width; //PrimaryScreen為取得主顯示器，WorkingArea可取得顯示器的工作區(不包含工作列…等)
            int DeskHeight = Screen.PrimaryScreen.WorkingArea.Height;
            this.Width = Convert.ToInt32(DeskWidth * 0.8);
            this.Height = Convert.ToInt32(DeskHeight * 0.8);


            int screenWidth = Screen.PrimaryScreen.Bounds.Width;
            int screenHeight = Screen.PrimaryScreen.Bounds.Height;
            richTextBox1.AppendText("螢幕解析度 : " + screenWidth.ToString() + "*" + screenHeight.ToString() + "\n");






[C#]WinForm利用Bitmap的MakeTransparent將圖片某些顏色透明化
            Bitmap bmp2 = new Bitmap(asm.GetManifestResourceStream(name + ".puma.bmp"));//載入圖片資源
            bmp2.MakeTransparent(Color.White);//將圖片白色部分透明化;
            this.pictureBox2.Image = bmp2;
            
            bit = new Bitmap("picture1.jpg");  //圖片放在debug內
            bit.MakeTransparent(Color.White);  //將視窗中白色的部份變為透明
            
            

vcs抓網路上的檔案

            try
            {
                //抓現在時間
                DateTime dt = DateTime.Now;
                string filetime = dt.ToString("yyyy-MM-dd-HHmm");  //將檔案寫入現在時間

                WebClient wc = new WebClient();
                wc.DownloadFile("http://data.taipei/bus/PathDetail",    //抓取檔案網址
                "C:\\TEMP\\1_PathDetail\\PathDetail_" + filetime + ".gz");    //寫入本機的路徑
            }
            catch
            {
                Environment.Exit(0);    //如果抓不到檔案就離開程式，沒這行程式會一直卡在這如果沒抓到檔案的話…
            }
        
C# 讓視窗背景顯示GIF動畫 
private void Form1_Load(object sender, EventArgs e)
        {
            bit = new Bitmap("1.gif");
            this.pictureBox1.Image = bit;
        }        
        註：1.gif一樣是放在專案資料夾下：WindowsFormsApp1\WindowsFormsApp1\bin\Debug

 C# 限定textbox只能輸入數字 
 
        private void textBox1_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (((int)e.KeyChar < 48 | (int)e.KeyChar > 57) & (int)e.KeyChar != 8)
            {
                e.Handled = true;
            }
        }
 
 

            int[] tall = new int[] { 10, 20, 30, 40, 50 };
            int sum = 0;
            foreach (int height in tall)
            {
                sum += height;
            }
            richTextBox1.Text += "Sum = " + sum.ToString() + "\n";



            String[] animal = new String[] { "lion", "mouse", "cat", "dog", "elephant" };
            foreach (String name in animal)
            {
                richTextBox1.Text += name + "\n";
            }
            richTextBox1.Text += "\n";






從第5項填資料到ListView
            //測試中
            ListViewItem i1 = new ListViewItem("File_add.txt");
            ListViewItem.ListViewSubItem sub_i1a = new ListViewItem.ListViewSubItem();
            sub_i1a.Text = "3333";
            i1.SubItems.Add(sub_i1a);
            ListViewItem.ListViewSubItem sub_i1b = new ListViewItem.ListViewSubItem();
            sub_i1b.Text = "2016/5/25 02:10上午";
            i1.SubItems.Add(sub_i1b);

            listView1.Items.Add(i1);

            //設置ListView最後一行可見
            listView1.Items[listView1.Items.Count - 1].EnsureVisible();





        private void nudgeWindow()
        {
            // 記錄視窗舊位置
            int oldLeft = Left;
            int oldTop = Top;
            // 變動位置
            Random r = new Random();
            for (int i = 0; i <= 500; i++)
            {
                int left = r.Next(Left - 20, Left + 20);
                Left = left;
                int top = r.Next(Top - 20, Top + 20);
                Top = top;
                Left = oldLeft;
                Top = oldTop;
            }
        }



            System.Drawing.StringFormat drawFormat = new System.Drawing.StringFormat();
            drawFormat.FormatFlags = StringFormatFlags.DirectionVertical;
            g.DrawString("畫字串畫直的", this.Font, new SolidBrush(Color.Black), 300, 100, drawFormat);


----------------many ST----------------

richTextBox1.Text += System.DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss") + "\n";
2019/05/21 14:52:41

richTextBox1.Text += DateTime.Now.ToString() + "\n";
2019/5/21 下午 02:52:42

----------------many SP----------------

using System.Windows.Media.Imaging要引用PresentationCore

只需要在引用-->程序集-->框架-->PresentationCore




string my_string = "   歡迎來到Myson Century!   ";

string str2 = "ON-C";
bool res;
res = my_string.ToLower().Replace(" ", "").Contains(str2.ToLower().Replace("-", ""));
richTextBox1.Text += "result = " + res.ToString() + "\n";



在Windows上，[路徑]必須<248拜，[檔名加路徑]名必須<260拜

	List<Point> points = new List<Point>(); // 紀錄滑鼠軌跡的陣列。	

	List<MyFileInfo> fileinfos = new List<MyFileInfo>();             

1維list宣告
	List<string> myLists = new List<string>();
	
	myLists.Add("A001");
	myLists.Add("A002");
	myLists.Add("A003"); 

2維list宣告
	List<List<string>> myLists = new List<List<string>>();

	myLists.Add(new List<string>() { "A001", "David" });
	myLists.Add(new List<string>() { "A002", "John" });
	myLists.Add(new List<string>() { "A003", "Tom" });             
             
             
             
             
             
bmp
https://www.pcschool.com.tw/campus/share/lib/160/
http://crazycat1130.pixnet.net/blog/post/1345538-%E9%BB%9E%E9%99%A3%E5%9C%96%EF%BC%88bitmap%EF%BC%89%E6%AA%94%E6%A1%88%E6%A0%BC%E5%BC%8F

[C#] List 的用法
http://frank1025.pixnet.net/blog/post/347251643-%5Bc%23%5D-list

C# axWindowsMediaPlayer制作播放器
http://www.mamicode.com/info-detail-986551.html


AxWindowsMediaPlayer媒体文件主要方法屬性
https://blog.csdn.net/ivan_ljf/article/details/9774231


AForge Webcam 錄影
https://blog.csdn.net/m_buddy/article/details/62417912

        private void button1_Click(object sender, EventArgs e)
        {

            /*
            Random 亂數 = new Random();//亂數種子
            int i = 亂數.Next(0, 100);//回傳0-99的亂數
            如果用for 或其它回圈抓亂數，一定要把 Random 亂數 = new Random();//亂數種子 放在回圈外面。
            */


            Random 亂數 = new Random();//亂數種子
            for (int i = 0; i < 100; i++)
            {
                int j = 亂數.Next(0, 100);
                richTextBox1.Text += j.ToString() + "  ";
            }
            richTextBox1.Text += "\n";


        }

        //C# 是否為JPG檔案 record

        private bool 是否為JPG檔案(string 檔案)
        {
            if (!File.Exists(檔案))
                return false;

            using (System.Drawing.Image img = System.Drawing.Image.FromFile(檔案))
            {
                if (img.RawFormat.Equals(System.Drawing.Imaging.ImageFormat.Jpeg))
                    return true;
            }
            return false;
        }



一些vcs資料
http://createps.pixnet.net/blog/category/1630969/2

g.DrawString("直接設定字型與大小", new Font("宋体", 30), Brushes.Red, 10, 10);


C# - 取得隨機字串的快速方法 


C#語言下路徑指定方式有兩種:

    是使用兩個斜線，例如    "C:\\Test.txt"
    第二種是在路徑前加上@符號，例如    @"C:\Test.txt"



取得硬碟資訊
            System.IO.DriveInfo di = new System.IO.DriveInfo(@"C:\");
            richTextBox1.Text += "TotalFreeSpace : " + di.TotalFreeSpace.ToString() + "\n";
            richTextBox1.Text += "VolumeLabel : " + di.VolumeLabel + "\n";




         Bitmap myImage = new Bitmap(Screen.PrimaryScreen.Bounds.Width, Screen.PrimaryScreen.Bounds.Height); 
            Graphics g = Graphics.FromImage(myImage); 
            g.CopyFromScreen(new Point(0,0), new Point(0, 0), new Size(Screen.PrimaryScreen.Bounds.Width, Screen.PrimaryScreen.Bounds.Height)); 
            IntPtr dc1 = g.GetHdc(); 
            g.ReleaseHdc(dc1); 
            myImage.Save(@"c:\screen0.jpg");
            
            




 瞭解程式執行時間 

using System.Diagnostics;
//-------------------------------------------
Stopwatch sw = new Stopwatch();
long num = 0;
sw.Reset();
sw = Stopwatch.StartNew();
//要測速的程式放這裡
sw.Stop();
TimeSpan el = sw.Elapsed;
Console.WriteLine("花費 {0} ", el);
long ms = sw.ElapsedMilliseconds;
Console.WriteLine("花費 {0} 毫秒", ms);

補充說明: 不一定每次測到的時間都相同喔!
建議值: 超過100毫秒就有點太慢囉…. (電腦爛會Lag更長)






tmp code


            richTextBox1.Text += "年：" + dt.Year.ToString() + "\n";
            richTextBox1.Text += "月：" + dt.Month.ToString() + "\n";
            richTextBox1.Text += "日：" + dt.Day.ToString() + "\n";
            richTextBox1.Text += "天：" + dt.DayOfYear.ToString() + "\n";
            richTextBox1.Text += "星：" + dt.DayOfWeek.ToString() + "\n";
            richTextBox1.Text += "時：" + dt.Hour.ToString() + "\n";
            richTextBox1.Text += "分：" + dt.Minute.ToString() + "\n";
            richTextBox1.Text += "秒：" + dt.Second.ToString() + "\n";
            richTextBox1.Text += "毫秒：" + dt.Millisecond.ToString() + "\n";
            richTextBox1.Text += "Ticks：" + dt.Ticks.ToString() + "\n";
            richTextBox1.Text += "TimeOfDay：" + dt.TimeOfDay.ToString() + "\n";

            System.Globalization.TaiwanCalendar TC = new System.Globalization.TaiwanCalendar();
            System.Globalization.TaiwanLunisolarCalendar TA = new System.Globalization.TaiwanLunisolarCalendar();

            DateTime dt = DateTime.Now;
            string message = "";
            message += string.Format("{0}", dt.Year) + "\n";
            message += ("西元年:" + dt.Year.ToString()) + "\n";
            message += ("民國年:" + TC.GetYear(dt)) + "\n";
            message += (string.Format("西元:{0}/{1}/{2}", dt.Year, dt.Month, dt.Day)) + "\n";
            message += (string.Format("民國:{0}/{1}/{2}", TC.GetYear(dt), TC.GetMonth(dt), TC.GetDayOfMonth(dt))) + "\n";
            message += (string.Format("農曆:{0}/{1}/{2}", TA.GetYear(dt), TA.GetMonth(dt), TA.GetDayOfMonth(dt))) + "\n";



            System.DateTime dt = System.DateTime.Now;
            richTextBox1.Text += "現在日期： " + dt.ToLongDateString() + Environment.NewLine;
            richTextBox1.Text += "現在時間： " + dt.ToLongTimeString() + Environment.NewLine;

            //現在日期加天數寫法(本例為加5天):
            System.DateTime Add5Day = dt.AddDays(5);
            richTextBox1.Text += "現在日期加5天： " + Add5Day.ToLongDateString() + Environment.NewLine;

            //現在時間加小時寫法(本例為加12個小時):
            System.DateTime Add12Hours = dt.AddHours(12);
            richTextBox1.Text += "現在時間加12小時： " + Add12Hours.ToLongTimeString() + Environment.NewLine;

            //現在時間減分鐘寫法(本例為減30分鐘):
            System.DateTime Minus30Minutes = dt.AddMinutes(-30);
            richTextBox1.Text += "現在時間減30分鐘： " + Minus30Minutes.ToLongTimeString() + Environment.NewLine;
        }
        
        
        
星期一        








C# 取得檔案版本資訊
using System.Diagnostics;
            richTextBox1.Text += "data : " + FileVersionInfo.GetVersionInfo(@"C:\WINDOWS\NOTEPAD.EXE").FileVersion.ToString() + "\n"; 
data : 10.0.17134.220 (WinBuild.160101.0800)



        public Form1()
        {
            InitializeComponent();

            /*
            //測試沒有標題沒有邊框的Form
            this.Text = string.Empty;
            this.ControlBox = false;
            */

        }
        

 取得目前可用字型，顯示於ListBox。

	this.listBox1.Items.AddRange(FontFamily.Families);


this.Cursor = System.Windows.Forms.Cursors.Hand;


改變鼠標

        private void panel1_MouseHover(object sender, EventArgs e)
        {
            this.Cursor = System.Windows.Forms.Cursors.VSplit;
        }

        private void panel1_MouseLeave(object sender, EventArgs e)
        {
            this.Cursor = System.Windows.Forms.Cursors.Default;
        }
        
21. 變更滑鼠鼠標圖案 ( 有效範圍在Form內 )。
1             this.Cursor = new Cursor("C:\\test.ico"); // "C:\\test.ico" 改成您的圖檔，接受的影像格式為cur與ico
        






C#初體驗，畫圖的讀、寫、顯示 
https://darkblack01.blogspot.com/2014/03/c.html



vs2010的c#找不到Calendar控件




C# 程式學習 系列	30篇
https://ithelp.ithome.com.tw/users/20023570/ironman/110


很多C#範例
http://fecbob.pixnet.net/blog/post/38088065-c%23-%E5%9C%93%E8%A7%92-panel


複製部分圖片


[C#] DrawRoundRetangle
//繪製圓角矩形
private GraphicsPath DrawRoundRect(float x, float y, float width, float height, float cornerRadius) {
            GraphicsPath roundedRect = new GraphicsPath();
            Rectangle rect = new Rectangle((int)x, (int)y, (int)width, (int)height);
            roundedRect.AddArc(rect.X, rect.Y, cornerRadius * 2, cornerRadius * 2, 180, 90);
            roundedRect.AddLine(rect.X + cornerRadius, rect.Y, rect.Right - cornerRadius * 2, rect.Y);
            roundedRect.AddArc(rect.X + rect.Width - cornerRadius * 2, rect.Y, cornerRadius * 2, cornerRadius * 2, 270, 90);
            roundedRect.AddLine(rect.Right, rect.Y + cornerRadius * 2, rect.Right, rect.Y + rect.Height - cornerRadius * 2);
            roundedRect.AddArc(rect.X + rect.Width - cornerRadius * 2, rect.Y + rect.Height - cornerRadius * 2, cornerRadius * 2, cornerRadius * 2, 0, 90);
            roundedRect.AddLine(rect.Right - cornerRadius * 2, rect.Bottom, rect.X + cornerRadius * 2, rect.Bottom);
            roundedRect.AddArc(rect.X, rect.Bottom - cornerRadius * 2, cornerRadius * 2, cornerRadius * 2, 90, 90);
            roundedRect.AddLine(rect.X, rect.Bottom - cornerRadius * 2, rect.X, rect.Y + cornerRadius * 2);
            roundedRect.CloseFigure();
            return roundedRect;
        }
        
        
        

[SDK] 於 C#.net 環境下, 如何將相機影像繪製於 PictureBox 中?
https://www.aisys.com.tw/web/tech/tech.php?question_id=127
[SDK] 於 C#.net 環境下, 如何將相機影像繪製於 PictureBox 中?

[宣告]
Graphics G;  //存放 Control.CreateGraphics 建立的物件
IntPtr pHdc; //存放 Graphics.GetHdc 回傳的 hdc 位址

[初始化]
G = pictureBox1.CreateGraphics(); //使用 pictureBox1 建立一Graphics物件

[繪製影像]
private void axAxAltairU1_OnSurfaceDraw(object sender, AxAxAltairUDrv.IAxAltairUEvents_OnSurfaceDrawEvent e)
{   // AltairU::OnSurfaceDraw 事件
    pHdc = G.GetHdc(); //取得 Hdc
    axAxAltairU1.DrawSurface(e.surfaceHandle, pHdc.ToInt32(), 1, 1, 0, 0); //繪製影像於 Hdc
    G.ReleaseHdc();    //釋放 Hdc
}


測新版的visual studio	看有無書附光碟




vcs
string與String有何不同？



vcs抓螢幕畫面，如何區分全螢幕和active畫面？






檔案：D://Xilinx_SDK_2018.3_1207_2324_Win64.exe,	


MD5：			0E83E8251D76B51B5D311EEA2B2FB8FC
MD5 SUM Value : 	0e83e8251d76b51b5d311eea2b2fb8fc    
			0E83E8251D76B51B5D311EEA2B2FB8FC

vcs_MD5

D:\Xilinx_SDK_2018.3_1207_2324_Win64.exe :   0E83E8251D76B51B5D311EEA2B2FB8FC

D:\Xilinx_SDK_2018.3_1207_2324_Win64.exe :   0E83E8251D76B51B5D311EEA2B2FB8FC




不足位元補零 十進位及十六進位

byte byteValue = 254;

// Display integer values by calling the ToString method.
richTextBox1.Text += byteValue.ToString("D8").ToString() + "\t" + byteValue.ToString("X8") + "\n";






vcs AForge

    加入了參考AForge.Video.FFMPEG，編譯還是不過

注意一下有沒有加進FFMPEG的參考，直接在Visual Studio裡加是不行的，會報錯。
要直接把目錄下的檔案複製到輸出目錄。

https://dahao.blogspot.com/2016/08/caforgenet.html



基于C#和Aforge.net實現圖像素描效果

https://blog.csdn.net/dark00800/article/details/41651499


各種webcam程式比較
http://www.cnblogs.com/xrwang/archive/2010/02/13/HowToCaptureCameraVideoViaDotNet.html


AForge啟動webcam
http://www.voidcn.com/article/p-kvujrudv-ru.html



       

vcs_WMP
richTextBox1.Text += " 歌曲名称：" + axWindowsMediaPlayer1.currentMedia.getItemInfo("Title");

mute & un-mute
        private void pictureBox7_Click(object sender, EventArgs e)//静音
        {
            if (MM)
            {
                pictureBox7.Image = (Image)Properties.Resources.音量按钮变色;
                axWindowsMediaPlayer1.settings.mute = true;
                MM = false;
            }
            else
            {
                pictureBox7.Image = (Image)Properties.Resources.音量按钮;
                axWindowsMediaPlayer1.settings.mute = false;
                MM = true;
            }
        }


參考
063_使用C#操作INI文件
給vcs_WMP 設定常用的mp3資料夾

vcs_WMP要改成可以多選檔案  或選整個或多個資料夾 一起播放








vcs

星期幾
            string[] Day = new string[] { "星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六" };
            string week = Day[Convert.ToInt32(DateTime.Now.DayOfWeek.ToString("d"))].ToString();
            richTextBox1.Text += week + "\n";



vcs
ex069	讀取正中、簡中、日文，是否接OK？
ex062	複製文件時顯示複製進度，應用慢速U盤來測



string color
color_r
color_g
color_b




[C#]如何抓取Google Static Map
https://dotblogs.com.tw/larrynung/2013/01/06/86807

Supalogo-免費的線上Logo圖片產生器
https://dotblogs.com.tw/larrynung/2010/07/15/16580

[C#]原子能委員會輻射監控非官方API
https://dotblogs.com.tw/larrynung/2011/03/17/21890




[C#] QRCode Generator & Reader 
http://foxktr560.blogspot.com/2013/08/c-qrcode-generator-reader.html


vcs
vcs的QR code編碼解碼
參考：http://foxktr560.blogspot.com/2013/08/c-qrcode-generator-reader.html
把 zxing.dll 加入參考

先下載一個開放的函示庫(DLL) "Zxing"
http://zxingnet.codeplex.com/



C#中使用SendMessage進行進程通信的實例
https://blog.csdn.net/yl2isoft/article/details/20227421


(C#)WinAPI的SendMessage傳送

[DllImport("user32.dll")]

public static extern long SendMessage(int hWnd, uint msg, uint wparam, string text);

public const uint WM_SETTEXT = 0x0c;
public const uint WM_GETTEXT = 0x0d;
public const uint WM_LBUTTONUP = 0x0202;
public const uint WM_LBUTTONDOWN = 0x0201;

SendMessage(輸入欄位的Handle, WM_SETTEXT, 0, "你要送的字串" );

對按鈕按下去的訊號：

SendMessage(按鈕的Handle, WM_LBUTTONDOWN, 0, null);

SendMessage(按鈕的Handle, WM_LBUTTONUP, 0, null);


兩個執行檔間數值的傳遞與接收



vcs 之 WebCam 使用大集成










/**
* @brief   Convert a 6 digit HTML code (hex) into a color value.
*/
#define HTML2COLOR(h)		((color_t)((((h) & 0xF80000)>>8) | (((h) & 0x00FC00)>>5) | (((h) & 0x0000F8)>>3)))
#define HTML2COLOR(h)		((COLOR_TYPE)(HTML2COLOR_R(h) | HTML2COLOR_G(h) | HTML2COLOR_B(h)))
#define HTML2COLOR(h)		((COLOR_TYPE)(((((h)&0xFF0000)>>16)+(((h)&0x00FF00)>>7)+((h)&0x0000FF)) >> (10-COLOR_BITS)))

#define COLOR_BITS		16
#define COLOR_TYPE		uint16_t
#define COLOR_TYPE_BITS		16


		
/**
 * @name   Some basic colors
 * @{
 */
#define White			HTML2COLOR(0xFFFFFF)
#define Black			HTML2COLOR(0x000000)
#define Gray			HTML2COLOR(0x808080)
#define Grey			Gray
#define Blue			HTML2COLOR(0x0000FF)
#define Red			HTML2COLOR(0xFF0000)
#define Fuchsia			HTML2COLOR(0xFF00FF)
#define Magenta			Fuchsia
#define Green			HTML2COLOR(0x008000)
#define Yellow			HTML2COLOR(0xFFFF00)
#define Aqua			HTML2COLOR(0x00FFFF)
#define Cyan			Aqua
#define Lime			HTML2COLOR(0x00FF00)
#define Maroon			HTML2COLOR(0x800000)
#define Navy			HTML2COLOR(0x000080)
#define Olive			HTML2COLOR(0x808000)
#define Purple			HTML2COLOR(0x800080)
#define Silver			HTML2COLOR(0xC0C0C0)
#define Teal			HTML2COLOR(0x008080)
#define Orange			HTML2COLOR(0xFFA500)
#define Pink			HTML2COLOR(0xFFC0CB)
#define SkyBlue			HTML2COLOR(0x87CEEB)
/** @} */
      


vcs 取得WebCam影像：		使用Emgu

參考：
C# 控制 Webcam 【using Emgu】 
http://blog.kenyang.net/2012/03/04/c-webcam-using-emgu
[C#] 取得WebCam影像
http://foxktr560.blogspot.com/2013/08/c-webcam.html

OpenCV是一套強大的影像處理library，由INTEL開發，
非常強大，甚至你可以利用OpenCV去做到OCR，很方便。
也由於OpenCV沒有支援C#，那C#要怎麼使用OpenCV呢?
就是靠Emgu，Emgu是一套允許OpenCV的function在C#等語言中被使用。

開啟vcs專案，拉一個pictureBox，準備顯示WebCam回傳的影像

專案加入參考：
C:/Emgu/emgucv-windows-x86 2.3.0.1416/bin/ 有4個dll

    Emgu.CV.dll
    Emgu.CV.ML.dll
    Emgu.CV.UI.dll
    Emgu.Util.dll
    
加入以後，請先儲存你的專案，
拷貝以下2個dll
    opencv_core231.dll
    opencv_highgui231.dll
放到專案的/bin/Debug/底下

因為Emgu.CV.dll會使用到上述兩個dll。


先import會使用到的lib，如下:

	using Emgu.CV;
	using Emgu.CV.Structure;

先宣告一個Capture物件，如下:

	private Capture cap = null;                 // Webcam物件

這個物件就是用來連結到你的webcam。



Form1_Load event，
連結到攝影機以及建立一個event用來抓取畫面，如下:

private void Form1_Load(object sender, EventArgs e)
{
     cap = new Capture(0); // 連結到攝影機0，如果你有兩台攝影機，第二台就是1
     Application.Idle += new EventHandler(Application_Idle); // 在Idle的event下，把畫面設定到pictureBox上(當然你也可以用timer事件)
}


接下來要寫抓取畫面event的code，

void Application_Idle(object sender, EventArgs e)
{
     Image<Bgr, Byte> frame = cap.QueryFrame(); // 去query該畫面
     pictureBox1.Image = frame.ToBitmap(); // 把畫面轉換成bitmap型態，再餵給pictureBox元件
}

        


加入四個參考 
Emgu.CV.dll
Emgu.CV.ML.dll
Emgu.CV.UI.dll
Emgu.Util.dll
 (該dll放於EmguCV安裝完的bin底下)




3.2 常用接口说明
caputure
        public Capture();			//Create a capture using the default camera
        public Capture(int camIndex);		//对应摄像头的缩影, 从0开始
        public Capture(string fileName);	//The name of a file, or an url pointed to a stream.
        





2011/5/8(SUN)
2011/5/8(日) 20:28 著信


string與String有何不同？



vcs抓螢幕畫面，如何區分全螢幕和active畫面？


bmp.Save(@"D:\ssss.jpg");


vcs_WMP
richTextBox1.Text += " 歌曲名称：" + axWindowsMediaPlayer1.currentMedia.getItemInfo("Title");

mute & un-mute
        private void pictureBox7_Click(object sender, EventArgs e)//静音
        {
            if (MM)
            {
                pictureBox7.Image = (Image)Properties.Resources.音量按钮变色;
                axWindowsMediaPlayer1.settings.mute = true;
                MM = false;
            }
            else
            {
                pictureBox7.Image = (Image)Properties.Resources.音量按钮;
                axWindowsMediaPlayer1.settings.mute = false;
                MM = true;
            }
        }


參考
063_使用C#操作INI文件
給vcs_WMP 設定常用的mp3資料夾

vcs_WMP要改成可以多選檔案  或選整個或多個資料夾 一起播放





C# 如何取得兩個 DateTime 日期之間的天數

取得兩個日期之間的「天數」（不足一天者採「無條件刪去法」） 

    new TimeSpan(date1.Ticks - date2.Ticks).Days

取得兩個日期之間的「天數」（回傳型別為 double 雙精確度）

    new TimeSpan(date1.Ticks - date2.Ticks).TotalDays

取得兩個日期之間的「小時數」（回傳型別為 double 雙精確度）

    new TimeSpan(date1.Ticks - date2.Ticks).TotalHours

取得兩個日期之間的「分鐘數」（回傳型別為 double 雙精確度） 

    new TimeSpan(date1.Ticks - date2.Ticks).TotalMinutes




DateTime date1 = new DateTime(2008, 12,31, 23,59,59, DateTimeKind.Local);
DateTime date2 = new DateTime(2003, 2,13, 23,59,59, DateTimeKind.Local);
TimeSpan s = new TimeSpan(date1.Ticks - date2.Ticks);    







ID3格式


開頭 	3 	「TAG」，標籤。
標題 	30 	歌曲標題，最多30個英文字元。
藝術家 	30 	作曲或演唱者的名字，最多30個英文字元。
專輯 	30 	專輯名稱，最多30個英文字元。
年分 	4 	西元年分，四個數字。
評論 	28[3]或30 	就是評論。
零位元組[3] 	1 	如果有儲存曲目，那麼這個位元組會儲存一個二進位的0。
曲目[3] 	1 	這首歌在該專輯中的曲目，或者為0。若前一個位元組非零，則此欄內容無效。
藝術類型 


header 	3 	"TAG"
title 	30 	30 characters of the title
artist 	30 	30 characters of the artist name
album 	30 	30 characters of the album name
year 	4 	A four-digit year
comment 	28[7] or 30 	The comment.
zero-byte[7] 	1 	If a track number is stored, this byte contains a binary 0.
track[7] 	1 	The number of the track on the album, or 0. Invalid, if previous byte is not a binary 0.
genre 	1 	Index in a list of genres, or 255 












看範例學C# 系列
https://ithelp.ithome.com.tw/users/20044155/ironman/241



wmp改變視窗大小
https://blog.csdn.net/ivan_ljf/article/details/9774231
axWindowsMediaPlayer1.DisplaySize　　　　　　　?置播放?象大小  
　　　　1-MpDefaultSize　　　　　　　　　原始大小  
　　　　2-MpHalfSize　　　　　　　　　　 原始大小的一半  
　　　　3-MpDoubleSize　　　　　　　　　 原始大小的?倍  
　　　　4-MpFullScreen　　　　　　　　　 全屏  
　　　　5-MpOneSixteenthScreen　　　　　 屏幕大小的1/16  
　　　　6-MpOneFourthScreen　　　　　　　屏幕大小的1/4  
　　　　7-MpOneHalfScreen　　　　　　　　屏幕大小的1/2  

axWindowsMediaPlayer1.settings.balance = 1; 伴唱
axWindowsMediaPlayer1.settings.balance = -1;原唱





windows media player
在視頻播放之後,可以通過如下方式讀取源視頻的寬度和高度,然後設置其還原為原始的大小.
         private void ResizeOriginal()
         {
             int intWidth = axWindowsMediaPlayer1.currentMedia.imageSourceWidth;
             int intHeight = axWindowsMediaPlayer1.currentMedia.imageSourceHeight;
             axWindowsMediaPlayer1.Width = intWidth + 2;
             axWindowsMediaPlayer1.Height = intHeight + 2;
         }
         
         
         
         



//Wait
System.Threading.Thread.Sleep( 5000 ); // wait 5 seconds (5000 milliseconds)



//Take a screenshot 

// Take a screenshot
// By Ali Hamdar (http://alihamdar.com/)
// http://social.msdn.microsoft.com/Forums/en/csharpgeneral/thread/79efecc4-fa6d-4078-afe4-bb1379bb968b

// Default values for full screen
int width = System.Windows.Forms.Screen.PrimaryScreen.Bounds.Width;
int height = System.Windows.Forms.Screen.PrimaryScreen.Bounds.Height;
int top = 0;
int left = 0;

System.Drawing.Bitmap printscreen = new System.Drawing.Bitmap( width, height );
System.Drawing.Graphics graphics = System.Drawing.Graphics.FromImage( printscreen as Image );
graphics.CopyFromScreen( top, left, 0, 0, printscreen.Size );
printscreen.Save( outputfile, imagetype );




PNG 轉 BMP
using System.Drawing.Imaging;   //for PixelFormat

        private void button1_Click(object sender, EventArgs e)
        {
            System.Drawing.Image PngImg = System.Drawing.Image.FromFile(@"C:\______test_files\sample.png");
            Bitmap myImage = new Bitmap(PngImg.Width, PngImg.Height, PixelFormat.Format32bppRgb);
            using (Graphics g = Graphics.FromImage(myImage))
            {
                g.InterpolationMode = System.Drawing.Drawing2D.InterpolationMode.HighQualityBicubic;
                g.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.HighQuality;
                g.CompositingQuality = System.Drawing.Drawing2D.CompositingQuality.HighQuality;
                g.DrawImage(PngImg, 0, 0);
            }
            PngImg.Save(@"C:\______test_files\sample.bmp", ImageFormat.Bmp);
        }



label 之 cursor 可以改變游標指到label時，會改變的滑鼠游標。

vcs人物分類
帝王類
其他


vcs照片+文字、照片+浮水印



vcs history
大scale
小scale
可置換table
處理BC數字


VCS到某區域內，鼠標換成滴管，這樣用來檢測每個點的RGB值

C#	w/ XML分析



vcs
richtextbox裡，如何知道目前游標所在的line與position

bmp
如何把bmp檔讀出所有點 直接去改裡面數字 另存新檔
看能不能做到顏色平移的效果



vcs
ImageViewer is from _Yusuf Shakeel_CSharp



            
            
            
"
Bitmap Image (.bmp)|*.bmp|
Gif Image (.gif)|*.gif|
JPEG Image (.jpeg)|*.jpeg|
Png Image (.png)|*.png|
Tiff Image (.tiff)|*.tiff|
Wmf Image (.wmf)|*.wmf

";







vcs開啟一個純文字檔到richtextbox裡面
目前沒辦法處理正中、簡中、日文同時存在的純文字檔


//開啟檔案
FileStream myFile = File.Open(@"C:\myWriter.txt", FileMode.OpenOrCreate, FileAccess.ReadWrite);

BinaryReader myReader = new BinaryReader(myFile);

int dl = System.Convert.ToInt16(myFile.Length);
//讀取位元陣列

byte[] myData = myReader.ReadBytes(dl);
//釋放資源

myReader.Close();

myFile.Close();



ImageViewer	研究選單架構


using System.Drawing.Imaging;

           Bitmap mimg = new Bitmap(width * 2, height);

            for (int y = 0; y < height; y++)
            {
                for (int lx = 0, rx = width * 2 - 1; lx < width; lx++, rx--)
                {
                    cnt++;
                    //get source pixel value
                    Color p = simg.GetPixel(lx, y);
                    if ((cnt % 10000) == 0)
                    {
                        richTextBox1.Text += p.A.ToString("X2") + p.R.ToString("X2") + p.G.ToString("X2") + p.B.ToString("X2") + "  ";
                        //richTextBox1.Text += p.A.ToString() + p.R.ToString() + p.G.ToString() + p.B.ToString() + "  ";
                    }

                    //set mirror pixel value
                    mimg.SetPixel(lx, y, p);
                    mimg.SetPixel(rx, y, p);
                }
            }

            //load mirror image in picturebox2
            pictureBox2.Image = mimg;

            //save (write) mirror image
            //mimg.Save("C:\\MirrorImage.png");
            mimg.Save("C:\\MirrorImage.jpg", ImageFormat.Jpeg);
            mimg.Save("C:\\MirrorImage.png", ImageFormat.Png);
            mimg.Save("C:\\MirrorImage.bmp", ImageFormat.Bmp);


vcs不可畫點，用畫橢圓取代




//-------------------------------------------------------------------------------------

            this.pictureBox1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.pictureBox1.Dock = System.Windows.Forms.DockStyle.Bottom;


openFileDialog1.Filter = "XML設定檔|*.xml";
openFileDialog1.Filter = "*.jpg,*.jpeg,*.bmp,*.gif,*.ico,*.png,*.wmf|*.jpg;*.jpeg;*.bmp;*.gif;*.ico;*.png;*.wmf";

            OpenFileDialog ofd = new OpenFileDialog();
            ofd.Filter = "jpg (*.jpg)|*.jpg|bmp (*.bmp)|*.bmp|png (*.png)|*.png";


            SaveFileDialog sfd = new SaveFileDialog();
            sfd.Filter = "jpg (*.jpg)|*.jpg|bmp (*.bmp)|*.bmp|png (*.png)|*.png";


            

        //----選到textbox時，選取全部文字
        private void TextBox_Enter(object sender, EventArgs e)
        {
            TextBox tb = sender as TextBox;
            tb.SelectAll();
        }



        //縮小pictureBox1
        //pictureBox1.SizeMode = PictureBoxSizeMode.AutoSize;/*AutoSize可能無法縮小圖片*/
        //先改成等比例縮小圖片SizeMode
        pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;












改變pictureBox大小改變表單位置

pictureBox1.Image.Save(@"D:\bbbbb.jpg");




改變部分字體顏色
            richTextBox1.SelectionStart = 10;
            richTextBox1.SelectionLength = 5;
            richTextBox1.SelectionColor = Color.Red;
            richTextBox1.SelectionBackColor = Color.Green;



Pen blackPen = new Pen(Color.FromArgb(255, 0, 0, 0), 5);
DrawImage(bmp, 0, 0);
DrawImage(bmp, 0, 0); // 在表單上顯示 bmp 記憶體圖像
this.Refresh() ; //執行 Form1_Paint()


Bitmap bmp =new Bitmap(@"D:\bear.jpg");


pictureBox1.SizeMode = pictureBoxSizeMode.AutoSize; //自動調整大小
pictureBox1.Image = bmp; //顯示在 pictureBox1 圖片控制項中

// bmp 的大小和pictureBox1 相同
Bitmap bmp = new Bitmap(this.PictureBox1.Width,
this.PictureBox1.Height);
// 以記憶體圖像 bmp 建立 myDraw 記憶體畫布
Graphics myDraw = Graphics.FromImage(bmp);
MyDraw.Clear(this.pictureBox1.BackColor); //畫布背景色
MyDraw.DrawLine(new pen(Color.Red,2),x,y,e.X,e.Y); //可



王濬樓船下益州，金陵王氣黯然收。
千尋鐵鎖沉江底，一片降幡出石頭。
人世幾回傷往事，山形依舊枕寒流。
今逢四海為家日，故壘蕭蕭蘆荻秋。
朱雀橋邊野草花，烏衣巷口夕陽斜。
舊時王謝堂前燕，飛入尋常百姓家。
吾愛孟夫子，風流天下聞。紅顏棄軒冕，白首臥鬆雲。
醉月頻中聖，迷花不事君。高山安可仰，徒此揖清芬。
寥落古行宮，宮花寂寞紅。
白頭宮女在，閒坐說玄宗。
功蓋三分國，名成八陣圖。
江流石不轉，遺恨失吞吳。





------------------------------------------------------------------------------------------------------------------------


char[] bbv={'江','一','人'};

王濬樓船下益州，金陵王氣黯然收。
千尋鐵鎖沉江底，一片降幡出石頭。
人世幾回傷往事，山形依舊枕寒流。
今逢四海為家日，故壘蕭蕭蘆荻秋。";



            char[] bbv={'蕭','一','樓'};
            string abc = "王濬樓船下益州，金陵王氣黯然收。千尋鐵鎖沉江底，一片降幡出石頭。人世幾回傷往事，山形依舊枕寒流。今逢四海為家日，故壘蕭蕭蘆荻秋。";
       
            int aa = abc.IndexOfAny(bbv);
            int bb = abc.IndexOfAny(bbv, 32);
            int cc = abc.IndexOfAny(bbv, 32, 10);
            int dd = abc.IndexOfAny(bbv, 32, 20);
            int ee = abc.IndexOfAny(bbv, 32, 30);

            richTextBox2.Text += "length of abc = " + abc.Length.ToString() + "\n";
            richTextBox2.Text += "aa = " + aa.ToString() + "\n";
            richTextBox2.Text += "bb = " + bb.ToString() + "\n";
            richTextBox2.Text += "cc = " + cc.ToString() + "\n";
            richTextBox2.Text += "dd = " + dd.ToString() + "\n";
            richTextBox2.Text += "ee = " + ee.ToString() + "\n";




------------------------------------------------------------------------------------------------------------------------


this.richTextBox1.Size = new System.Drawing.Size(382, 594);



------------------------------------------------------------------------------------------------------------------------




------------------------------------------------------------------------------------------------------------------------






------------------------------------------------------------------------------------------------------------------------


------------------------------------------------------------------------------------------------------------------------






------------------------------------------------------------------------------------------------------------------------




------------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------------------------------------


------------------------------------------------------------------------------------------------------------------------



------------------------------------------------------------------------------------------------------------------------

            int[] x = { 0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420, 450, 480, 510, 540, 570, 600 };
            int[] y = { 200, 295, 368, 399, 381, 319, 228, 129, 48, 4, 8, 58, 144, 243, 331, 387, 397, 359, 282, 184, 91 };
            Bitmap bitM = new Bitmap(this.panel1.Width, this.panel1.Height);
            //MessageBox.Show("Width = " + this.panel1.Width + "  Height = " + this.panel1.Height);
            Graphics g = Graphics.FromImage(bitM);
            g.Clear(Color.WhiteSmoke);
            Point[] points = new Point[21];
            Random r = new Random();
            for (int i = 0; i < 21; i++)
            {
                points[i].X = x[i];
                points[i].Y = y[i];
            }
            g.DrawLines(new Pen(Color.FromArgb(r.Next(1, 255), r.Next(1, 255), r.Next(1, 255))), points);  //繪製折線 
            this.panel1.BackgroundImage = bitM;

------------------------------------------------------------------------------------------------------------------------


            int[] x = { 0, 40, 80, 120, 160, 200, 240, 280, 320, 360, 400, 440, 480, 520, 560, 600 };
            int[] y = { 200, 328, 396, 373, 268, 131, 26, 3, 71, 200, 328, 396, 373, 268, 131, 26 };

            for (int i = 0; i < 10; i++)
            {
                Application.DoEvents();
                for (int j = 0; j < 20; j++)
                    System.Threading.Thread.Sleep(1);

                g.DrawLine(Pens.Red, new Point(x[i], 400 - y[i]), new Point(x[i + 1], 400 - y[i + 1]));
            }
            MessageBox.Show("OK");


------------------------------------------------------------




-----------------------------------------





XML 註解	<!-- --> 的內容。


@"C:\______test_files\cat\cat2.png"

Pen blackPen = new Pen(Color.FromArgb(255, 0, 0, 0), 5);



DrawImage(bmp, 0, 0);
DrawImage(bmp, 0, 0); // 在表單上顯示 bmp 記憶體圖像

this.Refresh() ; //執行 Form1_Paint()


Bitmap bmp =new Bitmap(@"D:\bear.jpg");
pictureBox1.SizeMode = pictureBoxSizeMode.AutoSize; //自動調整大小
pictureBox1.Image = bmp; //顯示在 pictureBox1 圖片控制項中

// bmp 的大小和pictureBox1 相同
Bitmap bmp = new Bitmap(this.PictureBox1.Width,
this.PictureBox1.Height);
// 以記憶體圖像 bmp 建立 myDraw 記憶體畫布
Graphics myDraw = Graphics.FromImage(bmp);
MyDraw.Clear(this.pictureBox1.BackColor); //畫布背景色
MyDraw.DrawLine(new pen(Color.Red,2),x,y,e.X,e.Y); //可以繪圖了






繪製圖形物件的方法

Graphics類別GDI+提供下列方法來繪製上述清單中的項目： 


DrawLines

DrawCurve
DrawClosedCurve


        private void Form1_Resize(object sender, EventArgs e)
        {
            pictureBox1.Width = this.ClientSize.Width - 20;
            pictureBox1.Height = this.ClientSize.Height - 20;
        }

	DrawCircle(200, 200, 100);

        private void DrawCircle(int center_x, int center_y, int radius)
        {
            int linewidth = 5;
            // Create a Graphics object for the Control.
            Graphics g = pictureBox1.CreateGraphics();
            // Create a new pen.
            Pen PenStyle = new Pen(Color.Red, 5);
            // Set the pen's width.
            PenStyle.Width = linewidth;
            // Draw the circle
            g.DrawEllipse(PenStyle, new Rectangle(center_x - radius, center_y - radius, radius * 2, radius * 2));
            //Dispose of the pen.
            PenStyle.Dispose();
        }


	private void DrawPixel(int xx, int yy)
	{
		
	}
	


PictureBoxSizeMode

                case 0: pictureBox1.SizeMode = PictureBoxSizeMode.AutoSize; break;
                case 1: pictureBox1.SizeMode = PictureBoxSizeMode.CenterImage; break;
                case 2: pictureBox1.SizeMode = PictureBoxSizeMode.Normal; break;
                case 3: pictureBox1.SizeMode = PictureBoxSizeMode.StretchImage; break;
                case 4: pictureBox1.SizeMode = PictureBoxSizeMode.Zoom; break;


建立畫布

Graphics 畫布物件變數;
畫布物件變數 = 控制項名稱.CreateGraphics();

例如：在表單上建立畫布g：
Graphics g;
g = this.CreateGraphics();


例如：在圖片方塊pictureBox1上建立畫布g：
Graphics g;
g = pictureBox1.CreateGraphics();

畫筆Pen物件

Pen 畫筆 = new Pen(畫筆顏色, 畫筆粗細);
Pen p = new Pen(Color.Blue, 5);
p.Color = Color.Red;
p.Width = 2;

筆刷物件（單色S、圖案T、花紋H、漸層L）

筆刷類別
SolidBrush		建立單一顏色的筆刷
	SolidBrush sb = new SolidBrush(Color.Red);
	Pen p = new Pen(sb, 2);
TextureBrush		建立以圖形物件當作圖案的筆刷
	TextureBrush tb = new TextureBrush("bmp1.bmp");
	Pen p = new Pen(tb, 2);
HatchBrush		建立花紋筆刷
	HatchBrush 花紋筆刷變數 = new HatchBrush(花紋筆刷, 前景顏色, 背景顏色);
	HatchBrush hb = new HatchBrush(HatchStyle.Wave, Color.Blue, Color.Red);
	Pen p = new Pen(hb, 10);
	(要先加入：using System.Drawing.Drawing2D;)
LinearGradienBrush	建立漸層筆刷
	LinearGradientBrush 漸層筆刷變數 = new LinearGradientBrush(漸層矩形區域, 前景顏色, 背景顏色, 漸層傾斜角度);
	
	Rectangle rect1 = new Rectangle(0, 0, pictureBox1.Size.Width, pictureBox1.Size.Height);
	LinearGradientBrush lgb = new LinearGradientBrush(rect1, Color.Blue, Color.Red, 90);
	Pen p = new Pen(lgb, 10);
	(要先加入：using System.Drawing.Drawing2D;)


Pen 畫筆 = new Pen(畫筆顏色, 畫筆粗細);






設定顏色的方法	呼叫靜態函式：Color.FromArgb()

ex:
Color red= Color.FromArgb(255,0,0)
this.BackColor=Color.White;


Pen只有一類
Brush有四類

Pen用於告訴Graphics如何繪製線條
Brush用於填充區域

Point的用法
Point b=new Point(20,10);
Point a=new Point();
a.X=20;
a.Y=10;


繪製虛線，可設定Pen的DashStyle屬性為Dash,Dot,DashDot或者DashDotDot等
改變直線端點的形狀，可以設定StartCap和EndCap屬性

blackPen.StartCap=LineCap.ArrowAnchor;







自己繪製bitmap圖片保存,生成ico文件或者對象
今天回答一個問題的時候的隨筆
 

Bitmap bit = new Bitmap(100, 30);
Graphics g = Graphics.FromImage(bit);
SolidBrush sb = new SolidBrush(Color.Blue);
Rectangle rg = new Rectangle(new Point(0, 0), bit.Size);
g.FillRectangle(sb, rg);
g.DrawString("測試測試呵呵", this.Font, new SolidBrush(Color.White), new PointF(0, 0));
bit.Save("d://123.bmp");//保存下來這個可以看生成的圖片 
                
                

vcs
Form2的元件的Modifiers要改成Internal, 預設為private

//char * wday[] = {"Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"};
在預設的情況下，C# 不能使用指標，若要用指標的話，要在編譯器設定中啟用 unsafe 模式才行。



共用事件範例	WinEventHandler

            Color cl = Color.Red;
            panel1.BackColor = cl;
            richTextBox1.Text += cl.R.ToString() + "," + cl.G.ToString() + "," + cl.B.ToString() + "\n";
            //txtColor.Text = ColorTranslator.ToHtml(cl).ToString();

            byte Alpha = 0xff;
            byte Red = 0x00;
            byte Green = 0xff;
            byte Blue = 0x00;

            Color cc = Color.FromArgb(Alpha, Red, Green, Blue);
            panel1.BackColor = cc;
            richTextBox1.Text += cl.R.ToString() + "," + cl.G.ToString() + "," + cl.B.ToString() + "\n";



-------------------------------------------------------------------------------------------------------------------------------------
根據內容比對檔案

using System.IO;


            StreamReader sr1 = new StreamReader(textBox1.Text);		//創建StreamReader對象
            StreamReader sr2 = new StreamReader(textBox2.Text);		//創建StreamReader對象
            if (object.Equals(sr1.ReadToEnd(), sr2.ReadToEnd()))	//讀取文件內容並判斷
            {
                MessageBox.Show("兩個檔案相同");
            }
            else
            {
                MessageBox.Show("兩個檔案不相同");
            }
            
-------------------------------------------------------------------------------------------------------------------------------------
建立臨時檔案

            FolderBrowserDialog P_FolderBrowserDialog = new FolderBrowserDialog();	//選擇資料夾
            if (P_FolderBrowserDialog.ShowDialog() == DialogResult.OK)	//選擇資料夾
            {
                File.Create(P_FolderBrowserDialog.SelectedPath + "\\" + DateTime.Now.ToString("yyyyMMddhhmmss") + ".txt");//創建文件
            }


-------------------------------------------------------------------------------------------------------------------------------------
計算時間間隔
dtpicker_first dtpicker_second 為DateTimePicker
            MessageBox.Show("間隔 "+
                DateAndTime.DateDiff(	//使用DateDiff方法獲取日期間隔
                DateInterval.Day, dtpicker_first.Value, dtpicker_second.Value,
                FirstDayOfWeek.Sunday, FirstWeekOfYear.Jan1).ToString()+" 天", "間隔時間");






-------------------------------------------------------------------------------------------------------------------------------------



-------------------------------------------------------------------------------------------------------------------------------------
使用MD5加密

using System.Security.Cryptography; //for MD5

        public string Encrypt(string strPwd)
        {
            MD5 md5 = new MD5CryptoServiceProvider();   //創建MD5對象
            byte[] data = System.Text.Encoding.Default.GetBytes(strPwd);//將字串編碼為一個Byte序列
            byte[] md5data = md5.ComputeHash(data);//計算dataByte的Hash值
            md5.Clear();    //清空MD5對象
            string str = "";//定義一個變量，用來記錄加密後的密碼
            for (int i = 0; i < md5data.Length - 1; i++)//遍歷byte數組
            {
                str += md5data[i].ToString("x").PadLeft(2, '0');//對遍歷到的Byte進行加密
            }
            return str;//返回得到的加密字串
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string P_str_Code = "ABCDEFG";
            richTextBox1.Text += "使用MD5加密後的結果為：" + Encrypt(P_str_Code) + "\n";
        }






-------------------------------------------------------------------------------------------------------------------------------------
計算GB MB KB

        const int GB = 1024 * 1024 * 1024;//定義GB的計算常量
        const int MB = 1024 * 1024;//定義MBW的計算常量
        const int KB = 1024;//定義KB的計算常量
        public string ByteConversionGBMBKB(Int64 KSize)
        {
            if (KSize / GB >= 1)
                return (Math.Round(KSize / (float)GB, 2)).ToString() + "GB";
            else if (KSize / MB >= 1)
                return (Math.Round(KSize / (float)MB, 2)).ToString() + "MB";
            else if (KSize / KB >= 1)
                return (Math.Round(KSize / (float)KB, 2)).ToString() + "KB";
            else
                return KSize.ToString() + "Byte";//顯示Byte值
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += ByteConversionGBMBKB(Convert.ToInt64(textBox1.Text)) + "\n";
        }






-------------------------------------------------------------------------------------------------------------------------------------

程式只能同時運行一個  在Form1_Load加入:

        private void Form1_Load(object sender, EventArgs e)
        {
            bool Exist;//定義一個bool變量 用來表示是否已經運行
            //創建Mutex互斥對象
            System.Threading.Mutex newMutex = new System.Threading.Mutex(true, "僅一次", out Exist);
            if (Exist)//如果沒有運行
            {
                newMutex.ReleaseMutex();//運行新窗体
            }
            else
            {
                MessageBox.Show("本程式一次只能運行一個實例！", "提示", MessageBoxButtons.OK, MessageBoxIcon.Information);//彈出提示信息
                this.Close();//關閉當前窗体
            }

        }
        






-------------------------------------------------------------------------------------------------------------------------------------





-------------------------------------------------------------------------------------------------------------------------------------








-------------------------------------------------------------------------------------------------------------------------------------





-------------------------------------------------------------------------------------------------------------------------------------








-------------------------------------------------------------------------------------------------------------------------------------





-------------------------------------------------------------------------------------------------------------------------------------








-------------------------------------------------------------------------------------------------------------------------------------





-------------------------------------------------------------------------------------------------------------------------------------










-------------------------------------------------------------------------------------------------------------------------------------





-------------------------------------------------------------------------------------------------------------------------------------









-------------------------------------------------------------------------------------------------------------------------------------





-------------------------------------------------------------------------------------------------------------------------------------









-------------------------------------------------------------------------------------------------------------------------------------





-------------------------------------------------------------------------------------------------------------------------------------








-------------------------------------------------------------------------------------------------------------------------------------





-------------------------------------------------------------------------------------------------------------------------------------








richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個



richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個


richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個


richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個



richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個



richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個


richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個


richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個



richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個



richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個


richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個


richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個



richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個



richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個


richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個


richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個



richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

----------------常用的程式片段 ST cccc----------------


string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
string filename = @"D:\_git\vcs\_1.data\______test_files1\__text\war_and_peace.txt";

//以下複製到每個檔案

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//------------------------------------------------------------

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

//1515
//---------------  # 15個


/*  可搬出

*/


