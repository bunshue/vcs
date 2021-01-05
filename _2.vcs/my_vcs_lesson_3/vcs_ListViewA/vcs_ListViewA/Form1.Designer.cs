namespace vcs_ListViewA
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
            this.listView1 = new System.Windows.Forms.ListView();
            this.btnSizeMinus2 = new System.Windows.Forms.Button();
            this.btnSizeMinus1 = new System.Windows.Forms.Button();
            this.btnSize100 = new System.Windows.Forms.Button();
            this.txtColumn = new System.Windows.Forms.TextBox();
            this.Label2 = new System.Windows.Forms.Label();
            this.txtRow = new System.Windows.Forms.TextBox();
            this.Label1 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // listView1
            // 
            this.listView1.Location = new System.Drawing.Point(3, 3);
            this.listView1.Name = "listView1";
            this.listView1.Size = new System.Drawing.Size(997, 251);
            this.listView1.TabIndex = 0;
            this.listView1.UseCompatibleStateImageBehavior = false;
            this.listView1.MouseMove += new System.Windows.Forms.MouseEventHandler(this.listView1_MouseMove);
            // 
            // btnSizeMinus2
            // 
            this.btnSizeMinus2.Location = new System.Drawing.Point(193, 290);
            this.btnSizeMinus2.Name = "btnSizeMinus2";
            this.btnSizeMinus2.Size = new System.Drawing.Size(75, 21);
            this.btnSizeMinus2.TabIndex = 7;
            this.btnSizeMinus2.Text = "Size = -2";
            this.btnSizeMinus2.UseVisualStyleBackColor = true;
            this.btnSizeMinus2.Click += new System.EventHandler(this.btnSizeMinus2_Click);
            // 
            // btnSizeMinus1
            // 
            this.btnSizeMinus1.Location = new System.Drawing.Point(98, 290);
            this.btnSizeMinus1.Name = "btnSizeMinus1";
            this.btnSizeMinus1.Size = new System.Drawing.Size(75, 21);
            this.btnSizeMinus1.TabIndex = 6;
            this.btnSizeMinus1.Text = "Size = -1";
            this.btnSizeMinus1.UseVisualStyleBackColor = true;
            this.btnSizeMinus1.Click += new System.EventHandler(this.btnSizeMinus1_Click);
            // 
            // btnSize100
            // 
            this.btnSize100.Location = new System.Drawing.Point(3, 290);
            this.btnSize100.Name = "btnSize100";
            this.btnSize100.Size = new System.Drawing.Size(75, 21);
            this.btnSize100.TabIndex = 5;
            this.btnSize100.Text = "Size = 100";
            this.btnSize100.UseVisualStyleBackColor = true;
            this.btnSize100.Click += new System.EventHandler(this.btnSize100_Click);
            // 
            // txtColumn
            // 
            this.txtColumn.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.txtColumn.Location = new System.Drawing.Point(433, 291);
            this.txtColumn.Name = "txtColumn";
            this.txtColumn.Size = new System.Drawing.Size(32, 22);
            this.txtColumn.TabIndex = 18;
            this.txtColumn.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // Label2
            // 
            this.Label2.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.Label2.AutoSize = true;
            this.Label2.Location = new System.Drawing.Point(385, 294);
            this.Label2.Name = "Label2";
            this.Label2.Size = new System.Drawing.Size(46, 12);
            this.Label2.TabIndex = 17;
            this.Label2.Text = "Column:";
            // 
            // txtRow
            // 
            this.txtRow.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.txtRow.Location = new System.Drawing.Point(337, 291);
            this.txtRow.Name = "txtRow";
            this.txtRow.Size = new System.Drawing.Size(32, 22);
            this.txtRow.TabIndex = 16;
            this.txtRow.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // Label1
            // 
            this.Label1.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.Label1.AutoSize = true;
            this.Label1.Location = new System.Drawing.Point(305, 294);
            this.Label1.Name = "Label1";
            this.Label1.Size = new System.Drawing.Size(30, 12);
            this.Label1.TabIndex = 15;
            this.Label1.Text = "Row:";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1003, 334);
            this.Controls.Add(this.txtColumn);
            this.Controls.Add(this.Label2);
            this.Controls.Add(this.txtRow);
            this.Controls.Add(this.Label1);
            this.Controls.Add(this.btnSizeMinus2);
            this.Controls.Add(this.btnSizeMinus1);
            this.Controls.Add(this.btnSize100);
            this.Controls.Add(this.listView1);
            this.Name = "Form1";
            this.Text = "Array資料填到ListView";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.ListView listView1;
        private System.Windows.Forms.Button btnSizeMinus2;
        private System.Windows.Forms.Button btnSizeMinus1;
        private System.Windows.Forms.Button btnSize100;
        internal System.Windows.Forms.TextBox txtColumn;
        internal System.Windows.Forms.Label Label2;
        internal System.Windows.Forms.TextBox txtRow;
        internal System.Windows.Forms.Label Label1;
    }
}

