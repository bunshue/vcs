using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WinChkLstBx
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // 建立pcLot陣列，其陣列元素為pcLot[0]~pcLot[5]
        // 用來存放本期大樂透的6個號碼
        int[] pcLot = new int[6];

        private void Form1_Load(object sender, EventArgs e)
        {
            checkedListBox1.MultiColumn = true;	// chkListLot水平欄顯示
            checkedListBox1.ColumnWidth = 45;    	// chkListLot水平欄寬45
            // 在chkListLot核取清單方塊加入 1- 49大樂透號碼，可讓使用者勾選
            for (int i = 1; i <= 49; i++)
            {
                checkedListBox1.Items.Add(i.ToString());
            }
            lblShow.Text = "本期未開獎...";
        }

        // 按 [對獎] 鈕執行
        private void btnCheckLot_Click(object sender, EventArgs e)
        {
            // 宣告 count變數，用來記錄使用者勾選大樂透幾個號碼
            int count = 0;
            // 使用for 迴圈記錄目前共勾選幾個號碼
            for (int i = 0; i < checkedListBox1.Items.Count; i++)
            {
                if (checkedListBox1.GetItemChecked(i))
                {
                    count++;
                }
            }
            // 如果沒有勾選 6 個號碼就離開此事件處理函式
            if (count != 6)
            {
                MessageBox.Show("請選擇 6 個號碼!");
                return;  // 離開此事件處理函式
            }
            // 呼叫SetLot方法， 產生本期大樂透6個號碼並放入pcLot陣列內
            SetLot(ref pcLot, 1, 49, pcLot.Length);
            // 將pcLot陣列內的大樂透號碼進行遞增排序，以方便比對是否中獎
            Array.Sort(pcLot);
            // 宣告 myNumStr變數用來存放使用者所選的號碼字串
            // 宣告 pcNumStr變數用來存放本期大樂透號碼字串
            string myNumStr = "", pcNumStr = "";
            // 將本期大樂透號碼逐一指定給pcNumStr字串變數
            // 以便將來和使用者所選號碼myNumStr字串比對
            for (int i = 0; i <= pcLot.GetUpperBound(0); i++)
            {
                pcNumStr += pcLot[i].ToString() + ", ";
            }
            // 將使用者在chkListLot所選號碼逐一指定給myNumStr字串變數
            // 以便將來和大樂透號碼pcNumStr字串比對
            for (int i = 0; i < checkedListBox1.Items.Count; i++)
            {
                if (checkedListBox1.GetItemChecked(i))
                {
                    myNumStr += checkedListBox1.Items[i].ToString() + ", ";
                }
            }
            // lblShow顯示本期開獎號碼
            lblShow.Text = "本期大樂透號碼如下\n" + pcNumStr + "\n";
            // 判斷是否中獎
            if (pcNumStr == myNumStr)
            {
                lblShow.Text += "恭禧你中大獎了...";
            }
            else
            {
                lblShow.Text += "沒中，請再接再厲...";
            }
        }

        private void btnCls_Click(object sender, EventArgs e)
        {
        }


        // SetLot可用來設定num個min~max之間的亂數，並將亂數值放入choose陣列內
        void SetLot(ref  int[] choose, int min, int max, int num)
        {
            int[] lot = new int[50];//陣列元素為lot[0]~lot[49],lot[49]省略不用 
            int max_dim, choice;
            int i, j;
            max_dim = max - min + 1;
            for (i = 0; i < max_dim; i++)
            {
                lot[i] = min + i;
            }
            Random rndObj = new Random();  // 建立亂數物件rndObj
            for (i = 0; i < num; i++)
            {
                choice = rndObj.Next(0, max_dim);
                choose[i] = lot[choice];
                for (j = choice; j < max_dim; j++)
                {
                    lot[j] = lot[j + 1];
                }
                max_dim--;
            }
        }
    }
}
