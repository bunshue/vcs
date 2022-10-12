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
            this.ActiveControl = this.rtbInput;//�]�f�I�J�ج��E������
            this.LoadOperateTokenTree();
        }


        #region ������k

        /// <summary>
        /// �[���ާ@�O�������
        /// </summary>
        /// <remarks>Author:Alex Leo; Date:2008-6-12;</remarks>
        private void LoadOperateTokenTree()
        {
            this.trvOperateToken.BeginUpdate();
            this.trvOperateToken.Nodes.Clear();

            TreeNode nodRootKeyword = new TreeNode("����r");
            this.LoadOperateTokenChildNode(nodRootKeyword, TokenKeywordFactory.KeywordDictionary, TokenKeywordFactory.KeyWordRemarkDictionary, OperateTokenTypeEnum.TokenKeyword);

            TreeNode nodRootSymbol = new TreeNode("�B���");
            this.LoadOperateTokenChildNode(nodRootSymbol, TokenSymbolFactory.SymbolDictionary, TokenSymbolFactory.SymbolRemarkDictionary, OperateTokenTypeEnum.TokenSymbol);

            this.trvOperateToken.Nodes.Add(nodRootKeyword);
            this.trvOperateToken.Nodes.Add(nodRootSymbol);

            this.trvOperateToken.EndUpdate();
        }

        /// <summary>
        /// �[���ާ@�O���U�Ÿ`�I
        /// </summary>
        /// <param name="ParentNode">���`�I</param>
        /// <param name="OperateTokenDictionary">�ާ@�O���r��</param>
        /// <param name="RemarkDictoinary">�`���r��</param>
        /// <param name="OperateTokenType">�ާ@�O������</param>
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
        /// �[���y�k��
        /// </summary>
        /// <param name="TokenTop">���ŰO����H</param>
        /// <remarks>Author:Alex Leo</remarks>
        private void LoadSyntaxTree(TokenRecord TokenTop)
        {
            this.trvSyntaxTree.BeginUpdate();

            TreeNode nodRoot = new TreeNode(TokenTop.ToString());//�s�خڸ`�I
            nodRoot.Tag = TokenTop;
            try
            {
                this.LoadSyntaxTreeSubNode(nodRoot, TokenTop);//���k�[���U�Ÿ`�I
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
                nodRoot.Nodes.Add(new TreeNode("�[���U�Ÿ`�I����"));
            }

            this.trvSyntaxTree.Nodes.Add(nodRoot);//�K�[�ڸ`�I��TreeView����
            this.trvSyntaxTree.EndUpdate();
        }

        /// <summary>
        /// �[���y�k��U�Ÿ`�I
        /// </summary>
        /// <param name="ParentNode">�W�Ÿ`�I</param>
        /// <param name="ParentToken">�W�ŰO��</param>
        /// <remarks>Author:Alex Leo</remarks>
        private void LoadSyntaxTreeSubNode(TreeNode ParentNode, TokenRecord ParentToken)
        {
            //�`���[���U�Ÿ`�I
            for (int intIndex = 0; intIndex < ParentToken.ChildList.Count; intIndex++)
            {
                TokenRecord TokenChild = ParentToken.ChildList[intIndex];
                TreeNode nodChild = new TreeNode(TokenChild.ToString());
                nodChild.Tag = TokenChild;
                ParentNode.Nodes.Add(nodChild);
                LoadSyntaxTreeSubNode(nodChild, TokenChild);//���k�[���U�Ÿ`�I
            }
        }

        /// <summary>
        /// ���J�r�Ŧ���I�J�奻��
        /// </summary>
        /// <param name="InsertString">�n���J���r�Ŧ�</param>
        /// <remarks>Author:Alex Leo</remarks>
        private void InsertIntoInputRichTextBox(string InsertString)
        {
            int intSelectionStart = this.rtbInput.SelectionStart;
            string strBehindSelectionStart = this.rtbInput.Text.Substring(intSelectionStart);

            this.rtbInput.Text = this.rtbInput.Text.Substring(0, intSelectionStart);
            this.rtbInput.Text += InsertString;
            this.rtbInput.Text += strBehindSelectionStart;
        }

        #endregion ������k


        #region ����ާ@

        /// <summary>
        /// ��ܾ�`�I
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void trvSyntaxTree_AfterSelect(object sender, TreeViewEventArgs e)
        {
            this.pgToken.SelectedObject = e.Node.Tag;//��ܿ襤�`�I��TokenRecord��H��PropertyGrid����
        }

        /// <summary>
        /// �I�J����L�˴��A��F5�ɰ���p��
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
        /// �����ާ@�ž���Ϫ��`�I�A�N�襤�`�I���ާ@�Ŵ��J�I�J��
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
                this.ActiveControl = this.rtbInput;//�]�f�I�J�ج��E������
            }
        }

        /// <summary>
        /// ���\�h���I�J�ƿ�ؾާ@
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
        /// �I�����p�⡨���s
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void btnExecute_Click(object sender, EventArgs e)
        {
            SyntaxAnalyse.DicVariable.Clear();
            if (this.rtbInput.Text.Trim().Replace("\n", "").Length == 0)
            {
                this.rtbOutput.Text = "�I�J����F�����ର�šA�Э��s�I�J�C";
            }
            else
            {
                string strSource;
                int intTotalIndex = 0;
                this.rtbOutput.Text = "";
                string[] strLines;
                this.trvSyntaxTree.Nodes.Clear();//�M�Ży�k��

                if (this.rtbInput.SelectedText.Trim().Length == 0)//����襤���N�X�A�p�G���襤�A�h�������
                {
                    strSource = this.rtbInput.Text;
                }
                else
                {
                    strSource = this.rtbInput.SelectedText;
                    intTotalIndex = this.rtbInput.SelectionStart;
                }

                if (this.chkAllowMultiLine.Checked)//�P�_�O���h������٬O������
                {
                    strLines = strSource.Split(new char[] { '\n' });//�h��h�δ���Ť��Φ��h��
                }
                else
                {
                    strLines = new string[] { strSource.Replace("\n", "") };//���h��������Ŧ��@��
                }

                foreach (string Line in strLines)
                {
                    if (Line.Trim().Length != 0)//�קK�����X�{�Ŧ�
                    {
                        try
                        {
                            TokenRecord TokenTop = myAnalyse.Analyse(Line);//�p���F��
                            this.rtbOutput.Text += TokenTop.GetValueString() + "\n";//��ܭp�⵲�G
                            this.LoadSyntaxTree(TokenTop);//�[���y�k���TreeView����
                        }
                        catch (Exception ex)
                        {
                            this.rtbOutput.Text += "�o�Ϳ��~\n" + ex.Message + "\n";//��ܿ��~�H��
                            if (ex is SyntaxException)//�p�G�O�y�k���~�A�h�襤���~���N�X
                            {
                                SyntaxException myException = (SyntaxException)ex;
                                this.ActiveControl = this.rtbInput;//�]�f�I�J�ج��E������
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
        /// �I�����h�X�����s
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void btnExit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        /// <summary>
        /// �I�������󡨫��s
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void btnAbout_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Author: Alex Leo\nEmail: alexleo321@hotmail.com\nBlog: http://www.cnblogs.com/conexpress/", "����", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }

        #endregion ����ާ@

        private void btnDraw_Click(object sender, EventArgs e)
        {
            frmDraw myDraw = new frmDraw();
            myDraw.Show();
        }

    }
}