namespace Song
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
        /// 此為設計工具支援所需的方法 - 請勿使用程式碼編輯器修改
        /// 這個方法的內容。
        /// </summary>
        private void InitializeComponent()
        {
            this.btnSortNo = new System.Windows.Forms.Button();
            this.txtMsg = new System.Windows.Forms.TextBox();
            this.txtSinger = new System.Windows.Forms.TextBox();
            this.btnSearch = new System.Windows.Forms.Button();
            this.btnSortSong = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // btnSortNo
            // 
            this.btnSortNo.Location = new System.Drawing.Point(553, 48);
            this.btnSortNo.Name = "btnSortNo";
            this.btnSortNo.Size = new System.Drawing.Size(75, 23);
            this.btnSortNo.TabIndex = 16;
            this.btnSortNo.Text = "依排名排序";
            this.btnSortNo.UseVisualStyleBackColor = true;
            this.btnSortNo.Click += new System.EventHandler(this.btnSortNo_Click);
            // 
            // txtMsg
            // 
            this.txtMsg.Location = new System.Drawing.Point(15, 14);
            this.txtMsg.Multiline = true;
            this.txtMsg.Name = "txtMsg";
            this.txtMsg.ReadOnly = true;
            this.txtMsg.Size = new System.Drawing.Size(507, 418);
            this.txtMsg.TabIndex = 15;
            // 
            // txtSinger
            // 
            this.txtSinger.Location = new System.Drawing.Point(528, 119);
            this.txtSinger.Name = "txtSinger";
            this.txtSinger.Size = new System.Drawing.Size(100, 22);
            this.txtSinger.TabIndex = 14;
            // 
            // btnSearch
            // 
            this.btnSearch.Location = new System.Drawing.Point(553, 90);
            this.btnSearch.Name = "btnSearch";
            this.btnSearch.Size = new System.Drawing.Size(75, 23);
            this.btnSearch.TabIndex = 13;
            this.btnSearch.Text = "查詢歌手";
            this.btnSearch.UseVisualStyleBackColor = true;
            this.btnSearch.Click += new System.EventHandler(this.btnSearch_Click);
            // 
            // btnSortSong
            // 
            this.btnSortSong.Location = new System.Drawing.Point(553, 10);
            this.btnSortSong.Name = "btnSortSong";
            this.btnSortSong.Size = new System.Drawing.Size(75, 23);
            this.btnSortSong.TabIndex = 12;
            this.btnSortSong.Text = "依歌曲排序";
            this.btnSortSong.UseVisualStyleBackColor = true;
            this.btnSortSong.Click += new System.EventHandler(this.btnSortSong_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(650, 491);
            this.Controls.Add(this.btnSortNo);
            this.Controls.Add(this.txtMsg);
            this.Controls.Add(this.txtSinger);
            this.Controls.Add(this.btnSearch);
            this.Controls.Add(this.btnSortSong);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button btnSortNo;
        private System.Windows.Forms.TextBox txtMsg;
        private System.Windows.Forms.TextBox txtSinger;
        private System.Windows.Forms.Button btnSearch;
        private System.Windows.Forms.Button btnSortSong;
    }
}

