using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Management;

using System.Drawing.Imaging;
using System.IO;

using System.Data.OleDb;

using System.Diagnostics;


using System.IO.Ports;
using System.Threading;

using System.Runtime.InteropServices;

namespace WindowsFormsApplication1gif
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
        }

        private void button1_Click(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            //動態處理DataTable
            //動態處理DataTable

            //1.創建表實例
            DataTable dt = new DataTable();

            //2.建立表結構
            dt.Columns.Add("ID");
            dt.Columns.Add("Name");

            //3.創建新行
            DataRow dr = dt.NewRow();

            //4.為新行賦值
            dr[0] = "1";
            dr[1] = "林林";

            //5.將新行添加到表
            dt.Rows.Add(dr);


            /*
            //1.創建表實例
            DataTable dt=new DataTable();

            //2.建立表結構
            dt.Columns.Add("ID");
            dt.Columns.Add("Name");

            //3.添加新行
            dt.Rows.Add("1", "Name");
            */
        }

        private void button6_Click(object sender, EventArgs e)
        {
            int lower = 0x20;
            int upper = 0xD7FF;

            string result = NextString(lower, upper, 30);
            richTextBox1.Text += result + "\n";
        }

        public string NextString(int charLowerBound, int charUpperBound, int length)
        {
            Random r = new Random();
            return new String(
                Enumerable.Repeat(0, length)
                    .Select(p => (char)r.Next(charLowerBound, charUpperBound))
                    .ToArray());
        }


        //计算两点GPS坐标距离 
        /// <summary>
        ///计算两点GPS坐标的距离
        /// </summary>
        /// <param name="n1">第一点的纬度坐标</param>
        /// <param name="e1">第一点的经度坐标</param>
        /// <param name="n2">第二点的纬度坐标</param>
        /// <param name="e2">第二点的经度坐标</param>
        /// <returns></returns>
        public static double Distance(double n1, double e1, double n2, double e2)
        {
            double jl_jd = 102834.74258026089786013677476285;   // 米/度
            double jl_wd = 111712.69150641055729984301412873;   // 米/度
            double b = Math.Abs((e1 - e2) * jl_jd);
            double a = Math.Abs((n1 - n2) * jl_wd);
            return Math.Sqrt((a * a + b * b));
        }

        private void button7_Click(object sender, EventArgs e)
        {

        }
    }
}
