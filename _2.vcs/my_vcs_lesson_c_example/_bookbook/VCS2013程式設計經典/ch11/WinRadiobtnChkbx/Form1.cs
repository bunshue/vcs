using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WinRadiobtnChkbx
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
            rdbXBoxOne.Checked = true;	// 預設XBox One選項鈕被選取
        }
        // 按 Xbox One 選項鈕執行
        private void rdbXBoxOne_CheckedChanged(object sender, EventArgs e)
        {
            chkXBoxOne_1.Enabled = true;	// 忍者外傳核取方塊不失效
            chkXBoxOne_2.Enabled = true;	// 生死格鬥核取方塊不失效
            chkXBoxOne_3.Enabled = true;	// 大聯盟核取方塊不失效
            chkPS4_1.Enabled = false;	// 火影忍者核取方塊失效
            chkPS4_2.Enabled = false;	// 航海王核取方塊失效
            chkPS4_3.Enabled = false;	// 瑪麗歐賽車核取方塊失效
        }
        // 按 PS4 選項鈕執行
        private void rdbPS4_CheckedChanged(object sender, EventArgs e)
        {
            chkXBoxOne_1.Enabled = false;
            chkXBoxOne_2.Enabled = false;
            chkXBoxOne_3.Enabled = false;
            chkPS4_1.Enabled = true;
            chkPS4_2.Enabled = true;
            chkPS4_3.Enabled = true;
        }
        // 按 [確定] 鈕執行
        private void btnOk_Click(object sender, EventArgs e)
        {
            string str = "謝謝您購買";
            if (rdbXBoxOne.Checked)   		// 判斷XBox One是否被選取
            {
                str += rdbXBoxOne.Text + "\n";
                if (chkXBoxOne_1.Checked)  	// 判斷忍者外傳是否被勾選
                {
                    str += chkXBoxOne_1.Text + ", ";
                }
                if (chkXBoxOne_2.Checked)   	// 判斷生死格鬥是否被勾選
                {
                    str += chkXBoxOne_2.Text + ", ";
                }
                if (chkXBoxOne_3.Checked)   	// 判斷大聯盟是否被勾選
                {
                    str += chkXBoxOne_3.Text + ", ";
                }
            }
            else if (rdbPS4.Checked)  		// 判斷PS 4 是否被選取
            {
                str += rdbPS4.Text + "\n";
                if (chkPS4_1.Checked)   		// 判斷火影忍者是否被勾選
                {
                    str += chkPS4_1.Text + ", ";
                }
                if (chkPS4_2.Checked)   		// 判斷航海王是否被勾選
                {
                    str += chkPS4_2.Text + ", ";
                }
                if (chkPS4_3.Checked)   		//  判斷瑪麗毆賽車是否被勾選
                {
                    str += chkPS4_3.Text + ", ";
                }
            }
            // 出現對話方塊顯示使用者所選購的主機及遊戲
            MessageBox.Show(str);
        }
    }
}
