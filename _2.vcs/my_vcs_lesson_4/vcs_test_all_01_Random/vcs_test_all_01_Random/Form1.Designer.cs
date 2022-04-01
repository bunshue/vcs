namespace vcs_test_all_01_Random
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
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.bt_random_text1 = new System.Windows.Forms.Button();
            this.bt_random12 = new System.Windows.Forms.Button();
            this.bt_random_color = new System.Windows.Forms.Button();
            this.groupBox4 = new System.Windows.Forms.GroupBox();
            this.label4 = new System.Windows.Forms.Label();
            this.btnRandomize = new System.Windows.Forms.Button();
            this.lstArray = new System.Windows.Forms.ListBox();
            this.lstList = new System.Windows.Forms.ListBox();
            this.groupBox3 = new System.Windows.Forms.GroupBox();
            this.button31 = new System.Windows.Forms.Button();
            this.txtResult = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.btnPick = new System.Windows.Forms.Button();
            this.txtNames = new System.Windows.Forms.TextBox();
            this.bt_random11 = new System.Windows.Forms.Button();
            this.bt_random10 = new System.Windows.Forms.Button();
            this.bt_random9 = new System.Windows.Forms.Button();
            this.bt_random8 = new System.Windows.Forms.Button();
            this.bt_random7 = new System.Windows.Forms.Button();
            this.bt_random2 = new System.Windows.Forms.Button();
            this.bt_random6 = new System.Windows.Forms.Button();
            this.bt_random5 = new System.Windows.Forms.Button();
            this.bt_random4 = new System.Windows.Forms.Button();
            this.bt_random3 = new System.Windows.Forms.Button();
            this.bt_random1 = new System.Windows.Forms.Button();
            this.bt_clear = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.button1 = new System.Windows.Forms.Button();
            this.groupBox1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.groupBox4.SuspendLayout();
            this.groupBox3.SuspendLayout();
            this.SuspendLayout();
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.button1);
            this.groupBox1.Controls.Add(this.pictureBox1);
            this.groupBox1.Controls.Add(this.bt_random_text1);
            this.groupBox1.Controls.Add(this.bt_random12);
            this.groupBox1.Controls.Add(this.bt_random_color);
            this.groupBox1.Controls.Add(this.groupBox4);
            this.groupBox1.Controls.Add(this.groupBox3);
            this.groupBox1.Controls.Add(this.bt_random11);
            this.groupBox1.Controls.Add(this.bt_random10);
            this.groupBox1.Controls.Add(this.bt_random9);
            this.groupBox1.Controls.Add(this.bt_random8);
            this.groupBox1.Controls.Add(this.bt_random7);
            this.groupBox1.Controls.Add(this.bt_random2);
            this.groupBox1.Controls.Add(this.bt_random6);
            this.groupBox1.Controls.Add(this.bt_random5);
            this.groupBox1.Controls.Add(this.bt_random4);
            this.groupBox1.Controls.Add(this.bt_random3);
            this.groupBox1.Controls.Add(this.bt_random1);
            this.groupBox1.Location = new System.Drawing.Point(12, 12);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(832, 875);
            this.groupBox1.TabIndex = 27;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "亂數";
            // 
            // pictureBox1
            // 
            this.pictureBox1.BackColor = System.Drawing.Color.LightGray;
            this.pictureBox1.Location = new System.Drawing.Point(598, 21);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(50, 50);
            this.pictureBox1.TabIndex = 47;
            this.pictureBox1.TabStop = false;
            this.pictureBox1.Paint += new System.Windows.Forms.PaintEventHandler(this.pictureBox1_Paint);
            // 
            // bt_random_text1
            // 
            this.bt_random_text1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_random_text1.Location = new System.Drawing.Point(17, 342);
            this.bt_random_text1.Name = "bt_random_text1";
            this.bt_random_text1.Size = new System.Drawing.Size(321, 40);
            this.bt_random_text1.TabIndex = 37;
            this.bt_random_text1.Text = "隨機文字";
            this.bt_random_text1.UseVisualStyleBackColor = true;
            this.bt_random_text1.Click += new System.EventHandler(this.bt_random_text1_Click);
            // 
            // bt_random12
            // 
            this.bt_random12.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_random12.Location = new System.Drawing.Point(183, 296);
            this.bt_random12.Name = "bt_random12";
            this.bt_random12.Size = new System.Drawing.Size(155, 40);
            this.bt_random12.TabIndex = 36;
            this.bt_random12.Text = "亂數方法比較";
            this.bt_random12.UseVisualStyleBackColor = true;
            this.bt_random12.Click += new System.EventHandler(this.bt_random12_Click);
            // 
            // bt_random_color
            // 
            this.bt_random_color.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_random_color.Location = new System.Drawing.Point(17, 296);
            this.bt_random_color.Name = "bt_random_color";
            this.bt_random_color.Size = new System.Drawing.Size(155, 40);
            this.bt_random_color.TabIndex = 35;
            this.bt_random_color.Text = "隨機顏色";
            this.bt_random_color.UseVisualStyleBackColor = true;
            this.bt_random_color.Click += new System.EventHandler(this.bt_random_color_Click);
            // 
            // groupBox4
            // 
            this.groupBox4.Controls.Add(this.label4);
            this.groupBox4.Controls.Add(this.btnRandomize);
            this.groupBox4.Controls.Add(this.lstArray);
            this.groupBox4.Controls.Add(this.lstList);
            this.groupBox4.Location = new System.Drawing.Point(17, 441);
            this.groupBox4.Name = "groupBox4";
            this.groupBox4.Size = new System.Drawing.Size(321, 182);
            this.groupBox4.TabIndex = 34;
            this.groupBox4.TabStop = false;
            this.groupBox4.Text = "任意陣列";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label4.Location = new System.Drawing.Point(74, 12);
            this.label4.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(155, 16);
            this.label4.TabIndex = 44;
            this.label4.Text = "Array                      List";
            // 
            // btnRandomize
            // 
            this.btnRandomize.Location = new System.Drawing.Point(115, 154);
            this.btnRandomize.Name = "btnRandomize";
            this.btnRandomize.Size = new System.Drawing.Size(75, 21);
            this.btnRandomize.TabIndex = 7;
            this.btnRandomize.Text = "Randomize";
            this.btnRandomize.UseVisualStyleBackColor = true;
            // 
            // lstArray
            // 
            this.lstArray.FormattingEnabled = true;
            this.lstArray.IntegralHeight = false;
            this.lstArray.ItemHeight = 12;
            this.lstArray.Location = new System.Drawing.Point(14, 30);
            this.lstArray.Name = "lstArray";
            this.lstArray.Size = new System.Drawing.Size(140, 120);
            this.lstArray.TabIndex = 5;
            // 
            // lstList
            // 
            this.lstList.FormattingEnabled = true;
            this.lstList.IntegralHeight = false;
            this.lstList.ItemHeight = 12;
            this.lstList.Location = new System.Drawing.Point(162, 30);
            this.lstList.Name = "lstList";
            this.lstList.Size = new System.Drawing.Size(140, 120);
            this.lstList.TabIndex = 6;
            // 
            // groupBox3
            // 
            this.groupBox3.Controls.Add(this.button31);
            this.groupBox3.Controls.Add(this.txtResult);
            this.groupBox3.Controls.Add(this.label3);
            this.groupBox3.Controls.Add(this.btnPick);
            this.groupBox3.Controls.Add(this.txtNames);
            this.groupBox3.Location = new System.Drawing.Point(45, 629);
            this.groupBox3.Name = "groupBox3";
            this.groupBox3.Size = new System.Drawing.Size(258, 170);
            this.groupBox3.TabIndex = 33;
            this.groupBox3.TabStop = false;
            this.groupBox3.Text = "選幾個";
            // 
            // button31
            // 
            this.button31.Location = new System.Drawing.Point(165, 54);
            this.button31.Name = "button31";
            this.button31.Size = new System.Drawing.Size(75, 21);
            this.button31.TabIndex = 8;
            this.button31.Text = "選5個";
            this.button31.UseVisualStyleBackColor = true;
            // 
            // txtResult
            // 
            this.txtResult.Location = new System.Drawing.Point(160, 81);
            this.txtResult.Multiline = true;
            this.txtResult.Name = "txtResult";
            this.txtResult.ReadOnly = true;
            this.txtResult.Size = new System.Drawing.Size(92, 80);
            this.txtResult.TabIndex = 7;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(122, 106);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(37, 12);
            this.label3.TabIndex = 6;
            this.label3.Text = "Result:";
            // 
            // btnPick
            // 
            this.btnPick.Location = new System.Drawing.Point(165, 27);
            this.btnPick.Name = "btnPick";
            this.btnPick.Size = new System.Drawing.Size(75, 21);
            this.btnPick.TabIndex = 5;
            this.btnPick.Text = "選一個";
            this.btnPick.UseVisualStyleBackColor = true;
            // 
            // txtNames
            // 
            this.txtNames.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)));
            this.txtNames.Location = new System.Drawing.Point(16, 27);
            this.txtNames.Multiline = true;
            this.txtNames.Name = "txtNames";
            this.txtNames.Size = new System.Drawing.Size(100, 124);
            this.txtNames.TabIndex = 4;
            this.txtNames.Text = "Ann\r\nBob\r\nCindy\r\nDan\r\nEdwina\r\nFrank\r\nGina\r\nHarry\r\nIvy\r\nJack\r\nKlaudia\r\nLeonard\r\nMa" +
                "rcie\r\nNate\r\nOlivia\r\nPaul\r\nQueenie\r\nRussell\r\nSally\r\nTim\r\nUma\r\nVern\r\nWendy\r\nXavier" +
                "\r\nYoko\r\nZack";
            // 
            // bt_random11
            // 
            this.bt_random11.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_random11.Location = new System.Drawing.Point(183, 250);
            this.bt_random11.Name = "bt_random11";
            this.bt_random11.Size = new System.Drawing.Size(155, 40);
            this.bt_random11.TabIndex = 32;
            this.bt_random11.Text = "產生任意字串";
            this.bt_random11.UseVisualStyleBackColor = true;
            this.bt_random11.Click += new System.EventHandler(this.bt_random11_Click);
            // 
            // bt_random10
            // 
            this.bt_random10.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_random10.Location = new System.Drawing.Point(184, 203);
            this.bt_random10.Name = "bt_random10";
            this.bt_random10.Size = new System.Drawing.Size(155, 40);
            this.bt_random10.TabIndex = 31;
            this.bt_random10.Text = "整個string array都變成亂數陣列";
            this.bt_random10.UseVisualStyleBackColor = true;
            this.bt_random10.Click += new System.EventHandler(this.bt_random10_Click);
            // 
            // bt_random9
            // 
            this.bt_random9.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_random9.Location = new System.Drawing.Point(183, 157);
            this.bt_random9.Name = "bt_random9";
            this.bt_random9.Size = new System.Drawing.Size(155, 40);
            this.bt_random9.TabIndex = 30;
            this.bt_random9.Text = "整個int array都變成亂數陣列";
            this.bt_random9.UseVisualStyleBackColor = true;
            this.bt_random9.Click += new System.EventHandler(this.bt_random9_Click);
            // 
            // bt_random8
            // 
            this.bt_random8.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_random8.Location = new System.Drawing.Point(184, 111);
            this.bt_random8.Name = "bt_random8";
            this.bt_random8.Size = new System.Drawing.Size(155, 40);
            this.bt_random8.TabIndex = 29;
            this.bt_random8.Text = "整個array都變成亂數陣列";
            this.bt_random8.UseVisualStyleBackColor = true;
            this.bt_random8.Click += new System.EventHandler(this.bt_random8_Click);
            // 
            // bt_random7
            // 
            this.bt_random7.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_random7.Location = new System.Drawing.Point(184, 21);
            this.bt_random7.Name = "bt_random7";
            this.bt_random7.Size = new System.Drawing.Size(155, 84);
            this.bt_random7.TabIndex = 28;
            this.bt_random7.Text = "隨機產生一些英文字母, 統計各種字母出現次數";
            this.bt_random7.UseVisualStyleBackColor = true;
            this.bt_random7.Click += new System.EventHandler(this.bt_random7_Click);
            // 
            // bt_random2
            // 
            this.bt_random2.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_random2.Location = new System.Drawing.Point(17, 66);
            this.bt_random2.Name = "bt_random2";
            this.bt_random2.Size = new System.Drawing.Size(155, 40);
            this.bt_random2.TabIndex = 27;
            this.bt_random2.Text = "產生不重複亂數";
            this.bt_random2.UseVisualStyleBackColor = true;
            this.bt_random2.Click += new System.EventHandler(this.bt_random2_Click);
            // 
            // bt_random6
            // 
            this.bt_random6.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_random6.Location = new System.Drawing.Point(17, 250);
            this.bt_random6.Name = "bt_random6";
            this.bt_random6.Size = new System.Drawing.Size(155, 40);
            this.bt_random6.TabIndex = 26;
            this.bt_random6.Text = "name score";
            this.bt_random6.UseVisualStyleBackColor = true;
            this.bt_random6.Click += new System.EventHandler(this.bt_random6_Click);
            // 
            // bt_random5
            // 
            this.bt_random5.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_random5.Location = new System.Drawing.Point(17, 204);
            this.bt_random5.Name = "bt_random5";
            this.bt_random5.Size = new System.Drawing.Size(155, 40);
            this.bt_random5.TabIndex = 25;
            this.bt_random5.Text = "產生一組亂數";
            this.bt_random5.UseVisualStyleBackColor = true;
            this.bt_random5.Click += new System.EventHandler(this.bt_random5_Click);
            // 
            // bt_random4
            // 
            this.bt_random4.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_random4.Location = new System.Drawing.Point(17, 158);
            this.bt_random4.Name = "bt_random4";
            this.bt_random4.Size = new System.Drawing.Size(155, 40);
            this.bt_random4.TabIndex = 24;
            this.bt_random4.Text = "產生亂數的方式";
            this.bt_random4.UseVisualStyleBackColor = true;
            this.bt_random4.Click += new System.EventHandler(this.bt_random4_Click);
            // 
            // bt_random3
            // 
            this.bt_random3.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_random3.Location = new System.Drawing.Point(17, 112);
            this.bt_random3.Name = "bt_random3";
            this.bt_random3.Size = new System.Drawing.Size(155, 40);
            this.bt_random3.TabIndex = 23;
            this.bt_random3.Text = "產生任意字串";
            this.bt_random3.UseVisualStyleBackColor = true;
            this.bt_random3.Click += new System.EventHandler(this.bt_random3_Click);
            // 
            // bt_random1
            // 
            this.bt_random1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_random1.Location = new System.Drawing.Point(17, 20);
            this.bt_random1.Name = "bt_random1";
            this.bt_random1.Size = new System.Drawing.Size(155, 40);
            this.bt_random1.TabIndex = 22;
            this.bt_random1.Text = "亂數";
            this.bt_random1.UseVisualStyleBackColor = true;
            this.bt_random1.Click += new System.EventHandler(this.bt_random1_Click);
            // 
            // bt_clear
            // 
            this.bt_clear.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_clear.Location = new System.Drawing.Point(757, 557);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(54, 35);
            this.bt_clear.TabIndex = 26;
            this.bt_clear.Text = "clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            // 
            // richTextBox1
            // 
            this.richTextBox1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.richTextBox1.Location = new System.Drawing.Point(817, 19);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(454, 740);
            this.richTextBox1.TabIndex = 25;
            this.richTextBox1.Text = "";
            // 
            // timer1
            // 
            this.timer1.Enabled = true;
            this.timer1.Interval = 1000;
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // button1
            // 
            this.button1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button1.Location = new System.Drawing.Point(357, 20);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(155, 40);
            this.button1.TabIndex = 48;
            this.button1.Text = "產生隨機字串";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1298, 837);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.bt_clear);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox1.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.groupBox4.ResumeLayout(false);
            this.groupBox4.PerformLayout();
            this.groupBox3.ResumeLayout(false);
            this.groupBox3.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.Button bt_random_text1;
        private System.Windows.Forms.Button bt_random12;
        private System.Windows.Forms.Button bt_random_color;
        private System.Windows.Forms.GroupBox groupBox4;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Button btnRandomize;
        private System.Windows.Forms.ListBox lstArray;
        private System.Windows.Forms.ListBox lstList;
        private System.Windows.Forms.GroupBox groupBox3;
        private System.Windows.Forms.Button button31;
        private System.Windows.Forms.TextBox txtResult;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Button btnPick;
        private System.Windows.Forms.TextBox txtNames;
        private System.Windows.Forms.Button bt_random11;
        private System.Windows.Forms.Button bt_random10;
        private System.Windows.Forms.Button bt_random9;
        private System.Windows.Forms.Button bt_random8;
        private System.Windows.Forms.Button bt_random7;
        private System.Windows.Forms.Button bt_random2;
        private System.Windows.Forms.Button bt_random6;
        private System.Windows.Forms.Button bt_random5;
        private System.Windows.Forms.Button bt_random4;
        private System.Windows.Forms.Button bt_random3;
        private System.Windows.Forms.Button bt_random1;
        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Timer timer1;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.Button button1;
    }
}

