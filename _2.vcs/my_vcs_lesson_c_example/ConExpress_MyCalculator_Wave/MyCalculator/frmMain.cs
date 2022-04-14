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
            this.ActiveControl = this.rtbInput;//���������Ϊ����ؼ�
            this.LoadOperateTokenTree();
        }


        #region �ڲ�����

        /// <summary>
        /// ���ز����Ǻ�����ͼ
        /// </summary>
        /// <remarks>Author:Alex Leo; Date:2008-6-12;</remarks>
        private void LoadOperateTokenTree()
        {
            this.trvOperateToken.BeginUpdate();
            this.trvOperateToken.Nodes.Clear();
            
            TreeNode nodRootKeyword = new TreeNode("�ؼ���");
            this.LoadOperateTokenChildNode(nodRootKeyword, TokenKeywordFactory.KeywordDictionary,TokenKeywordFactory.KeyWordRemarkDictionary, OperateTokenTypeEnum.TokenKeyword);

            TreeNode nodRootSymbol = new TreeNode("�����");
            this.LoadOperateTokenChildNode(nodRootSymbol, TokenSymbolFactory.SymbolDictionary, TokenSymbolFactory.SymbolRemarkDictionary, OperateTokenTypeEnum.TokenSymbol);

            this.trvOperateToken.Nodes.Add(nodRootKeyword);
            this.trvOperateToken.Nodes.Add(nodRootSymbol);

            this.trvOperateToken.EndUpdate();
        }

        /// <summary>
        /// ���ز����Ǻ��¼��ڵ�
        /// </summary>
        /// <param name="ParentNode">���ڵ�</param>
        /// <param name="OperateTokenDictionary">�����Ǻ��ֵ�</param>
        /// <param name="RemarkDictoinary">ע���ֵ�</param>
        /// <param name="OperateTokenType">�����Ǻ�����</param>
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
        /// �����﷨��
        /// </summary>
        /// <param name="TokenTop">�����ǺŶ���</param>
        /// <remarks>Author:Alex Leo</remarks>
        private void LoadSyntaxTree(TokenRecord TokenTop)
        {
            this.trvSyntaxTree.BeginUpdate();

            TreeNode nodRoot = new TreeNode(TokenTop.ToString());//�½����ڵ�
            nodRoot.Tag = TokenTop;
            try
            {
                this.LoadSyntaxTreeSubNode(nodRoot, TokenTop);//�ݹ�����¼��ڵ�
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
                nodRoot.Nodes.Add(new TreeNode("�����¼��ڵ�ʧ��"));
            }

            this.trvSyntaxTree.Nodes.Add(nodRoot);//��Ӹ��ڵ㵽TreeView�ؼ�
            this.trvSyntaxTree.EndUpdate();
        }

        /// <summary>
        /// �����﷨���¼��ڵ�
        /// </summary>
        /// <param name="ParentNode">�ϼ��ڵ�</param>
        /// <param name="ParentToken">�ϼ��Ǻ�</param>
        /// <remarks>Author:Alex Leo</remarks>
        private void LoadSyntaxTreeSubNode(TreeNode ParentNode, TokenRecord ParentToken)
        {
            //ѭ�������¼��ڵ�
            for (int intIndex = 0; intIndex < ParentToken.ChildList.Count; intIndex++)
            {
                TokenRecord TokenChild = ParentToken.ChildList[intIndex];
                TreeNode nodChild = new TreeNode(TokenChild.ToString());
                nodChild.Tag = TokenChild;
                ParentNode.Nodes.Add(nodChild);
                LoadSyntaxTreeSubNode(nodChild, TokenChild);//�ݹ�����¼��ڵ�
            }
        }

        /// <summary>
        /// �����ַ����������ı���
        /// </summary>
        /// <param name="InsertString">Ҫ������ַ���</param>
        /// <remarks>Author:Alex Leo</remarks>
        private void InsertIntoInputRichTextBox(string InsertString)
        {
            int intSelectionStart = this.rtbInput.SelectionStart;
            string strBehindSelectionStart = this.rtbInput.Text.Substring(intSelectionStart);

            this.rtbInput.Text = this.rtbInput.Text.Substring(0, intSelectionStart);
            this.rtbInput.Text += InsertString;
            this.rtbInput.Text += strBehindSelectionStart;
        }

        #endregion �ڲ�����


        #region �ؼ�����

        /// <summary>
        /// ѡ�����ڵ�
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void trvSyntaxTree_AfterSelect(object sender, TreeViewEventArgs e)
        {
            this.pgToken.SelectedObject = e.Node.Tag;//��ʾѡ�нڵ��TokenRecord����PropertyGrid�ؼ���
        }

        /// <summary>
        /// �������̼�⣬��F5ʱִ�м���
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
        /// ˫������������ͼ�Ľڵ㣬��ѡ�нڵ�Ĳ��������������
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
                this.ActiveControl = this.rtbInput;//���������Ϊ����ؼ�
            }
        }

        /// <summary>
        /// ����������븴ѡ�����
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
        /// ��������㡱��ť
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void btnExecute_Click(object sender, EventArgs e)
        {
            SyntaxAnalyse.DicVariable.Clear();
            if (this.rtbInput.Text.Trim().Replace("\n", "").Length == 0)
            {
                this.rtbOutput.Text = "����ı��ʽ����Ϊ�գ����������롣";
            }
            else
            {
                string strSource;
                int intTotalIndex = 0;
                this.rtbOutput.Text = "";
                string[] strLines;
                this.trvSyntaxTree.Nodes.Clear();//����﷨��

                if (this.rtbInput.SelectedText.Trim().Length == 0)//��ȡѡ�еĴ��룬���δѡ�У���ִ��ȫ��
                {
                    strSource = this.rtbInput.Text;
                }
                else
                {
                    strSource = this.rtbInput.SelectedText;
                    intTotalIndex = this.rtbInput.SelectionStart;
                }

                if (this.chkAllowMultiLine.Checked)//�ж��ǰ�����ִ�л��ǵ���ִ��
                {
                    strLines = strSource.Split(new char[] { '\n' });//�������û��з��ָ�ɶ���
                }
                else
                {
                    strLines = new string[] { strSource.Replace("\n", "") };//�������Ƴ����з���һ��
                }

                foreach (string Line in strLines)
                {
                    if (Line.Trim().Length != 0)//�����м���ֿ���
                    {
                        try
                        {
                            TokenRecord TokenTop = myAnalyse.Analyse(Line);//������ʽ
                            this.rtbOutput.Text += TokenTop.GetValueString() + "\n";//��ʾ������
                            this.LoadSyntaxTree(TokenTop);//�����﷨����TreeView�ؼ�
                        }
                        catch (Exception ex)
                        {
                            this.rtbOutput.Text += "��������\n" + ex.Message + "\n";//��ʾ������Ϣ
                            if (ex is SyntaxException)//������﷨������ѡ�д���Ĵ���
                            {
                                SyntaxException myException = (SyntaxException)ex;
                                this.ActiveControl = this.rtbInput;//���������Ϊ����ؼ�
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
        /// ������˳�����ť
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void btnExit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        /// <summary>
        /// ��������ڡ���ť
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void btnAbout_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Author: Alex Leo\nEmail: alexleo321@hotmail.com\nBlog: http://www.cnblogs.com/conexpress/", "����", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }

        #endregion �ؼ�����

        private void btnDraw_Click(object sender, EventArgs e)
        {
            frmDraw myDraw = new frmDraw();
            myDraw.Show();
        }

    }
}