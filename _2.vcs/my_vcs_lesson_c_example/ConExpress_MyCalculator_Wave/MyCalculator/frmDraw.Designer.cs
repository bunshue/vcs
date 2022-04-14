namespace ConExpress.Calculator
{
    partial class frmDraw
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(frmDraw));
            this.picImage = new System.Windows.Forms.PictureBox();
            this.toolStrip1 = new System.Windows.Forms.ToolStrip();
            this.btnDraw = new System.Windows.Forms.ToolStripButton();
            this.btnSave = new System.Windows.Forms.ToolStripButton();
            this.toolStripSeparator1 = new System.Windows.Forms.ToolStripSeparator();
            this.toolStripLabel1 = new System.Windows.Forms.ToolStripLabel();
            this.numMin = new ConExpress.Controls.ToolStripNumericUpDown();
            this.toolStripLabel2 = new System.Windows.Forms.ToolStripLabel();
            this.numMax = new ConExpress.Controls.ToolStripNumericUpDown();
            this.toolStripSeparator2 = new System.Windows.Forms.ToolStripSeparator();
            this.toolStripLabel3 = new System.Windows.Forms.ToolStripLabel();
            this.numScale = new ConExpress.Controls.ToolStripNumericUpDown();
            this.toolStripSeparator3 = new System.Windows.Forms.ToolStripSeparator();
            this.btnShowProperty = new System.Windows.Forms.ToolStripButton();
            this.splitContainer1 = new System.Windows.Forms.SplitContainer();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.lstDrawInfo = new System.Windows.Forms.ListBox();
            this.bdsDrawInfo = new System.Windows.Forms.BindingSource(this.components);
            this.toolStrip2 = new System.Windows.Forms.ToolStrip();
            this.btnAdd = new System.Windows.Forms.ToolStripButton();
            this.btnDelete = new System.Windows.Forms.ToolStripButton();
            this.propertyGrid1 = new System.Windows.Forms.PropertyGrid();
            this.panel1 = new System.Windows.Forms.Panel();
            this.lblProperty = new System.Windows.Forms.Label();
            this.dlgSaveImage = new System.Windows.Forms.SaveFileDialog();
            ((System.ComponentModel.ISupportInitialize)(this.picImage)).BeginInit();
            this.toolStrip1.SuspendLayout();
            this.splitContainer1.Panel1.SuspendLayout();
            this.splitContainer1.Panel2.SuspendLayout();
            this.splitContainer1.SuspendLayout();
            this.groupBox1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.bdsDrawInfo)).BeginInit();
            this.toolStrip2.SuspendLayout();
            this.panel1.SuspendLayout();
            this.SuspendLayout();
            // 
            // picImage
            // 
            this.picImage.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.picImage.Dock = System.Windows.Forms.DockStyle.Fill;
            this.picImage.Location = new System.Drawing.Point(0, 0);
            this.picImage.Name = "picImage";
            this.picImage.Size = new System.Drawing.Size(714, 635);
            this.picImage.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.picImage.TabIndex = 6;
            this.picImage.TabStop = false;
            // 
            // toolStrip1
            // 
            this.toolStrip1.GripStyle = System.Windows.Forms.ToolStripGripStyle.Hidden;
            this.toolStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.btnDraw,
            this.btnSave,
            this.toolStripSeparator1,
            this.toolStripLabel1,
            this.numMin,
            this.toolStripLabel2,
            this.numMax,
            this.toolStripSeparator2,
            this.toolStripLabel3,
            this.numScale,
            this.toolStripSeparator3,
            this.btnShowProperty});
            this.toolStrip1.Location = new System.Drawing.Point(0, 0);
            this.toolStrip1.Name = "toolStrip1";
            this.toolStrip1.Size = new System.Drawing.Size(914, 25);
            this.toolStrip1.TabIndex = 9;
            this.toolStrip1.Text = "toolStrip1";
            // 
            // btnDraw
            // 
            this.btnDraw.Image = ((System.Drawing.Image)(resources.GetObject("btnDraw.Image")));
            this.btnDraw.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.btnDraw.Name = "btnDraw";
            this.btnDraw.Size = new System.Drawing.Size(73, 22);
            this.btnDraw.Text = "绘制图像";
            this.btnDraw.Click += new System.EventHandler(this.btnDraw_Click);
            // 
            // btnSave
            // 
            this.btnSave.Enabled = false;
            this.btnSave.Image = ((System.Drawing.Image)(resources.GetObject("btnSave.Image")));
            this.btnSave.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.btnSave.Name = "btnSave";
            this.btnSave.Size = new System.Drawing.Size(73, 22);
            this.btnSave.Text = "保存图片";
            this.btnSave.Click += new System.EventHandler(this.btnSave_Click);
            // 
            // toolStripSeparator1
            // 
            this.toolStripSeparator1.Name = "toolStripSeparator1";
            this.toolStripSeparator1.Size = new System.Drawing.Size(6, 25);
            // 
            // toolStripLabel1
            // 
            this.toolStripLabel1.Name = "toolStripLabel1";
            this.toolStripLabel1.Size = new System.Drawing.Size(59, 22);
            this.toolStripLabel1.Text = "N的范围：";
            // 
            // numMin
            // 
            this.numMin.Maximum = new decimal(new int[] {
            10000000,
            0,
            0,
            0});
            this.numMin.Minimum = new decimal(new int[] {
            10000000,
            0,
            0,
            -2147483648});
            this.numMin.Name = "numMin";
            this.numMin.Size = new System.Drawing.Size(100, 22);
            this.numMin.ThousandsSeparator = true;
            this.numMin.Value = new decimal(new int[] {
            360,
            0,
            0,
            -2147483648});
            // 
            // toolStripLabel2
            // 
            this.toolStripLabel2.Name = "toolStripLabel2";
            this.toolStripLabel2.Size = new System.Drawing.Size(17, 22);
            this.toolStripLabel2.Text = "到";
            // 
            // numMax
            // 
            this.numMax.Maximum = new decimal(new int[] {
            10000000,
            0,
            0,
            0});
            this.numMax.Minimum = new decimal(new int[] {
            10000000,
            0,
            0,
            -2147483648});
            this.numMax.Name = "numMax";
            this.numMax.Size = new System.Drawing.Size(100, 22);
            this.numMax.ThousandsSeparator = true;
            this.numMax.Value = new decimal(new int[] {
            360,
            0,
            0,
            0});
            // 
            // toolStripSeparator2
            // 
            this.toolStripSeparator2.Name = "toolStripSeparator2";
            this.toolStripSeparator2.Size = new System.Drawing.Size(6, 25);
            // 
            // toolStripLabel3
            // 
            this.toolStripLabel3.Name = "toolStripLabel3";
            this.toolStripLabel3.Size = new System.Drawing.Size(41, 22);
            this.toolStripLabel3.Text = "刻度：";
            // 
            // numScale
            // 
            this.numScale.Minimum = new decimal(new int[] {
            5,
            0,
            0,
            0});
            this.numScale.Name = "numScale";
            this.numScale.Size = new System.Drawing.Size(100, 22);
            this.numScale.Value = new decimal(new int[] {
            25,
            0,
            0,
            0});
            // 
            // toolStripSeparator3
            // 
            this.toolStripSeparator3.Name = "toolStripSeparator3";
            this.toolStripSeparator3.Size = new System.Drawing.Size(6, 25);
            // 
            // btnShowProperty
            // 
            this.btnShowProperty.Checked = true;
            this.btnShowProperty.CheckOnClick = true;
            this.btnShowProperty.CheckState = System.Windows.Forms.CheckState.Checked;
            this.btnShowProperty.Image = ((System.Drawing.Image)(resources.GetObject("btnShowProperty.Image")));
            this.btnShowProperty.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.btnShowProperty.Name = "btnShowProperty";
            this.btnShowProperty.Size = new System.Drawing.Size(73, 22);
            this.btnShowProperty.Text = "显示属性";
            this.btnShowProperty.Click += new System.EventHandler(this.btnShowProperty_Click);
            // 
            // splitContainer1
            // 
            this.splitContainer1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.splitContainer1.FixedPanel = System.Windows.Forms.FixedPanel.Panel2;
            this.splitContainer1.Location = new System.Drawing.Point(0, 25);
            this.splitContainer1.Name = "splitContainer1";
            // 
            // splitContainer1.Panel1
            // 
            this.splitContainer1.Panel1.AutoScroll = true;
            this.splitContainer1.Panel1.Controls.Add(this.picImage);
            // 
            // splitContainer1.Panel2
            // 
            this.splitContainer1.Panel2.Controls.Add(this.groupBox1);
            this.splitContainer1.Panel2.Controls.Add(this.propertyGrid1);
            this.splitContainer1.Panel2.Controls.Add(this.panel1);
            this.splitContainer1.Size = new System.Drawing.Size(914, 635);
            this.splitContainer1.SplitterDistance = 714;
            this.splitContainer1.TabIndex = 11;
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.lstDrawInfo);
            this.groupBox1.Controls.Add(this.toolStrip2);
            this.groupBox1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.groupBox1.Location = new System.Drawing.Point(0, 268);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(196, 367);
            this.groupBox1.TabIndex = 13;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "绘图信息列表";
            // 
            // lstDrawInfo
            // 
            this.lstDrawInfo.DataSource = this.bdsDrawInfo;
            this.lstDrawInfo.DisplayMember = "Name";
            this.lstDrawInfo.Dock = System.Windows.Forms.DockStyle.Fill;
            this.lstDrawInfo.FormattingEnabled = true;
            this.lstDrawInfo.ItemHeight = 12;
            this.lstDrawInfo.Location = new System.Drawing.Point(3, 42);
            this.lstDrawInfo.Name = "lstDrawInfo";
            this.lstDrawInfo.SelectionMode = System.Windows.Forms.SelectionMode.MultiExtended;
            this.lstDrawInfo.Size = new System.Drawing.Size(190, 316);
            this.lstDrawInfo.TabIndex = 4;
            this.lstDrawInfo.SelectedIndexChanged += new System.EventHandler(this.lstDrawInfo_SelectedIndexChanged);
            // 
            // bdsDrawInfo
            // 
            this.bdsDrawInfo.DataSource = typeof(ConExpress.Calculator.DrawInfo);
            // 
            // toolStrip2
            // 
            this.toolStrip2.GripStyle = System.Windows.Forms.ToolStripGripStyle.Hidden;
            this.toolStrip2.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.btnAdd,
            this.btnDelete});
            this.toolStrip2.Location = new System.Drawing.Point(3, 17);
            this.toolStrip2.Name = "toolStrip2";
            this.toolStrip2.Size = new System.Drawing.Size(190, 25);
            this.toolStrip2.TabIndex = 3;
            this.toolStrip2.Text = "toolStrip2";
            // 
            // btnAdd
            // 
            this.btnAdd.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.btnAdd.Image = ((System.Drawing.Image)(resources.GetObject("btnAdd.Image")));
            this.btnAdd.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.btnAdd.Name = "btnAdd";
            this.btnAdd.Size = new System.Drawing.Size(23, 22);
            this.btnAdd.Text = "新增";
            this.btnAdd.Click += new System.EventHandler(this.btnAdd_Click);
            // 
            // btnDelete
            // 
            this.btnDelete.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.btnDelete.Image = ((System.Drawing.Image)(resources.GetObject("btnDelete.Image")));
            this.btnDelete.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.btnDelete.Name = "btnDelete";
            this.btnDelete.Size = new System.Drawing.Size(23, 22);
            this.btnDelete.Text = "删除";
            this.btnDelete.Click += new System.EventHandler(this.btnDelete_Click);
            // 
            // propertyGrid1
            // 
            this.propertyGrid1.Dock = System.Windows.Forms.DockStyle.Top;
            this.propertyGrid1.Location = new System.Drawing.Point(0, 22);
            this.propertyGrid1.Name = "propertyGrid1";
            this.propertyGrid1.Size = new System.Drawing.Size(196, 246);
            this.propertyGrid1.TabIndex = 12;
            // 
            // panel1
            // 
            this.panel1.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.panel1.Controls.Add(this.lblProperty);
            this.panel1.Dock = System.Windows.Forms.DockStyle.Top;
            this.panel1.Location = new System.Drawing.Point(0, 0);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(196, 22);
            this.panel1.TabIndex = 11;
            // 
            // lblProperty
            // 
            this.lblProperty.AutoSize = true;
            this.lblProperty.ForeColor = System.Drawing.SystemColors.ActiveCaptionText;
            this.lblProperty.Location = new System.Drawing.Point(6, 6);
            this.lblProperty.Name = "lblProperty";
            this.lblProperty.Size = new System.Drawing.Size(29, 12);
            this.lblProperty.TabIndex = 0;
            this.lblProperty.Text = "属性";
            // 
            // dlgSaveImage
            // 
            this.dlgSaveImage.Filter = "PNG图片|*.png|JPG图片|*.jpg|GIF图片|*.gif|BMP图片|*.bmp";
            // 
            // frmDraw
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(914, 660);
            this.Controls.Add(this.splitContainer1);
            this.Controls.Add(this.toolStrip1);
            this.Name = "frmDraw";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "绘制波形";
            this.Load += new System.EventHandler(this.frmDraw_Load);
            ((System.ComponentModel.ISupportInitialize)(this.picImage)).EndInit();
            this.toolStrip1.ResumeLayout(false);
            this.toolStrip1.PerformLayout();
            this.splitContainer1.Panel1.ResumeLayout(false);
            this.splitContainer1.Panel1.PerformLayout();
            this.splitContainer1.Panel2.ResumeLayout(false);
            this.splitContainer1.ResumeLayout(false);
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.bdsDrawInfo)).EndInit();
            this.toolStrip2.ResumeLayout(false);
            this.toolStrip2.PerformLayout();
            this.panel1.ResumeLayout(false);
            this.panel1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox picImage;
        private System.Windows.Forms.ToolStrip toolStrip1;
        private System.Windows.Forms.ToolStripButton btnDraw;
        private System.Windows.Forms.ToolStripLabel toolStripLabel1;
        private ConExpress.Controls.ToolStripNumericUpDown numMin;
        private System.Windows.Forms.ToolStripLabel toolStripLabel2;
        private ConExpress.Controls.ToolStripNumericUpDown numMax;
        private System.Windows.Forms.ToolStripSeparator toolStripSeparator1;
        private System.Windows.Forms.ToolStripSeparator toolStripSeparator2;
        private System.Windows.Forms.ToolStripLabel toolStripLabel3;
        private ConExpress.Controls.ToolStripNumericUpDown numScale;
        private System.Windows.Forms.ToolStripButton btnSave;
        private System.Windows.Forms.ToolStripSeparator toolStripSeparator3;
        private System.Windows.Forms.ToolStripButton btnShowProperty;
        private System.Windows.Forms.SplitContainer splitContainer1;
        private System.Windows.Forms.PropertyGrid propertyGrid1;
        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.Label lblProperty;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.ListBox lstDrawInfo;
        private System.Windows.Forms.ToolStrip toolStrip2;
        private System.Windows.Forms.ToolStripButton btnAdd;
        private System.Windows.Forms.ToolStripButton btnDelete;
        private System.Windows.Forms.BindingSource bdsDrawInfo;
        private System.Windows.Forms.SaveFileDialog dlgSaveImage;
    }
}