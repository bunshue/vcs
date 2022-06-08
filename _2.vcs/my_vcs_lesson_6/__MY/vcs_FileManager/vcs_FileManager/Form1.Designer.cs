namespace vcs_FileManager
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
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.rb_sort2 = new System.Windows.Forms.RadioButton();
            this.rb_sort1 = new System.Windows.Forms.RadioButton();
            this.rb_sort0 = new System.Windows.Forms.RadioButton();
            this.button3 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.button1 = new System.Windows.Forms.Button();
            this.bt_clear1 = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.bt_clear2 = new System.Windows.Forms.Button();
            this.richTextBox2 = new System.Windows.Forms.RichTextBox();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.cb_show2 = new System.Windows.Forms.CheckBox();
            this.cb_show1 = new System.Windows.Forms.CheckBox();
            this.cb_show0 = new System.Windows.Forms.CheckBox();
            this.button4 = new System.Windows.Forms.Button();
            this.cb_compare0 = new System.Windows.Forms.CheckBox();
            this.cb_compare2 = new System.Windows.Forms.CheckBox();
            this.groupBox3 = new System.Windows.Forms.GroupBox();
            this.cb_compare4 = new System.Windows.Forms.CheckBox();
            this.cb_compare1 = new System.Windows.Forms.CheckBox();
            this.cb_compare3 = new System.Windows.Forms.CheckBox();
            this.listView1 = new System.Windows.Forms.ListView();
            this.button5 = new System.Windows.Forms.Button();
            this.bt_start_files = new System.Windows.Forms.Button();
            this.listBox1 = new System.Windows.Forms.ListBox();
            this.bt_clear_dir = new System.Windows.Forms.Button();
            this.bt_remove_dir = new System.Windows.Forms.Button();
            this.bt_add_dir = new System.Windows.Forms.Button();
            this.folderBrowserDialog1 = new System.Windows.Forms.FolderBrowserDialog();
            this.groupBox_file = new System.Windows.Forms.GroupBox();
            this.cb_checkcount = new System.Windows.Forms.CheckBox();
            this.tb_count = new System.Windows.Forms.TextBox();
            this.cb_filesize = new System.Windows.Forms.CheckBox();
            this.tb_filesize = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.bt_clear3 = new System.Windows.Forms.Button();
            this.button6 = new System.Windows.Forms.Button();
            this.tb_find = new System.Windows.Forms.TextBox();
            this.button7 = new System.Windows.Forms.Button();
            this.bt_start_files2 = new System.Windows.Forms.Button();
            this.button8 = new System.Windows.Forms.Button();
            this.button9 = new System.Windows.Forms.Button();
            this.bt_setup = new System.Windows.Forms.Button();
            this.button0 = new System.Windows.Forms.Button();
            this.groupBox1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.groupBox3.SuspendLayout();
            this.groupBox_file.SuspendLayout();
            this.SuspendLayout();
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.rb_sort2);
            this.groupBox1.Controls.Add(this.rb_sort1);
            this.groupBox1.Controls.Add(this.rb_sort0);
            this.groupBox1.Location = new System.Drawing.Point(125, 471);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(140, 145);
            this.groupBox1.TabIndex = 11;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "排序";
            // 
            // rb_sort2
            // 
            this.rb_sort2.AutoSize = true;
            this.rb_sort2.Location = new System.Drawing.Point(16, 104);
            this.rb_sort2.Name = "rb_sort2";
            this.rb_sort2.Size = new System.Drawing.Size(107, 16);
            this.rb_sort2.TabIndex = 2;
            this.rb_sort2.Text = "依檔案日期排序";
            this.rb_sort2.UseVisualStyleBackColor = true;
            // 
            // rb_sort1
            // 
            this.rb_sort1.AutoSize = true;
            this.rb_sort1.Location = new System.Drawing.Point(16, 72);
            this.rb_sort1.Name = "rb_sort1";
            this.rb_sort1.Size = new System.Drawing.Size(107, 16);
            this.rb_sort1.TabIndex = 1;
            this.rb_sort1.Text = "依檔案大小排序";
            this.rb_sort1.UseVisualStyleBackColor = true;
            // 
            // rb_sort0
            // 
            this.rb_sort0.AutoSize = true;
            this.rb_sort0.Checked = true;
            this.rb_sort0.Location = new System.Drawing.Point(16, 33);
            this.rb_sort0.Name = "rb_sort0";
            this.rb_sort0.Size = new System.Drawing.Size(83, 16);
            this.rb_sort0.TabIndex = 0;
            this.rb_sort0.TabStop = true;
            this.rb_sort0.Text = "依檔名排序";
            this.rb_sort0.UseVisualStyleBackColor = true;
            // 
            // button3
            // 
            this.button3.Location = new System.Drawing.Point(12, 202);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(100, 60);
            this.button3.TabIndex = 10;
            this.button3.Text = "顯示全部";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(12, 139);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(100, 60);
            this.button2.TabIndex = 9;
            this.button2.Text = "從一個資料夾中撈出所有檔案 標準版 多層";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(12, 73);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(100, 60);
            this.button1.TabIndex = 8;
            this.button1.Text = "從一個資料夾中撈出所有檔案 標準版  一層";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // bt_clear1
            // 
            this.bt_clear1.Location = new System.Drawing.Point(1697, 591);
            this.bt_clear1.Name = "bt_clear1";
            this.bt_clear1.Size = new System.Drawing.Size(63, 30);
            this.bt_clear1.TabIndex = 13;
            this.bt_clear1.Text = "Clear";
            this.bt_clear1.UseVisualStyleBackColor = true;
            this.bt_clear1.Click += new System.EventHandler(this.bt_clear1_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(479, 440);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(1293, 185);
            this.richTextBox1.TabIndex = 12;
            this.richTextBox1.Text = "";
            // 
            // bt_clear2
            // 
            this.bt_clear2.Location = new System.Drawing.Point(359, 280);
            this.bt_clear2.Name = "bt_clear2";
            this.bt_clear2.Size = new System.Drawing.Size(63, 30);
            this.bt_clear2.TabIndex = 15;
            this.bt_clear2.Text = "Clear";
            this.bt_clear2.UseVisualStyleBackColor = true;
            this.bt_clear2.Click += new System.EventHandler(this.bt_clear2_Click);
            // 
            // richTextBox2
            // 
            this.richTextBox2.Location = new System.Drawing.Point(335, 255);
            this.richTextBox2.Name = "richTextBox2";
            this.richTextBox2.Size = new System.Drawing.Size(111, 111);
            this.richTextBox2.TabIndex = 14;
            this.richTextBox2.Text = "";
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.cb_show2);
            this.groupBox2.Controls.Add(this.cb_show1);
            this.groupBox2.Controls.Add(this.cb_show0);
            this.groupBox2.Location = new System.Drawing.Point(271, 471);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(107, 145);
            this.groupBox2.TabIndex = 12;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "顯示";
            // 
            // cb_show2
            // 
            this.cb_show2.AutoSize = true;
            this.cb_show2.Location = new System.Drawing.Point(20, 104);
            this.cb_show2.Name = "cb_show2";
            this.cb_show2.Size = new System.Drawing.Size(72, 16);
            this.cb_show2.TabIndex = 2;
            this.cb_show2.Text = "檔案日期";
            this.cb_show2.UseVisualStyleBackColor = true;
            // 
            // cb_show1
            // 
            this.cb_show1.AutoSize = true;
            this.cb_show1.Location = new System.Drawing.Point(20, 72);
            this.cb_show1.Name = "cb_show1";
            this.cb_show1.Size = new System.Drawing.Size(72, 16);
            this.cb_show1.TabIndex = 1;
            this.cb_show1.Text = "檔案大小";
            this.cb_show1.UseVisualStyleBackColor = true;
            // 
            // cb_show0
            // 
            this.cb_show0.AutoSize = true;
            this.cb_show0.Checked = true;
            this.cb_show0.CheckState = System.Windows.Forms.CheckState.Checked;
            this.cb_show0.Enabled = false;
            this.cb_show0.Location = new System.Drawing.Point(20, 33);
            this.cb_show0.Name = "cb_show0";
            this.cb_show0.Size = new System.Drawing.Size(48, 16);
            this.cb_show0.TabIndex = 0;
            this.cb_show0.Text = "檔名";
            this.cb_show0.UseVisualStyleBackColor = true;
            // 
            // button4
            // 
            this.button4.Location = new System.Drawing.Point(12, 268);
            this.button4.Name = "button4";
            this.button4.Size = new System.Drawing.Size(100, 60);
            this.button4.TabIndex = 16;
            this.button4.Text = "比較";
            this.button4.UseVisualStyleBackColor = true;
            this.button4.Click += new System.EventHandler(this.button4_Click);
            // 
            // cb_compare0
            // 
            this.cb_compare0.AutoSize = true;
            this.cb_compare0.Location = new System.Drawing.Point(20, 20);
            this.cb_compare0.Name = "cb_compare0";
            this.cb_compare0.Size = new System.Drawing.Size(60, 16);
            this.cb_compare0.TabIndex = 0;
            this.cb_compare0.Text = "真檔名";
            this.cb_compare0.UseVisualStyleBackColor = true;
            this.cb_compare0.CheckedChanged += new System.EventHandler(this.check_cb_compare);
            // 
            // cb_compare2
            // 
            this.cb_compare2.AutoSize = true;
            this.cb_compare2.Location = new System.Drawing.Point(20, 60);
            this.cb_compare2.Name = "cb_compare2";
            this.cb_compare2.Size = new System.Drawing.Size(72, 16);
            this.cb_compare2.TabIndex = 1;
            this.cb_compare2.Text = "檔案大小";
            this.cb_compare2.UseVisualStyleBackColor = true;
            // 
            // groupBox3
            // 
            this.groupBox3.Controls.Add(this.cb_compare4);
            this.groupBox3.Controls.Add(this.cb_compare1);
            this.groupBox3.Controls.Add(this.cb_compare3);
            this.groupBox3.Controls.Add(this.cb_compare2);
            this.groupBox3.Controls.Add(this.cb_compare0);
            this.groupBox3.Location = new System.Drawing.Point(129, 119);
            this.groupBox3.Name = "groupBox3";
            this.groupBox3.Size = new System.Drawing.Size(134, 130);
            this.groupBox3.TabIndex = 13;
            this.groupBox3.TabStop = false;
            this.groupBox3.Text = "比較";
            // 
            // cb_compare4
            // 
            this.cb_compare4.AutoSize = true;
            this.cb_compare4.Checked = true;
            this.cb_compare4.CheckState = System.Windows.Forms.CheckState.Checked;
            this.cb_compare4.Location = new System.Drawing.Point(20, 100);
            this.cb_compare4.Name = "cb_compare4";
            this.cb_compare4.Size = new System.Drawing.Size(84, 16);
            this.cb_compare4.TabIndex = 4;
            this.cb_compare4.Text = "僅影音檔案";
            this.cb_compare4.UseVisualStyleBackColor = true;
            // 
            // cb_compare1
            // 
            this.cb_compare1.AutoSize = true;
            this.cb_compare1.Checked = true;
            this.cb_compare1.CheckState = System.Windows.Forms.CheckState.Checked;
            this.cb_compare1.Location = new System.Drawing.Point(20, 40);
            this.cb_compare1.Name = "cb_compare1";
            this.cb_compare1.Size = new System.Drawing.Size(72, 16);
            this.cb_compare1.TabIndex = 3;
            this.cb_compare1.Text = "模糊檔名";
            this.cb_compare1.UseVisualStyleBackColor = true;
            this.cb_compare1.CheckedChanged += new System.EventHandler(this.check_cb_compare);
            // 
            // cb_compare3
            // 
            this.cb_compare3.AutoSize = true;
            this.cb_compare3.Enabled = false;
            this.cb_compare3.Location = new System.Drawing.Point(20, 80);
            this.cb_compare3.Name = "cb_compare3";
            this.cb_compare3.Size = new System.Drawing.Size(72, 16);
            this.cb_compare3.TabIndex = 2;
            this.cb_compare3.Text = "檔案內容";
            this.cb_compare3.UseVisualStyleBackColor = true;
            // 
            // listView1
            // 
            this.listView1.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.listView1.Location = new System.Drawing.Point(479, 12);
            this.listView1.Name = "listView1";
            this.listView1.Size = new System.Drawing.Size(1293, 422);
            this.listView1.TabIndex = 17;
            this.listView1.UseCompatibleStateImageBehavior = false;
            this.listView1.View = System.Windows.Forms.View.Details;
            this.listView1.KeyDown += new System.Windows.Forms.KeyEventHandler(this.listView1_KeyDown);
            this.listView1.MouseClick += new System.Windows.Forms.MouseEventHandler(this.listView1_MouseClick);
            this.listView1.MouseDoubleClick += new System.Windows.Forms.MouseEventHandler(this.listView1_MouseDoubleClick);
            // 
            // button5
            // 
            this.button5.Location = new System.Drawing.Point(12, 326);
            this.button5.Name = "button5";
            this.button5.Size = new System.Drawing.Size(100, 60);
            this.button5.TabIndex = 18;
            this.button5.Text = "test";
            this.button5.UseVisualStyleBackColor = true;
            this.button5.Click += new System.EventHandler(this.button5_Click);
            // 
            // bt_start_files
            // 
            this.bt_start_files.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("bt_start_files.BackgroundImage")));
            this.bt_start_files.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_start_files.Font = new System.Drawing.Font("細明體", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_start_files.Location = new System.Drawing.Point(360, 10);
            this.bt_start_files.Name = "bt_start_files";
            this.bt_start_files.Size = new System.Drawing.Size(50, 50);
            this.bt_start_files.TabIndex = 19;
            this.bt_start_files.UseVisualStyleBackColor = true;
            this.bt_start_files.Click += new System.EventHandler(this.bt_start_files_Click);
            // 
            // listBox1
            // 
            this.listBox1.FormattingEnabled = true;
            this.listBox1.ItemHeight = 12;
            this.listBox1.Location = new System.Drawing.Point(129, 12);
            this.listBox1.Name = "listBox1";
            this.listBox1.Size = new System.Drawing.Size(194, 100);
            this.listBox1.TabIndex = 30;
            // 
            // bt_clear_dir
            // 
            this.bt_clear_dir.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_clear_dir.Font = new System.Drawing.Font("細明體", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_clear_dir.Location = new System.Drawing.Point(330, 82);
            this.bt_clear_dir.Name = "bt_clear_dir";
            this.bt_clear_dir.Size = new System.Drawing.Size(20, 20);
            this.bt_clear_dir.TabIndex = 34;
            this.bt_clear_dir.Text = "C";
            this.bt_clear_dir.UseVisualStyleBackColor = true;
            this.bt_clear_dir.Click += new System.EventHandler(this.bt_clear_dir_Click);
            // 
            // bt_remove_dir
            // 
            this.bt_remove_dir.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_remove_dir.Font = new System.Drawing.Font("細明體", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_remove_dir.Location = new System.Drawing.Point(330, 52);
            this.bt_remove_dir.Name = "bt_remove_dir";
            this.bt_remove_dir.Size = new System.Drawing.Size(20, 20);
            this.bt_remove_dir.TabIndex = 33;
            this.bt_remove_dir.Text = "-";
            this.bt_remove_dir.UseVisualStyleBackColor = true;
            this.bt_remove_dir.Click += new System.EventHandler(this.bt_remove_dir_Click);
            // 
            // bt_add_dir
            // 
            this.bt_add_dir.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_add_dir.Font = new System.Drawing.Font("細明體", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_add_dir.Location = new System.Drawing.Point(330, 22);
            this.bt_add_dir.Name = "bt_add_dir";
            this.bt_add_dir.Size = new System.Drawing.Size(20, 20);
            this.bt_add_dir.TabIndex = 32;
            this.bt_add_dir.Text = "+";
            this.bt_add_dir.UseVisualStyleBackColor = true;
            this.bt_add_dir.Click += new System.EventHandler(this.bt_add_dir_Click);
            // 
            // groupBox_file
            // 
            this.groupBox_file.Controls.Add(this.cb_checkcount);
            this.groupBox_file.Controls.Add(this.tb_count);
            this.groupBox_file.Controls.Add(this.cb_filesize);
            this.groupBox_file.Controls.Add(this.tb_filesize);
            this.groupBox_file.Controls.Add(this.label2);
            this.groupBox_file.Location = new System.Drawing.Point(129, 255);
            this.groupBox_file.Name = "groupBox_file";
            this.groupBox_file.Size = new System.Drawing.Size(198, 98);
            this.groupBox_file.TabIndex = 48;
            this.groupBox_file.TabStop = false;
            this.groupBox_file.Text = "選項";
            // 
            // cb_checkcount
            // 
            this.cb_checkcount.AutoSize = true;
            this.cb_checkcount.Checked = true;
            this.cb_checkcount.CheckState = System.Windows.Forms.CheckState.Checked;
            this.cb_checkcount.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.cb_checkcount.Location = new System.Drawing.Point(11, 54);
            this.cb_checkcount.Name = "cb_checkcount";
            this.cb_checkcount.Size = new System.Drawing.Size(91, 20);
            this.cb_checkcount.TabIndex = 48;
            this.cb_checkcount.Text = "結束個數";
            this.cb_checkcount.UseVisualStyleBackColor = true;
            // 
            // tb_count
            // 
            this.tb_count.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_count.Location = new System.Drawing.Point(108, 50);
            this.tb_count.Name = "tb_count";
            this.tb_count.Size = new System.Drawing.Size(52, 30);
            this.tb_count.TabIndex = 46;
            this.tb_count.Text = "30";
            this.tb_count.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // cb_filesize
            // 
            this.cb_filesize.AutoSize = true;
            this.cb_filesize.Checked = true;
            this.cb_filesize.CheckState = System.Windows.Forms.CheckState.Checked;
            this.cb_filesize.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.cb_filesize.Location = new System.Drawing.Point(11, 21);
            this.cb_filesize.Name = "cb_filesize";
            this.cb_filesize.Size = new System.Drawing.Size(91, 20);
            this.cb_filesize.TabIndex = 45;
            this.cb_filesize.Text = "檔案大小";
            this.cb_filesize.UseVisualStyleBackColor = true;
            // 
            // tb_filesize
            // 
            this.tb_filesize.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_filesize.Location = new System.Drawing.Point(108, 17);
            this.tb_filesize.Name = "tb_filesize";
            this.tb_filesize.Size = new System.Drawing.Size(52, 30);
            this.tb_filesize.TabIndex = 17;
            this.tb_filesize.Text = "300";
            this.tb_filesize.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(166, 25);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(23, 12);
            this.label2.TabIndex = 18;
            this.label2.Text = "MB";
            // 
            // bt_clear3
            // 
            this.bt_clear3.Font = new System.Drawing.Font("細明體", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_clear3.Location = new System.Drawing.Point(1121, 269);
            this.bt_clear3.Name = "bt_clear3";
            this.bt_clear3.Size = new System.Drawing.Size(63, 30);
            this.bt_clear3.TabIndex = 58;
            this.bt_clear3.Text = "清除";
            this.bt_clear3.UseVisualStyleBackColor = true;
            this.bt_clear3.Click += new System.EventHandler(this.bt_clear3_Click);
            // 
            // button6
            // 
            this.button6.Location = new System.Drawing.Point(12, 389);
            this.button6.Name = "button6";
            this.button6.Size = new System.Drawing.Size(100, 60);
            this.button6.TabIndex = 59;
            this.button6.Text = "搜尋特定檔名";
            this.button6.UseVisualStyleBackColor = true;
            this.button6.Click += new System.EventHandler(this.button6_Click);
            // 
            // tb_find
            // 
            this.tb_find.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_find.Location = new System.Drawing.Point(118, 374);
            this.tb_find.Name = "tb_find";
            this.tb_find.Size = new System.Drawing.Size(141, 36);
            this.tb_find.TabIndex = 60;
            this.tb_find.Text = "maron";
            // 
            // button7
            // 
            this.button7.Location = new System.Drawing.Point(12, 450);
            this.button7.Name = "button7";
            this.button7.Size = new System.Drawing.Size(100, 60);
            this.button7.TabIndex = 61;
            this.button7.Text = "優優檔";
            this.button7.UseVisualStyleBackColor = true;
            this.button7.Click += new System.EventHandler(this.button7_Click);
            // 
            // bt_start_files2
            // 
            this.bt_start_files2.Location = new System.Drawing.Point(360, 60);
            this.bt_start_files2.Name = "bt_start_files2";
            this.bt_start_files2.Size = new System.Drawing.Size(50, 50);
            this.bt_start_files2.TabIndex = 62;
            this.bt_start_files2.Text = "全選 播放";
            this.bt_start_files2.UseVisualStyleBackColor = true;
            this.bt_start_files2.Click += new System.EventHandler(this.bt_start_files2_Click);
            // 
            // button8
            // 
            this.button8.Location = new System.Drawing.Point(12, 509);
            this.button8.Name = "button8";
            this.button8.Size = new System.Drawing.Size(100, 60);
            this.button8.TabIndex = 63;
            this.button8.Text = "get_shortname";
            this.button8.UseVisualStyleBackColor = true;
            this.button8.Click += new System.EventHandler(this.button8_Click);
            // 
            // button9
            // 
            this.button9.Location = new System.Drawing.Point(12, 575);
            this.button9.Name = "button9";
            this.button9.Size = new System.Drawing.Size(100, 60);
            this.button9.TabIndex = 64;
            this.button9.Text = "大檔資料存檔";
            this.button9.UseVisualStyleBackColor = true;
            this.button9.Click += new System.EventHandler(this.button9_Click);
            // 
            // bt_setup
            // 
            this.bt_setup.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("bt_setup.BackgroundImage")));
            this.bt_setup.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_setup.Location = new System.Drawing.Point(360, 110);
            this.bt_setup.Name = "bt_setup";
            this.bt_setup.Size = new System.Drawing.Size(50, 50);
            this.bt_setup.TabIndex = 65;
            this.bt_setup.UseVisualStyleBackColor = true;
            this.bt_setup.Click += new System.EventHandler(this.bt_setup_Click);
            // 
            // button0
            // 
            this.button0.Location = new System.Drawing.Point(12, 12);
            this.button0.Name = "button0";
            this.button0.Size = new System.Drawing.Size(100, 60);
            this.button0.TabIndex = 66;
            this.button0.UseVisualStyleBackColor = true;
            this.button0.Click += new System.EventHandler(this.button0_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1784, 756);
            this.Controls.Add(this.button0);
            this.Controls.Add(this.bt_setup);
            this.Controls.Add(this.button9);
            this.Controls.Add(this.button8);
            this.Controls.Add(this.bt_start_files2);
            this.Controls.Add(this.button7);
            this.Controls.Add(this.tb_find);
            this.Controls.Add(this.button6);
            this.Controls.Add(this.bt_clear3);
            this.Controls.Add(this.groupBox_file);
            this.Controls.Add(this.bt_clear_dir);
            this.Controls.Add(this.bt_remove_dir);
            this.Controls.Add(this.bt_add_dir);
            this.Controls.Add(this.listBox1);
            this.Controls.Add(this.bt_start_files);
            this.Controls.Add(this.button5);
            this.Controls.Add(this.listView1);
            this.Controls.Add(this.button4);
            this.Controls.Add(this.groupBox3);
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.bt_clear2);
            this.Controls.Add(this.richTextBox2);
            this.Controls.Add(this.bt_clear1);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.button1);
            this.Name = "Form1";
            this.Text = "檔案管理員";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.Form1_FormClosing);
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.groupBox2.ResumeLayout(false);
            this.groupBox2.PerformLayout();
            this.groupBox3.ResumeLayout(false);
            this.groupBox3.PerformLayout();
            this.groupBox_file.ResumeLayout(false);
            this.groupBox_file.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.RadioButton rb_sort2;
        private System.Windows.Forms.RadioButton rb_sort1;
        private System.Windows.Forms.RadioButton rb_sort0;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button bt_clear1;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Button bt_clear2;
        private System.Windows.Forms.RichTextBox richTextBox2;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.CheckBox cb_show2;
        private System.Windows.Forms.CheckBox cb_show1;
        private System.Windows.Forms.CheckBox cb_show0;
        private System.Windows.Forms.Button button4;
        private System.Windows.Forms.CheckBox cb_compare0;
        private System.Windows.Forms.CheckBox cb_compare2;
        private System.Windows.Forms.GroupBox groupBox3;
        private System.Windows.Forms.CheckBox cb_compare3;
        private System.Windows.Forms.CheckBox cb_compare1;
        private System.Windows.Forms.ListView listView1;
        private System.Windows.Forms.Button button5;
        private System.Windows.Forms.Button bt_start_files;
        private System.Windows.Forms.ListBox listBox1;
        private System.Windows.Forms.Button bt_clear_dir;
        private System.Windows.Forms.Button bt_remove_dir;
        private System.Windows.Forms.Button bt_add_dir;
        private System.Windows.Forms.FolderBrowserDialog folderBrowserDialog1;
        private System.Windows.Forms.GroupBox groupBox_file;
        private System.Windows.Forms.CheckBox cb_checkcount;
        private System.Windows.Forms.TextBox tb_count;
        private System.Windows.Forms.CheckBox cb_filesize;
        private System.Windows.Forms.TextBox tb_filesize;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Button bt_clear3;
        private System.Windows.Forms.Button button6;
        private System.Windows.Forms.TextBox tb_find;
        private System.Windows.Forms.Button button7;
        private System.Windows.Forms.Button bt_start_files2;
        private System.Windows.Forms.Button button8;
        private System.Windows.Forms.CheckBox cb_compare4;
        private System.Windows.Forms.Button button9;
        private System.Windows.Forms.Button bt_setup;
        private System.Windows.Forms.Button button0;
    }
}

