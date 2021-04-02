namespace BindingXMLToTreeView
{
    partial class BindingXMLToTreeView
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
            this.treeView1 = new System.Windows.Forms.TreeView();
            this.switchOn = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // treeView1
            // 
            this.treeView1.Location = new System.Drawing.Point(4, 5);
            this.treeView1.Name = "treeView1";
            this.treeView1.Size = new System.Drawing.Size(346, 231);
            this.treeView1.TabIndex = 0;
            this.treeView1.AfterSelect += new System.Windows.Forms.TreeViewEventHandler(this.treeView1_AfterSelect);
            // 
            // switchOn
            // 
            this.switchOn.Location = new System.Drawing.Point(280, 242);
            this.switchOn.Name = "switchOn";
            this.switchOn.Size = new System.Drawing.Size(51, 23);
            this.switchOn.TabIndex = 1;
            this.switchOn.Text = "打開";
            this.switchOn.UseVisualStyleBackColor = true;
            this.switchOn.Click += new System.EventHandler(this.switchOn_Click);
            // 
            // BindingXMLToTreeView
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(362, 270);
            this.Controls.Add(this.switchOn);
            this.Controls.Add(this.treeView1);
            this.Name = "BindingXMLToTreeView";
            this.Text = "將XML文件節點綁定到TreeView控制元件中";
            this.Load += new System.EventHandler(this.BindingXMLToTreeView_Load);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.TreeView treeView1;
        private System.Windows.Forms.Button switchOn;
    }
}

