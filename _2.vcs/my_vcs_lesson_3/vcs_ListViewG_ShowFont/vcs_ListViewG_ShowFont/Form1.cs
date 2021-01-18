using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Drawing.Text;  //for font

namespace vcs_ListViewG_ShowFont
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            Show_Font_by_ListView();
        }

        void Show_Font_by_ListView()
        {
            //需要先把 listView1 的 View 屬性設成 Details
            int iii = 0;
            //C#專案中常常要獲取系統字型
            InstalledFontCollection fontCol = new InstalledFontCollection();

            listView1.Clear();

            listView1.Columns.Add("項目", 100, HorizontalAlignment.Center);
            listView1.Columns.Add("字型", 500, HorizontalAlignment.Center);
            listView1.Columns.Add("範例", 700, HorizontalAlignment.Center);

            foreach (FontFamily temp in fontCol.Families)
            {
                iii++;
                ListViewItem i1 = new ListViewItem(iii.ToString());
                ListViewItem.ListViewSubItem sub_i1a = new ListViewItem.ListViewSubItem();
                sub_i1a.Text = temp.Name;
                i1.SubItems.Add(sub_i1a);
                ListViewItem.ListViewSubItem sub_i1b = new ListViewItem.ListViewSubItem();
                if (temp.Name[0] <= 'z')
                {
                    if (textBox1.Text.Length > 0)
                        sub_i1b.Text = textBox1.Text;
                    else
                        sub_i1b.Text = "2017 Happy New Year";
                }
                else
                {
                    if (textBox1.Text.Length > 0)
                        sub_i1b.Text = textBox1.Text;
                    else
                        sub_i1b.Text = "春水碧於天，畫船聽雨眠。";
                }
                i1.SubItems.Add(sub_i1b);

                try
                {
                    i1.Font = new Font(temp.Name, 24);
                }
                catch (Exception ex)
                {   //定義產生錯誤時的例外處理程式碼
                    sub_i1b.Text = ex.Message;
                }
                finally
                {
                    //一定會被執行的程式區段
                }
                listView1.Items.Add(i1);
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Show_Font_by_ListView();
        }
    }
}
