using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D; //for LinearGradientBrush   //自繪帶圖片的 ComboBox

namespace vcs_ComboBox1
{
    public partial class Form1 : Form
    {
        private ImageList G_ImageList;//声明ImageList字段

        public Form1()
        {
            InitializeComponent();
        }

        // Add colors and pictures to the ComboBoxes.
        private void Form1_Load(object sender, EventArgs e)
        {
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


            //從陣列抓資料到combobox清單內
            Cursor[] cursorList = new Cursor[] {  // 系統內建的全部滑鼠游標圖形 
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
                comboBox1.Items.Add(cursor);  // 加入到 comboBox1 清單內
            }



            comboBox2.DrawMode = DrawMode.OwnerDrawFixed;//设置绘制元素方式
            comboBox2.DropDownStyle = ComboBoxStyle.DropDownList; //设置组合框样式
            comboBox2.Items.Add("小车");//添加项
            comboBox2.Items.Add("卡车");//添加项
            comboBox2.Items.Add("工具");//添加项
            comboBox2.Items.Add("朋友");//添加项
            G_ImageList = new ImageList();//创建ImageList对象
            G_ImageList.Images.Add(Properties.Resources.a);//添加图片
            G_ImageList.Images.Add(Properties.Resources.b);//添加图片
            G_ImageList.Images.Add(Properties.Resources.c);//添加图片
            G_ImageList.Images.Add(Properties.Resources.d);//添加图片

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

            //comboBox4
            //添加項 
            comboBox4.Items.Add(new MyItem("000000", Image.FromFile(@"C:\______test_files\__pic\_angry_bird\AB_red.jpg")));
            comboBox4.Items.Add(new MyItem("111111", Image.FromFile(@"C:\______test_files\__pic\_angry_bird\AB_yellow.jpg")));
            comboBox4.Items.Add(new MyItem("222222", Image.FromFile(@"C:\______test_files\__pic\_angry_bird\AB_blue.jpg")));
            comboBox4.Items.Add(new MyItem("333333", Image.FromFile(@"C:\______test_files\__pic\_angry_bird\AB_black.jpg")));

            //默認選中項索引 
            comboBox4.SelectedIndex = 0;

            //自繪組合框需要設置的一些屬性 
            comboBox4.DrawMode = DrawMode.OwnerDrawFixed;
            comboBox4.DropDownStyle = ComboBoxStyle.DropDownList;
            comboBox4.ItemHeight = 50;
            comboBox4.Width = 200;

            //添加DrawItem事件處理函數 
            comboBox4.DrawItem += ComboBox4_DrawItem;


        }

        private void comboBox2_DrawItem(object sender, DrawItemEventArgs e)
        {
            if (G_ImageList != null)//判断ImageList是否为空
            {
                Graphics g = e.Graphics;//得到绘图对象
                Rectangle r = e.Bounds;//得到绘图范围
                Size imageSize = G_ImageList.ImageSize;//获取图像大小
                if (e.Index >= 0)//判断是否有绘制项
                {
                    Font fn = new Font("宋体", 10, FontStyle.Bold);//创建字体对象
                    string s = comboBox2.Items[e.Index].ToString();//得到绘制项的字符串
                    DrawItemState dis = e.State;
                    if (e.State == (DrawItemState.NoAccelerator | DrawItemState.NoFocusRect))
                    {
                        e.Graphics.FillRectangle(new SolidBrush(Color.LightYellow), r);//画条目背景
                        G_ImageList.Draw(e.Graphics, r.Left, r.Top, e.Index);//绘制图像
                        e.Graphics.DrawString(s, fn, new SolidBrush(Color.Black),//显示字符串
                            r.Left + imageSize.Width, r.Top);
                        e.DrawFocusRectangle();//显示取得焦点时的虚线框
                    }
                    else
                    {
                        e.Graphics.FillRectangle(new SolidBrush(Color.LightGreen), r);//画条目背景
                        G_ImageList.Draw(e.Graphics, r.Left, r.Top, e.Index);//绘制图像
                        e.Graphics.DrawString(s, fn, new SolidBrush(Color.Black),//显示字符串 
                            r.Left + imageSize.Width, r.Top);
                        e.DrawFocusRectangle();//显示取得焦点时的虚线框 
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

        private void button1_Click(object sender, EventArgs e)
        {
            //設置自動完成的模式
            comboBox3.AutoCompleteMode = AutoCompleteMode.SuggestAppend;
            //設置自動完成字串的來源
            comboBox3.AutoCompleteSource = AutoCompleteSource.ListItems;
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

