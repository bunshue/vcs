namespace WinMouseEvent
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
            this.menuStrip1 = new System.Windows.Forms.MenuStrip();
            this.檔案ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.開檔ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.存檔ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.清除ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.結束ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.畫筆粗細ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.pixelsToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.pixelsToolStripMenuItem1 = new System.Windows.Forms.ToolStripMenuItem();
            this.pixelsToolStripMenuItem2 = new System.Windows.Forms.ToolStripMenuItem();
            this.pixelsToolStripMenuItem3 = new System.Windows.Forms.ToolStripMenuItem();
            this.pixelsToolStripMenuItem4 = new System.Windows.Forms.ToolStripMenuItem();
            this.畫筆顏色ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.黑ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.紅ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.綠ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.藍ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.button1 = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.button2 = new System.Windows.Forms.Button();
            this.openFileDialog1 = new System.Windows.Forms.OpenFileDialog();
            this.button3 = new System.Windows.Forms.Button();
            this.saveFileDialog1 = new System.Windows.Forms.SaveFileDialog();
            this.menuStrip1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // menuStrip1
            // 
            this.menuStrip1.Font = new System.Drawing.Font("微軟正黑體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.檔案ToolStripMenuItem,
            this.畫筆粗細ToolStripMenuItem,
            this.畫筆顏色ToolStripMenuItem});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Padding = new System.Windows.Forms.Padding(8, 2, 0, 2);
            this.menuStrip1.Size = new System.Drawing.Size(925, 28);
            this.menuStrip1.TabIndex = 0;
            this.menuStrip1.Text = "menuStrip1";
            // 
            // 檔案ToolStripMenuItem
            // 
            this.檔案ToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.開檔ToolStripMenuItem,
            this.存檔ToolStripMenuItem,
            this.清除ToolStripMenuItem,
            this.結束ToolStripMenuItem});
            this.檔案ToolStripMenuItem.Name = "檔案ToolStripMenuItem";
            this.檔案ToolStripMenuItem.Size = new System.Drawing.Size(53, 24);
            this.檔案ToolStripMenuItem.Text = "檔案";
            // 
            // 開檔ToolStripMenuItem
            // 
            this.開檔ToolStripMenuItem.Name = "開檔ToolStripMenuItem";
            this.開檔ToolStripMenuItem.Size = new System.Drawing.Size(152, 24);
            this.開檔ToolStripMenuItem.Text = "開檔";
            this.開檔ToolStripMenuItem.Click += new System.EventHandler(this.開檔ToolStripMenuItem_Click);
            // 
            // 存檔ToolStripMenuItem
            // 
            this.存檔ToolStripMenuItem.Name = "存檔ToolStripMenuItem";
            this.存檔ToolStripMenuItem.Size = new System.Drawing.Size(152, 24);
            this.存檔ToolStripMenuItem.Text = "存檔";
            this.存檔ToolStripMenuItem.Click += new System.EventHandler(this.存檔ToolStripMenuItem_Click);
            // 
            // 清除ToolStripMenuItem
            // 
            this.清除ToolStripMenuItem.Name = "清除ToolStripMenuItem";
            this.清除ToolStripMenuItem.Size = new System.Drawing.Size(152, 24);
            this.清除ToolStripMenuItem.Text = "清除";
            this.清除ToolStripMenuItem.Click += new System.EventHandler(this.清除ToolStripMenuItem_Click);
            // 
            // 結束ToolStripMenuItem
            // 
            this.結束ToolStripMenuItem.Name = "結束ToolStripMenuItem";
            this.結束ToolStripMenuItem.Size = new System.Drawing.Size(152, 24);
            this.結束ToolStripMenuItem.Text = "結束";
            this.結束ToolStripMenuItem.Click += new System.EventHandler(this.結束ToolStripMenuItem_Click);
            // 
            // 畫筆粗細ToolStripMenuItem
            // 
            this.畫筆粗細ToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.pixelsToolStripMenuItem,
            this.pixelsToolStripMenuItem1,
            this.pixelsToolStripMenuItem2,
            this.pixelsToolStripMenuItem3,
            this.pixelsToolStripMenuItem4});
            this.畫筆粗細ToolStripMenuItem.Name = "畫筆粗細ToolStripMenuItem";
            this.畫筆粗細ToolStripMenuItem.Size = new System.Drawing.Size(85, 24);
            this.畫筆粗細ToolStripMenuItem.Text = "畫筆粗細";
            // 
            // pixelsToolStripMenuItem
            // 
            this.pixelsToolStripMenuItem.Name = "pixelsToolStripMenuItem";
            this.pixelsToolStripMenuItem.Size = new System.Drawing.Size(142, 24);
            this.pixelsToolStripMenuItem.Text = "1 Pixels";
            this.pixelsToolStripMenuItem.Click += new System.EventHandler(this.pixelsToolStripMenuItem_Click);
            // 
            // pixelsToolStripMenuItem1
            // 
            this.pixelsToolStripMenuItem1.Name = "pixelsToolStripMenuItem1";
            this.pixelsToolStripMenuItem1.Size = new System.Drawing.Size(142, 24);
            this.pixelsToolStripMenuItem1.Text = "3 Pixels";
            this.pixelsToolStripMenuItem1.Click += new System.EventHandler(this.pixelsToolStripMenuItem1_Click);
            // 
            // pixelsToolStripMenuItem2
            // 
            this.pixelsToolStripMenuItem2.Name = "pixelsToolStripMenuItem2";
            this.pixelsToolStripMenuItem2.Size = new System.Drawing.Size(142, 24);
            this.pixelsToolStripMenuItem2.Text = "5 Pixels";
            this.pixelsToolStripMenuItem2.Click += new System.EventHandler(this.pixelsToolStripMenuItem2_Click);
            // 
            // pixelsToolStripMenuItem3
            // 
            this.pixelsToolStripMenuItem3.Name = "pixelsToolStripMenuItem3";
            this.pixelsToolStripMenuItem3.Size = new System.Drawing.Size(142, 24);
            this.pixelsToolStripMenuItem3.Text = "7 Pixels";
            this.pixelsToolStripMenuItem3.Click += new System.EventHandler(this.pixelsToolStripMenuItem3_Click);
            // 
            // pixelsToolStripMenuItem4
            // 
            this.pixelsToolStripMenuItem4.Name = "pixelsToolStripMenuItem4";
            this.pixelsToolStripMenuItem4.Size = new System.Drawing.Size(142, 24);
            this.pixelsToolStripMenuItem4.Text = "10 Pixels";
            this.pixelsToolStripMenuItem4.Click += new System.EventHandler(this.pixelsToolStripMenuItem4_Click);
            // 
            // 畫筆顏色ToolStripMenuItem
            // 
            this.畫筆顏色ToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.黑ToolStripMenuItem,
            this.紅ToolStripMenuItem,
            this.綠ToolStripMenuItem,
            this.藍ToolStripMenuItem});
            this.畫筆顏色ToolStripMenuItem.Name = "畫筆顏色ToolStripMenuItem";
            this.畫筆顏色ToolStripMenuItem.Size = new System.Drawing.Size(85, 24);
            this.畫筆顏色ToolStripMenuItem.Text = "畫筆顏色";
            // 
            // 黑ToolStripMenuItem
            // 
            this.黑ToolStripMenuItem.Name = "黑ToolStripMenuItem";
            this.黑ToolStripMenuItem.Size = new System.Drawing.Size(94, 24);
            this.黑ToolStripMenuItem.Text = "黑";
            this.黑ToolStripMenuItem.Click += new System.EventHandler(this.黑ToolStripMenuItem_Click);
            // 
            // 紅ToolStripMenuItem
            // 
            this.紅ToolStripMenuItem.Name = "紅ToolStripMenuItem";
            this.紅ToolStripMenuItem.Size = new System.Drawing.Size(94, 24);
            this.紅ToolStripMenuItem.Text = "紅";
            this.紅ToolStripMenuItem.Click += new System.EventHandler(this.紅ToolStripMenuItem_Click);
            // 
            // 綠ToolStripMenuItem
            // 
            this.綠ToolStripMenuItem.Name = "綠ToolStripMenuItem";
            this.綠ToolStripMenuItem.Size = new System.Drawing.Size(94, 24);
            this.綠ToolStripMenuItem.Text = "綠";
            this.綠ToolStripMenuItem.Click += new System.EventHandler(this.綠ToolStripMenuItem_Click);
            // 
            // 藍ToolStripMenuItem
            // 
            this.藍ToolStripMenuItem.Name = "藍ToolStripMenuItem";
            this.藍ToolStripMenuItem.Size = new System.Drawing.Size(94, 24);
            this.藍ToolStripMenuItem.Text = "藍";
            this.藍ToolStripMenuItem.Click += new System.EventHandler(this.藍ToolStripMenuItem_Click);
            // 
            // pictureBox1
            // 
            this.pictureBox1.Location = new System.Drawing.Point(7, 40);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(779, 550);
            this.pictureBox1.TabIndex = 1;
            this.pictureBox1.TabStop = false;
            this.pictureBox1.MouseDown += new System.Windows.Forms.MouseEventHandler(this.pictureBox1_MouseDown);
            this.pictureBox1.MouseMove += new System.Windows.Forms.MouseEventHandler(this.pictureBox1_MouseMove);
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(807, 40);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(75, 23);
            this.button1.TabIndex = 2;
            this.button1.Text = "button1";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(807, 196);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(100, 394);
            this.richTextBox1.TabIndex = 3;
            this.richTextBox1.Text = "";
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(807, 78);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(75, 23);
            this.button2.TabIndex = 4;
            this.button2.Text = "button2";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // openFileDialog1
            // 
            this.openFileDialog1.FileName = "openFileDialog1";
            // 
            // button3
            // 
            this.button3.Location = new System.Drawing.Point(807, 116);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(75, 23);
            this.button3.TabIndex = 5;
            this.button3.Text = "button3";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(925, 602);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.menuStrip1);
            this.Font = new System.Drawing.Font("新細明體", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.MainMenuStrip = this.menuStrip1;
            this.Margin = new System.Windows.Forms.Padding(4);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.MenuStrip menuStrip1;
        private System.Windows.Forms.ToolStripMenuItem 檔案ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 開檔ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 存檔ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 清除ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 結束ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 畫筆粗細ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem pixelsToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem pixelsToolStripMenuItem1;
        private System.Windows.Forms.ToolStripMenuItem pixelsToolStripMenuItem2;
        private System.Windows.Forms.ToolStripMenuItem 畫筆顏色ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 黑ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 紅ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 綠ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 藍ToolStripMenuItem;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.ToolStripMenuItem pixelsToolStripMenuItem3;
        private System.Windows.Forms.ToolStripMenuItem pixelsToolStripMenuItem4;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.OpenFileDialog openFileDialog1;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.SaveFileDialog saveFileDialog1;
    }
}

