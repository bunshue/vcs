namespace vcs_ListBox8
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
            this.drawListBox1 = new vcs_ListBox8.DrawListBox();
            this.drawListBox2 = new vcs_ListBox8.DrawListBox();
            this.SuspendLayout();
            // 
            // drawListBox1
            // 
            this.drawListBox1.Color1 = System.Drawing.Color.CornflowerBlue;
            this.drawListBox1.Color1Gradual = System.Drawing.Color.Thistle;
            this.drawListBox1.Color2 = System.Drawing.Color.PaleGreen;
            this.drawListBox1.Color2Gradual = System.Drawing.Color.DarkKhaki;
            this.drawListBox1.ColorSelect = System.Drawing.Color.Gainsboro;
            this.drawListBox1.DrawMode = System.Windows.Forms.DrawMode.OwnerDrawFixed;
            this.drawListBox1.FormattingEnabled = true;
            this.drawListBox1.GradualC = false;
            this.drawListBox1.Items.AddRange(new object[] {
            "杜牧．秋夕",
            "杜牧．赤壁",
            "杜牧．題烏江亭",
            "杜牧．山行",
            "李煜．相見歡",
            "李煜．浪淘沙令",
            "周邦彥．少年遊",
            "周邦彥．蘇幕遮",
            "蘇軾．江城子",
            "蘇軾．江城子",
            "蘇軾．蝶戀花",
            "柳永．望海潮",
            "柳永．雨霖鈴",
            "辛棄疾．西江月",
            "辛棄疾．青玉案",
            "辛棄疾．南鄉子"});
            this.drawListBox1.Location = new System.Drawing.Point(12, 12);
            this.drawListBox1.Name = "drawListBox1";
            this.drawListBox1.Size = new System.Drawing.Size(529, 485);
            this.drawListBox1.TabIndex = 1;
            // 
            // drawListBox2
            // 
            this.drawListBox2.Color1 = System.Drawing.Color.CornflowerBlue;
            this.drawListBox2.Color1Gradual = System.Drawing.Color.Thistle;
            this.drawListBox2.Color2 = System.Drawing.Color.PaleGreen;
            this.drawListBox2.Color2Gradual = System.Drawing.Color.DarkKhaki;
            this.drawListBox2.ColorSelect = System.Drawing.Color.Gainsboro;
            this.drawListBox2.DrawMode = System.Windows.Forms.DrawMode.OwnerDrawFixed;
            this.drawListBox2.FormattingEnabled = true;
            this.drawListBox2.GradualC = false;
            this.drawListBox2.Location = new System.Drawing.Point(547, 15);
            this.drawListBox2.Name = "drawListBox2";
            this.drawListBox2.Size = new System.Drawing.Size(434, 485);
            this.drawListBox2.TabIndex = 0;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1066, 512);
            this.Controls.Add(this.drawListBox1);
            this.Controls.Add(this.drawListBox2);
            this.Name = "Form1";
            this.Text = "ListBox用多顏色背景表示";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);

        }

        #endregion

        private DrawListBox drawListBox2;
        private DrawListBox drawListBox1;

    }
}

