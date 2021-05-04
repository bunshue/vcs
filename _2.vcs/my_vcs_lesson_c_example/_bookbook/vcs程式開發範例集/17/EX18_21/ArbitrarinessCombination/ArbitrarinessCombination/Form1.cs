using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Collections;

namespace ArbitrarinessCombination
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        static string[] a =new string[6]{ "0", "1", "2", "3", "4", "5" };//定義數組
        int num = 6;//定義最大的個數
        int nIdx = 0, nSidx = 0;

        public void SetArbitrariness(int n, ArrayList List)
        {
            ArrayList SList = new ArrayList(a);//實例化ArrayList類
            SList.Clear();//清空ArrayList
            try
            {
                if (n >= 1)//如果大於等於1
                {
                    if (List.Count == 0)//如果List為空
                    {
                        for (nIdx = 0; nIdx <= num - 1; nIdx++)//新增單位數
                            SList.Add(a[nIdx]);
                    }
                    else
                    {
                        //新增多位數
                        for (nIdx = 0; nIdx <= num - 1; nIdx++)
                            for (nSidx = 0; nSidx <= List.Count - 1; nSidx++)
                                if (List[nSidx].ToString().IndexOf(a[nIdx]) == -1)//如查目前的值沒有新增
                                    SList.Add(a[nIdx] + List[nSidx].ToString());//新增
                    }
                    SetArbitrariness(n - 1, SList);//遞歸該方法
                }
                if (SList.Count > 0)//如果有數值
                {
                    List.Clear();//清空List
                    for (int i = 0; i < SList.Count; i++)//新增單位數
                        List.Add(SList[i].ToString());
                }
            }
            catch
            {
                SList.Clear();
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            ArrayList List = new ArrayList(a);//實例化ArrayList類
            List.Clear();//清空ArrayList類
            listBox1.Items.Clear();//清空listBox1控制元件
            SetArbitrariness(Convert.ToInt32(textBox1.Text), List);//呼叫自定義方法
            //將不同的數值新增到listBox1控制元件上
            for (int i = 0; i < List.Count; i++)
                listBox1.Items.Add(List[i].ToString());
            listBox1.Items.Add("Total:" + listBox1.Items.Count.ToString());//顯示一共執行了幾行
        }
    }
}
