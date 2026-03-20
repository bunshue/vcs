using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//樹視圖

namespace vcs_TreeView4
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            treeView1.ShowLines = true;
            treeView1.ImageList = imageList1;

            TreeNode newNode1 = treeView1.Nodes.Add("A", "商品信息", 1, 2);//一級節點

            int sn = 1;
            string name = "被子";
            int amount = 212;
            int price = 432;

            TreeNode newNode12 = new TreeNode("商品編號" + sn.ToString(), 3, 4);// 二級節點
            // 3表示沒有單擊節點時顯示的圖標索引值，
            newNode12.Nodes.Add("A", "商品名稱：" + name, 5, 6);
            newNode12.Nodes.Add("A", "商品數量：" + amount.ToString(), 7, 8);
            newNode12.Nodes.Add("A", "商品價格：" + price.ToString(), 9, 10);
            newNode1.Nodes.Add(newNode12);

            sn = 2;
            name = "肥皂";
            amount = 34;
            price = 3;
            newNode12 = new TreeNode("商品編號" + sn.ToString(), 3, 4);// 二級節點
            // 3表示沒有單擊節點時顯示的圖標索引值，
            newNode12.Nodes.Add("A", "商品名稱：" + name, 5, 6);
            newNode12.Nodes.Add("A", "商品數量：" + amount.ToString(), 7, 8);
            newNode12.Nodes.Add("A", "商品價格：" + price.ToString(), 9, 10);
            newNode1.Nodes.Add(newNode12);

            sn = 3;
            name = "毛巾";
            amount = 45;
            price = 4;
            newNode12 = new TreeNode("商品編號" + sn.ToString(), 3, 4);// 二級節點
            // 3表示沒有單擊節點時顯示的圖標索引值，
            newNode12.Nodes.Add("A", "商品名稱：" + name, 5, 6);
            newNode12.Nodes.Add("A", "商品數量：" + amount.ToString(), 7, 8);
            newNode12.Nodes.Add("A", "商品價格：" + price.ToString(), 9, 10);
            newNode1.Nodes.Add(newNode12);

            sn = 4;
            name = "書籍";
            amount = 321;
            price = 32;
            newNode12 = new TreeNode("商品編號" + sn.ToString(), 3, 4);// 二級節點
            // 3表示沒有單擊節點時顯示的圖標索引值，
            newNode12.Nodes.Add("A", "商品名稱：" + name, 5, 6);
            newNode12.Nodes.Add("A", "商品數量：" + amount.ToString(), 7, 8);
            newNode12.Nodes.Add("A", "商品價格：" + price.ToString(), 9, 10);
            newNode1.Nodes.Add(newNode12);

            sn = 5;
            name = "牙膏";
            amount = 32;
            price = 5;
            newNode12 = new TreeNode("商品編號" + sn.ToString(), 3, 4);// 二級節點
            // 3表示沒有單擊節點時顯示的圖標索引值，
            newNode12.Nodes.Add("A", "商品名稱：" + name, 5, 6);
            newNode12.Nodes.Add("A", "商品數量：" + amount.ToString(), 7, 8);
            newNode12.Nodes.Add("A", "商品價格：" + price.ToString(), 9, 10);
            newNode1.Nodes.Add(newNode12);

            sn = 6;
            name = "牙刷";
            amount = 432;
            price = 4;
            newNode12 = new TreeNode("商品編號" + sn.ToString(), 3, 4);// 二級節點
            // 3表示沒有單擊節點時顯示的圖標索引值，
            newNode12.Nodes.Add("A", "商品名稱：" + name, 5, 6);
            newNode12.Nodes.Add("A", "商品數量：" + amount.ToString(), 7, 8);
            newNode12.Nodes.Add("A", "商品價格：" + price.ToString(), 9, 10);
            newNode1.Nodes.Add(newNode12);

            sn = 7;
            name = "衣服";
            amount = 123;
            price = 38;
            newNode12 = new TreeNode("商品編號" + sn.ToString(), 3, 4);// 二級節點
            // 3表示沒有單擊節點時顯示的圖標索引值，
            newNode12.Nodes.Add("A", "商品名稱：" + name, 5, 6);
            newNode12.Nodes.Add("A", "商品數量：" + amount.ToString(), 7, 8);
            newNode12.Nodes.Add("A", "商品價格：" + price.ToString(), 9, 10);
            newNode1.Nodes.Add(newNode12);

            treeView1.ExpandAll();
        }
    }
}
