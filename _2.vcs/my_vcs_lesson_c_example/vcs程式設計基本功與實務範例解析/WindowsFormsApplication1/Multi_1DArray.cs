using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Multi_1DArray : Form
    {
        public Multi_1DArray()
        {
            InitializeComponent();
        }

        string[] name = {"王一", "李二", "陳三", "趙四", "馬五"};
        int[] math = {98, 80, 50, 76, 69};
        int[] chin = {85, 90, 78, 54, 67};

        private void Multi_1DArray_Load(object sender, EventArgs e)
        {
            string res = "名字\t數學\t國文\r\n"; //表頭字串
            res += "====\t====\t====\r\n";       //分隔線字串

                  for (int i = 0; i < 5; i++)

                  {
                      res += name[i] + "\t"; // 每一筆佔一列
                      res += math[i] + "\t";
                      res += chin[i] + "\r\n"; // 跳行
                  }

                  res += "====\t====\t====\r\n"; //分隔線字串
                  txtOutput.Text = res;
        }

        private void btnCompute_Click(object sender, EventArgs e)
        {
            string h = "名字\t數學\t國文";  //固定的表頭字串
            string sep = "====\t====\t===="; //固定的分隔線字串

            //檢查勾選的項目，加上對應的字串
            if (chkAvg.Checked){
                h += "\t平均";
                sep += "\t====";
            }
            if (chkFailNum.Checked)
            {
                h += "\t不及格";
                sep += "\t======";
            }
            if (chkRank.Checked)
            {
                h += "\t名次";
                sep += "\t====";
            }

            // 個別選項的處理

            double[] avg = new double[5];

            if (chkAvg.Checked)
            {
                for (int i = 0; i < 5; i++)
                    avg[i] = (math[i] + chin[i]) / 2.0;
            }

            int[] fail = new int[5];

            if (chkFailNum.Checked)
            {
                for (int i = 0; i < 5; i++)
                {
                    fail[i] = 0;
                    if(math[i] < 60) fail[i] += 1;
                    if(chin[i] < 60) fail[i] += 1;
                }
            }

            int[] rank = new int[5];

            if (chkRank.Checked)
            {
                for (int i = 0; i < 5; i++)
                {
                    rank[i] = 1; //先假設名次為1
                    
                    int sum = math[i] + chin[i]; //計算其總分

                    /*依序和他人比較，只要有人較高分，其名次即遞增1*/
                    for (int j = 0; j < 5; j++)
                        if (math[j] + chin[j] > sum) rank[i] += 1;
                }
            }

            int sumMath = 0, sumChin = 0;

            if (chkCourseAvg.Checked)
            {
                for (int i = 0; i < 5; i++)
                {
                    sumMath += math[i];
                    sumChin += chin[i];
                }
            }
 
            // 輸出的處理
            string res = h + "\r\n" + sep + "\r\n";

            for (int i = 0; i < 5; i++)
            {
                res += name[i] + "\t";
                res += math[i] + "\t";
                res += chin[i] + "\t";

                if (chkAvg.Checked) res += avg[i] + "\t";
                if (chkFailNum.Checked) res += fail[i] + "\t";
                if (chkRank.Checked) res += rank[i] + "\t";

                res += "\r\n";
            }

            res += sep + "\r\n";

            if (chkCourseAvg.Checked)
            {
                res += "平均\t";
                res += sumMath / 5.0 + "\t";
                res += sumChin / 5.0 + "\r\n";
            }
            
            txtOutput.Text = res;
        }

        private void btnSearch_Click(object sender, EventArgs e)
        {
            string n = txtName.Text;

            bool isFound = false;
            int i;

            for (i = 0; i < 5; i++)
            {
                if (n == name[i])
                {
                    isFound = true;
                    break;
                }
            }
            if (isFound)
                txtOutput.Text = "名字:" + name[i] + "\r\n"
                               + "數學:" + math[i] + "\r\n"
                               + "國文:" + chin[i] + "\r\n";
            else
                txtOutput.Text = "???學生" + n + "的資料不存在???";

        }
    }
}
