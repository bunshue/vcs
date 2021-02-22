using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_programming
{
    public partial class ListBoxDemo : Form
    {
        public ListBoxDemo()
        {
            InitializeComponent();
        }

        string[]  Types = {"電腦商品", "書籍類"};
        string[][] Items = { new string[] {"桌上型電腦","筆記型電腦","印表機","報表紙","隨身碟","DVD光碟"},
                            new string[] {"C#程式設計","計算機概論","微積分","資料結構","系統分析"}
                          };

        private void ListBoxDemo_Load(object sender, EventArgs e)
        {

            /*
             TypeList.DataSource = Types; //會引發TypeList_SelectedIndexChanged事件
             MessageBox.Show(TypeList.Items[0].ToString(), "");
             MessageBox.Show(TypeList.Items[1].ToString(), "");
             */

            TypeList.Items.Add("電腦商品");
            TypeList.Items.Add("書籍類");
            TypeList.SelectedIndex = 0; //會引發TypeList_SelectedIndexChanged事件

            TypeComboBox.Items.Add("電腦商品");
            TypeComboBox.Items.Add("書籍類");
            TypeComboBox.SelectedIndex = 0; //會引發TypeComboBox_SelectedIndexChanged事件

            output();
        
        }

        private void TypeList_SelectedIndexChanged(object sender, EventArgs e)
        {
           
            ItemsList.Items.Clear();

            int idx = TypeList.SelectedIndex;

            foreach(string s in Items[idx])
                ItemsList.Items.Add(s);
           
            /*for (int i = 0; i < Items[idx].Length; i++)
                ItemsList.Items.Add(Items[idx][i]);*/
            

        }

        private void output()
        {
            int ctr = BuyList.Items.Count;
            lblOutout.Text = txtName.Text + "你好!你共買了" + ctr +"項商品";
        }

        private void btnToRight_Click(object sender, EventArgs e)
        {
            int count = ItemsList.SelectedIndices.Count;
            //int count = ItemsList.SelectedItems.Count;

            // 使用SelectedItem
            /*for (int i = 0; i < count; i++)
            {
                string s = ItemsList.SelectedItem.ToString();
                BuyList.Items.Add(s);
                ItemsList.Items.Remove(s);
            }*/
            
            // 使用SelectedItems[i] (注意：索引必須遞減)
            for (int i = count-1 ; i >= 0; i--)            
            {
                string s = ItemsList.SelectedItems[i].ToString();
                BuyList.Items.Add(s);
                ItemsList.Items.Remove(s);
            }
            
            output();
        }

        private void btnToLeft_Click(object sender, EventArgs e)
        {
            int count = BuyList.SelectedIndices.Count;

            /*for (int i = 0; i < count; i++)
            {
                string s = BuyList.SelectedItem.ToString();
                ItemsList.Items.Add(s);
                BuyList.Items.Remove(s);
            }*/

            for (int i = count - 1; i >= 0; i--)
            {
                string s = BuyList.SelectedItems[i].ToString();
                ItemsList.Items.Add(s);
                BuyList.Items.Remove(s);
            }

            output();
        }

        private void TypeComboBox_SelectedIndexChanged(object sender, EventArgs e)
        {
            ItemsList.Items.Clear();

            int idx = TypeComboBox.SelectedIndex;

            foreach (string s in Items[idx])
                ItemsList.Items.Add(s);
        }
    }
}
