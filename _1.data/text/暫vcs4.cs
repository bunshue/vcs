
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


