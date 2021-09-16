using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Collections;

namespace xCh5_1_6_11
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            // 動態產生9位顧客的姓名
            string[] customerName = new string[] { 
                "張三峯", 
                "張無忌",
                "趙敏", 
                "郭靖", 
                "黃蓉", 
                "楊過", 
                "小龍女", 
                "喬峯",
                "虛竹"
            };

            // 建構ArrayList物件來儲存Customer物件
            ArrayList customerArray = new ArrayList();
            for (int i = 0; i < 9; i++)
            {
                customerArray.Add(new Customer("顧客："+customerName[i]));
            }

            // 利用亂數，隨機產生不同Customer物件所擁有的訂單數
            int seed = 0;
            foreach (Customer customer in customerArray)
            {
                // 顧客訂單數以1~10之間的亂數產生
                Random randObj = new Random(seed++*100);
                int upperLimit = randObj.Next(1, 10);
                
                for (int y = 1; y < upperLimit; y++)
                {
                    customer.CustomerOrders.Add(new Order("訂單#" + y.ToString()));
                }
            }

            // 暫不重繪TreeView，直至所有物件皆已建構
            treeView1.BeginUpdate();
            // 清除目前TreeView物的所有節點
            treeView1.Nodes.Clear();
            // 指定節點選取與非選取時所要使用的圖片 
            int selectedCustomerImageIndex =0;
            int unselectedCustomerImageIndex = 1;
            int selectedOrderImageIndex = 2;
            int unselectedOrderImageIndex = 3;

            // 將ArrayList中的Customer物件資料加入成為節點
            foreach (Customer customer in customerArray)
            {
                treeView1.Nodes.Add(new TreeNode(
                    customer.CustomerName, 
                    unselectedCustomerImageIndex, 
                    selectedCustomerImageIndex));
                // 為每一Customer節點加入其Order節點，
                // 並針對偶數的節點指定該節點被選取或取消選取時的圖像
                int i = 0;
                foreach (Order order in customer.CustomerOrders)
                {
                    i++;
                    if(i% 2 == 0)
                        treeView1.Nodes[customerArray.IndexOf(customer)].Nodes.Add(
                      new TreeNode(customer.CustomerName + "." + order.OrderID,                      
                          unselectedOrderImageIndex, selectedOrderImageIndex));
                    else
                        treeView1.Nodes[customerArray.IndexOf(customer)].Nodes.Add(
                      new TreeNode(customer.CustomerName + "." + order.OrderID));
                }
            }
            // 開始重繪TreeView物件
            treeView1.EndUpdate();

            // 設定TreeView屬性
            treeView1.CheckBoxes = true;
            treeView1.LabelEdit = true;
            treeView1.ShowNodeToolTips = true;
            treeView1.Nodes[0].ToolTipText = "非常重要的客戶";
            treeView1.Nodes[5].ToolTipText = "有呆帳風險 !!!";

            //建構ImageList物件
            ImageList myImageList = new ImageList();
            myImageList.ImageSize = new Size(32, 32);
            myImageList.Images.Add(Image.FromFile(@"c:\user_red32x32.png"));
            myImageList.Images.Add(Image.FromFile(@"c:\user32x32.png"));
            myImageList.Images.Add(Image.FromFile(@"c:\frai32x32.png"));
            myImageList.Images.Add(Image.FromFile(@"c:\leela32x32.png"));

            // 將ImageList物件設定TreeView的ImageList屬性
            treeView1.ImageList = myImageList;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            textBox2.Clear();
            IEnumerator myEnumerator = treeView1.Nodes.GetEnumerator();
            TreeNode x;
            while (myEnumerator.MoveNext())
            {
                object obj = myEnumerator.Current;
                x = (TreeNode)obj;
                AllCheckedNodes(x);
            }
        }
        // butto2的輔助功能
        private void AllCheckedNodes(TreeNode treeNode)
        {
            foreach (TreeNode node in treeNode.Nodes)
            {
                if (node.Checked == true)
                {
                    textBox2.AppendText(node.Text + '\n');
                }
                if (node.Nodes.Count > 0)
                {
                    this.AllCheckedNodes(node);
                }
            }
        }

        // treeView1的AftersSelect事件的處理程序
        private void treeView1_AfterSelect(object sender, TreeViewEventArgs e)
        {
            textBox1.Text = treeView1.SelectedNode.FullPath;
        }

        // treeView1的AfterCheck事件的處理程序
        private void treeView1_AfterCheck(object sender, TreeViewEventArgs e)
        {
            if (e.Action != TreeViewAction.Unknown)
            {
                if (e.Node.Nodes.Count > 0)
                {
                    this.AdjustAllChildNodes(e.Node, e.Node.Checked);
                }
            }
        }
        // treeView1的AfterCheck事件的輔助程式
        private void AdjustAllChildNodes(TreeNode treeNode, bool nodeChecked)
        {
            foreach (TreeNode node in treeNode.Nodes)
            {
                node.Checked = nodeChecked;
                if (node.Nodes.Count > 0)
                {
                    // 使用遞迴的方式處理子節點
                    this.AdjustAllChildNodes(node, nodeChecked);
                }
            }
        }
    }

    // 定義「顧客」類別
    public class Customer : System.Object
    {
        private string custName = "";
        protected ArrayList custOrders = new ArrayList();
        public Customer(string customername)
        {
            this.custName = customername;
        }
        public string CustomerName
        {
            get { return this.custName; }
            set { this.custName = value; }
        }
        public ArrayList CustomerOrders
        {
            get { return this.custOrders; }
        }
    }

    // 定義「訂單」類別
    public class Order : System.Object
    {
        private string ordID = "";
        public Order(string orderid)
        {
            this.ordID = orderid;
        }
        public string OrderID
        {
            get { return this.ordID; }
            set { this.ordID = value; }
        }
    }

 
}
