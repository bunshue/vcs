namespace vcs_TreeView5
{
    partial class Form1
    {
        /// <summary>
        /// 必需的設計器變數。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清理所有正在使用的資源。
        /// </summary>
        /// <param name="disposing">如果應釋放托管資源，為 true；否則為 false。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows 視窗設計器產生的代碼

        /// <summary>
        /// 設計器支援所需的方法 - 不要
        /// 使用代碼編輯器修改此方法的內容。
        /// </summary>
        private void InitializeComponent()
        {
            System.Windows.Forms.TreeNode treeNode1 = new System.Windows.Forms.TreeNode("企業類型設置");
            System.Windows.Forms.TreeNode treeNode2 = new System.Windows.Forms.TreeNode("企業性質設置");
            System.Windows.Forms.TreeNode treeNode3 = new System.Windows.Forms.TreeNode("企業級別設置");
            System.Windows.Forms.TreeNode treeNode4 = new System.Windows.Forms.TreeNode("企業資信設置");
            System.Windows.Forms.TreeNode treeNode5 = new System.Windows.Forms.TreeNode("基礎訊息維護", new System.Windows.Forms.TreeNode[] {
            treeNode1,
            treeNode2,
            treeNode3,
            treeNode4});
            System.Windows.Forms.TreeNode treeNode6 = new System.Windows.Forms.TreeNode("客戶訊息");
            System.Windows.Forms.TreeNode treeNode7 = new System.Windows.Forms.TreeNode("聯繫人訊息");
            System.Windows.Forms.TreeNode treeNode8 = new System.Windows.Forms.TreeNode("業務往來");
            System.Windows.Forms.TreeNode treeNode9 = new System.Windows.Forms.TreeNode("客戶信息維護", new System.Windows.Forms.TreeNode[] {
            treeNode6,
            treeNode7,
            treeNode8});
            System.Windows.Forms.TreeNode treeNode10 = new System.Windows.Forms.TreeNode("客戶投訴");
            System.Windows.Forms.TreeNode treeNode11 = new System.Windows.Forms.TreeNode("客戶回饋");
            System.Windows.Forms.TreeNode treeNode12 = new System.Windows.Forms.TreeNode("客戶服務", new System.Windows.Forms.TreeNode[] {
            treeNode10,
            treeNode11});
            System.Windows.Forms.TreeNode treeNode13 = new System.Windows.Forms.TreeNode("聯繫人訊息查詢");
            System.Windows.Forms.TreeNode treeNode14 = new System.Windows.Forms.TreeNode("客戶訊息查詢");
            System.Windows.Forms.TreeNode treeNode15 = new System.Windows.Forms.TreeNode("客戶訊息查詢", new System.Windows.Forms.TreeNode[] {
            treeNode13,
            treeNode14});
            System.Windows.Forms.TreeNode treeNode16 = new System.Windows.Forms.TreeNode("客戶訊息報表");
            System.Windows.Forms.TreeNode treeNode17 = new System.Windows.Forms.TreeNode("業務往來報表");
            System.Windows.Forms.TreeNode treeNode18 = new System.Windows.Forms.TreeNode("聯繫人訊息報表");
            System.Windows.Forms.TreeNode treeNode19 = new System.Windows.Forms.TreeNode("打印報表", new System.Windows.Forms.TreeNode[] {
            treeNode16,
            treeNode17,
            treeNode18});
            System.Windows.Forms.TreeNode treeNode20 = new System.Windows.Forms.TreeNode("Word");
            System.Windows.Forms.TreeNode treeNode21 = new System.Windows.Forms.TreeNode("Excel");
            System.Windows.Forms.TreeNode treeNode22 = new System.Windows.Forms.TreeNode("輔助工具", new System.Windows.Forms.TreeNode[] {
            treeNode20,
            treeNode21});
            this.menuStrip1 = new System.Windows.Forms.MenuStrip();
            this.基礎訊息維護ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.客戶信息維護ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.客戶服務ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.客戶訊息查詢ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.treeView1 = new System.Windows.Forms.TreeView();
            this.pictureBox2 = new System.Windows.Forms.PictureBox();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.menuStrip1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // menuStrip1
            // 
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.基礎訊息維護ToolStripMenuItem,
            this.客戶信息維護ToolStripMenuItem,
            this.客戶服務ToolStripMenuItem,
            this.客戶訊息查詢ToolStripMenuItem});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Size = new System.Drawing.Size(702, 24);
            this.menuStrip1.TabIndex = 0;
            this.menuStrip1.Text = "menuStrip1";
            // 
            // 基礎訊息維護ToolStripMenuItem
            // 
            this.基礎訊息維護ToolStripMenuItem.Name = "基礎訊息維護ToolStripMenuItem";
            this.基礎訊息維護ToolStripMenuItem.Size = new System.Drawing.Size(89, 20);
            this.基礎訊息維護ToolStripMenuItem.Text = "基礎訊息維護";
            // 
            // 客戶信息維護ToolStripMenuItem
            // 
            this.客戶信息維護ToolStripMenuItem.Name = "客戶信息維護ToolStripMenuItem";
            this.客戶信息維護ToolStripMenuItem.Size = new System.Drawing.Size(89, 20);
            this.客戶信息維護ToolStripMenuItem.Text = "客戶信息維護";
            // 
            // 客戶服務ToolStripMenuItem
            // 
            this.客戶服務ToolStripMenuItem.Name = "客戶服務ToolStripMenuItem";
            this.客戶服務ToolStripMenuItem.Size = new System.Drawing.Size(65, 20);
            this.客戶服務ToolStripMenuItem.Text = "客戶服務";
            // 
            // 客戶訊息查詢ToolStripMenuItem
            // 
            this.客戶訊息查詢ToolStripMenuItem.Name = "客戶訊息查詢ToolStripMenuItem";
            this.客戶訊息查詢ToolStripMenuItem.Size = new System.Drawing.Size(89, 20);
            this.客戶訊息查詢ToolStripMenuItem.Text = "客戶訊息查詢";
            // 
            // treeView1
            // 
            this.treeView1.Location = new System.Drawing.Point(0, 77);
            this.treeView1.Name = "treeView1";
            treeNode1.Name = "節點1";
            treeNode1.Text = "企業類型設置";
            treeNode2.Name = "節點2";
            treeNode2.Text = "企業性質設置";
            treeNode3.Name = "節點3";
            treeNode3.Text = "企業級別設置";
            treeNode4.Name = "節點4";
            treeNode4.Text = "企業資信設置";
            treeNode5.Name = "節點0";
            treeNode5.Text = "基礎訊息維護";
            treeNode6.Name = "節點6";
            treeNode6.Text = "客戶訊息";
            treeNode7.Name = "節點7";
            treeNode7.Text = "聯繫人訊息";
            treeNode8.Name = "節點9";
            treeNode8.Text = "業務往來";
            treeNode9.Name = "節點5";
            treeNode9.Text = "客戶信息維護";
            treeNode10.Name = "節點11";
            treeNode10.Text = "客戶投訴";
            treeNode11.Name = "節點12";
            treeNode11.Text = "客戶回饋";
            treeNode12.Name = "節點10";
            treeNode12.Text = "客戶服務";
            treeNode13.Name = "節點14";
            treeNode13.Text = "聯繫人訊息查詢";
            treeNode14.Name = "節點15";
            treeNode14.Text = "客戶訊息查詢";
            treeNode15.Name = "節點13";
            treeNode15.Text = "客戶訊息查詢";
            treeNode16.Name = "節點17";
            treeNode16.Text = "客戶訊息報表";
            treeNode17.Name = "節點18";
            treeNode17.Text = "業務往來報表";
            treeNode18.Name = "節點20";
            treeNode18.Text = "聯繫人訊息報表";
            treeNode19.Name = "節點16";
            treeNode19.Text = "打印報表";
            treeNode20.Name = "節點21";
            treeNode20.Text = "Word";
            treeNode21.Name = "節點22";
            treeNode21.Text = "Excel";
            treeNode22.Name = "節點19";
            treeNode22.Text = "輔助工具";
            this.treeView1.Nodes.AddRange(new System.Windows.Forms.TreeNode[] {
            treeNode5,
            treeNode9,
            treeNode12,
            treeNode15,
            treeNode19,
            treeNode22});
            this.treeView1.Size = new System.Drawing.Size(139, 393);
            this.treeView1.TabIndex = 2;
            // 
            // pictureBox2
            // 
            this.pictureBox2.Image = global::vcs_TreeView5.Properties.Resources.右;
            this.pictureBox2.Location = new System.Drawing.Point(136, 77);
            this.pictureBox2.Name = "pictureBox2";
            this.pictureBox2.Size = new System.Drawing.Size(581, 416);
            this.pictureBox2.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.pictureBox2.TabIndex = 3;
            this.pictureBox2.TabStop = false;
            // 
            // pictureBox1
            // 
            this.pictureBox1.Image = global::vcs_TreeView5.Properties.Resources.上;
            this.pictureBox1.Location = new System.Drawing.Point(0, 27);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(765, 56);
            this.pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.pictureBox1.TabIndex = 1;
            this.pictureBox1.TabStop = false;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(702, 473);
            this.Controls.Add(this.pictureBox2);
            this.Controls.Add(this.treeView1);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.menuStrip1);
            this.MainMenuStrip = this.menuStrip1;
            this.Name = "Form1";
            this.Text = "樹狀程式介面";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.MenuStrip menuStrip1;
        private System.Windows.Forms.ToolStripMenuItem 基礎訊息維護ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 客戶信息維護ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 客戶服務ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 客戶訊息查詢ToolStripMenuItem;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.TreeView treeView1;
        private System.Windows.Forms.PictureBox pictureBox2;
    }
}

