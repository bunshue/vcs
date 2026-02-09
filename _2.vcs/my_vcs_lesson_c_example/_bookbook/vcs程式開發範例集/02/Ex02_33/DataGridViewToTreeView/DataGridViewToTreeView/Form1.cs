using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Data.SqlClient;

namespace DataGridViewToTreeView
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        //宣告本程序需要的變數
        public static string[,] recordInfo;

        //視窗加載時，顯示原有的數據
        private void Form1_Load(object sender, EventArgs e)
        {
            //#region 在DataGridView及TreeView中顯示數據
            string connString = "server=.;database=pubs;integrated security=sspi";
            SqlConnection conn = new SqlConnection(connString);
            conn.Open();
            string selectString = "select au_id as 使用者編號,au_lname as 使用者名,phone as 聯繫電話 from authors";
            SqlDataAdapter Adapter = new SqlDataAdapter(selectString, conn);
            DataSet dataset = new DataSet();
            Adapter.Fill(dataset, "UserInfo");
            dataGridView1.DataSource = dataset.Tables["UserInfo"].DefaultView;

            TreeNode treeNode = new TreeNode("使用者訊息", 0, 0);
            treeView1.Nodes.Add(treeNode);
            //#endregion

            //預設情況下追加節點
            追加節點ToolStripMenuItem.Checked = true;
        }

        //DataGridView的按下滑鼠游標事件
        private void dataGridView1_MouseDown(object sender, MouseEventArgs e)
        {
            if (dataGridView1.SelectedCells.Count != 0)
            {
                //定義一個二維數組，數組中的每一行代表DataGridView中的一條記錄
                recordInfo = new string[dataGridView1.Rows.Count, dataGridView1.Columns.Count];

                //當按下滑鼠游標左鍵時，首先取得選定行，記錄每一行對應的訊息
                for (int i = 0; i < dataGridView1.Rows.Count; i++)
                {
                    if (dataGridView1.Rows[i].Selected)
                    {
                        for (int j = 0; j < dataGridView1.Columns.Count; j++)
                        {
                            recordInfo[i, j] = dataGridView1.Rows[i].Cells[j].Value.ToString();
                        }
                    }
                }
            }
        }

        //當滑鼠游標進入TreeView控制元件時，觸發的操作
        private void treeView1_MouseEnter(object sender, EventArgs e)
        {
            if (追加節點ToolStripMenuItem.Checked == true)
            {
                //#region 程式碼區域
                if (recordInfo != null && recordInfo.Length != 0)
                {
                    //用雙重for循環搜尋數組recordInfo中的內容
                    for (int i = 0; i < recordInfo.GetLength(0); i++)
                    {
                        for (int j = 0; j < recordInfo.GetLength(1); j++)
                        {
                            //判斷數組中的值是否為空
                            if (recordInfo[i, j] != null)
                            {
                                if (j == 0)
                                {
                                    //向TreeView中加入節點
                                    TreeNode Node1 = new TreeNode(recordInfo[i, j].ToString());
                                    treeView1.SelectedNode.Nodes.Add(Node1);
                                    treeView1.SelectedNode = Node1;
                                }
                                else
                                {
                                    //新增子級節點下的子節點
                                    TreeNode Node2 = new TreeNode(recordInfo[i, j].ToString());
                                    treeView1.SelectedNode.Nodes.Add(Node2);
                                }
                            }

                        }
                        treeView1.SelectedNode = treeView1.Nodes[0];
                        treeView1.ExpandAll();
                    }
                    //清空recordInfo中的記錄
                    for (int m = 0; m < recordInfo.GetLength(0); m++)
                    {
                        for (int n = 0; n < recordInfo.GetLength(1); n++)
                        {
                            recordInfo[m, n] = null;
                        }
                    }
                }
                //#endregion
            }

            if (清空內容ToolStripMenuItem.Checked == true)
            {
                if (treeView1.SelectedNode.Nodes.Count != 0)
                {
                    treeView1.SelectedNode.Remove();
                    TreeNode treeNode = new TreeNode("使用者訊息", 0, 0);
                    treeView1.Nodes.Add(treeNode);
                    treeView1.SelectedNode = treeNode;
                    //#region 程式碼區域
                    if (recordInfo != null && recordInfo.Length != 0)
                    {
                        //用雙重for循環搜尋數組recordInfo中的內容
                        for (int i = 0; i < recordInfo.GetLength(0); i++)
                        {
                            for (int j = 0; j < recordInfo.GetLength(1); j++)
                            {
                                //判斷數組中的值是否為空
                                if (recordInfo[i, j] != null)
                                {
                                    if (j == 0)
                                    {
                                        //向TreeView中加入節點
                                        TreeNode Node1 = new TreeNode(recordInfo[i, j].ToString());
                                        treeView1.SelectedNode.Nodes.Add(Node1);
                                        treeView1.SelectedNode = Node1;
                                    }
                                    else
                                    {
                                        //新增子級節點下的子節點
                                        TreeNode Node2 = new TreeNode(recordInfo[i, j].ToString());
                                        treeView1.SelectedNode.Nodes.Add(Node2);
                                    }
                                }

                            }
                            treeView1.SelectedNode = treeView1.Nodes[0];
                            treeView1.ExpandAll();
                        }
                        //清空recordInfo中的記錄
                        for (int m = 0; m < recordInfo.GetLength(0); m++)
                        {
                            for (int n = 0; n < recordInfo.GetLength(1); n++)
                            {
                                recordInfo[m, n] = null;
                            }
                        }
                    }
                    //#endregion
                    追加節點ToolStripMenuItem.Checked = true;
                    清空內容ToolStripMenuItem.Checked = false;
                }
            }
        }

        //#region 預設項的設定
        private void 清空內容ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if (追加節點ToolStripMenuItem.Checked == true)
            {
                清空內容ToolStripMenuItem.Checked = true;
                追加節點ToolStripMenuItem.Checked = false;
            }
        }

        private void 追加節點ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if (清空內容ToolStripMenuItem.Checked == true)
            {
                追加節點ToolStripMenuItem.Checked = true;
                清空內容ToolStripMenuItem.Checked = false;
            }
        }
        //#endregion
    }
}
