namespace 製作自己的網絡瀏覽軟件
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

        #region Windows 視窗設計器產生的程式碼

        /// <summary>
        /// 設計器支援所需的方法 - 不要
        /// 使用程式碼編輯器修改此方法的內容。
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.webBrowser1 = new System.Windows.Forms.WebBrowser();
            this.menuStrip1 = new System.Windows.Forms.MenuStrip();
            this.保存ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.保存DToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.dToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.打印瀏覽UToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.打印PToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.屬性NToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.退出IToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStrip1 = new System.Windows.Forms.ToolStrip();
            this.GoaButton = new System.Windows.Forms.ToolStripButton();
            this.backButton = new System.Windows.Forms.ToolStripButton();
            this.forwardButton = new System.Windows.Forms.ToolStripButton();
            this.stopButton = new System.Windows.Forms.ToolStripButton();
            this.refreshButton = new System.Windows.Forms.ToolStripButton();
            this.homeButton = new System.Windows.Forms.ToolStripButton();
            this.searchButton = new System.Windows.Forms.ToolStripButton();
            this.printButton = new System.Windows.Forms.ToolStripButton();
            this.toolStrip2 = new System.Windows.Forms.ToolStrip();
            this.toolStripTextBox1 = new System.Windows.Forms.ToolStripTextBox();
            this.toolStripLabel1 = new System.Windows.Forms.ToolStripLabel();
            this.menuStrip1.SuspendLayout();
            this.toolStrip1.SuspendLayout();
            this.toolStrip2.SuspendLayout();
            this.SuspendLayout();
            // 
            // webBrowser1
            // 
            this.webBrowser1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.webBrowser1.Location = new System.Drawing.Point(0, 24);
            this.webBrowser1.MinimumSize = new System.Drawing.Size(20, 20);
            this.webBrowser1.Name = "webBrowser1";
            this.webBrowser1.Size = new System.Drawing.Size(427, 251);
            this.webBrowser1.TabIndex = 0;
            this.webBrowser1.Navigated += new System.Windows.Forms.WebBrowserNavigatedEventHandler(this.webBrowser1_Navigated);
            // 
            // menuStrip1
            // 
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.保存ToolStripMenuItem});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Size = new System.Drawing.Size(427, 24);
            this.menuStrip1.TabIndex = 1;
            this.menuStrip1.Text = "menuStrip1";
            // 
            // 保存ToolStripMenuItem
            // 
            this.保存ToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.保存DToolStripMenuItem,
            this.dToolStripMenuItem,
            this.打印瀏覽UToolStripMenuItem,
            this.打印PToolStripMenuItem,
            this.屬性NToolStripMenuItem,
            this.退出IToolStripMenuItem});
            this.保存ToolStripMenuItem.Name = "保存ToolStripMenuItem";
            this.保存ToolStripMenuItem.Size = new System.Drawing.Size(55, 20);
            this.保存ToolStripMenuItem.Text = "文件(&F)";
            // 
            // 保存DToolStripMenuItem
            // 
            this.保存DToolStripMenuItem.Name = "保存DToolStripMenuItem";
            this.保存DToolStripMenuItem.Size = new System.Drawing.Size(134, 22);
            this.保存DToolStripMenuItem.Text = "保存（&D)";
            this.保存DToolStripMenuItem.Click += new System.EventHandler(this.保存DToolStripMenuItem_Click);
            // 
            // dToolStripMenuItem
            // 
            this.dToolStripMenuItem.Name = "dToolStripMenuItem";
            this.dToolStripMenuItem.Size = new System.Drawing.Size(134, 22);
            this.dToolStripMenuItem.Text = "頁面設定(&E)";
            this.dToolStripMenuItem.Click += new System.EventHandler(this.dToolStripMenuItem_Click);
            // 
            // 打印瀏覽UToolStripMenuItem
            // 
            this.打印瀏覽UToolStripMenuItem.Name = "打印瀏覽UToolStripMenuItem";
            this.打印瀏覽UToolStripMenuItem.Size = new System.Drawing.Size(134, 22);
            this.打印瀏覽UToolStripMenuItem.Text = "打印瀏覽(&U)";
            this.打印瀏覽UToolStripMenuItem.Click += new System.EventHandler(this.打印瀏覽UToolStripMenuItem_Click);
            // 
            // 打印PToolStripMenuItem
            // 
            this.打印PToolStripMenuItem.Name = "打印PToolStripMenuItem";
            this.打印PToolStripMenuItem.Size = new System.Drawing.Size(134, 22);
            this.打印PToolStripMenuItem.Text = "打印(&P)";
            this.打印PToolStripMenuItem.Click += new System.EventHandler(this.打印PToolStripMenuItem_Click);
            // 
            // 屬性NToolStripMenuItem
            // 
            this.屬性NToolStripMenuItem.Name = "屬性NToolStripMenuItem";
            this.屬性NToolStripMenuItem.Size = new System.Drawing.Size(134, 22);
            this.屬性NToolStripMenuItem.Text = "屬性(&N)";
            this.屬性NToolStripMenuItem.Click += new System.EventHandler(this.屬性NToolStripMenuItem_Click);
            // 
            // 退出IToolStripMenuItem
            // 
            this.退出IToolStripMenuItem.Name = "退出IToolStripMenuItem";
            this.退出IToolStripMenuItem.Size = new System.Drawing.Size(134, 22);
            this.退出IToolStripMenuItem.Text = "退出(&I)";
            this.退出IToolStripMenuItem.Click += new System.EventHandler(this.退出IToolStripMenuItem_Click);
            // 
            // toolStrip1
            // 
            this.toolStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.GoaButton,
            this.backButton,
            this.forwardButton,
            this.stopButton,
            this.refreshButton,
            this.homeButton,
            this.searchButton,
            this.printButton});
            this.toolStrip1.Location = new System.Drawing.Point(0, 24);
            this.toolStrip1.Name = "toolStrip1";
            this.toolStrip1.Size = new System.Drawing.Size(427, 25);
            this.toolStrip1.TabIndex = 3;
            this.toolStrip1.Text = "toolStrip1";
            // 
            // GoaButton
            // 
            this.GoaButton.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Text;
            this.GoaButton.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.GoaButton.Name = "GoaButton";
            this.GoaButton.Size = new System.Drawing.Size(33, 22);
            this.GoaButton.Text = "前往";
            this.GoaButton.Click += new System.EventHandler(this.GoaButton_Click);
            // 
            // backButton
            // 
            this.backButton.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Text;
            this.backButton.Image = ((System.Drawing.Image)(resources.GetObject("backButton.Image")));
            this.backButton.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.backButton.Name = "backButton";
            this.backButton.Size = new System.Drawing.Size(33, 22);
            this.backButton.Text = "後退";
            this.backButton.Click += new System.EventHandler(this.backButton_Click);
            // 
            // forwardButton
            // 
            this.forwardButton.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Text;
            this.forwardButton.Image = ((System.Drawing.Image)(resources.GetObject("forwardButton.Image")));
            this.forwardButton.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.forwardButton.Name = "forwardButton";
            this.forwardButton.Size = new System.Drawing.Size(33, 22);
            this.forwardButton.Text = "前進";
            this.forwardButton.Click += new System.EventHandler(this.forwardButton_Click);
            // 
            // stopButton
            // 
            this.stopButton.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Text;
            this.stopButton.Image = ((System.Drawing.Image)(resources.GetObject("stopButton.Image")));
            this.stopButton.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.stopButton.Name = "stopButton";
            this.stopButton.Size = new System.Drawing.Size(33, 22);
            this.stopButton.Text = "停止";
            this.stopButton.Click += new System.EventHandler(this.stopButton_Click);
            // 
            // refreshButton
            // 
            this.refreshButton.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Text;
            this.refreshButton.Image = ((System.Drawing.Image)(resources.GetObject("refreshButton.Image")));
            this.refreshButton.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.refreshButton.Name = "refreshButton";
            this.refreshButton.Size = new System.Drawing.Size(33, 22);
            this.refreshButton.Text = "更新";
            this.refreshButton.Click += new System.EventHandler(this.refreshButton_Click);
            // 
            // homeButton
            // 
            this.homeButton.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Text;
            this.homeButton.Image = ((System.Drawing.Image)(resources.GetObject("homeButton.Image")));
            this.homeButton.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.homeButton.Name = "homeButton";
            this.homeButton.Size = new System.Drawing.Size(33, 22);
            this.homeButton.Text = "主頁";
            this.homeButton.Click += new System.EventHandler(this.homeButton_Click);
            // 
            // searchButton
            // 
            this.searchButton.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Text;
            this.searchButton.Image = ((System.Drawing.Image)(resources.GetObject("searchButton.Image")));
            this.searchButton.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.searchButton.Name = "searchButton";
            this.searchButton.Size = new System.Drawing.Size(33, 22);
            this.searchButton.Text = "查詢";
            this.searchButton.Click += new System.EventHandler(this.searchButton_Click);
            // 
            // printButton
            // 
            this.printButton.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Text;
            this.printButton.Image = ((System.Drawing.Image)(resources.GetObject("printButton.Image")));
            this.printButton.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.printButton.Name = "printButton";
            this.printButton.Size = new System.Drawing.Size(33, 22);
            this.printButton.Text = "列印";
            this.printButton.Click += new System.EventHandler(this.printButton_Click);
            // 
            // toolStrip2
            // 
            this.toolStrip2.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.toolStripTextBox1,
            this.toolStripLabel1});
            this.toolStrip2.Location = new System.Drawing.Point(0, 49);
            this.toolStrip2.Name = "toolStrip2";
            this.toolStrip2.Size = new System.Drawing.Size(427, 25);
            this.toolStrip2.TabIndex = 4;
            this.toolStrip2.Text = "toolStrip2";
            // 
            // toolStripTextBox1
            // 
            this.toolStripTextBox1.Name = "toolStripTextBox1";
            this.toolStripTextBox1.Size = new System.Drawing.Size(400, 25);
            this.toolStripTextBox1.KeyDown += new System.Windows.Forms.KeyEventHandler(this.toolStripTextBox1_KeyDown);
            // 
            // toolStripLabel1
            // 
            this.toolStripLabel1.Name = "toolStripLabel1";
            this.toolStripLabel1.Size = new System.Drawing.Size(0, 22);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(427, 275);
            this.Controls.Add(this.toolStrip2);
            this.Controls.Add(this.toolStrip1);
            this.Controls.Add(this.webBrowser1);
            this.Controls.Add(this.menuStrip1);
            this.MainMenuStrip = this.menuStrip1;
            this.Name = "Form1";
            this.Text = "製作自己的網路瀏覽軟體";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            this.toolStrip1.ResumeLayout(false);
            this.toolStrip1.PerformLayout();
            this.toolStrip2.ResumeLayout(false);
            this.toolStrip2.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.WebBrowser webBrowser1;
        private System.Windows.Forms.MenuStrip menuStrip1;
        private System.Windows.Forms.ToolStripMenuItem 保存ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 保存DToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem dToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 打印瀏覽UToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 打印PToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 屬性NToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 退出IToolStripMenuItem;
        private System.Windows.Forms.ToolStrip toolStrip1;
        private System.Windows.Forms.ToolStripButton GoaButton;
        private System.Windows.Forms.ToolStripButton backButton;
        private System.Windows.Forms.ToolStripButton forwardButton;
        private System.Windows.Forms.ToolStripButton stopButton;
        private System.Windows.Forms.ToolStripButton refreshButton;
        private System.Windows.Forms.ToolStripButton homeButton;
        private System.Windows.Forms.ToolStripButton searchButton;
        private System.Windows.Forms.ToolStripButton printButton;
        private System.Windows.Forms.ToolStrip toolStrip2;
        private System.Windows.Forms.ToolStripTextBox toolStripTextBox1;
        private System.Windows.Forms.ToolStripLabel toolStripLabel1;
    }
}

