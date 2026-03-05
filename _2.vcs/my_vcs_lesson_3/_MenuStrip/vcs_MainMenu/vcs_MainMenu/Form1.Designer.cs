namespace vcs_MainMenu
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
            this.components = new System.ComponentModel.Container();
            this.mnuMain = new System.Windows.Forms.MainMenu(this.components);
            this.MenuItem1 = new System.Windows.Forms.MenuItem();
            this.mnuFileSayHi = new System.Windows.Forms.MenuItem();
            this.mnuFileExit = new System.Windows.Forms.MenuItem();
            this.SuspendLayout();
            // 
            // mnuMain
            // 
            this.mnuMain.MenuItems.AddRange(new System.Windows.Forms.MenuItem[] {
            this.MenuItem1});
            // 
            // MenuItem1
            // 
            this.MenuItem1.Index = 0;
            this.MenuItem1.MenuItems.AddRange(new System.Windows.Forms.MenuItem[] {
            this.mnuFileSayHi,
            this.mnuFileExit});
            this.MenuItem1.Text = "&File";
            // 
            // mnuFileSayHi
            // 
            this.mnuFileSayHi.Index = 0;
            this.mnuFileSayHi.OwnerDraw = true;
            this.mnuFileSayHi.Text = "SayHi";
            this.mnuFileSayHi.Click += new System.EventHandler(this.mnuFileSayHi_Click);
            this.mnuFileSayHi.DrawItem += new System.Windows.Forms.DrawItemEventHandler(this.mnuFileSayHi_DrawItem);
            this.mnuFileSayHi.MeasureItem += new System.Windows.Forms.MeasureItemEventHandler(this.mnuFileSayHi_MeasureItem);
            // 
            // mnuFileExit
            // 
            this.mnuFileExit.Index = 1;
            this.mnuFileExit.Text = "E&xit";
            this.mnuFileExit.Click += new System.EventHandler(this.mnuFileExit_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(777, 514);
            this.Menu = this.mnuMain;
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);

        }

        #endregion

        internal System.Windows.Forms.MainMenu mnuMain;
        internal System.Windows.Forms.MenuItem MenuItem1;
        internal System.Windows.Forms.MenuItem mnuFileSayHi;
        internal System.Windows.Forms.MenuItem mnuFileExit;
    }
}

