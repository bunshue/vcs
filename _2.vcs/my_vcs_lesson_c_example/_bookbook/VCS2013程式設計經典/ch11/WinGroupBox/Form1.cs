using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WinGroupBox
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        // 表單載入時執行
        private void Form1_Load(object sender, EventArgs e)
        {
            rdbXBoxOne.Checked = true;  // 預設XBox One選項鈕被選取
        }
        private void rdbXBoxOne_CheckedChanged(object sender, EventArgs e)
        {
            gbXBoxOne.Enabled = true;// XBox One 遊戲群組方塊不失效，可啟用
            gbPS4.Enabled = false;   // PS4遊戲群組方塊失效
        }
        // 按 PS4 選項鈕執行
        private void rdbPS4_CheckedChanged(object sender, EventArgs e)
        {
            gbXBoxOne.Enabled = false;
            gbPS4.Enabled = true;
        }
        // 按 [確定] 鈕執行
        private void btnOk_Click(object sender, EventArgs e)
        {
            string str = "謝謝您購買";
            if (rdbXBoxOne.Checked)   		// 判斷XBox One是否被選取
            {
                str += rdbXBoxOne.Text + "\n";
                if (gbChkXBoxOne_1.Checked)  	// 判斷忍者外傳是否被勾選
                {
                    str += gbChkXBoxOne_1.Text + ", ";
                }
                if (gbChkXBoxOne_2.Checked)   	// 判斷生死格鬥是否被勾選
                {
                    str += gbChkXBoxOne_2.Text + ", ";
                }
                if (gbChkXBoxOne_3.Checked)   	// 判斷大聯盟是否被勾選
                {
                    str += gbChkXBoxOne_3.Text + ", ";
                }
            }
            else if (rdbPS4.Checked)  		// 判斷PS 4 是否被選取
            {
                str += rdbPS4.Text + "\n";
                if (gbChkPS4_1.Checked)   	// 判斷火影忍者是否被勾選
                {
                    str += gbChkPS4_1.Text + ", ";
                }
                if (gbChkPS4_2.Checked)   	// 判斷航海王是否被勾選
                {
                    str += gbChkPS4_2.Text + ", ";
                }
                if (gbChkPS4_3.Checked)   	//  判斷瑪麗歐賽車是否被勾選
                {
                    str += gbChkPS4_3.Text + ", ";
                }
            }
            // 出現對話方塊顯示使用者所選購的主機及遊戲
            MessageBox.Show(str);
        }
    }
}
