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
            apply_listBox1();
            apply_listBox2();
            apply_listBox3();
            apply_listBox456();
            apply_listBox7();

            //apply_drawListBox0();
            apply_drawListBox1();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;
            int dd = 30;

            //button
            x_st = 10;
            y_st = 10;
            dx = 100 + 5;
            dy = 60 + 5;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);

            int w = 300;
            int h = 360;
            listBox0.Size = new Size(w, h);
            listBox1.Size = new Size(w, h);

            w = 180;
            listBox2.Size = new Size(w, h);
            listBox3.Size = new Size(w, h);
            listBox4.Size = new Size(w, h);
            listBox5.Size = new Size(w, h);
            listBox6.Size = new Size(w, h);
            listBox7.Size = new Size(w, h);
            listBox8.Size = new Size(w, h);
            listBox9.Size = new Size(w, h);
            drawListBox0.Size = new Size(w, h);
            drawListBox1.Size = new Size(w, h);

            label0.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            listBox0.Location = new Point(x_st + dx * 2, y_st + dy * 0 + dd);
            label1.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            listBox1.Location = new Point(x_st + dx * 2, y_st + dy * 6 + dd);

            richTextBox1.Text += "xx = " + (x_st + dx * 5).ToString() + "\n";
            richTextBox1.Text += "yy = " + (y_st + dy * 0).ToString() + "\n";
            x_st = 535;
            y_st = 10;
            dx = w + 10;

            label2.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            label3.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            label4.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            label5.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            label6.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            label7.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            label8.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            label9.Location = new Point(x_st + dx * 3, y_st + dy * 6);
            label10.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            label11.Location = new Point(x_st + dx * 4, y_st + dy * 6);

            listBox2.Location = new Point(x_st + dx * 0, y_st + dy * 0 + dd);
            listBox3.Location = new Point(x_st + dx * 0, y_st + dy * 6 + dd);
            listBox4.Location = new Point(x_st + dx * 1, y_st + dy * 0 + dd);
            listBox5.Location = new Point(x_st + dx * 1, y_st + dy * 6 + dd);
            listBox6.Location = new Point(x_st + dx * 2, y_st + dy * 0 + dd);
            listBox7.Location = new Point(x_st + dx * 2, y_st + dy * 6 + dd);
            listBox8.Location = new Point(x_st + dx * 3, y_st + dy * 0 + dd);
            listBox9.Location = new Point(x_st + dx * 3, y_st + dy * 6 + dd);
            drawListBox0.Location = new Point(x_st + dx * 4, y_st + dy * 0 + dd);
            drawListBox1.Location = new Point(x_st + dx * 4, y_st + dy * 6 + dd);

            richTextBox1.Size = new Size(240, 765 + 30);
            richTextBox1.Location = new Point(x_st + dx * 5, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1430 + 320, 830 + 30);

            label0.Text = "";
            label1.Text = "";
            label2.Text = "";
            label3.Text = "設定Tabs";
            label4.Text = "";
            label5.Text = "";
            label6.Text = "";
            label7.Text = "";
            label8.Text = "";
            label9.Text = "";
            label10.Text = "多顏色背景表示/自建ListBox";
            label11.Text = "";
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private const int ItemMargin2 = 5;
        private const float PictureHeight = 100f;
        void apply_listBox0()
        {
            listBox0.DrawItem += new DrawItemEventHandler(listBox0_DrawItem);
            listBox0.MeasureItem += new MeasureItemEventHandler(listBox0_MeasureItem);

            // Make the LIstBox owner drawn.
            listBox0.DrawMode = DrawMode.OwnerDrawVariable;

            listBox0.Items.Add(new Planet("Mercury", Properties.Resources.Mercury, "Distance: 0.39 AU, Radius: 0.38, Mass: 0.05, Day: 59 days, Year: 88 days"));
            listBox0.Items.Add(new Planet("Venus", Properties.Resources.Venus, "Distance: 0.72 AU, Radius: 0.95, Mass: 0.89, Day: 243 days, Year: 224 days"));
            listBox0.Items.Add(new Planet("Earth", Properties.Resources.Earth, "Distance: 1 AU, Radius: 1, Mass: 1, Day: 1 day, Year: 365 days"));
            listBox0.Items.Add(new Planet("Mars", Properties.Resources.Mars, "Distance: 1.5 AU, Radius: 0.53, Mass: 0.11, Day: 1.026 days, Year: 687 days"));
            listBox0.Items.Add(new Planet("Jupiter", Properties.Resources.Jupiter, "Distance: 5.2 AU, Radius: 11, Mass: 318, Day: 0.411 days, Year: 11.8 years"));
            listBox0.Items.Add(new Planet("Saturn", Properties.Resources.Saturn, "Distance: 9.5 AU, Radius: 9, Mass: 95, Day: 0.43 days, Year: 29.5 years"));
            listBox0.Items.Add(new Planet("Uranus", Properties.Resources.Uranus, "Distance: 19.2 AU, Radius: 4, Mass: 17, Day: 0.75 days, Year: 84 years"));
            listBox0.Items.Add(new Planet("Neptune", Properties.Resources.Neptune, "Distance: 30.1 AU, Radius: 4, Mass: 17, Day: 0.8 days, Year: 165 years"));
            listBox0.Items.Add(new Planet("Pluto", Properties.Resources.Pluto, "Distance: 39.5 AU, Radius: 0.18, Mass: 0.002, Day: 0.27 days, Year: 248 years"));
        }

        // Return enough space for the item.
        private void listBox0_MeasureItem(object sender, MeasureItemEventArgs e)
        {
            e.ItemHeight = (int)(PictureHeight + 2 * ItemMargin2);
        }

        // Draw the item.
        private void listBox0_DrawItem(object sender, DrawItemEventArgs e)
        {
            // Get the ListBox and the item.
            ListBox lst = sender as ListBox;
            Planet planet = (Planet)lst.Items[e.Index];

            // Draw the background.
            e.DrawBackground();

            // Draw the picture.
            float scale = PictureHeight / planet.Picture.Height;
            RectangleF source_rect = new RectangleF(
                0, 0, planet.Picture.Width, planet.Picture.Height);
            float picture_width = scale * planet.Picture.Width;
            RectangleF dest_rect = new RectangleF(
                e.Bounds.Left + ItemMargin2, e.Bounds.Top + ItemMargin2,
                picture_width, PictureHeight);
            e.Graphics.DrawImage(planet.Picture, dest_rect, source_rect, GraphicsUnit.Pixel);

            // See if the item is selected.
            Brush br;
            if ((e.State & DrawItemState.Selected) == DrawItemState.Selected)
                br = SystemBrushes.HighlightText;
            else
                br = new SolidBrush(e.ForeColor);

            // Find the area in which to put the text.
            float x = e.Bounds.Left + picture_width + 3 * ItemMargin2;
            float y = e.Bounds.Top + ItemMargin2;
            float width = e.Bounds.Right - ItemMargin2 - x;
            float height = e.Bounds.Bottom - ItemMargin2 - y;
            RectangleF layout_rect = new RectangleF(x, y, width, height);

            // Draw the text.
            string txt = planet.Name + '\n' + planet.Stats;
            e.Graphics.DrawString(txt, this.Font, br, layout_rect);

            // Outline the text.
            e.Graphics.DrawRectangle(Pens.Red, Rectangle.Round(layout_rect));

            // Draw the focus rectangle if appropriate.
            e.DrawFocusRectangle();
        }

        void apply_listBox1()
        {
            //ListBox客製化選單

            listBox1.MeasureItem += new MeasureItemEventHandler(listBox1_MeasureItem);
            listBox1.DrawItem += new DrawItemEventHandler(listBox1_DrawItem);

            // Make the ListBox owner drawn.
            // Create some items.
            listBox1.DrawMode = DrawMode.OwnerDrawVariable;

            listBox1.Items.Add("Name: Mercury\nMass: 0.055 Earths\nYear: 87.9691 Earth days\nTemp: −183 °C to 427 °C");
            listBox1.Items.Add("Name: Venus\nMass: 0.815 Earths\nYear: 243 Earth days");
            listBox1.Items.Add("Name: Earth\nMass: 1.0 Earths\nYear: 365.256 Earth days");
            listBox1.Items.Add("Name: Mars\nMass: 0.107 Earths\nYear: 686.971 Earth days");
        }

        // Calculate the size of an item.
        private int ItemMargin3 = 5;
        private void listBox1_MeasureItem(object sender, MeasureItemEventArgs e)
        {
            // Get the ListBox and the item.
            ListBox lst = sender as ListBox;
            string txt = (string)lst.Items[e.Index];

            // Measure the string.
            SizeF txt_size = e.Graphics.MeasureString(txt, this.Font);

            // Set the required size.
            e.ItemHeight = (int)txt_size.Height + 2 * ItemMargin3;
            e.ItemWidth = (int)txt_size.Width;
        }

        // Draw the item.
        private void listBox1_DrawItem(object sender, DrawItemEventArgs e)
        {
            // Get the ListBox and the item.
            ListBox lst = sender as ListBox;
            string txt = (string)lst.Items[e.Index];

            // Draw the background.
            e.DrawBackground();

            // See if the item is selected.
            if ((e.State & DrawItemState.Selected) == DrawItemState.Selected)
            {
                // Selected. Draw with the system highlight color.
                e.Graphics.DrawString(txt, this.Font,
                    SystemBrushes.HighlightText, e.Bounds.Left, e.Bounds.Top + ItemMargin3);
            }
            else
            {
                // Not selected. Draw with ListBox's foreground color.
                using (SolidBrush br = new SolidBrush(e.ForeColor))
                {
                    e.Graphics.DrawString(txt, this.Font, br,
                        e.Bounds.Left, e.Bounds.Top + ItemMargin3);
                }
            }

            // Draw the focus rectangle if appropriate.
            e.DrawFocusRectangle();

        }

        void apply_listBox2()
        {
            //多欄
            listBox2.Items.Clear();
            listBox2.MultiColumn = true;    //多欄
            listBox2.ColumnWidth = 45;      //欄寬
            int i;
            for (i = 0; i < 100; i++)
            {
                listBox2.Items.Add(i);
            }
        }

        void apply_listBox3()
        {
            // Set tabs.
            int[] tabs = { 75, 125, 175 };
            listBox1.SetTabs(tabs);

            int i;
            string txt = "";

            txt = "原數值" + "\t" + "平方項" + "\t" + "立方項";
            listBox1.Items.Add(txt);

            for (i = -5; i <= 5; i++)
            {
                txt = i.ToString() + "\t" + (i * i).ToString() + "\t" + (i * i * i).ToString();
                listBox3.Items.Add(txt);
            }
        }

        void apply_listBox456()
        {
            richTextBox1.Text += "字串一維陣列 轉 listBox\n";

            //字串一維陣列
            string[] ZodiacSign = { "水瓶座", "雙魚座", "牡羊座", "金牛座", "雙子座", "巨蟹座", "獅子座", "處女座", "天秤座", "天蠍座", "射手座", "魔羯座" };
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
                "牡羊座" 
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

        void apply_drawListBox1()
        {
            int i;
            for (i = 0; i < 20; i++)
            {
                drawListBox1.Items.Add("ListBox用多顏色背景表示\t\t" + i.ToString());
            }
        }

        private void button0_Click(object sender, EventArgs e)
        {
        }

        private void button1_Click(object sender, EventArgs e)
        {
        }

        private void button2_Click(object sender, EventArgs e)
        {
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
