using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace PcDiy
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // 宣告主機廠牌名稱及對應的單價
        string[] deskPC = new string[] { "華爍主機", "碁峰主機", "技佳主機", "津英主機" };
        int[] deskPCPrice = new int[] { 20000, 18000, 15000, 12000 };
        // 宣告液晶螢幕尺寸名稱及對應的單價
        string[] CRT = new string[] { "15吋", "17吋", "19吋" };
        int[] CRTPrice = new int[] { 4000, 5000, 6000 };
        // 表單載入時執行
        private void Form1_Load(object sender, EventArgs e)
        {
            for (int i = 0; i <= deskPC.GetUpperBound(0); i++)
            {
                lstdeskPC.Items.Add(deskPC[i] + "(" + Convert.ToString(deskPCPrice[i]) + ")");
            }
            lstdeskPC.SelectedIndex = 0;
            for (int i = 0; i <= CRT.GetUpperBound(0); i++)
            {
                cbxCRT.Items.Add(CRT[i] + "(" +
                  Convert.ToString(CRTPrice[i]) + ")");
            }
            cbxCRT.SelectedIndex = 0;
        }
        // 主機廠牌清單的索引改變時執行
        private void lstdeskPC_SelectedIndexChanged(object sender, EventArgs e)
        {
            try
            {
                // 計算主機+螢幕合計金額
                int sum = deskPCPrice[lstdeskPC.SelectedIndex] + CRTPrice[cbxCRT.SelectedIndex];
                lblSum.Text = "合計：" + Convert.ToString(sum);
            }
            catch { }
        }
        // 液晶螢幕尺寸下拉式清單的索引改變時執行
        private void cbxCRT_SelectedIndexChanged(object sender, EventArgs e)
        {
            try
            {
                // 計算主機+螢幕合計金額
                int sum = deskPCPrice[lstdeskPC.SelectedIndex] + CRTPrice[cbxCRT.SelectedIndex];
                lblSum.Text = "合計：" + Convert.ToString(sum);
            }
            catch { }
        }
    }
}
