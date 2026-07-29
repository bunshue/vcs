namespace vcs_test_all_05_Print4
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.groupBox0 = new System.Windows.Forms.GroupBox();
            this.button00 = new System.Windows.Forms.Button();
            this.button03 = new System.Windows.Forms.Button();
            this.button01 = new System.Windows.Forms.Button();
            this.button02 = new System.Windows.Forms.Button();
            this.bt_clear = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.pageSetupDialog0 = new System.Windows.Forms.PageSetupDialog();
            this.printDialog0 = new System.Windows.Forms.PrintDialog();
            this.printDocument0 = new System.Drawing.Printing.PrintDocument();
            this.printPreviewDialog0 = new System.Windows.Forms.PrintPreviewDialog();
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.button0 = new System.Windows.Forms.Button();
            this.button1 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.printDocument555 = new System.Drawing.Printing.PrintDocument();
            this.printPreviewDialog555 = new System.Windows.Forms.PrintPreviewDialog();
            this.printPreviewDialog_Calendar = new System.Windows.Forms.PrintPreviewDialog();
            this.printDocument_Calendar = new System.Drawing.Printing.PrintDocument();
            this.button3 = new System.Windows.Forms.Button();
            this.printDocument_image = new System.Drawing.Printing.PrintDocument();
            this.printPreviewDialog_image = new System.Windows.Forms.PrintPreviewDialog();
            this.dataGridView1 = new System.Windows.Forms.DataGridView();
            this.groupBox5 = new System.Windows.Forms.GroupBox();
            this.bt_dgv_print2 = new System.Windows.Forms.Button();
            this.label2 = new System.Windows.Forms.Label();
            this.txt_Range = new System.Windows.Forms.TextBox();
            this.rb_Range = new System.Windows.Forms.RadioButton();
            this.rb_All = new System.Windows.Forms.RadioButton();
            this.groupBox4 = new System.Windows.Forms.GroupBox();
            this.label3 = new System.Windows.Forms.Label();
            this.bt_dgv_print = new System.Windows.Forms.Button();
            this.textBox_page = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.printDocument_dgv = new System.Drawing.Printing.PrintDocument();
            this.printPreviewDialog_dgv = new System.Windows.Forms.PrintPreviewDialog();
            this.groupBox0.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView1)).BeginInit();
            this.groupBox5.SuspendLayout();
            this.groupBox4.SuspendLayout();
            this.SuspendLayout();
            // 
            // groupBox0
            // 
            this.groupBox0.Controls.Add(this.button00);
            this.groupBox0.Controls.Add(this.button03);
            this.groupBox0.Controls.Add(this.button01);
            this.groupBox0.Controls.Add(this.button02);
            this.groupBox0.Location = new System.Drawing.Point(12, 12);
            this.groupBox0.Name = "groupBox0";
            this.groupBox0.Size = new System.Drawing.Size(200, 280);
            this.groupBox0.TabIndex = 151;
            this.groupBox0.TabStop = false;
            // 
            // button00
            // 
            this.button00.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button00.Location = new System.Drawing.Point(10, 20);
            this.button00.Name = "button00";
            this.button00.Size = new System.Drawing.Size(180, 55);
            this.button00.TabIndex = 146;
            this.button00.Text = "版面設定";
            this.button00.UseVisualStyleBackColor = true;
            this.button00.Click += new System.EventHandler(this.button00_Click);
            // 
            // button03
            // 
            this.button03.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button03.Location = new System.Drawing.Point(10, 204);
            this.button03.Name = "button03";
            this.button03.Size = new System.Drawing.Size(180, 55);
            this.button03.TabIndex = 149;
            this.button03.Text = "列印";
            this.button03.UseVisualStyleBackColor = true;
            this.button03.Click += new System.EventHandler(this.button03_Click);
            // 
            // button01
            // 
            this.button01.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button01.Location = new System.Drawing.Point(10, 81);
            this.button01.Name = "button01";
            this.button01.Size = new System.Drawing.Size(180, 55);
            this.button01.TabIndex = 147;
            this.button01.Text = "列印設定";
            this.button01.UseVisualStyleBackColor = true;
            this.button01.Click += new System.EventHandler(this.button01_Click);
            // 
            // button02
            // 
            this.button02.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button02.Location = new System.Drawing.Point(10, 142);
            this.button02.Name = "button02";
            this.button02.Size = new System.Drawing.Size(180, 55);
            this.button02.TabIndex = 148;
            this.button02.Text = "預覽列印";
            this.button02.UseVisualStyleBackColor = true;
            this.button02.Click += new System.EventHandler(this.button02_Click);
            // 
            // bt_clear
            // 
            this.bt_clear.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_clear.Location = new System.Drawing.Point(527, 51);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(72, 36);
            this.bt_clear.TabIndex = 153;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.richTextBox1.Location = new System.Drawing.Point(510, 14);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(100, 100);
            this.richTextBox1.TabIndex = 152;
            this.richTextBox1.Text = "";
            // 
            // printDialog0
            // 
            this.printDialog0.UseEXDialog = true;
            // 
            // printDocument0
            // 
            this.printDocument0.DocumentName = "document0";
            this.printDocument0.PrintPage += new System.Drawing.Printing.PrintPageEventHandler(this.printDocument0_PrintPage);
            // 
            // printPreviewDialog0
            // 
            this.printPreviewDialog0.AutoScrollMargin = new System.Drawing.Size(0, 0);
            this.printPreviewDialog0.AutoScrollMinSize = new System.Drawing.Size(0, 0);
            this.printPreviewDialog0.ClientSize = new System.Drawing.Size(400, 300);
            this.printPreviewDialog0.Document = this.printDocument0;
            this.printPreviewDialog0.Enabled = true;
            this.printPreviewDialog0.Icon = ((System.Drawing.Icon)(resources.GetObject("printPreviewDialog0.Icon")));
            this.printPreviewDialog0.Name = "printPreviewDialog1";
            this.printPreviewDialog0.Visible = false;
            // 
            // textBox1
            // 
            this.textBox1.Location = new System.Drawing.Point(237, 12);
            this.textBox1.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.textBox1.Multiline = true;
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(100, 100);
            this.textBox1.TabIndex = 154;
            // 
            // button0
            // 
            this.button0.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button0.Location = new System.Drawing.Point(22, 320);
            this.button0.Name = "button0";
            this.button0.Size = new System.Drawing.Size(180, 55);
            this.button0.TabIndex = 150;
            this.button0.Text = "版面設定";
            this.button0.UseVisualStyleBackColor = true;
            this.button0.Click += new System.EventHandler(this.button0_Click);
            // 
            // button1
            // 
            this.button1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button1.Location = new System.Drawing.Point(22, 381);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(180, 55);
            this.button1.TabIndex = 155;
            this.button1.Text = "預覽列印555";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // button2
            // 
            this.button2.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button2.Location = new System.Drawing.Point(22, 442);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(180, 55);
            this.button2.TabIndex = 156;
            this.button2.Text = "預覽列印 月曆";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // printDocument555
            // 
            this.printDocument555.BeginPrint += new System.Drawing.Printing.PrintEventHandler(this.printDocument555_BeginPrint);
            this.printDocument555.PrintPage += new System.Drawing.Printing.PrintPageEventHandler(this.printDocument555_PrintPage);
            // 
            // printPreviewDialog555
            // 
            this.printPreviewDialog555.AutoScrollMargin = new System.Drawing.Size(0, 0);
            this.printPreviewDialog555.AutoScrollMinSize = new System.Drawing.Size(0, 0);
            this.printPreviewDialog555.ClientSize = new System.Drawing.Size(400, 300);
            this.printPreviewDialog555.Document = this.printDocument555;
            this.printPreviewDialog555.Enabled = true;
            this.printPreviewDialog555.Icon = ((System.Drawing.Icon)(resources.GetObject("printPreviewDialog555.Icon")));
            this.printPreviewDialog555.Name = "printPreviewDialog555";
            this.printPreviewDialog555.Visible = false;
            // 
            // printPreviewDialog_Calendar
            // 
            this.printPreviewDialog_Calendar.AutoScrollMargin = new System.Drawing.Size(0, 0);
            this.printPreviewDialog_Calendar.AutoScrollMinSize = new System.Drawing.Size(0, 0);
            this.printPreviewDialog_Calendar.ClientSize = new System.Drawing.Size(400, 300);
            this.printPreviewDialog_Calendar.Document = this.printDocument_Calendar;
            this.printPreviewDialog_Calendar.Enabled = true;
            this.printPreviewDialog_Calendar.Icon = ((System.Drawing.Icon)(resources.GetObject("printPreviewDialog_Calendar.Icon")));
            this.printPreviewDialog_Calendar.Name = "printPreviewDialog_Calendar";
            this.printPreviewDialog_Calendar.Visible = false;
            // 
            // printDocument_Calendar
            // 
            this.printDocument_Calendar.PrintPage += new System.Drawing.Printing.PrintPageEventHandler(this.printDocument_Calendar_PrintPage);
            this.printDocument_Calendar.QueryPageSettings += new System.Drawing.Printing.QueryPageSettingsEventHandler(this.printDocument_Calendar_QueryPageSettings);
            // 
            // button3
            // 
            this.button3.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button3.Location = new System.Drawing.Point(22, 503);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(180, 55);
            this.button3.TabIndex = 157;
            this.button3.Text = "預覽列印 圖片";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // printDocument_image
            // 
            this.printDocument_image.PrintPage += new System.Drawing.Printing.PrintPageEventHandler(this.printDocument_image_PrintPage);
            // 
            // printPreviewDialog_image
            // 
            this.printPreviewDialog_image.AutoScrollMargin = new System.Drawing.Size(0, 0);
            this.printPreviewDialog_image.AutoScrollMinSize = new System.Drawing.Size(0, 0);
            this.printPreviewDialog_image.ClientSize = new System.Drawing.Size(400, 300);
            this.printPreviewDialog_image.Document = this.printDocument_image;
            this.printPreviewDialog_image.Enabled = true;
            this.printPreviewDialog_image.Icon = ((System.Drawing.Icon)(resources.GetObject("printPreviewDialog_image.Icon")));
            this.printPreviewDialog_image.Name = "printPreviewDialog_image";
            this.printPreviewDialog_image.Visible = false;
            // 
            // dataGridView1
            // 
            this.dataGridView1.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridView1.Location = new System.Drawing.Point(237, 311);
            this.dataGridView1.Name = "dataGridView1";
            this.dataGridView1.RowTemplate.Height = 24;
            this.dataGridView1.Size = new System.Drawing.Size(100, 100);
            this.dataGridView1.TabIndex = 160;
            // 
            // groupBox5
            // 
            this.groupBox5.Controls.Add(this.bt_dgv_print2);
            this.groupBox5.Controls.Add(this.label2);
            this.groupBox5.Controls.Add(this.txt_Range);
            this.groupBox5.Controls.Add(this.rb_Range);
            this.groupBox5.Controls.Add(this.rb_All);
            this.groupBox5.Location = new System.Drawing.Point(237, 215);
            this.groupBox5.Name = "groupBox5";
            this.groupBox5.Size = new System.Drawing.Size(435, 71);
            this.groupBox5.TabIndex = 163;
            this.groupBox5.TabStop = false;
            this.groupBox5.Text = "页码范围设置";
            // 
            // bt_dgv_print2
            // 
            this.bt_dgv_print2.Location = new System.Drawing.Point(332, 12);
            this.bt_dgv_print2.Name = "bt_dgv_print2";
            this.bt_dgv_print2.Size = new System.Drawing.Size(72, 36);
            this.bt_dgv_print2.TabIndex = 4;
            this.bt_dgv_print2.Text = "打印";
            this.bt_dgv_print2.UseVisualStyleBackColor = true;
            this.bt_dgv_print2.Click += new System.EventHandler(this.bt_dgv_print2_Click);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(259, 47);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(83, 12);
            this.label2.TabIndex = 3;
            this.label2.Text = "(例如：1,2,3-5)";
            // 
            // txt_Range
            // 
            this.txt_Range.Enabled = false;
            this.txt_Range.Location = new System.Drawing.Point(87, 43);
            this.txt_Range.Name = "txt_Range";
            this.txt_Range.Size = new System.Drawing.Size(166, 22);
            this.txt_Range.TabIndex = 2;
            // 
            // rb_Range
            // 
            this.rb_Range.AutoSize = true;
            this.rb_Range.Location = new System.Drawing.Point(10, 44);
            this.rb_Range.Name = "rb_Range";
            this.rb_Range.Size = new System.Drawing.Size(71, 16);
            this.rb_Range.TabIndex = 1;
            this.rb_Range.Text = "页码范围";
            this.rb_Range.UseVisualStyleBackColor = true;
            // 
            // rb_All
            // 
            this.rb_All.AutoSize = true;
            this.rb_All.Checked = true;
            this.rb_All.Location = new System.Drawing.Point(10, 22);
            this.rb_All.Name = "rb_All";
            this.rb_All.Size = new System.Drawing.Size(47, 16);
            this.rb_All.TabIndex = 0;
            this.rb_All.TabStop = true;
            this.rb_All.Text = "全部";
            this.rb_All.UseVisualStyleBackColor = true;
            // 
            // groupBox4
            // 
            this.groupBox4.Controls.Add(this.label3);
            this.groupBox4.Controls.Add(this.bt_dgv_print);
            this.groupBox4.Controls.Add(this.textBox_page);
            this.groupBox4.Controls.Add(this.label1);
            this.groupBox4.Location = new System.Drawing.Point(237, 142);
            this.groupBox4.Name = "groupBox4";
            this.groupBox4.Size = new System.Drawing.Size(435, 67);
            this.groupBox4.TabIndex = 162;
            this.groupBox4.TabStop = false;
            this.groupBox4.Text = "分页打印设置";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.ForeColor = System.Drawing.Color.Red;
            this.label3.Location = new System.Drawing.Point(17, 47);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(245, 12);
            this.label3.TabIndex = 2;
            this.label3.Text = "注意：请在输入每页打印行数之后按回车键！";
            // 
            // bt_dgv_print
            // 
            this.bt_dgv_print.Location = new System.Drawing.Point(321, 21);
            this.bt_dgv_print.Name = "bt_dgv_print";
            this.bt_dgv_print.Size = new System.Drawing.Size(72, 36);
            this.bt_dgv_print.TabIndex = 3;
            this.bt_dgv_print.Text = "打印";
            this.bt_dgv_print.UseVisualStyleBackColor = true;
            this.bt_dgv_print.Click += new System.EventHandler(this.bt_dgv_print_Click);
            // 
            // textBox_page
            // 
            this.textBox_page.Location = new System.Drawing.Point(103, 21);
            this.textBox_page.Name = "textBox_page";
            this.textBox_page.Size = new System.Drawing.Size(28, 22);
            this.textBox_page.TabIndex = 1;
            this.textBox_page.Text = "30";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(17, 24);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(89, 12);
            this.label1.TabIndex = 0;
            this.label1.Text = "每页打印行数：";
            // 
            // printDocument_dgv
            // 
            this.printDocument_dgv.PrintPage += new System.Drawing.Printing.PrintPageEventHandler(this.printDocument_dgv_PrintPage);
            // 
            // printPreviewDialog_dgv
            // 
            this.printPreviewDialog_dgv.AutoScrollMargin = new System.Drawing.Size(0, 0);
            this.printPreviewDialog_dgv.AutoScrollMinSize = new System.Drawing.Size(0, 0);
            this.printPreviewDialog_dgv.ClientSize = new System.Drawing.Size(400, 300);
            this.printPreviewDialog_dgv.Document = this.printDocument_dgv;
            this.printPreviewDialog_dgv.Enabled = true;
            this.printPreviewDialog_dgv.Icon = ((System.Drawing.Icon)(resources.GetObject("printPreviewDialog_dgv.Icon")));
            this.printPreviewDialog_dgv.Name = "printPreviewDialog_dgv";
            this.printPreviewDialog_dgv.Visible = false;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1047, 582);
            this.Controls.Add(this.groupBox5);
            this.Controls.Add(this.groupBox4);
            this.Controls.Add(this.dataGridView1);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.button0);
            this.Controls.Add(this.textBox1);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.groupBox0);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox0.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView1)).EndInit();
            this.groupBox5.ResumeLayout(false);
            this.groupBox5.PerformLayout();
            this.groupBox4.ResumeLayout(false);
            this.groupBox4.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.GroupBox groupBox0;
        private System.Windows.Forms.Button button00;
        private System.Windows.Forms.Button button03;
        private System.Windows.Forms.Button button01;
        private System.Windows.Forms.Button button02;
        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.PageSetupDialog pageSetupDialog0;
        private System.Windows.Forms.PrintDialog printDialog0;
        private System.Drawing.Printing.PrintDocument printDocument0;
        private System.Windows.Forms.PrintPreviewDialog printPreviewDialog0;
        private System.Windows.Forms.TextBox textBox1;
        private System.Windows.Forms.Button button0;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button button2;
        private System.Drawing.Printing.PrintDocument printDocument555;
        private System.Windows.Forms.PrintPreviewDialog printPreviewDialog555;
        private System.Windows.Forms.PrintPreviewDialog printPreviewDialog_Calendar;
        private System.Drawing.Printing.PrintDocument printDocument_Calendar;
        private System.Windows.Forms.Button button3;
        private System.Drawing.Printing.PrintDocument printDocument_image;
        private System.Windows.Forms.PrintPreviewDialog printPreviewDialog_image;
        private System.Windows.Forms.DataGridView dataGridView1;
        private System.Windows.Forms.GroupBox groupBox5;
        private System.Windows.Forms.Button bt_dgv_print2;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox txt_Range;
        private System.Windows.Forms.RadioButton rb_Range;
        private System.Windows.Forms.RadioButton rb_All;
        private System.Windows.Forms.GroupBox groupBox4;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Button bt_dgv_print;
        private System.Windows.Forms.TextBox textBox_page;
        private System.Windows.Forms.Label label1;
        private System.Drawing.Printing.PrintDocument printDocument_dgv;
        private System.Windows.Forms.PrintPreviewDialog printPreviewDialog_dgv;
    }
}

