namespace ConExpress.Calculator
{
    partial class frmMain
    {
        /// <summary>
        /// 必需的设计器变量。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清理所有正在使用的资源。
        /// </summary>
        /// <param name="disposing">如果应释放托管资源，为 true；否则为 false。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows 窗体设计器生成的代码

        /// <summary>
        /// 设计器支持所需的方法 - 不要
        /// 使用代码编辑器修改此方法的内容。
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(frmMain));
            this.rtbInput = new System.Windows.Forms.RichTextBox();
            this.tabControl1 = new System.Windows.Forms.TabControl();
            this.tabPage1 = new System.Windows.Forms.TabPage();
            this.splitContainer3 = new System.Windows.Forms.SplitContainer();
            this.groupBox5 = new System.Windows.Forms.GroupBox();
            this.trvOperateToken = new System.Windows.Forms.TreeView();
            this.splitContainer1 = new System.Windows.Forms.SplitContainer();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.rtbOutput = new System.Windows.Forms.RichTextBox();
            this.tabPage2 = new System.Windows.Forms.TabPage();
            this.splitContainer2 = new System.Windows.Forms.SplitContainer();
            this.groupBox3 = new System.Windows.Forms.GroupBox();
            this.trvSyntaxTree = new System.Windows.Forms.TreeView();
            this.groupBox4 = new System.Windows.Forms.GroupBox();
            this.pgToken = new System.Windows.Forms.PropertyGrid();
            this.btnExecute = new System.Windows.Forms.Button();
            this.btnExit = new System.Windows.Forms.Button();
            this.chkAllowMultiLine = new System.Windows.Forms.CheckBox();
            this.toolTip1 = new System.Windows.Forms.ToolTip(this.components);
            this.btnAbout = new System.Windows.Forms.Button();
            this.btnDraw = new System.Windows.Forms.Button();
            this.tabControl1.SuspendLayout();
            this.tabPage1.SuspendLayout();
            this.splitContainer3.Panel1.SuspendLayout();
            this.splitContainer3.Panel2.SuspendLayout();
            this.splitContainer3.SuspendLayout();
            this.groupBox5.SuspendLayout();
            this.splitContainer1.Panel1.SuspendLayout();
            this.splitContainer1.Panel2.SuspendLayout();
            this.splitContainer1.SuspendLayout();
            this.groupBox1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.tabPage2.SuspendLayout();
            this.splitContainer2.Panel1.SuspendLayout();
            this.splitContainer2.Panel2.SuspendLayout();
            this.splitContainer2.SuspendLayout();
            this.groupBox3.SuspendLayout();
            this.groupBox4.SuspendLayout();
            this.SuspendLayout();
            // 
            // rtbInput
            // 
            this.rtbInput.Dock = System.Windows.Forms.DockStyle.Fill;
            this.rtbInput.HideSelection = false;
            this.rtbInput.ImeMode = System.Windows.Forms.ImeMode.Disable;
            this.rtbInput.Location = new System.Drawing.Point(3, 17);
            this.rtbInput.Name = "rtbInput";
            this.rtbInput.Size = new System.Drawing.Size(346, 128);
            this.rtbInput.TabIndex = 0;
            this.rtbInput.Text = "";
            this.toolTip1.SetToolTip(this.rtbInput, "可输入多行进行计算,也可选择部分表达式计算\r\n未选择时计算输入的全部表达式");
            this.rtbInput.KeyUp += new System.Windows.Forms.KeyEventHandler(this.rtbInput_KeyUp);
            // 
            // tabControl1
            // 
            this.tabControl1.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.tabControl1.Controls.Add(this.tabPage1);
            this.tabControl1.Controls.Add(this.tabPage2);
            this.tabControl1.Location = new System.Drawing.Point(12, 12);
            this.tabControl1.Name = "tabControl1";
            this.tabControl1.SelectedIndex = 0;
            this.tabControl1.Size = new System.Drawing.Size(482, 328);
            this.tabControl1.TabIndex = 0;
            // 
            // tabPage1
            // 
            this.tabPage1.Controls.Add(this.splitContainer3);
            this.tabPage1.Location = new System.Drawing.Point(4, 21);
            this.tabPage1.Name = "tabPage1";
            this.tabPage1.Padding = new System.Windows.Forms.Padding(3);
            this.tabPage1.Size = new System.Drawing.Size(474, 303);
            this.tabPage1.TabIndex = 0;
            this.tabPage1.Text = "计算表达式";
            this.toolTip1.SetToolTip(this.tabPage1, "输入表达式和查看计算结果");
            this.tabPage1.UseVisualStyleBackColor = true;
            // 
            // splitContainer3
            // 
            this.splitContainer3.Dock = System.Windows.Forms.DockStyle.Fill;
            this.splitContainer3.Location = new System.Drawing.Point(3, 3);
            this.splitContainer3.Name = "splitContainer3";
            // 
            // splitContainer3.Panel1
            // 
            this.splitContainer3.Panel1.Controls.Add(this.groupBox5);
            // 
            // splitContainer3.Panel2
            // 
            this.splitContainer3.Panel2.Controls.Add(this.splitContainer1);
            this.splitContainer3.Size = new System.Drawing.Size(468, 297);
            this.splitContainer3.SplitterDistance = 112;
            this.splitContainer3.TabIndex = 4;
            // 
            // groupBox5
            // 
            this.groupBox5.Controls.Add(this.trvOperateToken);
            this.groupBox5.Dock = System.Windows.Forms.DockStyle.Fill;
            this.groupBox5.Location = new System.Drawing.Point(0, 0);
            this.groupBox5.Name = "groupBox5";
            this.groupBox5.Size = new System.Drawing.Size(112, 297);
            this.groupBox5.TabIndex = 0;
            this.groupBox5.TabStop = false;
            this.groupBox5.Text = "操作符";
            // 
            // trvOperateToken
            // 
            this.trvOperateToken.Dock = System.Windows.Forms.DockStyle.Fill;
            this.trvOperateToken.Indent = 19;
            this.trvOperateToken.ItemHeight = 19;
            this.trvOperateToken.Location = new System.Drawing.Point(3, 17);
            this.trvOperateToken.Name = "trvOperateToken";
            this.trvOperateToken.ShowNodeToolTips = true;
            this.trvOperateToken.Size = new System.Drawing.Size(106, 277);
            this.trvOperateToken.TabIndex = 0;
            this.toolTip1.SetToolTip(this.trvOperateToken, "双击操作符即可在当前输入位置插入选择的操作符");
            this.trvOperateToken.NodeMouseDoubleClick += new System.Windows.Forms.TreeNodeMouseClickEventHandler(this.trvOperateToken_NodeMouseDoubleClick);
            // 
            // splitContainer1
            // 
            this.splitContainer1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.splitContainer1.FixedPanel = System.Windows.Forms.FixedPanel.Panel2;
            this.splitContainer1.Location = new System.Drawing.Point(0, 0);
            this.splitContainer1.Name = "splitContainer1";
            this.splitContainer1.Orientation = System.Windows.Forms.Orientation.Horizontal;
            // 
            // splitContainer1.Panel1
            // 
            this.splitContainer1.Panel1.Controls.Add(this.groupBox1);
            this.splitContainer1.Panel1MinSize = 100;
            // 
            // splitContainer1.Panel2
            // 
            this.splitContainer1.Panel2.Controls.Add(this.groupBox2);
            this.splitContainer1.Panel2MinSize = 100;
            this.splitContainer1.Size = new System.Drawing.Size(352, 297);
            this.splitContainer1.SplitterDistance = 148;
            this.splitContainer1.TabIndex = 3;
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.rtbInput);
            this.groupBox1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.groupBox1.Location = new System.Drawing.Point(0, 0);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(352, 148);
            this.groupBox1.TabIndex = 1;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "输入表达式";
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.rtbOutput);
            this.groupBox2.Dock = System.Windows.Forms.DockStyle.Fill;
            this.groupBox2.Location = new System.Drawing.Point(0, 0);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(352, 145);
            this.groupBox2.TabIndex = 2;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "计算结果";
            // 
            // rtbOutput
            // 
            this.rtbOutput.Dock = System.Windows.Forms.DockStyle.Fill;
            this.rtbOutput.Location = new System.Drawing.Point(3, 17);
            this.rtbOutput.Name = "rtbOutput";
            this.rtbOutput.Size = new System.Drawing.Size(346, 125);
            this.rtbOutput.TabIndex = 0;
            this.rtbOutput.Text = "";
            this.toolTip1.SetToolTip(this.rtbOutput, "显示计算结果，多行计算时分行显示");
            // 
            // tabPage2
            // 
            this.tabPage2.Controls.Add(this.splitContainer2);
            this.tabPage2.Location = new System.Drawing.Point(4, 21);
            this.tabPage2.Name = "tabPage2";
            this.tabPage2.Padding = new System.Windows.Forms.Padding(3);
            this.tabPage2.Size = new System.Drawing.Size(474, 303);
            this.tabPage2.TabIndex = 1;
            this.tabPage2.Text = "语法树分析";
            this.toolTip1.SetToolTip(this.tabPage2, "查看表达式的语法树分析");
            this.tabPage2.UseVisualStyleBackColor = true;
            // 
            // splitContainer2
            // 
            this.splitContainer2.Dock = System.Windows.Forms.DockStyle.Fill;
            this.splitContainer2.FixedPanel = System.Windows.Forms.FixedPanel.Panel2;
            this.splitContainer2.Location = new System.Drawing.Point(3, 3);
            this.splitContainer2.Name = "splitContainer2";
            // 
            // splitContainer2.Panel1
            // 
            this.splitContainer2.Panel1.Controls.Add(this.groupBox3);
            this.splitContainer2.Panel1MinSize = 100;
            // 
            // splitContainer2.Panel2
            // 
            this.splitContainer2.Panel2.Controls.Add(this.groupBox4);
            this.splitContainer2.Panel2MinSize = 100;
            this.splitContainer2.Size = new System.Drawing.Size(468, 297);
            this.splitContainer2.SplitterDistance = 265;
            this.splitContainer2.TabIndex = 2;
            // 
            // groupBox3
            // 
            this.groupBox3.Controls.Add(this.trvSyntaxTree);
            this.groupBox3.Dock = System.Windows.Forms.DockStyle.Fill;
            this.groupBox3.Location = new System.Drawing.Point(0, 0);
            this.groupBox3.Name = "groupBox3";
            this.groupBox3.Size = new System.Drawing.Size(265, 297);
            this.groupBox3.TabIndex = 0;
            this.groupBox3.TabStop = false;
            this.groupBox3.Text = "语法树";
            // 
            // trvSyntaxTree
            // 
            this.trvSyntaxTree.Dock = System.Windows.Forms.DockStyle.Fill;
            this.trvSyntaxTree.Location = new System.Drawing.Point(3, 17);
            this.trvSyntaxTree.Name = "trvSyntaxTree";
            this.trvSyntaxTree.Size = new System.Drawing.Size(259, 277);
            this.trvSyntaxTree.TabIndex = 0;
            this.toolTip1.SetToolTip(this.trvSyntaxTree, "表达式的语法树分析，选择节点后在右边显示节点属性");
            this.trvSyntaxTree.AfterSelect += new System.Windows.Forms.TreeViewEventHandler(this.trvSyntaxTree_AfterSelect);
            // 
            // groupBox4
            // 
            this.groupBox4.Controls.Add(this.pgToken);
            this.groupBox4.Dock = System.Windows.Forms.DockStyle.Fill;
            this.groupBox4.Location = new System.Drawing.Point(0, 0);
            this.groupBox4.Name = "groupBox4";
            this.groupBox4.Size = new System.Drawing.Size(199, 297);
            this.groupBox4.TabIndex = 1;
            this.groupBox4.TabStop = false;
            this.groupBox4.Text = "节点属性";
            // 
            // pgToken
            // 
            this.pgToken.Dock = System.Windows.Forms.DockStyle.Fill;
            this.pgToken.Location = new System.Drawing.Point(3, 17);
            this.pgToken.Name = "pgToken";
            this.pgToken.Size = new System.Drawing.Size(193, 277);
            this.pgToken.TabIndex = 0;
            this.toolTip1.SetToolTip(this.pgToken, "显示选中的节点属性");
            // 
            // btnExecute
            // 
            this.btnExecute.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
            this.btnExecute.Location = new System.Drawing.Point(334, 346);
            this.btnExecute.Name = "btnExecute";
            this.btnExecute.Size = new System.Drawing.Size(75, 23);
            this.btnExecute.TabIndex = 1;
            this.btnExecute.Text = "计算(&C)";
            this.toolTip1.SetToolTip(this.btnExecute, "点击按钮或按F5键执行计算\r\n当未选中\"允许多行计算\"时,回车也执行计算");
            this.btnExecute.UseVisualStyleBackColor = true;
            this.btnExecute.Click += new System.EventHandler(this.btnExecute_Click);
            // 
            // btnExit
            // 
            this.btnExit.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
            this.btnExit.DialogResult = System.Windows.Forms.DialogResult.Cancel;
            this.btnExit.Location = new System.Drawing.Point(412, 346);
            this.btnExit.Name = "btnExit";
            this.btnExit.Size = new System.Drawing.Size(75, 23);
            this.btnExit.TabIndex = 2;
            this.btnExit.Text = "退出(&E)";
            this.toolTip1.SetToolTip(this.btnExit, "点击按钮或按Esc键退出程序");
            this.btnExit.UseVisualStyleBackColor = true;
            this.btnExit.Click += new System.EventHandler(this.btnExit_Click);
            // 
            // chkAllowMultiLine
            // 
            this.chkAllowMultiLine.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
            this.chkAllowMultiLine.AutoSize = true;
            this.chkAllowMultiLine.Location = new System.Drawing.Point(232, 350);
            this.chkAllowMultiLine.Name = "chkAllowMultiLine";
            this.chkAllowMultiLine.Size = new System.Drawing.Size(96, 16);
            this.chkAllowMultiLine.TabIndex = 4;
            this.chkAllowMultiLine.Text = "允许多行计算";
            this.toolTip1.SetToolTip(this.chkAllowMultiLine, "选中时可以输入多行表达式，否则回车后执行计算");
            this.chkAllowMultiLine.UseVisualStyleBackColor = true;
            this.chkAllowMultiLine.CheckedChanged += new System.EventHandler(this.chkAllowMultiLine_CheckedChanged);
            // 
            // toolTip1
            // 
            this.toolTip1.IsBalloon = true;
            this.toolTip1.ToolTipIcon = System.Windows.Forms.ToolTipIcon.Info;
            this.toolTip1.ToolTipTitle = "提示信息";
            // 
            // btnAbout
            // 
            this.btnAbout.Location = new System.Drawing.Point(12, 345);
            this.btnAbout.Name = "btnAbout";
            this.btnAbout.Size = new System.Drawing.Size(75, 23);
            this.btnAbout.TabIndex = 5;
            this.btnAbout.Text = "关于(&A)";
            this.btnAbout.UseVisualStyleBackColor = true;
            this.btnAbout.Click += new System.EventHandler(this.btnAbout_Click);
            // 
            // btnDraw
            // 
            this.btnDraw.Location = new System.Drawing.Point(93, 346);
            this.btnDraw.Name = "btnDraw";
            this.btnDraw.Size = new System.Drawing.Size(75, 23);
            this.btnDraw.TabIndex = 6;
            this.btnDraw.Text = "波形";
            this.btnDraw.UseVisualStyleBackColor = true;
            this.btnDraw.Click += new System.EventHandler(this.btnDraw_Click);
            // 
            // frmMain
            // 
            this.AcceptButton = this.btnExecute;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.CancelButton = this.btnExit;
            this.ClientSize = new System.Drawing.Size(503, 378);
            this.Controls.Add(this.btnDraw);
            this.Controls.Add(this.btnAbout);
            this.Controls.Add(this.chkAllowMultiLine);
            this.Controls.Add(this.btnExit);
            this.Controls.Add(this.btnExecute);
            this.Controls.Add(this.tabControl1);
            this.DoubleBuffered = true;
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Name = "frmMain";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "MyCalculator - Alex Leo @ ConExpress";
            this.Load += new System.EventHandler(this.frmMain_Load);
            this.tabControl1.ResumeLayout(false);
            this.tabPage1.ResumeLayout(false);
            this.splitContainer3.Panel1.ResumeLayout(false);
            this.splitContainer3.Panel2.ResumeLayout(false);
            this.splitContainer3.ResumeLayout(false);
            this.groupBox5.ResumeLayout(false);
            this.splitContainer1.Panel1.ResumeLayout(false);
            this.splitContainer1.Panel2.ResumeLayout(false);
            this.splitContainer1.ResumeLayout(false);
            this.groupBox1.ResumeLayout(false);
            this.groupBox2.ResumeLayout(false);
            this.tabPage2.ResumeLayout(false);
            this.splitContainer2.Panel1.ResumeLayout(false);
            this.splitContainer2.Panel2.ResumeLayout(false);
            this.splitContainer2.ResumeLayout(false);
            this.groupBox3.ResumeLayout(false);
            this.groupBox4.ResumeLayout(false);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.RichTextBox rtbInput;
        private System.Windows.Forms.TabControl tabControl1;
        private System.Windows.Forms.TabPage tabPage1;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.TabPage tabPage2;
        private System.Windows.Forms.Button btnExecute;
        private System.Windows.Forms.Button btnExit;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.RichTextBox rtbOutput;
        private System.Windows.Forms.GroupBox groupBox3;
        private System.Windows.Forms.GroupBox groupBox4;
        private System.Windows.Forms.PropertyGrid pgToken;
        private System.Windows.Forms.TreeView trvSyntaxTree;
        private System.Windows.Forms.CheckBox chkAllowMultiLine;
        private System.Windows.Forms.SplitContainer splitContainer1;
        private System.Windows.Forms.SplitContainer splitContainer2;
        private System.Windows.Forms.SplitContainer splitContainer3;
        private System.Windows.Forms.GroupBox groupBox5;
        private System.Windows.Forms.TreeView trvOperateToken;
        private System.Windows.Forms.ToolTip toolTip1;
        private System.Windows.Forms.Button btnAbout;
        private System.Windows.Forms.Button btnDraw;
    }
}

