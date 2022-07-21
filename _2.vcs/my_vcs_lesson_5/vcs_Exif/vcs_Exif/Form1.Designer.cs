namespace vcs_Exif
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
            this.button1 = new System.Windows.Forms.Button();
            this.listView1 = new System.Windows.Forms.ListView();
            this.columnHeader1 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.columnHeader2 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.columnHeader3 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.columnHeader4 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.columnHeader5 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.bt_clear = new System.Windows.Forms.Button();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.button2 = new System.Windows.Forms.Button();
            this.button3 = new System.Windows.Forms.Button();
            this.button4 = new System.Windows.Forms.Button();
            this.button5 = new System.Windows.Forms.Button();
            this.pictureBox2 = new System.Windows.Forms.PictureBox();
            this.button6 = new System.Windows.Forms.Button();
            this.picOriginal = new System.Windows.Forms.PictureBox();
            this.picOrientation = new System.Windows.Forms.PictureBox();
            this.lblOrientation = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picOriginal)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picOrientation)).BeginInit();
            this.SuspendLayout();
            // 
            // button1
            // 
            this.button1.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button1.Location = new System.Drawing.Point(12, 12);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(111, 88);
            this.button1.TabIndex = 0;
            this.button1.Text = "讀取照片的Exif資料";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // listView1
            // 
            this.listView1.Columns.AddRange(new System.Windows.Forms.ColumnHeader[] {
            this.columnHeader1,
            this.columnHeader2,
            this.columnHeader3,
            this.columnHeader4,
            this.columnHeader5});
            this.listView1.Location = new System.Drawing.Point(827, 12);
            this.listView1.Name = "listView1";
            this.listView1.Size = new System.Drawing.Size(644, 376);
            this.listView1.TabIndex = 1;
            this.listView1.UseCompatibleStateImageBehavior = false;
            this.listView1.View = System.Windows.Forms.View.Details;
            // 
            // columnHeader1
            // 
            this.columnHeader1.Text = "Property";
            this.columnHeader1.Width = 160;
            // 
            // columnHeader2
            // 
            this.columnHeader2.Text = "ID";
            // 
            // columnHeader3
            // 
            this.columnHeader3.Text = "Data Type";
            this.columnHeader3.Width = 170;
            // 
            // columnHeader4
            // 
            this.columnHeader4.Text = "Data Length";
            this.columnHeader4.Width = 80;
            // 
            // columnHeader5
            // 
            this.columnHeader5.Text = "Value";
            this.columnHeader5.Width = 150;
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(828, 394);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(644, 325);
            this.richTextBox1.TabIndex = 2;
            this.richTextBox1.Text = "ListView的用法:\n1. 插入ListView控件\n2. listView1屬性/Columns打開(集合)/ColumnHeader集合編輯器加入5個項目" +
                ",\n   修改顯示文字(Text)及顯示寬度(Width)\n3. listView1屬性/View/改成Details\n \n ";
            // 
            // bt_clear
            // 
            this.bt_clear.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_clear.Location = new System.Drawing.Point(1399, 632);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(73, 44);
            this.bt_clear.TabIndex = 3;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // pictureBox1
            // 
            this.pictureBox1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pictureBox1.Location = new System.Drawing.Point(12, 219);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(400, 500);
            this.pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.pictureBox1.TabIndex = 4;
            this.pictureBox1.TabStop = false;
            // 
            // button2
            // 
            this.button2.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button2.Location = new System.Drawing.Point(129, 12);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(111, 88);
            this.button2.TabIndex = 5;
            this.button2.Text = "讀取照片的拍攝時間";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // button3
            // 
            this.button3.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button3.Location = new System.Drawing.Point(363, 12);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(111, 88);
            this.button3.TabIndex = 6;
            this.button3.Text = "取得圖片的EXIF資料";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // button4
            // 
            this.button4.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button4.Location = new System.Drawing.Point(246, 12);
            this.button4.Name = "button4";
            this.button4.Size = new System.Drawing.Size(111, 88);
            this.button4.TabIndex = 7;
            this.button4.Text = "取得拍照時間";
            this.button4.UseVisualStyleBackColor = true;
            this.button4.Click += new System.EventHandler(this.button4_Click);
            // 
            // button5
            // 
            this.button5.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button5.Location = new System.Drawing.Point(480, 12);
            this.button5.Name = "button5";
            this.button5.Size = new System.Drawing.Size(111, 88);
            this.button5.TabIndex = 8;
            this.button5.Text = "取得圖片的EXIF資料";
            this.button5.UseVisualStyleBackColor = true;
            this.button5.Click += new System.EventHandler(this.button5_Click);
            // 
            // pictureBox2
            // 
            this.pictureBox2.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pictureBox2.Location = new System.Drawing.Point(418, 219);
            this.pictureBox2.Name = "pictureBox2";
            this.pictureBox2.Size = new System.Drawing.Size(400, 500);
            this.pictureBox2.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.pictureBox2.TabIndex = 9;
            this.pictureBox2.TabStop = false;
            // 
            // button6
            // 
            this.button6.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button6.Location = new System.Drawing.Point(301, 119);
            this.button6.Name = "button6";
            this.button6.Size = new System.Drawing.Size(111, 88);
            this.button6.TabIndex = 10;
            this.button6.Text = "檢查圖片的方向";
            this.button6.UseVisualStyleBackColor = true;
            this.button6.Click += new System.EventHandler(this.button6_Click);
            // 
            // picOriginal
            // 
            this.picOriginal.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.picOriginal.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picOriginal.Location = new System.Drawing.Point(561, 119);
            this.picOriginal.Name = "picOriginal";
            this.picOriginal.Size = new System.Drawing.Size(114, 97);
            this.picOriginal.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.picOriginal.TabIndex = 26;
            this.picOriginal.TabStop = false;
            // 
            // picOrientation
            // 
            this.picOrientation.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.picOrientation.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picOrientation.Location = new System.Drawing.Point(681, 119);
            this.picOrientation.Name = "picOrientation";
            this.picOrientation.Size = new System.Drawing.Size(121, 97);
            this.picOrientation.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.picOrientation.TabIndex = 25;
            this.picOrientation.TabStop = false;
            // 
            // lblOrientation
            // 
            this.lblOrientation.Font = new System.Drawing.Font("Microsoft Sans Serif", 16F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblOrientation.Location = new System.Drawing.Point(435, 135);
            this.lblOrientation.Name = "lblOrientation";
            this.lblOrientation.Size = new System.Drawing.Size(120, 59);
            this.lblOrientation.TabIndex = 24;
            this.lblOrientation.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label3.Location = new System.Drawing.Point(26, 128);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(430, 24);
            this.label3.TabIndex = 27;
            this.label3.Text = "取得圖片內的方向值, 自動轉換圖片方向";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label2.Location = new System.Drawing.Point(421, 186);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(78, 24);
            this.label2.TabIndex = 29;
            this.label2.Text = "Orinted";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label1.Location = new System.Drawing.Point(26, 186);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(58, 24);
            this.label1.TabIndex = 28;
            this.label1.Text = "原圖";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1484, 731);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.picOriginal);
            this.Controls.Add(this.picOrientation);
            this.Controls.Add(this.lblOrientation);
            this.Controls.Add(this.button6);
            this.Controls.Add(this.pictureBox2);
            this.Controls.Add(this.button5);
            this.Controls.Add(this.button4);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.listView1);
            this.Controls.Add(this.button1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picOriginal)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picOrientation)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.ListView listView1;
        private System.Windows.Forms.ColumnHeader columnHeader1;
        private System.Windows.Forms.ColumnHeader columnHeader2;
        private System.Windows.Forms.ColumnHeader columnHeader3;
        private System.Windows.Forms.ColumnHeader columnHeader4;
        private System.Windows.Forms.ColumnHeader columnHeader5;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.Button button4;
        private System.Windows.Forms.Button button5;
        private System.Windows.Forms.PictureBox pictureBox2;
        private System.Windows.Forms.Button button6;
        private System.Windows.Forms.PictureBox picOriginal;
        private System.Windows.Forms.PictureBox picOrientation;
        private System.Windows.Forms.Label lblOrientation;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label1;
    }
}

