using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Score
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {   //stu陣列存放學生姓名
            string[] stu = new string[] { "趙一", "林二", "張三", "李四" };
            string[] sub = new string[] { "計概", "程設", "專題" };//存放科目名稱
            int[,] score = new int[,] { { 91, 92, 93 },{ 81, 82, 83 },
            { 71, 72, 73 }, { 61, 62, 63 } };//在score陣列中存入學生成績
            int[] sum = new int[4]; //sum陣列存放四位學生的總分
            // 計算各學生的總分置入sum[y]
            for (int y = 0; y <= 3; y++)   //學生迴圈
            {
                for (int x = 0; x <= 2; x++)    //科目迴圈
                {
                    sum[y] += score[y, x];
                }
            }
            string msg = "姓名\t";    //宣告msg為字串變數
            foreach (string s in sub)    //讀取科目名稱加到msg
            {
                msg += s + "\t";
            }
            msg += "總分\n";
            // 逐列顯示學生姓名、計概、程設、專題、總分等成績
            for (int y = 0; y <= 3; y++)   //學生迴圈
            {
                msg += stu[y] + "\t";   //加入學生姓名
                for (int x = 0; x <= 2; x++)  //科目迴圈逐一讀取學生的各科成績
                {
                    msg += score[y, x].ToString() + "\t";
                }
                msg += sum[y].ToString() + "\n";   //加入學生總分
            }
            MessageBox.Show(msg, "成績表");
            Application.Exit();
        }
    }
}
