using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//ListBox用多顏色背景表示
//自建ListBox
//加入/現有項目 選取DrawListBox.cs

/*
DrawListBox使用方法
方案總管/加入/現有項目, 選DrawListBox.cs, 會自動帶入DrawListBox.Designer.cs
改namespace
工具箱會出現 DrawListBox
使用方法如同ListBox, 就是多了顏色, 把GradualC改為true
*/

namespace vcs_ListBox1
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

            apply_listBox0();
            apply_listBox2();
            apply_listBox3();
            apply_listBox456();
            apply_listBox7();
            apply_listBox8();

            //apply_drawListBox0();
            apply_drawListBox1();
        }

        void show_item_location()
        {
            int x_st = 10;
            int y_st = 12;
            int dd = 34;
            int w = 190;
            int h = 320;
            int dx = w + 10;
            int dy = h + 50;

            listBox0.Size = new Size(w, h);
            listBox1.Size = new Size(w, h);
            listBox2.Size = new Size(w, h);
            listBox3.Size = new Size(w, h);
            listBox4.Size = new Size(w, h);
            listBox5.Size = new Size(w, h);
            listBox6.Size = new Size(w, h);
            listBox7.Size = new Size(w, h);
            listBox8.Size = new Size(w + 100, h);
            listBox9.Size = new Size(w + 100, h);
            drawListBox0.Size = new Size(w * 1, h);
            drawListBox1.Size = new Size(w * 1, h);

            label0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            label1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            label2.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            label3.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            label4.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            label5.Location = new Point(x_st + dx * 2, y_st + dy * 1 - 10);
            label6.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            label7.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            label8.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            label9.Location = new Point(x_st + dx * 4, y_st + dy * 1);
            label10.Location = new Point(x_st + dx * 5 + 100, y_st + dy * 0 - 10);
            label11.Location = new Point(x_st + dx * 5 + 100, y_st + dy * 1 - 10);

            listBox0.Location = new Point(x_st + dx * 0, y_st + dy * 0 + dd);
            listBox1.Location = new Point(x_st + dx * 0, y_st + dy * 1 + dd);
            listBox2.Location = new Point(x_st + dx * 1, y_st + dy * 0 + dd);
            listBox3.Location = new Point(x_st + dx * 1, y_st + dy * 1 + dd);
            listBox4.Location = new Point(x_st + dx * 2, y_st + dy * 0 + dd);
            listBox5.Location = new Point(x_st + dx * 2, y_st + dy * 1 + dd);
            listBox6.Location = new Point(x_st + dx * 3, y_st + dy * 0 + dd);
            listBox7.Location = new Point(x_st + dx * 3, y_st + dy * 1 + dd);
            listBox8.Location = new Point(x_st + dx * 4, y_st + dy * 0 + dd);
            listBox9.Location = new Point(x_st + dx * 4, y_st + dy * 1 + dd);
            drawListBox0.Location = new Point(x_st + dx * 5 + 100, y_st + dy * 0 + dd);
            drawListBox1.Location = new Point(x_st + dx * 5 + 100, y_st + dy * 1 + dd);

            richTextBox1.Size = new Size(240, 765 + 30);
            richTextBox1.Location = new Point(x_st + dx * 6 + 100, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1640, 830 + 20);

            label0.Text = "(0)各種方法";
            label1.Text = "(1)";
            label2.Text = "(2)多欄, 每欄40";
            label3.Text = "(3)設定Tabs";
            label4.Text = "(4)字串一維陣列";
            label5.Text = "(5)字串一維陣列\n     轉 List";
            label6.Text = "(6)使用字串List";
            label7.Text = "(7)使用 Class";
            label8.Text = "(8)";
            label9.Text = "(9)";
            label10.Text = "(10)多顏色背景表示\n     自建ListBox";
            label11.Text = "(11)多顏色背景表示\n     建ListBox";
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        void apply_listBox0()
        {
            //ListBox客製化選單, 需要以下3個
            listBox0.MeasureItem += new MeasureItemEventHandler(listBox0_MeasureItem);
            listBox0.DrawItem += new DrawItemEventHandler(listBox0_DrawItem);
            listBox0.DrawMode = DrawMode.OwnerDrawVariable;

            //字串一維陣列
            richTextBox1.Text += "字串一維陣列 轉 listBox\n";
            //字串一維陣列
            string[] ZodiacSign = { "水瓶座", "雙魚座\n財運\n愛情", "牡羊座", "金牛座\n事業", "雙子座", "巨蟹座\n學習成長" };
            listBox0.DataSource = ZodiacSign;//字串一維陣列直接餵給listBox
            /* 另法填資料
            listBox0.Items.Add("Name: Mercury\nMass: 0.055 Earths\nYear: 87.9691 Earth days\nTemp: ?183 °C to 427 °C");
            listBox0.Items.Add("Name: Venus\nMass: 0.815 Earths\nYear: 243 Earth days");
            listBox0.Items.Add("Name: Earth\nMass: 1.0 Earths\nYear: 365.256 Earth days");
            listBox0.Items.Add("Name: Mars\nMass: 0.107 Earths\nYear: 686.971 Earth days");
            */

            listBox0.Click += new EventHandler(listBox0_Click);
            listBox0.DoubleClick += new EventHandler(listBox0_DoubleClick);
            listBox0.Enter += new EventHandler(listBox0_Enter);
            listBox0.KeyPress += new KeyPressEventHandler(listBox0_KeyPress);
        }

        // Calculate the size of an item.
        private int ItemMargin0 = 10;
        private void listBox0_MeasureItem(object sender, MeasureItemEventArgs e)
        {
            ListBox lst = sender as ListBox;
            string txt = (string)lst.Items[e.Index];
            richTextBox1.Text += "第 " + e.Index.ToString() + " 項\t" + txt + "\n";

            //量測字串的大小
            Font font = new Font("標楷體", 11);
            //Font font = this.Font;
            SizeF txt_size = e.Graphics.MeasureString(txt, font);
            richTextBox1.Text += "W = " + txt_size.Width.ToString() + ", H = " + txt_size.Height.ToString() + "\n";

            // Set the required size.
            e.ItemHeight = (int)txt_size.Height + 2 * ItemMargin0;
            e.ItemWidth = (int)txt_size.Width;
            richTextBox1.Text += "eW = " + e.ItemWidth.ToString() + ", eH = " + e.ItemHeight.ToString() + "\n\n";
        }

        private void listBox0_DrawItem(object sender, DrawItemEventArgs e)
        {
            richTextBox1.Text += "2222\n";
            ListBox lst = sender as ListBox;
            string txt = (string)lst.Items[e.Index];
            //richTextBox1.Text += "第 " + e.Index.ToString() + " 項\t" + txt + "\n";

            e.DrawBackground();//畫listBox的背景

            int x_st = e.Bounds.Left;
            int y_st = e.Bounds.Top;
            int x_sp = e.Bounds.Right;
            int y_sp = e.Bounds.Bottom;
            int w = x_sp - x_st;
            int h = y_sp - y_st;
            Font font = new Font("標楷體", 11);
            //Font font = this.Font;
            //量測字串的大小
            SizeF txt_size = e.Graphics.MeasureString(txt, font);

            // See if the item is selected.
            if ((e.State & DrawItemState.Selected) == DrawItemState.Selected)
            {
                //richTextBox1.Text += "已選擇\n";
                //e.Graphics.DrawString(txt, font, SystemBrushes.HighlightText, x_st, y_st + ItemMargin0);
                e.Graphics.DrawString(txt, font, SystemBrushes.HighlightText, x_st, y_st + ItemMargin0);
            }
            else
            {
                //richTextBox1.Text += "未選擇\n";
                using (SolidBrush br = new SolidBrush(e.ForeColor))
                {
                    e.Graphics.FillRectangle(new SolidBrush(Color.Pink), x_st, y_st, w - 2, h - 2);
                    e.Graphics.DrawRectangle(Pens.Red, x_st, y_st, w - 2, h - 2);
                    e.Graphics.DrawString(txt, font, br, x_st, y_st + ItemMargin0);
                    e.Graphics.DrawRectangle(Pens.Green, x_st, y_st + ItemMargin0, txt_size.Width, txt_size.Height);
                }
            }

            // Draw the focus rectangle if appropriate.
            e.DrawFocusRectangle();
        }

        void listBox0_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Click : " + listBox0.SelectedIndex.ToString() + "\t" + listBox0.SelectedItem + "\n";
        }

        void listBox0_DoubleClick(object sender, EventArgs e)
        {
            richTextBox1.Text += "D ";
        }

        void listBox0_Enter(object sender, EventArgs e)
        {
            richTextBox1.Text += "你進入了 listBox0\n";
        }

        void listBox0_KeyPress(object sender, KeyPressEventArgs e)
        {
            richTextBox1.Text += "P ";
        }

        //------------------------------------------------------------  # 60個

        void apply_listBox2()
        {
            //多欄
            listBox2.Items.Clear();
            listBox2.MultiColumn = true;    //多欄
            listBox2.ColumnWidth = 40;      //欄寬
            for (int i = 0; i < 300; i++)
            {
                listBox2.Items.Add(i);
            }
        }

        void apply_listBox3()
        {
            //設定每個Tab的寬度
            int[] tabs = { 40, 40, 40 };
            listBox3.SetTabs(tabs);

            string txt = "原數值\t平方項\t立方項";
            listBox3.Items.Add(txt);

            for (int i = -5; i <= 5; i++)
            {
                txt = i.ToString() + "\t" + (i * i).ToString() + "\t" + (i * i * i).ToString();
                listBox3.Items.Add(txt);
            }
        }

        void apply_listBox456()
        {
            richTextBox1.Text += "字串一維陣列 轉 listBox\n";

            //字串一維陣列
            string[] ZodiacSign = { "水瓶座", "雙魚座", "牡羊座", "金牛座", "雙子座", "巨蟹座" };
            listBox4.DataSource = ZodiacSign;//字串一維陣列直接餵給listBox

            //3030

            richTextBox1.Text += "字串一維陣列 轉 List 轉 listBox\n";

            //字串一維陣列 轉 List
            List<string> ZodiacSignList = new List<string>(ZodiacSign);       //string 轉 List
            listBox5.DataSource = ZodiacSignList;

            //3030

            //使用字串List
            List<string> ZodiacSignList2 = new List<string>() 
            { 
                "水瓶座", 
                "雙魚座", 
                "牡羊座",
                "金牛座",
                "雙子座",
                "巨蟹座" 
            };
            listBox6.DataSource = ZodiacSignList2;
        }

        void apply_listBox7()
        {
            //使用 Class
            Person[] people = 
            {
                new Person() { FirstName="Simon", LastName="Green" },
                new Person() { FirstName="Terry", LastName="Pratchett" },
                new Person() { FirstName="Eowin", LastName="Colfer" },
            };
            listBox7.DataSource = people;
        }

        //------------------------------------------------------------  # 60個

        private int ItemMargin8 = 5;
        private float PictureHeight = 100f;
        void apply_listBox8()
        {
            //ListBox客製化選單, 需要以下3個
            listBox8.DrawItem += new DrawItemEventHandler(listBox8_DrawItem);
            listBox8.MeasureItem += new MeasureItemEventHandler(listBox8_MeasureItem);
            listBox8.DrawMode = DrawMode.OwnerDrawVariable;

            listBox8.Items.Add(new Planet("Mercury", Properties.Resources.Mercury, "Distance: 0.39 AU, Radius: 0.38, Mass: 0.05, Day: 59 days, Year: 88 days"));
            listBox8.Items.Add(new Planet("Venus", Properties.Resources.Venus, "Distance: 0.72 AU, Radius: 0.95, Mass: 0.89, Day: 243 days, Year: 224 days"));
            listBox8.Items.Add(new Planet("Earth", Properties.Resources.Earth, "Distance: 1 AU, Radius: 1, Mass: 1, Day: 1 day, Year: 365 days"));
            listBox8.Items.Add(new Planet("Mars", Properties.Resources.Mars, "Distance: 1.5 AU, Radius: 0.53, Mass: 0.11, Day: 1.026 days, Year: 687 days"));
            listBox8.Items.Add(new Planet("Jupiter", Properties.Resources.Jupiter, "Distance: 5.2 AU, Radius: 11, Mass: 318, Day: 0.411 days, Year: 11.8 years"));
            listBox8.Items.Add(new Planet("Saturn", Properties.Resources.Saturn, "Distance: 9.5 AU, Radius: 9, Mass: 95, Day: 0.43 days, Year: 29.5 years"));
            listBox8.Items.Add(new Planet("Uranus", Properties.Resources.Uranus, "Distance: 19.2 AU, Radius: 4, Mass: 17, Day: 0.75 days, Year: 84 years"));
            listBox8.Items.Add(new Planet("Neptune", Properties.Resources.Neptune, "Distance: 30.1 AU, Radius: 4, Mass: 17, Day: 0.8 days, Year: 165 years"));
            listBox8.Items.Add(new Planet("Pluto", Properties.Resources.Pluto, "Distance: 39.5 AU, Radius: 0.18, Mass: 0.002, Day: 0.27 days, Year: 248 years"));
        }

        // Return enough space for the item.
        private void listBox8_MeasureItem(object sender, MeasureItemEventArgs e)
        {
            e.ItemHeight = (int)(PictureHeight + 2 * ItemMargin8);
        }

        private void listBox8_DrawItem(object sender, DrawItemEventArgs e)
        {
            // Get the ListBox and the item.
            ListBox lst = sender as ListBox;
            Planet planet = (Planet)lst.Items[e.Index];

            e.DrawBackground();//畫listBox的背景

            // Draw the picture.
            float scale = PictureHeight / planet.Picture.Height;
            RectangleF source_rect = new RectangleF(
                0, 0, planet.Picture.Width, planet.Picture.Height);
            float picture_width = scale * planet.Picture.Width;
            RectangleF dest_rect = new RectangleF(
                e.Bounds.Left + ItemMargin8, e.Bounds.Top + ItemMargin8,
                picture_width, PictureHeight);
            e.Graphics.DrawImage(planet.Picture, dest_rect, source_rect, GraphicsUnit.Pixel);

            // See if the item is selected.
            Brush br;
            if ((e.State & DrawItemState.Selected) == DrawItemState.Selected)
                br = SystemBrushes.HighlightText;
            else
                br = new SolidBrush(e.ForeColor);

            // Find the area in which to put the text.
            float x = e.Bounds.Left + picture_width + 3 * ItemMargin8;
            float y = e.Bounds.Top + ItemMargin8;
            float width = e.Bounds.Right - ItemMargin8 - x;
            float height = e.Bounds.Bottom - ItemMargin8 - y;
            RectangleF layout_rect = new RectangleF(x, y, width, height);

            // Draw the text.
            //Font font = new Font("標楷體", 14);
            Font font = this.Font;

            string txt = planet.Name + '\n' + planet.Stats;
            e.Graphics.DrawString(txt, font, br, layout_rect);

            // Outline the text.
            e.Graphics.DrawRectangle(Pens.Red, Rectangle.Round(layout_rect));

            // Draw the focus rectangle if appropriate.
            e.DrawFocusRectangle();
        }

        //------------------------------------------------------------  # 60個

        void apply_drawListBox1()
        {
            for (int i = 0; i < 20; i++)
            {
                drawListBox1.Items.Add("多顏色背景表示\t" + i.ToString());
            }
        }
    }

    //Person類別
    public class Person
    {
        public string FirstName { get; set; }
        public string LastName { get; set; }

        public override string ToString()
        {
            return FirstName + " " + LastName;
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



