namespace PaginationFunction
{
    partial class PaginationFunction
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
            this.ListData = new System.Windows.Forms.DataGridView();
            this.Column1 = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.Column2 = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.Column3 = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.LastPage = new System.Windows.Forms.Button();
            this.NextPage = new System.Windows.Forms.Button();
            this.PreviousPage = new System.Windows.Forms.Button();
            this.FistPage = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.ListData)).BeginInit();
            this.groupBox1.SuspendLayout();
            this.SuspendLayout();
            // 
            // ListData
            // 
            this.ListData.AllowUserToAddRows = false;
            this.ListData.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.ListData.Columns.AddRange(new System.Windows.Forms.DataGridViewColumn[] {
            this.Column1,
            this.Column2,
            this.Column3});
            this.ListData.Location = new System.Drawing.Point(4, 3);
            this.ListData.Name = "ListData";
            this.ListData.RowTemplate.Height = 23;
            this.ListData.Size = new System.Drawing.Size(431, 226);
            this.ListData.TabIndex = 0;
            // 
            // Column1
            // 
            this.Column1.HeaderText = "用戶編號";
            this.Column1.Name = "Column1";
            // 
            // Column2
            // 
            this.Column2.HeaderText = "用戶姓名";
            this.Column2.Name = "Column2";
            // 
            // Column3
            // 
            this.Column3.HeaderText = "工作時間";
            this.Column3.Name = "Column3";
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.LastPage);
            this.groupBox1.Controls.Add(this.NextPage);
            this.groupBox1.Controls.Add(this.PreviousPage);
            this.groupBox1.Controls.Add(this.FistPage);
            this.groupBox1.Location = new System.Drawing.Point(4, 235);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(431, 80);
            this.groupBox1.TabIndex = 1;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "操作類型";
            // 
            // LastPage
            // 
            this.LastPage.Location = new System.Drawing.Point(318, 34);
            this.LastPage.Name = "LastPage";
            this.LastPage.Size = new System.Drawing.Size(75, 23);
            this.LastPage.TabIndex = 0;
            this.LastPage.Text = "尾頁";
            this.LastPage.UseVisualStyleBackColor = true;
            this.LastPage.Click += new System.EventHandler(this.LastPage_Click);
            // 
            // NextPage
            // 
            this.NextPage.Location = new System.Drawing.Point(212, 34);
            this.NextPage.Name = "NextPage";
            this.NextPage.Size = new System.Drawing.Size(75, 23);
            this.NextPage.TabIndex = 0;
            this.NextPage.Text = "下一頁";
            this.NextPage.UseVisualStyleBackColor = true;
            this.NextPage.Click += new System.EventHandler(this.nextpage_Click);
            // 
            // PreviousPage
            // 
            this.PreviousPage.Location = new System.Drawing.Point(120, 34);
            this.PreviousPage.Name = "PreviousPage";
            this.PreviousPage.Size = new System.Drawing.Size(75, 23);
            this.PreviousPage.TabIndex = 0;
            this.PreviousPage.Text = "上一頁";
            this.PreviousPage.UseVisualStyleBackColor = true;
            this.PreviousPage.Click += new System.EventHandler(this.PreviousPage_Click);
            // 
            // FistPage
            // 
            this.FistPage.Location = new System.Drawing.Point(23, 34);
            this.FistPage.Name = "FistPage";
            this.FistPage.Size = new System.Drawing.Size(75, 23);
            this.FistPage.TabIndex = 0;
            this.FistPage.Text = "首頁";
            this.FistPage.UseVisualStyleBackColor = true;
            this.FistPage.Click += new System.EventHandler(this.fistpage_Click);
            // 
            // PaginationFunction
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(618, 565);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.ListData);
            this.Name = "PaginationFunction";
            this.Text = "完成DataGridView控制元件的分頁功能";
            this.Load += new System.EventHandler(this.PaginationFunction_Load);
            ((System.ComponentModel.ISupportInitialize)(this.ListData)).EndInit();
            this.groupBox1.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.DataGridView ListData;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.Button LastPage;
        private System.Windows.Forms.Button NextPage;
        private System.Windows.Forms.Button PreviousPage;
        private System.Windows.Forms.Button FistPage;
        private System.Windows.Forms.DataGridViewTextBoxColumn Column1;
        private System.Windows.Forms.DataGridViewTextBoxColumn Column2;
        private System.Windows.Forms.DataGridViewTextBoxColumn Column3;
    }
}

