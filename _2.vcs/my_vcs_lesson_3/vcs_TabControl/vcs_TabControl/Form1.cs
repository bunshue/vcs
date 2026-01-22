using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_TabControl
{
    public partial class Form1 : Form
    {
        // The size of the X in each tab's upper right corner.
        private int Xwid = 8;
        private const int tab_margin = 3;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            this.tabPage1.Parent = this.tabControl1;    //顯示
            this.tabPage2.Parent = this.tabControl1;    //顯示
            this.tabPage3.Parent = this.tabControl1;    //顯示
            this.tabPage4.Parent = this.tabControl1;    //顯示
            this.tabPage5.Parent = this.tabControl1;    //顯示
            this.tabPage6.Parent = null;                //隱藏
            this.tabPage7.Parent = null;                //隱藏
            this.tabPage8.Parent = null;                //隱藏
            this.tabPage9.Parent = null;                //隱藏
            this.tabPage10.Parent = null;               //隱藏

            radioButton1.Checked = false;
            radioButton2.Checked = false;
            radioButton3.Checked = false;
            radioButton4.Checked = true;
            radioButton5.Checked = false;

            tabControl1.SelectedIndex = 4;      //程式啟動時，直接跳到第5頁。
            label1.Text = "顯示所有頁面、tab選第5頁。";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            // We will draw the tabs.
            tabControl2.DrawMode = TabDrawMode.OwnerDrawFixed;

            // SizeMode must be Fixed to change tab size.
            tabControl2.SizeMode = TabSizeMode.Fixed;

            // Set the size for the tabs.
            Size tab_size = tabControl2.ItemSize;
            tab_size.Width = 100;
            tab_size.Height += 6;
            tabControl2.ItemSize = tab_size;

            // Register MouseClick events for the tabs.
            foreach (TabPage page in tabControl2.TabPages)
            {
                page.MouseClick += new MouseEventHandler(page_MouseClick);
            }


        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 200 + 10;
            dy = 60 + 10;

            label6.Location = new Point(tabControl2.Location.X, tabControl2.Location.Y - 30);
            richTextBox1.Size = new Size(300, 300);
            richTextBox1.Location = new Point(x_st + dx * 4, y_st + dy * 4 + 60);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1200, 710);
            this.Text = "vcs_TabControl";
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void radioButton1_CheckedChanged(object sender, EventArgs e)
        {
            this.tabPage1.Parent = this.tabControl1;    //顯示
            this.tabPage2.Parent = null;                //隱藏
            this.tabPage3.Parent = this.tabControl1;    //顯示
            this.tabPage4.Parent = null;                //隱藏
            this.tabPage5.Parent = this.tabControl1;    //顯示
            this.tabPage6.Parent = null;                //隱藏
            this.tabPage7.Parent = this.tabControl1;    //顯示
            this.tabPage8.Parent = null;                //隱藏
            this.tabPage9.Parent = this.tabControl1;    //顯示
            this.tabPage10.Parent = null;               //隱藏
            tabControl1.SelectedIndex = 2;              //接跳到第3頁。
            label1.Text = "A計畫，顯示單數頁面、tab選第3頁。";
        }

        private void radioButton2_CheckedChanged(object sender, EventArgs e)
        {
            this.tabPage1.Parent = null;                //隱藏
            this.tabPage2.Parent = this.tabControl1;    //顯示
            this.tabPage3.Parent = null;                //隱藏
            this.tabPage4.Parent = this.tabControl1;    //顯示
            this.tabPage5.Parent = null;                //隱藏
            this.tabPage6.Parent = this.tabControl1;    //顯示
            this.tabPage7.Parent = null;                //隱藏
            this.tabPage8.Parent = this.tabControl1;    //顯示
            this.tabPage9.Parent = null;                //隱藏
            this.tabPage10.Parent = this.tabControl1;   //顯示
            tabControl1.SelectedIndex = 2;              //接跳到第3頁。
            label1.Text = "B計畫，顯示雙數頁面、tab選第3頁。";
        }

        private void radioButton3_CheckedChanged(object sender, EventArgs e)
        {
            this.tabPage1.Parent = null;                //隱藏
            this.tabPage2.Parent = null;                //隱藏
            this.tabPage3.Parent = this.tabControl1;    //顯示
            this.tabPage4.Parent = null;                //隱藏
            this.tabPage5.Parent = null;                //隱藏
            this.tabPage6.Parent = this.tabControl1;    //顯示
            this.tabPage7.Parent = null;                //隱藏
            this.tabPage8.Parent = null;                //隱藏
            this.tabPage9.Parent = this.tabControl1;    //顯示
            this.tabPage10.Parent = null;               //隱藏
            tabControl1.SelectedIndex = 2;              //接跳到第3頁。
            label1.Text = "C計畫，顯示三倍數頁面、tab選第3頁。";
        }

        private void radioButton4_CheckedChanged(object sender, EventArgs e)
        {
            this.tabPage1.Parent = this.tabControl1;    //顯示
            this.tabPage2.Parent = this.tabControl1;    //顯示
            this.tabPage3.Parent = this.tabControl1;    //顯示
            this.tabPage4.Parent = this.tabControl1;    //顯示
            this.tabPage5.Parent = this.tabControl1;    //顯示
            this.tabPage6.Parent = this.tabControl1;    //顯示
            this.tabPage7.Parent = this.tabControl1;    //顯示
            this.tabPage8.Parent = this.tabControl1;    //顯示
            this.tabPage9.Parent = this.tabControl1;    //顯示
            this.tabPage10.Parent = this.tabControl1;   //顯示
            tabControl1.SelectedIndex = 2;              //接跳到第3頁。
            label1.Text = "全開，顯示所有頁面、tab選第3頁。";
        }

        private void radioButton5_CheckedChanged(object sender, EventArgs e)
        {
            this.tabPage1.Parent = null;                //隱藏
            this.tabPage2.Parent = null;                //隱藏
            this.tabPage3.Parent = null;                //隱藏
            this.tabPage4.Parent = null;                //隱藏
            this.tabPage5.Parent = null;                //隱藏
            this.tabPage6.Parent = null;                //隱藏
            this.tabPage7.Parent = null;                //隱藏
            this.tabPage8.Parent = null;                //隱藏
            this.tabPage9.Parent = null;                //隱藏
            this.tabPage10.Parent = null;               //隱藏
            tabControl1.SelectedIndex = 2;              //接跳到第3頁。
            label1.Text = "全關，顯示所有頁面、tab選第3頁。";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (radioButton3.Checked == true)
            {
                this.tabPage1.Parent = this.tabControl1;
                this.tabPage2.Parent = this.tabControl1;
                this.tabPage4.Parent = this.tabControl1;
                this.tabPage5.Parent = this.tabControl1;
                this.tabPage7.Parent = this.tabControl1;
                this.tabPage8.Parent = this.tabControl1;
            }
        }

        private void bt_info_Click(object sender, EventArgs e)
        {
            //把所有TabPage的資訊掃瞄一次

            foreach (TabPage tp in tabControl1.TabPages)
            {
                richTextBox1.Text += "tab page name : " + tp.Name + "\n";

                /*
                // Add the Panel to the list.
                Panel panel = page.Controls[0] as Panel;

                this.Controls.Add(panel);
                //Panels.Add(panel);

                // Reparent and move the Panel.
                panel.Parent = tabControl1.Parent;
                panel.Location = tabControl1.Location;
                panel.Visible = false;
                */
            }


        }

        //6060

        // The user has clicked this tab page.
        private void page_MouseClick(object sender, MouseEventArgs e)
        {
            Rectangle tab_rect = tabControl2.GetTabRect(0);
            RectangleF rect = new RectangleF(
                tab_rect.Left + tab_margin,
                tab_rect.Y + tab_margin,
                tab_rect.Width - 2 * tab_margin,
                tab_rect.Height - 2 * tab_margin);
            if (e.X >= rect.Right - Xwid &&
                e.X <= rect.Right &&
                e.Y >= rect.Top &&
                e.Y <= rect.Top + Xwid)
            {
                Console.WriteLine("Tab " + 0);
                // tabMenu.TabPages.RemoveAt(i);
                tabControl2.TabPages.Remove(tabControl2.TabPages[0]);
                return;
            }
        }

        // Draw a tab.
        private void tabControl2_DrawItem(object sender, DrawItemEventArgs e)
        {
            Brush txt_brush, box_brush;
            Pen box_pen;

            // We draw in the TabRect rather than on e.Bounds
            // so we can use TabRect later in MouseDown.
            Rectangle tab_rect = tabControl2.GetTabRect(e.Index);

            // Draw the background.
            // Pick appropriate pens and brushes.
            if (e.State == DrawItemState.Selected)
            {
                e.Graphics.FillRectangle(Brushes.DarkOrange, tab_rect);
                e.DrawFocusRectangle();

                txt_brush = Brushes.Yellow;
                box_brush = Brushes.Silver;
                box_pen = Pens.DarkBlue;
            }
            else
            {
                e.Graphics.FillRectangle(Brushes.PaleGreen, tab_rect);

                txt_brush = Brushes.DarkBlue;
                box_brush = Brushes.LightGray;
                box_pen = Pens.DarkBlue;
            }

            // Allow room for margins.
            RectangleF layout_rect = new RectangleF(
                tab_rect.Left + tab_margin, tab_rect.Y + tab_margin,
                tab_rect.Width - 2 * tab_margin, tab_rect.Height - 2 * tab_margin);
            using (StringFormat string_format = new StringFormat())
            {
                // Draw the tab # in the upper left corner.
                using (Font small_font = new Font(this.Font.FontFamily, 6, FontStyle.Bold))
                {
                    string_format.Alignment = StringAlignment.Near;
                    string_format.LineAlignment = StringAlignment.Near;
                    e.Graphics.DrawString(e.Index.ToString(),
                        small_font, txt_brush, layout_rect, string_format);
                }

                // Draw the tab's text centered.
                using (Font big_font = new Font(this.Font, FontStyle.Bold))
                {
                    string_format.Alignment = StringAlignment.Center;
                    string_format.LineAlignment = StringAlignment.Center;
                    e.Graphics.DrawString(
                        tabControl2.TabPages[e.Index].Text,
                        big_font, txt_brush, layout_rect, string_format);
                }

                // Draw an X in the upper right corner.
                Rectangle rect = tabControl2.GetTabRect(e.Index);
                e.Graphics.FillRectangle(box_brush, layout_rect.Right - Xwid,
                    layout_rect.Top, Xwid, Xwid);
                e.Graphics.DrawRectangle(box_pen, layout_rect.Right - Xwid,
                    layout_rect.Top, Xwid, Xwid);
                e.Graphics.DrawLine(box_pen, layout_rect.Right - Xwid,
                    layout_rect.Top, layout_rect.Right, layout_rect.Top + Xwid);
                e.Graphics.DrawLine(box_pen, layout_rect.Right - Xwid,
                    layout_rect.Top + Xwid, layout_rect.Right, layout_rect.Top);
            }
        }

        // If the mouse is over an X, close the tab.
        private void tabControl2_MouseDown(object sender, MouseEventArgs e)
        {
            // See if this is over a tab.
            for (int i = 0; i < tabControl2.TabPages.Count; i++)
            {
                // Get the TabRect plus room for margins.
                Rectangle tab_rect = tabControl2.GetTabRect(i);
                RectangleF rect = new RectangleF(
                    tab_rect.Left + tab_margin, tab_rect.Y + tab_margin,
                    tab_rect.Width - 2 * tab_margin, tab_rect.Height - 2 * tab_margin);
                if (e.X >= rect.Right - Xwid && e.X <= rect.Right &&
                    e.Y >= rect.Top && e.Y <= rect.Top + Xwid)
                {
                    Console.WriteLine("Removing Tab " + i);
                    // tabControl2.TabPages.RemoveAt(i);
                    tabControl2.TabPages.Remove(tabControl2.TabPages[i]);
                    return;
                }
            }
        }

        // Add a tab to the end of the TabControl.
        private void lblAddTab_Click(object sender, EventArgs e)
        {
            Console.WriteLine("Adding a new tab");

            TabPage page = new TabPage("New");
            page.BackColor = Color.LightBlue;
            tabControl2.TabPages.Add(page);

            Label label = new Label();
            label.Location = new Point(0, 0);
            label.Text = "Tab number " + (tabControl2.TabPages.Count - 1);
            label.AutoSize = true;
            page.Controls.Add(label);
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

