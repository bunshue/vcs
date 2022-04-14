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
            this.ActiveControl = this.rtbInput;//设置输入框为激活控件
            this.LoadOperateTokenTree();
        }


        #region 内部方法

        /// <summary>
        /// 加载操作记号树视图
        /// </summary>
        /// <remarks>Author:Alex Leo; Date:2008-6-12;</remarks>
        private void LoadOperateTokenTree()
        {
            this.trvOperateToken.BeginUpdate();
            this.trvOperateToken.Nodes.Clear();
            
            TreeNode nodRootKeyword = new TreeNode("关键字");
            this.LoadOperateTokenChildNode(nodRootKeyword, TokenKeywordFactory.KeywordDictionary,TokenKeywordFactory.KeyWordRemarkDictionary, OperateTokenTypeEnum.TokenKeyword);

            TreeNode nodRootSymbol = new TreeNode("运算符");
            this.LoadOperateTokenChildNode(nodRootSymbol, TokenSymbolFactory.SymbolDictionary, TokenSymbolFactory.SymbolRemarkDictionary, OperateTokenTypeEnum.TokenSymbol);

            this.trvOperateToken.Nodes.Add(nodRootKeyword);
            this.trvOperateToken.Nodes.Add(nodRootSymbol);

            this.trvOperateToken.EndUpdate();
        }

        /// <summary>
        /// 加载操作记号下级节点
        /// </summary>
        /// <param name="ParentNode">父节点</param>
        /// <param name="OperateTokenDictionary">操作记号字典</param>
        /// <param name="RemarkDictoinary">注释字典</param>
        /// <param name="OperateTokenType">操作记号类型</param>
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
        /// 加载语法树
        /// </summary>
        /// <param name="TokenTop">顶级记号对象</param>
        /// <remarks>Author:Alex Leo</remarks>
        private void LoadSyntaxTree(TokenRecord TokenTop)
        {
            this.trvSyntaxTree.BeginUpdate();

            TreeNode nodRoot = new TreeNode(TokenTop.ToString());//新建根节点
            nodRoot.Tag = TokenTop;
            try
            {
                this.LoadSyntaxTreeSubNode(nodRoot, TokenTop);//递归加载下级节点
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
                nodRoot.Nodes.Add(new TreeNode("加载下级节点失败"));
            }

            this.trvSyntaxTree.Nodes.Add(nodRoot);//添加根节点到TreeView控件
            this.trvSyntaxTree.EndUpdate();
        }

        /// <summary>
        /// 加载语法树下级节点
        /// </summary>
        /// <param name="ParentNode">上级节点</param>
        /// <param name="ParentToken">上级记号</param>
        /// <remarks>Author:Alex Leo</remarks>
        private void LoadSyntaxTreeSubNode(TreeNode ParentNode, TokenRecord ParentToken)
        {
            //循环加载下级节点
            for (int intIndex = 0; intIndex < ParentToken.ChildList.Count; intIndex++)
            {
                TokenRecord TokenChild = ParentToken.ChildList[intIndex];
                TreeNode nodChild = new TreeNode(TokenChild.ToString());
                nodChild.Tag = TokenChild;
                ParentNode.Nodes.Add(nodChild);
                LoadSyntaxTreeSubNode(nodChild, TokenChild);//递归加载下级节点
            }
        }

        /// <summary>
        /// 插入字符串到输入文本框
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

        #endregion 内部方法


        #region 控件操作

        /// <summary>
        /// 选择树节点
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void trvSyntaxTree_AfterSelect(object sender, TreeViewEventArgs e)
        {
            this.pgToken.SelectedObject = e.Node.Tag;//显示选中节点的TokenRecord对象到PropertyGrid控件中
        }

        /// <summary>
        /// 输入框键盘检测，按F5时执行计算
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
        /// 双击操作符树视图的节点，将选中节点的操作符插入输入框
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
                this.ActiveControl = this.rtbInput;//设置输入框为激活控件
            }
        }

        /// <summary>
        /// 允许多行输入复选框操作
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
        /// 点击“计算”按钮
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void btnExecute_Click(object sender, EventArgs e)
        {
            SyntaxAnalyse.DicVariable.Clear();
            if (this.rtbInput.Text.Trim().Replace("\n", "").Length == 0)
            {
                this.rtbOutput.Text = "输入的表达式不能为空，请重新输入。";
            }
            else
            {
                string strSource;
                int intTotalIndex = 0;
                this.rtbOutput.Text = "";
                string[] strLines;
                this.trvSyntaxTree.Nodes.Clear();//清空语法树

                if (this.rtbInput.SelectedText.Trim().Length == 0)//获取选中的代码，如果未选中，则执行全部
                {
                    strSource = this.rtbInput.Text;
                }
                else
                {
                    strSource = this.rtbInput.SelectedText;
                    intTotalIndex = this.rtbInput.SelectionStart;
                }

                if (this.chkAllowMultiLine.Checked)//判断是按多行执行还是单行执行
                {
                    strLines = strSource.Split(new char[] { '\n' });//多行则用换行符分割成多行
                }
                else
                {
                    strLines = new string[] { strSource.Replace("\n", "") };//单行则移除换行符成一行
                }

                foreach (string Line in strLines)
                {
                    if (Line.Trim().Length != 0)//避免中间出现空行
                    {
                        try
                        {
                            TokenRecord TokenTop = myAnalyse.Analyse(Line);//计算表达式
                            this.rtbOutput.Text += TokenTop.GetValueString() + "\n";//显示计算结果
                            this.LoadSyntaxTree(TokenTop);//加载语法树到TreeView控件
                        }
                        catch (Exception ex)
                        {
                            this.rtbOutput.Text += "发生错误\n" + ex.Message + "\n";//显示错误信息
                            if (ex is SyntaxException)//如果是语法错误，则选中错误的代码
                            {
                                SyntaxException myException = (SyntaxException)ex;
                                this.ActiveControl = this.rtbInput;//设置输入框为激活控件
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
        /// 点击“退出”按钮
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void btnExit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        /// <summary>
        /// 点击“关于”按钮
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void btnAbout_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Author: Alex Leo\nEmail: alexleo321@hotmail.com\nBlog: http://www.cnblogs.com/conexpress/", "关于", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }

        #endregion 控件操作

        private void btnDraw_Click(object sender, EventArgs e)
        {
            frmDraw myDraw = new frmDraw();
            myDraw.Show();
        }

    }
}