using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for Directory

using System.Net;
using System.Net.NetworkInformation;    //for UnicastIPAddressInformation

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        Graphics g;
        Pen p;
        SolidBrush sb;
        Bitmap bitmap1;

        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int[,] x = { { 2, 3, 2 }, { 5, 6, 1 }, { 4, 6, 2 }, { 4, 6, 3 } };

            //int[, , , ,] y;

            richTextBox1.Text += "len = " + x.Length.ToString() + "\n";
            richTextBox1.Text += "rank = " + x.Rank.ToString() + "\n";
            //richTextBox1.Text += "rank = " + y.Rank.ToString() + "\n";


            int[, , ,] dim = new int[2, 5, 3, 7];
            richTextBox1.Text += "rank = " + dim.Rank.ToString() + "\n";
            //Console.WriteLine(dim.Rank);//結果 4

            //int[] num = { { { 5, 6 }, { 7, 8 } }, { { 5, 6 }, { 7, 8 } }, { { 5, 6 }, { 7, 8 } } };
            //richTextBox1.Text += "rank = " + num.Rank.ToString() + "\n";
            //Console.WriteLine(num.Rank);//結果 3



        }

        private void button2_Click(object sender, EventArgs e)
        {
            //撈出資料夾內所有jpg檔
            var dirnames = Directory.GetDirectories(@"C:\______test_files");
            int i = 0;

            try
            {
                foreach (var dir in dirnames)
                {
                    richTextBox1.Text += "aaaa3 dir = " + dir + "\n";
                    var fnames = Directory.GetFiles(dir, "*.jpg").Select(Path.GetFileName);

                    DirectoryInfo d = new DirectoryInfo(dir);
                    FileInfo[] finfo = d.GetFiles("*.jpg");

                    foreach (var f in fnames)
                    {
                        i++;
                        //richTextBox1.Text += "The number of the file being renamed is: " + i.ToString() + "\n";

                        richTextBox1.Text += f + "\n";

                        if (!File.Exists(Path.Combine(dir, f.ToString().Replace("(", "").Replace(")", ""))))
                        {
                            File.Move(Path.Combine(dir, f), Path.Combine(dir, f.ToString().Replace("(", "").Replace(")", "")));
                        }
                        else
                        {
                            richTextBox1.Text += "The file you are attempting to rename already exists! The file path is " + dir + "\n";
                            foreach (FileInfo fi in finfo)
                            {
                                //richTextBox1.Text += "The file modify date is: " + File.GetLastWriteTime(dir) + "\n";
                            }
                        }
                    }
                }
            }
            catch (Exception ex)
            {
                richTextBox1.Text += ex.Message + "\n";
            }
            richTextBox1.Text += "dirnames : " + dirnames + "\n";

        }

        private void button3_Click(object sender, EventArgs e)
        {
            //隨時產生臨時檔名
            //richTextBox1.Text += "臨時檔名 : " + string.Format("filename-{0:yyyy-MM-dd_HH:mm:ss}.txt", DateTime.Now) + "\n";

            //richTextBox1.Text += "臨時檔名 : " + string.Format("{0}{1}.txt", "filename-", DateTime.Now.ToString("yyyy-MM-dd_HH:mm:ss")) + "\n";


            string filename = string.Format("csv-{0:yyyy_MMdd_HHmmss}.csv", DateTime.Now);
            richTextBox1.Text += "filename : " + filename + "\n";

            int aaa = 123;
            int bbb = 456;

            using (var stream = File.CreateText(filename))
            {
                string first = aaa.ToString();
                string second = bbb.ToString();
                string csv = string.Format("{0},{1}\n", first, second);
                //File.WriteAllText(filename, csv);
                stream.WriteLine(csv);
                richTextBox1.Text += "csv : " + csv + "\n";
            }

        }

        private void button4_Click(object sender, EventArgs e)
        {
            //取得網卡的IPV6位置
            foreach (var ip in GetLocalIPV6IP())
            {
                richTextBox1.Text += "ip = " + ip.ToString() + "\n";
            }
        }

        private static IEnumerable<String> GetLocalIPV6IP()
        {
            return (from adapter in NetworkInterface.GetAllNetworkInterfaces()
                    where adapter.NetworkInterfaceType == NetworkInterfaceType.Ethernet
                    from AddressInfo in adapter.GetIPProperties().UnicastAddresses.OfType<UnicastIPAddressInformation>()
                    where AddressInfo.Address.AddressFamily == System.Net.Sockets.AddressFamily.InterNetworkV6
                    let ipAddress = AddressInfo.Address.ToString()
                    select ipAddress);
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //this.Size = new Size(1920 *2, 1080 / 1);

            //不規則陣列

            // Declare the array of two elements.
            int[][] arr = new int[3][];

            // Initialize the elements.
            arr[0] = new int[5] { 1, 3, 5, 7, 9 };
            arr[1] = new int[4] { 2, 4, 6, 8 };
            arr[2] = new int[2] { 2, 4 };



            // Display the array elements.
            for (int i = 0; i < arr.Length; i++)
            {
                richTextBox1.Text += "row(" + i.ToString() + "):\tlen = " + arr[i].Length.ToString() + "\t";

                for (int j = 0; j < arr[i].Length; j++)
                {
                    richTextBox1.Text += arr[i][j].ToString() + "_";
                    //System.Console.Write("{0}{1}", arr[i][j], j == (arr[i].Length - 1) ? "" : " ");
                }
                richTextBox1.Text += "\n";
            }
            /*

            int row = arr.Rank;//獲取行數
            int col1 = arr.GetLength(0);//獲取指定維中的元 個數，這裡也就是列數了。（1表示的是第二維，0是第一維）
            int col2 = arr.GetUpperBound(0) + 1;//獲取指定維度的上限，在 上一個1就是列數
            int num1 = arr.Length;//獲取整個二維陣列的長度，即所有元 的個數

            richTextBox1.Text += "row = " + row.ToString() + "\n";
            richTextBox1.Text += "col1 = " + col1.ToString() + "\n";
            richTextBox1.Text += "col2 = " + col2.ToString() + "\n";
            richTextBox1.Text += "num1 = " + num1.ToString() + "\n";
            */

        }

        private void button6_Click(object sender, EventArgs e)
        {
            int i;

            //二維List for string
            List<string[]> steps = new List<string[]>();

            for (i = 0; i < 9; i++)
            {
                steps.Add(new string[] { i.ToString(), ('A' + i).ToString() });
            }

            //steps.Clear();

            if (steps.Count > 0)
                richTextBox1.Text += "共有 " + steps.Count.ToString() + " 個項目, 分別是:\n";

            for (i = 0; i < steps.Count; i++)
            {
                int tt = int.Parse(steps[i][1]);
                richTextBox1.Text += "steps[" + i.ToString() + "][0] = " + steps[i][0].ToString() + "\tsteps[" + i.ToString() + "][1] = " + (char)tt + "\n";
            }

            //刪除第N項
            int N;

            N = 1; steps.RemoveAt(N);  //index = N, 刪除第N項

            N = 3; steps.RemoveAt(N);  //index = N, 刪除第N項

            N = 5; steps.RemoveAt(N);  //index = N, 刪除第N項

            if (steps.Count > 0)
                richTextBox1.Text += "共有 " + steps.Count.ToString() + " 個項目, 分別是:\n";

            for (i = 0; i < steps.Count; i++)
            {
                int aaa = int.Parse(steps[i][1]);
                richTextBox1.Text += "steps[" + i.ToString() + "][0] = " + steps[i][0].ToString() + "\tsteps[" + i.ToString() + "][1] = " + (char)aaa + "\n";
            }

            /*
            Random r = new Random();
            string result2 = "";
            for (i = 0; i < 5; i++)
            {
                result2 += r.Next(10).ToString() + " ";
            }
            richTextBox1.Text += "取0~10的亂數值：" + result2 + "\n";
            */


            Random r = new Random();

            int[] selected = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
            int tmp;

            for (i = 0; i < selected.Length; i++)
            {
                int n = r.Next(selected.Length);
                //richTextBox1.Text += "第" + i.ToString() + "項和第" + n.ToString() + "項交換\n";
                tmp = selected[i];
                selected[i] = selected[n];
                selected[n] = tmp;
            }
            richTextBox1.Text += "方法一結果：";
            for (i = 0; i < selected.Length; i++)
            {
                richTextBox1.Text += selected[i].ToString() + " ";
            }
            richTextBox1.Text += "\n";

            for (i = 0; i < selected.Length; i++)
            {
                selected[i] = i;
            }

            for (i = selected.Length - 1; i > 0; i--)
            {
                int n = r.Next(i + 1);
                //richTextBox1.Text += "第" + i.ToString() + "項和第" + n.ToString() + "項交換\n";
                tmp = selected[i];
                selected[i] = selected[n];
                selected[n] = tmp;
            }

            richTextBox1.Text += "方法二結果：";
            for (i = 0; i < selected.Length; i++)
            {
                richTextBox1.Text += selected[i].ToString() + " ";
            }
            richTextBox1.Text += "\n";

        }



    }


}
