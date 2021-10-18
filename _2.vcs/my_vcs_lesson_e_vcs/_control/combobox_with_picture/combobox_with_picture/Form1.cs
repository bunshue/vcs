using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D; //for LinearGradientBrush

//自繪帶圖片的 ComboBox

namespace combobox_with_picture
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //添加項 
            comboBox1.Items.Add(new MyItem("000000", Image.FromFile(@"C:\_git\vcs\_2.vcs\______test_files\_AB\AB_red.jpg")));
            comboBox1.Items.Add(new MyItem("111111", Image.FromFile(@"C:\_git\vcs\_2.vcs\______test_files\_AB\AB_yellow.jpg")));
            comboBox1.Items.Add(new MyItem("222222", Image.FromFile(@"C:\_git\vcs\_2.vcs\______test_files\_AB\AB_blue.jpg")));
            comboBox1.Items.Add(new MyItem("333333", Image.FromFile(@"C:\_git\vcs\_2.vcs\______test_files\_AB\AB_black.jpg")));

            //默認選中項索引 
            comboBox1.SelectedIndex = 0;

            //自繪組合框需要設置的一些屬性 
            comboBox1.DrawMode = DrawMode.OwnerDrawFixed;
            comboBox1.DropDownStyle = ComboBoxStyle.DropDownList;
            comboBox1.ItemHeight = 50;
            comboBox1.Width = 200;

            //添加DrawItem事件處理函數 
            comboBox1.DrawItem += ComboBox1_DrawItem;

        }

        private void ComboBox1_DrawItem(object sender, DrawItemEventArgs e)
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
            MyItem item = (MyItem)comboBox1.Items[e.Index];
            Image img = item.Img;

            //圖片繪制的區域 
            Rectangle imgRect = new Rectangle(6, e.Bounds.Y + 3, 45, 45);
            e.Graphics.DrawImage(img, imgRect);

            //文本內容顯示區域 
            Rectangle textRect =
                    new Rectangle(imgRect.Right + 2, imgRect.Y, e.Bounds.Width - imgRect.Width, e.Bounds.Height - 2);

            //獲得項文本內容,繪制文本 
            String itemText = comboBox1.Items[e.Index].ToString();

            //文本格式垂直居中 
            StringFormat strFormat = new StringFormat();
            strFormat.LineAlignment = StringAlignment.Center;
            e.Graphics.DrawString(itemText, new Font("微軟雅黑", 12), Brushes.Black, textRect, strFormat);
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

