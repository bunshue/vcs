using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

using System.Reflection;    //for BindingFlags

namespace test1101
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string filename_source = @"C:\______test_files\bear.jpg";
            string filename_destination = @"C:\______test_files\_cpfile\ccc.jpg";   //要寫完整檔名

            richTextBox1.Text += "檔案已存在的FileCopy/Move\n";
            try
            {
                //File.Copy(filename_source, filename_destination);     //若檔案已存在, 會出現IOException
                //File.Move(filename_source, filename_destination);     //若檔案已存在, 會出現IOException
                File.Copy(filename_source, filename_destination, true); //覆蓋檔案
                //File.Move(filename_source, filename_destination, true); //覆蓋檔案
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "xxx錯誤訊息m : " + ex.Message + "\n";
            }


        }

        private void button3_Click(object sender, EventArgs e)
        {
            string pathname = @"C:\______test_files\_cpfile";

            richTextBox1.Text += "Directory.Delete 目錄不是空的\n";
            try
            {
                //Directory.Delete(pathname); //若目錄不是空的, 會出現IOException
                Directory.Delete(pathname, true); //強制刪除不是空的目錄
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "xxx錯誤訊息m : " + ex.Message + "\n";
            }

        }

        private void button4_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\bear.jpg";

            richTextBox1.Text += File.GetAttributes(filename) + "\n";
            File.SetAttributes(filename, FileAttributes.ReadOnly);
            richTextBox1.Text += File.GetAttributes(filename) + "\n";



        }

        private void button5_Click(object sender, EventArgs e)
        {
            //用Reflection的方式取得系統中的所有Color，將利Color的名子加到comboBox中。
            Type type = typeof(Color);
            PropertyInfo[] propInfo = type.GetProperties(BindingFlags.Static | BindingFlags.Public);
            var names = from color in propInfo
                        where color.Name != "Transparent"
                        select color.Name;
            cmbColor.Items.Clear();
            foreach (var item in names)
            {
                cmbColor.Items.Add(item);
            }

        }

        private void cmbColor_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void cmbColor_DrawItem(object sender, DrawItemEventArgs e)
        {
            Graphics g = e.Graphics;
            Rectangle rect = e.Bounds;
            if (e.Index >= 0)
            {
                string colorName = ((ComboBox)sender).Items[e.Index].ToString();
                Font font = new Font("Arial", 9, FontStyle.Regular);
                Color color = Color.FromName(colorName);
                Brush brush = new SolidBrush(color);
                g.FillRectangle(brush, rect.X + 5, rect.Y, 10, rect.Height);
                g.DrawString(colorName, font, Brushes.Black, rect.X + 15, rect.Top);
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {


        }


    }
}
