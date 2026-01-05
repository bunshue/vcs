

richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個




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



                DateTime baseDateAndTime = new DateTime(1900, 1, 6, 2, 5, 0); //#1/6/1900 2:05:00 AM#
                DateTime newDate;
                    num = 525948.76 * (y - 1900) + sTermInfo[i - 1];
                    newDate = baseDateAndTime.AddMinutes(num);//按分钟计算


            //後一天
            DateTime nextDay = _date.AddDays(1);
            //前一天
            DateTime pervDay = _date.AddDays(-1);
            return new ChineseCalendar(pervDay);




        return "公元" + this._date.ToLongDateString();
        /// 当前是否公历闰年
                return DateTime.IsLeapYear(this._date.Year);






richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            /*
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
            */




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

        private void Form1_Load(object sender, EventArgs e)
        {
            //按Enter連動到button1
            this.AcceptButton = button1;
            //按ESC連動到button1
            this.CancelButton = button2;

            //不再TaskBar上顯示程式
            this.ShowInTaskbar = false;
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


