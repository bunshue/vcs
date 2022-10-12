using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace ConExpress.Calculator
{
    //Author: Alex Leo
    //Email: alexleo321@hotmail.com
    //Blog: http://www.cnblogs.com/conexpress/
    public partial class frmMain : Form
    {
        SyntaxAnalyse myAnalyse = new SyntaxAnalyse();

        public frmMain()
        {
            InitializeComponent();
        }

        private void frmMain_Load(object sender, EventArgs e)
        {
            this.ActiveControl = this.rtbInput;//設瞞胔入框為激活控件
            this.LoadOperateTokenTree();
        }


        #region 內部方法

        /// <summary>
        /// 加載操作記號樹視圖
        /// </summary>
        /// <remarks>Author:Alex Leo; Date:2008-6-12;</remarks>
        private void LoadOperateTokenTree()
        {
            this.trvOperateToken.BeginUpdate();
            this.trvOperateToken.Nodes.Clear();

            TreeNode nodRootKeyword = new TreeNode("關鍵字");
            this.LoadOperateTokenChildNode(nodRootKeyword, TokenKeywordFactory.KeywordDictionary, TokenKeywordFactory.KeyWordRemarkDictionary, OperateTokenTypeEnum.TokenKeyword);

            TreeNode nodRootSymbol = new TreeNode("運算符");
            this.LoadOperateTokenChildNode(nodRootSymbol, TokenSymbolFactory.SymbolDictionary, TokenSymbolFactory.SymbolRemarkDictionary, OperateTokenTypeEnum.TokenSymbol);

            this.trvOperateToken.Nodes.Add(nodRootKeyword);
            this.trvOperateToken.Nodes.Add(nodRootSymbol);

            this.trvOperateToken.EndUpdate();
        }

        /// <summary>
        /// 加載操作記號下級節點
        /// </summary>
        /// <param name="ParentNode">父節點</param>
        /// <param name="OperateTokenDictionary">操作記號字典</param>
        /// <param name="RemarkDictoinary">注釋字典</param>
        /// <param name="OperateTokenType">操作記號類型</param>
        /// <remarks>Author:Alex Leo; Date:2008-6-12;</remarks>
        private void LoadOperateTokenChildNode(TreeNode ParentNode, SortedDictionary<string, string> OperateTokenDictionary, SortedDictionary<string, string> RemarkDictoinary, OperateTokenTypeEnum OperateTokenType)
        {
            foreach (string OperateToken in OperateTokenDictionary.Keys)
            {
                TreeNode nodChild = new TreeNode(OperateToken);
                nodChild.ToolTipText = RemarkDictoinary[OperateToken];
                nodChild.Tag = OperateTokenType;
                ParentNode.Nodes.Add(nodChild);
            }
        }

        /// <summary>
        /// 加載語法樹
        /// </summary>
        /// <param name="TokenTop">頂級記號對象</param>
        /// <remarks>Author:Alex Leo</remarks>
        private void LoadSyntaxTree(TokenRecord TokenTop)
        {
            this.trvSyntaxTree.BeginUpdate();

            TreeNode nodRoot = new TreeNode(TokenTop.ToString());//新建根節點
            nodRoot.Tag = TokenTop;
            try
            {
                this.LoadSyntaxTreeSubNode(nodRoot, TokenTop);//遞歸加載下級節點
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
                nodRoot.Nodes.Add(new TreeNode("加載下級節點失敗"));
            }

            this.trvSyntaxTree.Nodes.Add(nodRoot);//添加根節點到TreeView控件
            this.trvSyntaxTree.EndUpdate();
        }

        /// <summary>
        /// 加載語法樹下級節點
        /// </summary>
        /// <param name="ParentNode">上級節點</param>
        /// <param name="ParentToken">上級記號</param>
        /// <remarks>Author:Alex Leo</remarks>
        private void LoadSyntaxTreeSubNode(TreeNode ParentNode, TokenRecord ParentToken)
        {
            //循環加載下級節點
            for (int intIndex = 0; intIndex < ParentToken.ChildList.Count; intIndex++)
            {
                TokenRecord TokenChild = ParentToken.ChildList[intIndex];
                TreeNode nodChild = new TreeNode(TokenChild.ToString());
                nodChild.Tag = TokenChild;
                ParentNode.Nodes.Add(nodChild);
                LoadSyntaxTreeSubNode(nodChild, TokenChild);//遞歸加載下級節點
            }
        }

        /// <summary>
        /// 插入字符串到胔入文本框
        /// </summary>
        /// <param name="InsertString">要插入的字符串</param>
        /// <remarks>Author:Alex Leo</remarks>
        private void InsertIntoInputRichTextBox(string InsertString)
        {
            int intSelectionStart = this.rtbInput.SelectionStart;
            string strBehindSelectionStart = this.rtbInput.Text.Substring(intSelectionStart);

            this.rtbInput.Text = this.rtbInput.Text.Substring(0, intSelectionStart);
            this.rtbInput.Text += InsertString;
            this.rtbInput.Text += strBehindSelectionStart;
        }

        #endregion 內部方法


        #region 控件操作

        /// <summary>
        /// 選擇樹節點
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void trvSyntaxTree_AfterSelect(object sender, TreeViewEventArgs e)
        {
            this.pgToken.SelectedObject = e.Node.Tag;//顯示選中節點的TokenRecord對象到PropertyGrid控件中
        }

        /// <summary>
        /// 胔入框鍵盤檢測，按F5時執行計算
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void rtbInput_KeyUp(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.F5)
            {
                this.btnExecute.PerformClick();
            }
        }

        /// <summary>
        /// 雙擊操作符樹視圖的節點，將選中節點的操作符插入胔入框
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void trvOperateToken_NodeMouseDoubleClick(object sender, TreeNodeMouseClickEventArgs e)
        {
            if (e.Node.Tag != null)
            {
                int intSelectionStart = this.rtbInput.SelectionStart;
                switch ((OperateTokenTypeEnum)e.Node.Tag)
                {
                    case OperateTokenTypeEnum.TokenKeyword:
                        this.InsertIntoInputRichTextBox(e.Node.Text + "()");
                        this.rtbInput.SelectionStart = intSelectionStart + e.Node.Text.Length + 1;
                        break;
                    case OperateTokenTypeEnum.TokenSymbol:
                        this.InsertIntoInputRichTextBox(e.Node.Text);
                        this.rtbInput.SelectionStart = intSelectionStart + e.Node.Text.Length;
                        break;
                    default:
                        break;
                }
                this.ActiveControl = this.rtbInput;//設瞞胔入框為激活控件
            }
        }

        /// <summary>
        /// 允許多行胔入複選框操作
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void chkAllowMultiLine_CheckedChanged(object sender, EventArgs e)
        {
            if (chkAllowMultiLine.Checked)
            {
                this.AcceptButton = null;
            }
            else
            {
                this.AcceptButton = this.btnExecute;
            }
        }

        /// <summary>
        /// 點擊“計算”按鈕
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void btnExecute_Click(object sender, EventArgs e)
        {
            SyntaxAnalyse.DicVariable.Clear();
            if (this.rtbInput.Text.Trim().Replace("\n", "").Length == 0)
            {
                this.rtbOutput.Text = "胔入的表達式不能為空，請重新胔入。";
            }
            else
            {
                string strSource;
                int intTotalIndex = 0;
                this.rtbOutput.Text = "";
                string[] strLines;
                this.trvSyntaxTree.Nodes.Clear();//清空語法樹

                if (this.rtbInput.SelectedText.Trim().Length == 0)//獲取選中的代碼，如果未選中，則執行全部
                {
                    strSource = this.rtbInput.Text;
                }
                else
                {
                    strSource = this.rtbInput.SelectedText;
                    intTotalIndex = this.rtbInput.SelectionStart;
                }

                if (this.chkAllowMultiLine.Checked)//判斷是按多行執行還是單行執行
                {
                    strLines = strSource.Split(new char[] { '\n' });//多行則用換行符分割成多行
                }
                else
                {
                    strLines = new string[] { strSource.Replace("\n", "") };//單行則移除換行符成一行
                }

                foreach (string Line in strLines)
                {
                    if (Line.Trim().Length != 0)//避免中間出現空行
                    {
                        try
                        {
                            TokenRecord TokenTop = myAnalyse.Analyse(Line);//計算表達式
                            this.rtbOutput.Text += TokenTop.GetValueString() + "\n";//顯示計算結果
                            this.LoadSyntaxTree(TokenTop);//加載語法樹到TreeView控件
                        }
                        catch (Exception ex)
                        {
                            this.rtbOutput.Text += "發生錯誤\n" + ex.Message + "\n";//顯示錯誤信息
                            if (ex is SyntaxException)//如果是語法錯誤，則選中錯誤的代碼
                            {
                                SyntaxException myException = (SyntaxException)ex;
                                this.ActiveControl = this.rtbInput;//設瞞胔入框為激活控件
                                this.rtbInput.Select(myException.Index + intTotalIndex, myException.Length);
                            }
                            return;
                        }//try
                    }//if
                    intTotalIndex += Line.Length + 1;
                }//foreach
            }//else
        }//btnExecute_Click

        /// <summary>
        /// 點擊“退出”按鈕
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void btnExit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        /// <summary>
        /// 點擊“關於”按鈕
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void btnAbout_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Author: Alex Leo\nEmail: alexleo321@hotmail.com\nBlog: http://www.cnblogs.com/conexpress/", "關於", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }

        #endregion 控件操作

        private void btnDraw_Click(object sender, EventArgs e)
        {
            frmDraw myDraw = new frmDraw();
            myDraw.Show();
        }

    }
}