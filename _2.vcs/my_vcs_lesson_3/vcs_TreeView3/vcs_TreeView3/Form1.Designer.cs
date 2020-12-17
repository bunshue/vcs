namespace vcs_TreeView3
{
    partial class Form1
    {
        /// <summary>
        /// 設計工具所需的變數。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清除任何使用中的資源。
        /// </summary>
        /// <param name="disposing">如果應該處置 Managed 資源則為 true，否則為 false。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form 設計工具產生的程式碼

        /// <summary>
        /// 此為設計工具支援所需的方法 - 請勿使用程式碼編輯器
        /// 修改這個方法的內容。
        /// </summary>
        private void InitializeComponent()
        {
            System.Windows.Forms.TreeNode treeNode1 = new System.Windows.Forms.TreeNode("General");
            System.Windows.Forms.TreeNode treeNode2 = new System.Windows.Forms.TreeNode("Documents");
            System.Windows.Forms.TreeNode treeNode3 = new System.Windows.Forms.TreeNode("Environment", new System.Windows.Forms.TreeNode[] {
            treeNode1,
            treeNode2});
            System.Windows.Forms.TreeNode treeNode4 = new System.Windows.Forms.TreeNode("General");
            System.Windows.Forms.TreeNode treeNode5 = new System.Windows.Forms.TreeNode("Defaults");
            System.Windows.Forms.TreeNode treeNode6 = new System.Windows.Forms.TreeNode("Projects", new System.Windows.Forms.TreeNode[] {
            treeNode4,
            treeNode5});
            System.Windows.Forms.TreeNode treeNode7 = new System.Windows.Forms.TreeNode("All Languages");
            System.Windows.Forms.TreeNode treeNode8 = new System.Windows.Forms.TreeNode("General");
            System.Windows.Forms.TreeNode treeNode9 = new System.Windows.Forms.TreeNode("Tabs");
            System.Windows.Forms.TreeNode treeNode10 = new System.Windows.Forms.TreeNode("Advanced");
            System.Windows.Forms.TreeNode treeNode11 = new System.Windows.Forms.TreeNode("C#", new System.Windows.Forms.TreeNode[] {
            treeNode8,
            treeNode9,
            treeNode10});
            System.Windows.Forms.TreeNode treeNode12 = new System.Windows.Forms.TreeNode("General");
            System.Windows.Forms.TreeNode treeNode13 = new System.Windows.Forms.TreeNode("Tabs");
            System.Windows.Forms.TreeNode treeNode14 = new System.Windows.Forms.TreeNode("Advanced");
            System.Windows.Forms.TreeNode treeNode15 = new System.Windows.Forms.TreeNode("Visual Basic", new System.Windows.Forms.TreeNode[] {
            treeNode12,
            treeNode13,
            treeNode14});
            System.Windows.Forms.TreeNode treeNode16 = new System.Windows.Forms.TreeNode("Text Editor", new System.Windows.Forms.TreeNode[] {
            treeNode7,
            treeNode11,
            treeNode15});
            this.treeView1 = new System.Windows.Forms.TreeView();
            this.treeView2 = new System.Windows.Forms.TreeView();
            this.label1 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // treeView1
            // 
            this.treeView1.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.treeView1.Location = new System.Drawing.Point(12, 12);
            this.treeView1.Name = "treeView1";
            this.treeView1.Size = new System.Drawing.Size(409, 530);
            this.treeView1.TabIndex = 0;
            // 
            // treeView2
            // 
            this.treeView2.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.treeView2.Location = new System.Drawing.Point(427, 12);
            this.treeView2.Name = "treeView2";
            treeNode1.Name = "Node1";
            treeNode1.Tag = "0";
            treeNode1.Text = "General";
            treeNode2.Name = "Node2";
            treeNode2.Tag = "1";
            treeNode2.Text = "Documents";
            treeNode3.Name = "Node0";
            treeNode3.Tag = "0";
            treeNode3.Text = "Environment";
            treeNode4.Name = "Node5";
            treeNode4.Tag = "2";
            treeNode4.Text = "General";
            treeNode5.Name = "Node6";
            treeNode5.Tag = "3";
            treeNode5.Text = "Defaults";
            treeNode6.Name = "Node4";
            treeNode6.Tag = "2";
            treeNode6.Text = "Projects";
            treeNode7.Name = "Node8";
            treeNode7.Tag = "4";
            treeNode7.Text = "All Languages";
            treeNode8.Name = "Node12";
            treeNode8.Tag = "5";
            treeNode8.Text = "General";
            treeNode9.Name = "Node13";
            treeNode9.Tag = "6";
            treeNode9.Text = "Tabs";
            treeNode10.Name = "Node14";
            treeNode10.Tag = "7";
            treeNode10.Text = "Advanced";
            treeNode11.Name = "Node9";
            treeNode11.Tag = "5";
            treeNode11.Text = "C#";
            treeNode12.Name = "Node15";
            treeNode12.Tag = "8";
            treeNode12.Text = "General";
            treeNode13.Name = "Node16";
            treeNode13.Tag = "9";
            treeNode13.Text = "Tabs";
            treeNode14.Name = "Node17";
            treeNode14.Tag = "10";
            treeNode14.Text = "Advanced";
            treeNode15.Name = "Node11";
            treeNode15.Tag = "8";
            treeNode15.Text = "Visual Basic";
            treeNode16.Name = "Node7";
            treeNode16.Tag = "4";
            treeNode16.Text = "Text Editor";
            this.treeView2.Nodes.AddRange(new System.Windows.Forms.TreeNode[] {
            treeNode3,
            treeNode6,
            treeNode16});
            this.treeView2.Size = new System.Drawing.Size(437, 530);
            this.treeView2.TabIndex = 1;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label1.Location = new System.Drawing.Point(22, 558);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(835, 24);
            this.label1.TabIndex = 2;
            this.label1.Text = "TreeView      左：由程式中加入Node，    右：在TreeView屬性中的Nodes加入項目";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(876, 604);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.treeView2);
            this.Controls.Add(this.treeView1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TreeView treeView1;
        private System.Windows.Forms.TreeView treeView2;
        private System.Windows.Forms.Label label1;
    }
}

