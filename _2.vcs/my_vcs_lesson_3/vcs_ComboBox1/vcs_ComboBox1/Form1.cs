using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Collections;   //for Hashtable
using System.Drawing.Drawing2D; //for LinearGradientBrush   //自繪帶圖片的 ComboBox

namespace vcs_ComboBox1
{
    public partial class Form1 : Form
    {
        private ImageList G_ImageList;//聲明ImageList字段

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            // Colors.
            Color[] colors =
            {
                Color.Red,
                Color.Orange,
                Color.Yellow,
                Color.Green,
                Color.Blue,
                Color.Indigo,
                Color.Purple,
            };
            cboColor.DisplayColorSamples(colors);
            cboColor.SelectedIndex = 0;

            // Faces.
            Image[] images = 
            {
                Properties.Resources.face1,
                Properties.Resources.face2,
                Properties.Resources.face3,
                Properties.Resources.face4,
            };
            cboFace.DisplayImages(images);
            cboFace.SelectedIndex = 0;
            cboFace.DropDownHeight = 200;

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //字串一維陣列
            string[] cities = new string[] { "台北", "新竹", "台中", "台南", "高雄" };
            comboBox1a.Items.AddRange(cities);
            comboBox1a.Text = cities[0];

            //預設選項包含關鍵字
            comboBox1a.SelectedItem = FindItemContaining(comboBox1a.Items, "台");

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //從陣列抓資料到combobox清單內
            //系統內建的全部滑鼠游標圖形
            //系統內建資料轉comboBox
            Cursor[] cursorList = new Cursor[] {
                Cursors.AppStarting, Cursors.Arrow, Cursors.Cross,
                Cursors.Default, Cursors.Hand, Cursors.Help,
                Cursors.HSplit, Cursors.IBeam, Cursors.No,
                Cursors.NoMove2D, Cursors.NoMoveHoriz, Cursors.NoMoveVert,
                Cursors.PanEast, Cursors.PanNE, Cursors.PanNorth,
                Cursors.PanNW, Cursors.PanSE, Cursors.PanSouth,
                Cursors.PanSW, Cursors.PanWest, Cursors.SizeAll,
                Cursors.SizeNESW, Cursors.SizeNS, Cursors.SizeNWSE,
                Cursors.SizeWE, Cursors.UpArrow, Cursors.VSplit, Cursors.WaitCursor};

            foreach (Cursor cursor in cursorList)
            {
                comboBox1b.Items.Add(cursor);  // 加入到 comboBox1b 清單內
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            comboBox2.DrawMode = DrawMode.OwnerDrawFixed;//設置繪制元素方式
            comboBox2.DropDownStyle = ComboBoxStyle.DropDownList; //設置組合框樣式
            comboBox2.Items.Add("小車");//添加項
            comboBox2.Items.Add("卡車");//添加項
            comboBox2.Items.Add("工具");//添加項
            comboBox2.Items.Add("朋友");//添加項
            G_ImageList = new ImageList();//創建ImageList對象
            G_ImageList.Images.Add(Properties.Resources.a);//添加圖片
            G_ImageList.Images.Add(Properties.Resources.b);//添加圖片
            G_ImageList.Images.Add(Properties.Resources.c);//添加圖片
            G_ImageList.Images.Add(Properties.Resources.d);//添加圖片

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            comboBox3.Items.Clear();
            comboBox3.Items.Add("Arial");
            comboBox3.Items.Add("Arial Black");
            comboBox3.Items.Add("Arial Narrow");
            comboBox3.Items.Add("Arial Rounded MT Bold");
            comboBox3.Items.Add("Arial Unicode MS");
            comboBox3.Items.Add("Bahnschrift");
            comboBox3.Items.Add("Bahnschrift Condensed");
            comboBox3.Items.Add("Bahnschrift Light");
            comboBox3.Items.Add("Bahnschrift Light Condensed");
            comboBox3.Items.Add("Bahnschrift Light SemiCondensed");
            comboBox3.Items.Add("Bahnschrift SemiBold");
            comboBox3.Items.Add("Bahnschrift SemiBold Condensed");
            comboBox3.Items.Add("Bahnschrift SemiBold SemiConden");
            comboBox3.Items.Add("Bahnschrift SemiCondensed");
            comboBox3.Items.Add("Segoe UI");
            comboBox3.Items.Add("Segoe UI Black");
            comboBox3.Items.Add("Segoe UI Emoji");
            comboBox3.Items.Add("Segoe UI Historic");
            comboBox3.Items.Add("Segoe UI Light");
            comboBox3.Items.Add("Segoe UI Semibold");
            comboBox3.Items.Add("Segoe UI Semilight");
            comboBox3.Items.Add("Segoe UI Symbol");
            comboBox3.Items.Add("新細明體");
            comboBox3.Items.Add("新細明體-ExtB");
            comboBox3.Items.Add("細明體");
            comboBox3.Items.Add("細明體-ExtB");
            comboBox3.Items.Add("細明體_HKSCS");
            comboBox3.Items.Add("細明體_HKSCS-ExtB");

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //添加項 
            comboBox4.Items.Add(new MyItem("000000", Image.FromFile(@"D:\_git\vcs\_1.data\______test_files1\__pic\_anime\_angry_bird\AB_red.jpg")));
            comboBox4.Items.Add(new MyItem("111111", Image.FromFile(@"D:\_git\vcs\_1.data\______test_files1\__pic\_anime\_angry_bird\AB_yellow.jpg")));
            comboBox4.Items.Add(new MyItem("222222", Image.FromFile(@"D:\_git\vcs\_1.data\______test_files1\__pic\_anime\_angry_bird\AB_blue.jpg")));
            comboBox4.Items.Add(new MyItem("333333", Image.FromFile(@"D:\_git\vcs\_1.data\______test_files1\__pic\_anime\_angry_bird\AB_black.jpg")));

            //默認選中項索引 
            comboBox4.SelectedIndex = 0;

            //自繪組合框需要設置的一些屬性 
            comboBox4.DrawMode = DrawMode.OwnerDrawFixed;
            comboBox4.DropDownStyle = ComboBoxStyle.DropDownList;
            comboBox4.ItemHeight = 50;
            comboBox4.Width = 200;

            //添加DrawItem事件處理函數 
            comboBox4.DrawItem += ComboBox4_DrawItem;

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            setup_comboBox5();

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            imageList8.Images.Add(new Bitmap("img/angry_bird/AB_red.jpg"));
            imageList8.Images.Add(new Bitmap("img/angry_bird/AB_yellow.jpg"));
            imageList8.Images.Add(new Bitmap("img/angry_bird/AB_blue.jpg"));
            imageList8.Images.Add(new Bitmap("img/angry_bird/AB_black.jpg"));
            imageList8.Images.Add(new Bitmap("img/angry_bird/AB_pig1.jpg"));
            imageList8.Images.Add(new Bitmap("img/angry_bird/AB_pig2.jpg"));
            imageList8.Images.Add(new Bitmap("img/angry_bird/AB_pig3.jpg"));
            imageList8.Images.Add(new Bitmap("img/angry_bird/AB_pig4.jpg"));

            richTextBox1.Text += "imageList8 共有 : " + imageList8.Images.Count.ToString() + " 張圖片\n";

            comboBox8.Size = new Size(300, 100);
            comboBox8.DrawMode = DrawMode.OwnerDrawFixed;
            comboBox8.DropDownStyle = ComboBoxStyle.DropDownList;

            comboBox8.Items.Add("紅鳥");
            comboBox8.Items.Add("黃鳥");
            comboBox8.Items.Add("藍鳥");
            comboBox8.Items.Add("黑鳥");
            comboBox8.Items.Add("小豬1");
            comboBox8.Items.Add("小豬2");
            comboBox8.Items.Add("小豬3");
            comboBox8.Items.Add("小豬4");
            comboBox8.SelectedIndex = 0;//設置ComboBox控件默認選中第一項

            //comboBox8.DrawItem += new DrawItemEventHandler(comboBox8_DrawItem);

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            int w = 400;
            int h = 150;

            groupBox1.Size = new Size(w, h * 4 + 120);
            groupBox6.Size = new Size(w, h * 3 / 2);

            x_st = 10;
            y_st = 10;
            dx = w + 10;
            dy = h + 10;
            groupBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            groupBox6.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            pictureBox1.Size = new Size(200, 150);
            pictureBox1.BackColor = Color.Pink;

            richTextBox1.Size = new Size(420, 600);
            richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            //groupBox內部的
            x_st = 20;
            y_st = 30;
            dx = 200;
            dy = 80;
            int dd = 25;

            label1a.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            comboBox1a.Location = new Point(x_st + dx * 0, y_st + dy * 0 + dd);

            label1b.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            comboBox1b.Location = new Point(x_st + dx * 0, y_st + dy * 1 + dd);

            label2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            comboBox2.Location = new Point(x_st + dx * 0, y_st + dy * 2 + dd);

            label3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            comboBox3.Location = new Point(x_st + dx * 0, y_st + dy * 3 + dd);
            button1.Location = new Point(x_st + dx * 0 + 230, y_st + dy * 3 + dd);

            label4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            comboBox4.Location = new Point(x_st + dx * 0, y_st + dy * 4 + dd);

            comboBox5.Location = new Point(x_st + dx * 0, y_st + dy * 5 + dd);

            comboBox8.Location = new Point(x_st + dx * 0, y_st + dy * 6 + dd);

            cboColor.Location = new Point(x_st + dx * 0, y_st + dy * 7 + dd);
            cboFace.Location = new Point(x_st + dx * 0 + 150, y_st + dy * 7 + dd);

            this.Size = new Size(1200, 800);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void comboBox8_DrawItem(object sender, DrawItemEventArgs e)
        {
            Graphics gComboBox = e.Graphics;//聲明一個GDI+繪圖圖面類的對象
            Rectangle rComboBox = e.Bounds;//聲明一個表示矩形的位置和大小類的對象
            Size imageSize = imageList8.ImageSize;//聲明一個有序整數對的對象
            FontDialog typeFace = new FontDialog();//定義一個字體類對像
            Font Style = typeFace.Font;//定義一個定義特定的文本格式類對像
            if (e.Index >= 0)//當繪製的索引項存在時
            {
                string temp = (string)comboBox8.Items[e.Index];//獲取ComboBox控件索引項下的文本內容
                StringFormat stringFormat = new StringFormat();//定義一個封裝文本佈局信息類的對象
                stringFormat.Alignment = StringAlignment.Near;//設定文本的佈局方式
                if (e.State == (DrawItemState.NoAccelerator | DrawItemState.NoFocusRect))//當繪製項沒有鍵盤加速鍵和焦點可視化提示時
                {
                    e.Graphics.FillRectangle(new SolidBrush(Color.Red), rComboBox);//用指定的顏色填充自定義矩形的內部
                    imageList8.Draw(e.Graphics, rComboBox.Left, rComboBox.Top, e.Index);//在指定位置繪製指定索引的圖片
                    e.Graphics.DrawString(temp, Style, new SolidBrush(Color.Black), rComboBox.Left + imageSize.Width, rComboBox.Top);//在指定的位置並且用指定的Font對像繪製指定的文本字符串
                    e.DrawFocusRectangle();//在指定的邊界範圍內繪製聚焦框
                }
                else //當繪製項有鍵盤加速鍵或者焦點可視化提示時
                {
                    e.Graphics.FillRectangle(new SolidBrush(Color.LightBlue), rComboBox);//用指定的顏色填充自定義矩形的內部
                    imageList8.Draw(e.Graphics, rComboBox.Left, rComboBox.Top, e.Index);//在指定位置繪製指定索引的圖片
                    e.Graphics.DrawString(temp, Style, new SolidBrush(Color.Black), rComboBox.Left + imageSize.Width, rComboBox.Top);//在指定的位置並且用指定的Font對像繪製指定的文本字符串
                    e.DrawFocusRectangle();//在指定的邊界範圍內繪製聚焦框
                }
            }
        }

        private object FindItemContaining(IEnumerable items, string target)
        {
            foreach (object item in items)
            {
                if (item.ToString().Contains(target))
                {
                    return item;
                }
            }
            return null;
        }

        private void comboBox2_DrawItem(object sender, DrawItemEventArgs e)
        {
            if (G_ImageList != null)//判斷ImageList是否為空
            {
                Graphics g = e.Graphics;//得到繪圖對象
                Rectangle r = e.Bounds;//得到繪圖范圍
                Size imageSize = G_ImageList.ImageSize;//獲取圖像大小
                if (e.Index >= 0)//判斷是否有繪制項
                {
                    Font fn = new Font("標楷體", 10, FontStyle.Bold);//創建字體對象
                    string s = comboBox2.Items[e.Index].ToString();//得到繪制項的字符串
                    DrawItemState dis = e.State;
                    if (e.State == (DrawItemState.NoAccelerator | DrawItemState.NoFocusRect))
                    {
                        e.Graphics.FillRectangle(new SolidBrush(Color.LightYellow), r);//畫條目背景
                        G_ImageList.Draw(e.Graphics, r.Left, r.Top, e.Index);//繪制圖像
                        e.Graphics.DrawString(s, fn, new SolidBrush(Color.Black),//顯示字符串
                            r.Left + imageSize.Width, r.Top);
                        e.DrawFocusRectangle();//顯示取得焦點時的虛線框
                    }
                    else
                    {
                        e.Graphics.FillRectangle(new SolidBrush(Color.LightGreen), r);//畫條目背景
                        G_ImageList.Draw(e.Graphics, r.Left, r.Top, e.Index);//繪制圖像
                        e.Graphics.DrawString(s, fn, new SolidBrush(Color.Black),//顯示字符串 
                            r.Left + imageSize.Width, r.Top);
                        e.DrawFocusRectangle();//顯示取得焦點時的虛線框 
                    }
                }
            }
        }

        private void ComboBox4_DrawItem(object sender, DrawItemEventArgs e)
        {
            //鼠標選中在這個項上 
            if ((e.State & DrawItemState.Selected) != 0)
            {
                //漸變畫刷 
                LinearGradientBrush brush = new LinearGradientBrush(e.Bounds, Color.FromArgb(255, 251, 237),
                                                 Color.FromArgb(255, 236, 181), LinearGradientMode.Vertical);
                //填充區域 
                Rectangle borderRect = new Rectangle(3, e.Bounds.Y, e.Bounds.Width - 5, e.Bounds.Height - 2);

                e.Graphics.FillRectangle(brush, borderRect);

                //畫邊框 
                Pen pen = new Pen(Color.FromArgb(229, 195, 101));
                e.Graphics.DrawRectangle(pen, borderRect);
            }
            else
            {
                SolidBrush brush = new SolidBrush(Color.FromArgb(255, 255, 255));
                e.Graphics.FillRectangle(brush, e.Bounds);
            }

            //獲得項圖片,繪制圖片 
            MyItem item = (MyItem)comboBox4.Items[e.Index];
            Image img = item.Img;

            //圖片繪制的區域 
            Rectangle imgRect = new Rectangle(6, e.Bounds.Y + 3, 45, 45);
            e.Graphics.DrawImage(img, imgRect);

            //文本內容顯示區域 
            Rectangle textRect =
                    new Rectangle(imgRect.Right + 2, imgRect.Y, e.Bounds.Width - imgRect.Width, e.Bounds.Height - 2);

            //獲得項文本內容,繪制文本 
            String itemText = comboBox4.Items[e.Index].ToString();

            //文本格式垂直居中 
            StringFormat strFormat = new StringFormat();
            strFormat.LineAlignment = StringAlignment.Center;
            e.Graphics.DrawString(itemText, new Font("微軟雅黑", 12), Brushes.Black, textRect, strFormat);
        }

        void setup_comboBox5()
        {
            // Make a font for the item text.
            Font font = new Font("Times New Roman", 14);

            // Make image and text data.
            ImageAndText[] planets =
            {
                new ImageAndText(Properties.Resources.Mercury,
                    "Name: Mercury" + '\n' +
                    "Distance: 0.31-0.47" + '\n' +
                    "Distance: 0.31-0.47" + '\n' +
                    "Mass: 0.06" + '\n' +
                    "Diameter: 0.382" + '\n' +
                    "Year: 0.24" + '\n' +
                    "Day: 58.64",
                    font),
                new ImageAndText(Properties.Resources.Venus,
                    "Name: Venus" + '\n' +
                    "Distance: 0.72" + '\n' +
                    "Mass: 0.82" + '\n' +
                    "Diameter: 0.949" + '\n' +
                    "Year: 0.62" + '\n' +
                    "Day: -243.02",
                    font),
                new ImageAndText(Properties.Resources.Earth,
                    "Name: Earth" + '\n' +
                    "Distance: 1" + '\n' +
                    "Mass: 1" + '\n' +
                    "Diameter: 1" + '\n' +
                    "Year: 1" + '\n' +
                    "Day: 1",
                    font),
                new ImageAndText(Properties.Resources.Mars,
                    "Name: Mars" + '\n' +
                    "Distance: 1.52" + '\n' +
                    "Mass: 0.11" + '\n' +
                    "Diameter: 0.532" + '\n' +
                    "Year: 1.88" + '\n' +
                    "Day: 1.03",
                    font),
                new ImageAndText(Properties.Resources.Jupiter,
                    "Name: Jupiter" + '\n' +
                    "Distance: 5.2" + '\n' +
                    "Mass: 317.8" + '\n' +
                    "Diameter: 11.209" + '\n' +
                    "Year: 11.86" + '\n' +
                    "Day: 0.41",
                    font),
                new ImageAndText(Properties.Resources.Saturn,
                    "Name: Saturn" + '\n' +
                    "Distance: 9.54" + '\n' +
                    "Mass: 95.2" + '\n' +
                    "Diameter: 9.449" + '\n' +
                    "Year: 29.46" + '\n' +
                    "Day: 0.43",
                    font),
                new ImageAndText(Properties.Resources.Uranus,
                    "Name: Uranus" + '\n' +
                    "Distance: 19.22" + '\n' +
                    "Mass: 14.6" + '\n' +
                    "Diameter: 4.007" + '\n' +
                    "Year: 84.01" + '\n' +
                    "Day: −0.72",
                    font),
                new ImageAndText(Properties.Resources.Neptune,
                    "Name: Neptune" + '\n' +
                    "Distance: 30.06" + '\n' +
                    "Mass: 17.2" + '\n' +
                    "Diameter: 3.883" + '\n' +
                    "Year: 164.8" + '\n' +
                    "Day: 0.67",
                    font),
            };

            comboBox5.DisplayImagesAndText(planets);
            comboBox5.SelectedIndex = 0;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //設置自動完成的模式
            comboBox3.AutoCompleteMode = AutoCompleteMode.SuggestAppend;
            //設置自動完成字串的來源
            comboBox3.AutoCompleteSource = AutoCompleteSource.ListItems;
        }

        Hashtable ht = new Hashtable();
        string foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic\_anime\_MU";

        //多層 且指明副檔名
        public void GetAllFiles(string foldername)
        {
            DirectoryInfo di = new DirectoryInfo(foldername);
            //richTextBox1.Text += "資料夾 : " + di.FullName + "\n";
            FileSystemInfo[] fileinfo = di.GetFileSystemInfos();
            foreach (FileSystemInfo fi in fileinfo)
            {
                if (fi is DirectoryInfo)
                {
                    GetAllFiles(((DirectoryInfo)fi).FullName);
                }
                else
                {
                    string fullname = fi.FullName;
                    string shortname = fi.Name;
                    string ext = fi.Extension.ToLower();
                    string forename = shortname.Substring(0, shortname.Length - ext.Length);    //前檔名

                    if (ext == ".jpg" || ext == ".jpeg" || ext == ".bmp" || ext == ".png" || ext == ".gif")
                    {
                        //ht.add(key, value), key不能重複
                        ht.Add(forename, fullname);

                        richTextBox1.Text += "加入 前檔名 : " + forename + "\t長檔名 : " + fullname + "\n";
                    }
                }
            }
        }

        private void showPic(string name)
        {
            this.pictureBox1.ImageLocation = name;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //尋找檔案
            GetAllFiles(foldername);

            foreach (DictionaryEntry de in ht)
            {
                this.comboBox6.Items.Add(de.Key);
            }
            if (comboBox6.Items.Count > 0)
                comboBox6.SelectedIndex = 0;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //顯示
            richTextBox1.Text += comboBox6.SelectedIndex.ToString() + "\n";

            if (comboBox6.SelectedIndex == -1)
                return;
            if (ht.Values.Count > 0)
            {
                showPic(ht[this.comboBox6.Text].ToString());
            }
            else
            {
                MessageBox.Show("目前還沒有圖片相關訊息！！！");
            }

        }

        private void button4_Click(object sender, EventArgs e)
        {
            //Info
            int len = ht.Count;

            richTextBox1.Text += "len = " + len.ToString() + "\n";

            //方法一：遍歷traversal 1:
            foreach (DictionaryEntry de in ht)
            {
                richTextBox1.Text += "key = " + de.Key + "\t" + "value = " + de.Value + "\n";
            }

            //方法二：遍歷traversal 2:
            IDictionaryEnumerator d = ht.GetEnumerator();
            while (d.MoveNext())
            {
                //richTextBox1.Text += "key = " + d.Entry.Key + "\t" + "value = " + d.Entry.Value + "\n";
            }

        }

    }

    //自定義組合框項 
    class MyItem
    {
        //項文本內容 
        private String Text;

        //項圖片 
        public Image Img;

        //構造函數 
        public MyItem(String text, Image img)
        {
            Text = text;
            Img = img;
        }

        //重寫ToString函數，返回項文本 
        public override string ToString()
        {
            return Text;
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


/*  可搬出

*/


