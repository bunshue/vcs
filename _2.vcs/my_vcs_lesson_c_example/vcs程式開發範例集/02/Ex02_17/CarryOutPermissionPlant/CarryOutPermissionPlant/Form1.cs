using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace CarryOutPermissionPlant
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void checkedListBox3_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void ckInfo_CheckedChanged(object sender, EventArgs e)
        {
            if (ckInfo.Checked == true)
            {
                ckLinfo.Visible = true;

                CheckAll(ckLinfo);
            }
            else
            {
                ckLinfo.Visible = false;
                CheckAllEsce(ckLinfo);
            }// end block 
        }

        private void ckShop_CheckedChanged(object sender, EventArgs e)
        {
            if (ckShop.Checked == true)
            {
                cklShop.Visible = true;
                CheckAll(cklShop);
            }
            else
            {
                cklShop.Visible = false;
                CheckAllEsce(cklShop);
            }// end block if 

        }

        private void ckSell_CheckedChanged(object sender, EventArgs e)
        {
            if (ckSell.Checked == true)
            {
                cklSell.Visible = true;
                CheckAll(cklSell);
            }
            else
            {
                cklSell.Visible = false;
                CheckAllEsce(cklSell);
            }// end block if 
        }

        private void ckMange_CheckedChanged(object sender, EventArgs e)
        {
            if (ckMange.Checked == true)
            {
                cklMange.Visible = true;
                CheckAll(cklMange);
            }
            else
            {
                cklMange.Visible = false;
                CheckAllEsce(cklMange);

            }// end block 
        }
        //全部選中方法，參數傳控件名稱name 屬性值 
        public void CheckAll(object chckList)
        {
            if (chckList.GetType().ToString() == "System.Windows.Forms.CheckedListBox")
            {
                CheckedListBox ckl = (CheckedListBox)chckList;
                for (int i = 0; i < ckl.Items.Count; i++)
                { ckl.SetItemCheckState(i, CheckState.Checked); }
            }// end block if 
        }//end mehtod block 
        //全部取選中方法，參數傳控件名稱name 屬性值 
        public void CheckAllEsce(object chckList)
        {
            if (chckList.GetType().ToString() == "System.Windows.Forms.CheckedListBox")
            {
                CheckedListBox ckl = (CheckedListBox)chckList;
                for (int i = 0; i < ckl.Items.Count; i++)
                { ckl.SetItemCheckState(i, CheckState.Unchecked); }
            }// end block if 
        }

        private void button1_Click(object sender, EventArgs e)
        {
            try
            {
                if (textBox1.Text == "")
                {
                    MessageBox.Show("用戶姓名不能為空", "提示");
                    return;
                }
                if (textBox2.Text == "")
                {
                    MessageBox.Show("用戶密碼", "提示");
                    return;
                }
                if (radMan.Checked == false && radWoman.Checked == false)
                {
                    MessageBox.Show("請選擇用戶性別", "提示");
                    return;
                }
                if (ckInfo.Checked == false && ckMange.Checked == false && ckSell.Checked == false && ckShop.Checked == false)
                {
                    MessageBox.Show("請任選一項用戶權限", "提示");
                    return;
                }// end 
                string strName = textBox1.Text.ToString();
                string strPassword = textBox2.Text;
                string strPhon = textBox3.Text;
                string srtEmail = textBox4.Text;
                string strAdress = textBox5.Text;
                string strSex;
                if (radWoman.Checked == true)
                {
                    strSex = "女";
                }
                else
                {
                    strSex = "男";
                }

                string strCkNabge = "庫存管理：" + "\n";
                string strCklsell = "銷售管理：" + "\n";
                string strCklShop = "進貨管理:" + "\n";

                string strCkl = "基本檔案:" + "\n";
                if (ckLinfo.Visible == true)
                {

                    for (int i = 0; i < ckLinfo.CheckedItems.Count; i++)
                    {

                        strCkl += ckLinfo.CheckedItems[i].ToString() + "\n";
                    }
                }// end block if 
                if (cklMange.Visible == true)
                {

                    for (int i = 0; i < cklMange.CheckedItems.Count; i++)
                    {
                        strCkNabge += cklMange.CheckedItems[i].ToString() + "\n";
                    }

                }// end block 
                if (cklSell.Visible == true)
                {

                    for (int i = 0; i < cklSell.CheckedItems.Count; i++)
                    {
                        strCklsell += cklSell.CheckedItems[i].ToString() + "\n";
                    }

                }// end block 
                if (cklShop.Visible == true)
                {
                    for (int i = 0; i < cklShop.CheckedItems.Count; i++)
                    {
                        strCklShop += cklShop.CheckedItems[i].ToString() + "\n";

                    }
                }// end blick if 
                MessageBox.Show("註冊信息如下：" + "\n" + "姓名:" + strName + "\n" + "密碼：" + strPassword + "\n" + "電話:" + strPhon + "\n" + "郵箱:" + srtEmail + "\n" + "地址:" + strAdress + "\n" + "性別：" + strSex + "\n" + "用戶權限如下：" + "\n" + strCkl + strCkNabge + strCklsell + strCklShop, "信息確認");
            }
            catch (Exception ee)
            {
                MessageBox.Show(ee.Message);
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            radWoman.Checked = false;
            radMan.Checked = false;
            //  VisbCheck(false);

        }

        private void button2_Click(object sender, EventArgs e)
        {
            textBox1.Text = "";
            textBox2.Text = "";
            textBox3.Text = "";
            textBox4.Text = "";
            textBox5.Text = "";
            radWoman.Checked = false;
            radMan.Checked = false;
            ckInfo.Checked = false;
            ckMange.Checked = false;
            ckSell.Checked = false;
            ckShop.Checked = false;
        }//end mehtod block 
        //public void VisbCheck(bool vib)
        //{
        //    ckInfo.Visible = vib;
        //    cklMange.Visible = vib;
        //    cklSell.Visible = vib;
        //    cklShop.Visible = vib;

        //}
    }
}