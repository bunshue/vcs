namespace vcs_DrAP
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
            this.label1 = new System.Windows.Forms.Label();
            this.comboBox1 = new System.Windows.Forms.ComboBox();
            this.bt_search_all_files = new System.Windows.Forms.Button();
            this.bt_search_one_layer_files = new System.Windows.Forms.Button();
            this.bt_clear_data = new System.Windows.Forms.Button();
            this.bt_help = new System.Windows.Forms.Button();
            this.bt_copy_data = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.folderBrowserDialog1 = new System.Windows.Forms.FolderBrowserDialog();
            this.saveFileDialog1 = new System.Windows.Forms.SaveFileDialog();
            this.listView1 = new System.Windows.Forms.ListView();
            this.checkBox2 = new System.Windows.Forms.CheckBox();
            this.tb_file_l = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.richTextBox2 = new System.Windows.Forms.RichTextBox();
            this.tb_search_text_pattern = new System.Windows.Forms.TextBox();
            this.bt_find_big_files = new System.Windows.Forms.Button();
            this.textBox3 = new System.Windows.Forms.TextBox();
            this.bt_find_same_files = new System.Windows.Forms.Button();
            this.bt_add_dir = new System.Windows.Forms.Button();
            this.listBox1 = new System.Windows.Forms.ListBox();
            this.bt_remove_dir = new System.Windows.Forms.Button();
            this.bt_clear_dir = new System.Windows.Forms.Button();
            this.bt_find_small_folders = new System.Windows.Forms.Button();
            this.label3 = new System.Windows.Forms.Label();
            this.textBox4 = new System.Windows.Forms.TextBox();
            this.bt_test = new System.Windows.Forms.Button();
            this.bt_clear1 = new System.Windows.Forms.Button();
            this.bt_clear2 = new System.Windows.Forms.Button();
            this.bt_find_same_files2 = new System.Windows.Forms.Button();
            this.checkBox3 = new System.Windows.Forms.CheckBox();
            this.cb_video_only = new System.Windows.Forms.CheckBox();
            this.cb_video_s = new System.Windows.Forms.CheckBox();
            this.cb_generate_text = new System.Windows.Forms.CheckBox();
            this.checkBox7 = new System.Windows.Forms.CheckBox();
            this.groupBox_video = new System.Windows.Forms.GroupBox();
            this.cb_video_l = new System.Windows.Forms.CheckBox();
            this.cb_video_m = new System.Windows.Forms.CheckBox();
            this.groupBox_file = new System.Windows.Forms.GroupBox();
            this.cb_file_l = new System.Windows.Forms.CheckBox();
            this.tb_file_s = new System.Windows.Forms.TextBox();
            this.cb_file_m = new System.Windows.Forms.CheckBox();
            this.cb_file_s = new System.Windows.Forms.CheckBox();
            this.cb_file_size = new System.Windows.Forms.CheckBox();
            this.checkBox8 = new System.Windows.Forms.CheckBox();
            this.bt_copy_rtb_data = new System.Windows.Forms.Button();
            this.bt_setup = new System.Windows.Forms.Button();
            this.bt_search_pattern_matlab = new System.Windows.Forms.Button();
            this.bt_save_rtb_data = new System.Windows.Forms.Button();
            this.bt_search_pattern_python = new System.Windows.Forms.Button();
            this.bt_search_pattern_vcs = new System.Windows.Forms.Button();
            this.bt_delete_file = new System.Windows.Forms.Button();
            this.bt_start_files = new System.Windows.Forms.Button();
            this.bt_open_dir = new System.Windows.Forms.Button();
            this.bt_save_data = new System.Windows.Forms.Button();
            this.bt_find_empty_folders = new System.Windows.Forms.Button();
            this.groupBox_video.SuspendLayout();
            this.groupBox_file.SuspendLayout();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("細明體", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label1.Location = new System.Drawing.Point(724, 37);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(35, 13);
            this.label1.TabIndex = 0;
            this.label1.Text = "類型";
            // 
            // comboBox1
            // 
            this.comboBox1.Font = new System.Drawing.Font("細明體", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.comboBox1.FormattingEnabled = true;
            this.comboBox1.Items.AddRange(new object[] {
            "影片",
            "全部檔案",
            "音樂"});
            this.comboBox1.Location = new System.Drawing.Point(765, 34);
            this.comboBox1.Name = "comboBox1";
            this.comboBox1.Size = new System.Drawing.Size(88, 21);
            this.comboBox1.TabIndex = 1;
            this.comboBox1.SelectedIndexChanged += new System.EventHandler(this.comboBox1_SelectedIndexChanged);
            // 
            // bt_search_all_files
            // 
            this.bt_search_all_files.Font = new System.Drawing.Font("細明體", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_search_all_files.Location = new System.Drawing.Point(537, 7);
            this.bt_search_all_files.Name = "bt_search_all_files";
            this.bt_search_all_files.Size = new System.Drawing.Size(75, 23);
            this.bt_search_all_files.TabIndex = 2;
            this.bt_search_all_files.Text = "轉出";
            this.bt_search_all_files.UseVisualStyleBackColor = true;
            this.bt_search_all_files.Click += new System.EventHandler(this.bt_search_all_files_Click);
            // 
            // bt_search_one_layer_files
            // 
            this.bt_search_one_layer_files.Font = new System.Drawing.Font("細明體", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_search_one_layer_files.Location = new System.Drawing.Point(618, 7);
            this.bt_search_one_layer_files.Name = "bt_search_one_layer_files";
            this.bt_search_one_layer_files.Size = new System.Drawing.Size(75, 23);
            this.bt_search_one_layer_files.TabIndex = 3;
            this.bt_search_one_layer_files.Text = "轉出一層";
            this.bt_search_one_layer_files.UseVisualStyleBackColor = true;
            this.bt_search_one_layer_files.Click += new System.EventHandler(this.bt_search_one_layer_files_Click);
            // 
            // bt_clear_data
            // 
            this.bt_clear_data.Font = new System.Drawing.Font("細明體", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_clear_data.Location = new System.Drawing.Point(699, 5);
            this.bt_clear_data.Name = "bt_clear_data";
            this.bt_clear_data.Size = new System.Drawing.Size(60, 23);
            this.bt_clear_data.TabIndex = 5;
            this.bt_clear_data.Text = "清除";
            this.bt_clear_data.UseVisualStyleBackColor = true;
            this.bt_clear_data.Click += new System.EventHandler(this.bt_clear_data_Click);
            // 
            // bt_help
            // 
            this.bt_help.Font = new System.Drawing.Font("細明體", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_help.Location = new System.Drawing.Point(846, 4);
            this.bt_help.Name = "bt_help";
            this.bt_help.Size = new System.Drawing.Size(75, 23);
            this.bt_help.TabIndex = 8;
            this.bt_help.Text = "Help";
            this.bt_help.UseVisualStyleBackColor = true;
            this.bt_help.Click += new System.EventHandler(this.bt_help_Click);
            // 
            // bt_copy_data
            // 
            this.bt_copy_data.Font = new System.Drawing.Font("細明體", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_copy_data.Location = new System.Drawing.Point(765, 5);
            this.bt_copy_data.Name = "bt_copy_data";
            this.bt_copy_data.Size = new System.Drawing.Size(75, 23);
            this.bt_copy_data.TabIndex = 6;
            this.bt_copy_data.Text = "複製全部";
            this.bt_copy_data.UseVisualStyleBackColor = true;
            this.bt_copy_data.Click += new System.EventHandler(this.bt_copy_data_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Font = new System.Drawing.Font("細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.richTextBox1.Location = new System.Drawing.Point(12, 619);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(1300, 388);
            this.richTextBox1.TabIndex = 10;
            this.richTextBox1.Text = "";
            this.richTextBox1.TextChanged += new System.EventHandler(this.richTextBox1_TextChanged);
            // 
            // listView1
            // 
            this.listView1.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.listView1.Location = new System.Drawing.Point(12, 113);
            this.listView1.Name = "listView1";
            this.listView1.Size = new System.Drawing.Size(1653, 500);
            this.listView1.TabIndex = 14;
            this.listView1.UseCompatibleStateImageBehavior = false;
            this.listView1.View = System.Windows.Forms.View.Details;
            this.listView1.KeyDown += new System.Windows.Forms.KeyEventHandler(this.listView1_KeyDown);
            this.listView1.MouseClick += new System.Windows.Forms.MouseEventHandler(this.listView1_MouseClick);
            this.listView1.MouseDoubleClick += new System.Windows.Forms.MouseEventHandler(this.listView1_MouseDoubleClick);
            // 
            // checkBox2
            // 
            this.checkBox2.AutoSize = true;
            this.checkBox2.Checked = true;
            this.checkBox2.CheckState = System.Windows.Forms.CheckState.Checked;
            this.checkBox2.Location = new System.Drawing.Point(388, 65);
            this.checkBox2.Name = "checkBox2";
            this.checkBox2.Size = new System.Drawing.Size(48, 16);
            this.checkBox2.TabIndex = 16;
            this.checkBox2.Text = "排序";
            this.checkBox2.UseVisualStyleBackColor = true;
            // 
            // tb_file_l
            // 
            this.tb_file_l.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_file_l.Location = new System.Drawing.Point(153, 14);
            this.tb_file_l.Name = "tb_file_l";
            this.tb_file_l.Size = new System.Drawing.Size(52, 30);
            this.tb_file_l.TabIndex = 17;
            this.tb_file_l.Text = "100";
            this.tb_file_l.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            this.tb_file_l.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.textBox1_KeyPress);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(263, 23);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(23, 12);
            this.label2.TabIndex = 18;
            this.label2.Text = "MB";
            // 
            // richTextBox2
            // 
            this.richTextBox2.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.richTextBox2.Location = new System.Drawing.Point(1318, 619);
            this.richTextBox2.Name = "richTextBox2";
            this.richTextBox2.Size = new System.Drawing.Size(347, 388);
            this.richTextBox2.TabIndex = 19;
            this.richTextBox2.Text = "";
            this.richTextBox2.TextChanged += new System.EventHandler(this.richTextBox2_TextChanged);
            // 
            // tb_search_text_pattern
            // 
            this.tb_search_text_pattern.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_search_text_pattern.Location = new System.Drawing.Point(252, 14);
            this.tb_search_text_pattern.Name = "tb_search_text_pattern";
            this.tb_search_text_pattern.Size = new System.Drawing.Size(99, 30);
            this.tb_search_text_pattern.TabIndex = 20;
            this.tb_search_text_pattern.Text = "雍正";
            this.tb_search_text_pattern.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // bt_find_big_files
            // 
            this.bt_find_big_files.Font = new System.Drawing.Font("細明體", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_find_big_files.Location = new System.Drawing.Point(360, 6);
            this.bt_find_big_files.Name = "bt_find_big_files";
            this.bt_find_big_files.Size = new System.Drawing.Size(50, 50);
            this.bt_find_big_files.TabIndex = 21;
            this.bt_find_big_files.Text = "搜尋大檔";
            this.bt_find_big_files.UseVisualStyleBackColor = true;
            this.bt_find_big_files.Click += new System.EventHandler(this.bt_find_big_files_Click);
            // 
            // textBox3
            // 
            this.textBox3.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.textBox3.Location = new System.Drawing.Point(1526, 37);
            this.textBox3.Name = "textBox3";
            this.textBox3.Size = new System.Drawing.Size(142, 30);
            this.textBox3.TabIndex = 24;
            this.textBox3.Text = "TBGBMBKB";
            this.textBox3.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            this.textBox3.KeyDown += new System.Windows.Forms.KeyEventHandler(this.textBox3_KeyDown);
            this.textBox3.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.textBox3_KeyPress);
            // 
            // bt_find_same_files
            // 
            this.bt_find_same_files.Font = new System.Drawing.Font("細明體", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_find_same_files.Location = new System.Drawing.Point(537, 30);
            this.bt_find_same_files.Name = "bt_find_same_files";
            this.bt_find_same_files.Size = new System.Drawing.Size(156, 23);
            this.bt_find_same_files.TabIndex = 27;
            this.bt_find_same_files.Text = "找同檔";
            this.bt_find_same_files.UseVisualStyleBackColor = true;
            this.bt_find_same_files.Click += new System.EventHandler(this.bt_find_same_files_Click);
            // 
            // bt_add_dir
            // 
            this.bt_add_dir.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_add_dir.Font = new System.Drawing.Font("細明體", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_add_dir.Location = new System.Drawing.Point(213, 14);
            this.bt_add_dir.Name = "bt_add_dir";
            this.bt_add_dir.Size = new System.Drawing.Size(20, 20);
            this.bt_add_dir.TabIndex = 28;
            this.bt_add_dir.Text = "+";
            this.bt_add_dir.UseVisualStyleBackColor = true;
            this.bt_add_dir.Click += new System.EventHandler(this.bt_add_dir_Click);
            // 
            // listBox1
            // 
            this.listBox1.FormattingEnabled = true;
            this.listBox1.ItemHeight = 12;
            this.listBox1.Location = new System.Drawing.Point(12, 7);
            this.listBox1.Name = "listBox1";
            this.listBox1.Size = new System.Drawing.Size(194, 100);
            this.listBox1.TabIndex = 29;
            // 
            // bt_remove_dir
            // 
            this.bt_remove_dir.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_remove_dir.Font = new System.Drawing.Font("細明體", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_remove_dir.Location = new System.Drawing.Point(213, 44);
            this.bt_remove_dir.Name = "bt_remove_dir";
            this.bt_remove_dir.Size = new System.Drawing.Size(20, 20);
            this.bt_remove_dir.TabIndex = 30;
            this.bt_remove_dir.Text = "-";
            this.bt_remove_dir.UseVisualStyleBackColor = true;
            this.bt_remove_dir.Click += new System.EventHandler(this.bt_remove_dir_Click);
            // 
            // bt_clear_dir
            // 
            this.bt_clear_dir.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_clear_dir.Font = new System.Drawing.Font("細明體", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_clear_dir.Location = new System.Drawing.Point(213, 74);
            this.bt_clear_dir.Name = "bt_clear_dir";
            this.bt_clear_dir.Size = new System.Drawing.Size(20, 20);
            this.bt_clear_dir.TabIndex = 31;
            this.bt_clear_dir.Text = "C";
            this.bt_clear_dir.UseVisualStyleBackColor = true;
            this.bt_clear_dir.Click += new System.EventHandler(this.bt_clear_dir_Click);
            // 
            // bt_find_small_folders
            // 
            this.bt_find_small_folders.Font = new System.Drawing.Font("細明體", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_find_small_folders.Location = new System.Drawing.Point(1263, 71);
            this.bt_find_small_folders.Name = "bt_find_small_folders";
            this.bt_find_small_folders.Size = new System.Drawing.Size(94, 23);
            this.bt_find_small_folders.TabIndex = 32;
            this.bt_find_small_folders.Text = "找小資料夾";
            this.bt_find_small_folders.UseVisualStyleBackColor = true;
            this.bt_find_small_folders.Click += new System.EventHandler(this.bt_find_small_folders_Click);
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(1237, 75);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(23, 12);
            this.label3.TabIndex = 34;
            this.label3.Text = "MB";
            // 
            // textBox4
            // 
            this.textBox4.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.textBox4.Location = new System.Drawing.Point(1189, 67);
            this.textBox4.Name = "textBox4";
            this.textBox4.Size = new System.Drawing.Size(42, 30);
            this.textBox4.TabIndex = 33;
            this.textBox4.Text = "10";
            this.textBox4.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // bt_test
            // 
            this.bt_test.Font = new System.Drawing.Font("細明體", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_test.Location = new System.Drawing.Point(1593, 77);
            this.bt_test.Name = "bt_test";
            this.bt_test.Size = new System.Drawing.Size(75, 23);
            this.bt_test.TabIndex = 35;
            this.bt_test.Text = "TEST";
            this.bt_test.UseVisualStyleBackColor = true;
            this.bt_test.Click += new System.EventHandler(this.bt_test_Click);
            // 
            // bt_clear1
            // 
            this.bt_clear1.Font = new System.Drawing.Font("細明體", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_clear1.Location = new System.Drawing.Point(1248, 620);
            this.bt_clear1.Name = "bt_clear1";
            this.bt_clear1.Size = new System.Drawing.Size(63, 30);
            this.bt_clear1.TabIndex = 36;
            this.bt_clear1.Text = "清除";
            this.bt_clear1.UseVisualStyleBackColor = true;
            this.bt_clear1.Click += new System.EventHandler(this.bt_clear1_Click);
            // 
            // bt_clear2
            // 
            this.bt_clear2.Font = new System.Drawing.Font("細明體", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_clear2.Location = new System.Drawing.Point(1605, 620);
            this.bt_clear2.Name = "bt_clear2";
            this.bt_clear2.Size = new System.Drawing.Size(63, 30);
            this.bt_clear2.TabIndex = 37;
            this.bt_clear2.Text = "清除";
            this.bt_clear2.UseVisualStyleBackColor = true;
            this.bt_clear2.Click += new System.EventHandler(this.bt_clear2_Click);
            // 
            // bt_find_same_files2
            // 
            this.bt_find_same_files2.Font = new System.Drawing.Font("細明體", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_find_same_files2.Location = new System.Drawing.Point(1363, 70);
            this.bt_find_same_files2.Name = "bt_find_same_files2";
            this.bt_find_same_files2.Size = new System.Drawing.Size(144, 23);
            this.bt_find_same_files2.TabIndex = 38;
            this.bt_find_same_files2.Text = "找可能相同檔案";
            this.bt_find_same_files2.UseVisualStyleBackColor = true;
            this.bt_find_same_files2.Click += new System.EventHandler(this.bt_find_same_files2_Click);
            // 
            // checkBox3
            // 
            this.checkBox3.AutoSize = true;
            this.checkBox3.Checked = true;
            this.checkBox3.CheckState = System.Windows.Forms.CheckState.Checked;
            this.checkBox3.Location = new System.Drawing.Point(310, 65);
            this.checkBox3.Name = "checkBox3";
            this.checkBox3.Size = new System.Drawing.Size(72, 16);
            this.checkBox3.TabIndex = 41;
            this.checkBox3.Text = "磁碟資訊";
            this.checkBox3.UseVisualStyleBackColor = true;
            // 
            // cb_video_only
            // 
            this.cb_video_only.AutoSize = true;
            this.cb_video_only.Checked = true;
            this.cb_video_only.CheckState = System.Windows.Forms.CheckState.Checked;
            this.cb_video_only.Location = new System.Drawing.Point(461, 65);
            this.cb_video_only.Name = "cb_video_only";
            this.cb_video_only.Size = new System.Drawing.Size(60, 16);
            this.cb_video_only.TabIndex = 42;
            this.cb_video_only.Text = "看影片";
            this.cb_video_only.UseVisualStyleBackColor = true;
            this.cb_video_only.CheckedChanged += new System.EventHandler(this.cb_video_only_CheckedChanged);
            // 
            // cb_video_s
            // 
            this.cb_video_s.AutoSize = true;
            this.cb_video_s.Checked = true;
            this.cb_video_s.CheckState = System.Windows.Forms.CheckState.Checked;
            this.cb_video_s.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.cb_video_s.Location = new System.Drawing.Point(109, 21);
            this.cb_video_s.Name = "cb_video_s";
            this.cb_video_s.Size = new System.Drawing.Size(43, 20);
            this.cb_video_s.TabIndex = 43;
            this.cb_video_s.Text = "小";
            this.cb_video_s.UseVisualStyleBackColor = true;
            this.cb_video_s.CheckedChanged += new System.EventHandler(this.cb_video_s_CheckedChanged);
            // 
            // cb_generate_text
            // 
            this.cb_generate_text.AutoSize = true;
            this.cb_generate_text.Checked = true;
            this.cb_generate_text.CheckState = System.Windows.Forms.CheckState.Checked;
            this.cb_generate_text.Location = new System.Drawing.Point(310, 87);
            this.cb_generate_text.Name = "cb_generate_text";
            this.cb_generate_text.Size = new System.Drawing.Size(144, 16);
            this.cb_generate_text.TabIndex = 44;
            this.cb_generate_text.Text = "目錄下檔名轉出純文字";
            this.cb_generate_text.UseVisualStyleBackColor = true;
            this.cb_generate_text.CheckedChanged += new System.EventHandler(this.cb_generate_text_CheckedChanged);
            // 
            // checkBox7
            // 
            this.checkBox7.AutoSize = true;
            this.checkBox7.Checked = true;
            this.checkBox7.CheckState = System.Windows.Forms.CheckState.Checked;
            this.checkBox7.Location = new System.Drawing.Point(1526, 81);
            this.checkBox7.Name = "checkBox7";
            this.checkBox7.Size = new System.Drawing.Size(62, 16);
            this.checkBox7.TabIndex = 45;
            this.checkBox7.Text = "message";
            this.checkBox7.UseVisualStyleBackColor = true;
            this.checkBox7.CheckedChanged += new System.EventHandler(this.checkBox7_CheckedChanged);
            // 
            // groupBox_video
            // 
            this.groupBox_video.Controls.Add(this.cb_video_l);
            this.groupBox_video.Controls.Add(this.cb_video_m);
            this.groupBox_video.Controls.Add(this.cb_video_s);
            this.groupBox_video.Location = new System.Drawing.Point(521, 59);
            this.groupBox_video.Name = "groupBox_video";
            this.groupBox_video.Size = new System.Drawing.Size(160, 50);
            this.groupBox_video.TabIndex = 46;
            this.groupBox_video.TabStop = false;
            this.groupBox_video.Text = "影片大小";
            // 
            // cb_video_l
            // 
            this.cb_video_l.AutoSize = true;
            this.cb_video_l.Checked = true;
            this.cb_video_l.CheckState = System.Windows.Forms.CheckState.Checked;
            this.cb_video_l.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.cb_video_l.Location = new System.Drawing.Point(11, 21);
            this.cb_video_l.Name = "cb_video_l";
            this.cb_video_l.Size = new System.Drawing.Size(43, 20);
            this.cb_video_l.TabIndex = 45;
            this.cb_video_l.Text = "大";
            this.cb_video_l.UseVisualStyleBackColor = true;
            this.cb_video_l.CheckedChanged += new System.EventHandler(this.cb_video_l_CheckedChanged);
            // 
            // cb_video_m
            // 
            this.cb_video_m.AutoSize = true;
            this.cb_video_m.Checked = true;
            this.cb_video_m.CheckState = System.Windows.Forms.CheckState.Checked;
            this.cb_video_m.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.cb_video_m.Location = new System.Drawing.Point(60, 21);
            this.cb_video_m.Name = "cb_video_m";
            this.cb_video_m.Size = new System.Drawing.Size(43, 20);
            this.cb_video_m.TabIndex = 44;
            this.cb_video_m.Text = "中";
            this.cb_video_m.UseVisualStyleBackColor = true;
            this.cb_video_m.CheckedChanged += new System.EventHandler(this.cb_video_m_CheckedChanged);
            // 
            // groupBox_file
            // 
            this.groupBox_file.Controls.Add(this.cb_file_l);
            this.groupBox_file.Controls.Add(this.tb_file_s);
            this.groupBox_file.Controls.Add(this.cb_file_m);
            this.groupBox_file.Controls.Add(this.cb_file_s);
            this.groupBox_file.Controls.Add(this.tb_file_l);
            this.groupBox_file.Controls.Add(this.label2);
            this.groupBox_file.Location = new System.Drawing.Point(760, 59);
            this.groupBox_file.Name = "groupBox_file";
            this.groupBox_file.Size = new System.Drawing.Size(292, 50);
            this.groupBox_file.TabIndex = 47;
            this.groupBox_file.TabStop = false;
            this.groupBox_file.Text = "檔案大小";
            // 
            // cb_file_l
            // 
            this.cb_file_l.AutoSize = true;
            this.cb_file_l.Checked = true;
            this.cb_file_l.CheckState = System.Windows.Forms.CheckState.Checked;
            this.cb_file_l.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.cb_file_l.Location = new System.Drawing.Point(11, 21);
            this.cb_file_l.Name = "cb_file_l";
            this.cb_file_l.Size = new System.Drawing.Size(43, 20);
            this.cb_file_l.TabIndex = 45;
            this.cb_file_l.Text = "大";
            this.cb_file_l.UseVisualStyleBackColor = true;
            this.cb_file_l.CheckedChanged += new System.EventHandler(this.cb_file_l_CheckedChanged);
            // 
            // tb_file_s
            // 
            this.tb_file_s.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_file_s.Location = new System.Drawing.Point(210, 14);
            this.tb_file_s.Name = "tb_file_s";
            this.tb_file_s.Size = new System.Drawing.Size(52, 30);
            this.tb_file_s.TabIndex = 48;
            this.tb_file_s.Text = "10";
            this.tb_file_s.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // cb_file_m
            // 
            this.cb_file_m.AutoSize = true;
            this.cb_file_m.Checked = true;
            this.cb_file_m.CheckState = System.Windows.Forms.CheckState.Checked;
            this.cb_file_m.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.cb_file_m.Location = new System.Drawing.Point(60, 21);
            this.cb_file_m.Name = "cb_file_m";
            this.cb_file_m.Size = new System.Drawing.Size(43, 20);
            this.cb_file_m.TabIndex = 44;
            this.cb_file_m.Text = "中";
            this.cb_file_m.UseVisualStyleBackColor = true;
            this.cb_file_m.CheckedChanged += new System.EventHandler(this.cb_file_m_CheckedChanged);
            // 
            // cb_file_s
            // 
            this.cb_file_s.AutoSize = true;
            this.cb_file_s.Checked = true;
            this.cb_file_s.CheckState = System.Windows.Forms.CheckState.Checked;
            this.cb_file_s.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.cb_file_s.Location = new System.Drawing.Point(109, 21);
            this.cb_file_s.Name = "cb_file_s";
            this.cb_file_s.Size = new System.Drawing.Size(43, 20);
            this.cb_file_s.TabIndex = 43;
            this.cb_file_s.Text = "小";
            this.cb_file_s.UseVisualStyleBackColor = true;
            this.cb_file_s.CheckedChanged += new System.EventHandler(this.cb_file_s_CheckedChanged);
            // 
            // cb_file_size
            // 
            this.cb_file_size.AutoSize = true;
            this.cb_file_size.Checked = true;
            this.cb_file_size.CheckState = System.Windows.Forms.CheckState.Checked;
            this.cb_file_size.Location = new System.Drawing.Point(684, 65);
            this.cb_file_size.Name = "cb_file_size";
            this.cb_file_size.Size = new System.Drawing.Size(72, 16);
            this.cb_file_size.TabIndex = 49;
            this.cb_file_size.Text = "檔案大小";
            this.cb_file_size.UseVisualStyleBackColor = true;
            this.cb_file_size.CheckedChanged += new System.EventHandler(this.cb_file_size_CheckedChanged);
            // 
            // checkBox8
            // 
            this.checkBox8.AutoSize = true;
            this.checkBox8.Checked = true;
            this.checkBox8.CheckState = System.Windows.Forms.CheckState.Checked;
            this.checkBox8.Location = new System.Drawing.Point(1730, 77);
            this.checkBox8.Name = "checkBox8";
            this.checkBox8.Size = new System.Drawing.Size(72, 16);
            this.checkBox8.TabIndex = 51;
            this.checkBox8.Text = "滿30結束";
            this.checkBox8.UseVisualStyleBackColor = true;
            // 
            // bt_copy_rtb_data
            // 
            this.bt_copy_rtb_data.BackgroundImage = global::vcs_DrAP.Properties.Resources.clipboard;
            this.bt_copy_rtb_data.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_copy_rtb_data.Font = new System.Drawing.Font("細明體", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_copy_rtb_data.Location = new System.Drawing.Point(1605, 649);
            this.bt_copy_rtb_data.Name = "bt_copy_rtb_data";
            this.bt_copy_rtb_data.Size = new System.Drawing.Size(45, 45);
            this.bt_copy_rtb_data.TabIndex = 53;
            this.bt_copy_rtb_data.UseVisualStyleBackColor = true;
            this.bt_copy_rtb_data.Click += new System.EventHandler(this.bt_copy_rtb_data_Click);
            // 
            // bt_setup
            // 
            this.bt_setup.BackgroundImage = global::vcs_DrAP.Properties.Resources.setup;
            this.bt_setup.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_setup.Font = new System.Drawing.Font("細明體", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_setup.Location = new System.Drawing.Point(1824, 113);
            this.bt_setup.Name = "bt_setup";
            this.bt_setup.Size = new System.Drawing.Size(50, 50);
            this.bt_setup.TabIndex = 52;
            this.bt_setup.UseVisualStyleBackColor = true;
            this.bt_setup.Click += new System.EventHandler(this.bt_setup_Click);
            // 
            // bt_search_pattern_matlab
            // 
            this.bt_search_pattern_matlab.BackColor = System.Drawing.Color.White;
            this.bt_search_pattern_matlab.BackgroundImage = global::vcs_DrAP.Properties.Resources.matlab;
            this.bt_search_pattern_matlab.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_search_pattern_matlab.Font = new System.Drawing.Font("細明體", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_search_pattern_matlab.Location = new System.Drawing.Point(1674, 115);
            this.bt_search_pattern_matlab.Name = "bt_search_pattern_matlab";
            this.bt_search_pattern_matlab.Size = new System.Drawing.Size(50, 50);
            this.bt_search_pattern_matlab.TabIndex = 50;
            this.bt_search_pattern_matlab.UseVisualStyleBackColor = false;
            this.bt_search_pattern_matlab.Click += new System.EventHandler(this.bt_search_pattern_matlab_Click);
            // 
            // bt_save_rtb_data
            // 
            this.bt_save_rtb_data.BackgroundImage = global::vcs_DrAP.Properties.Resources.save_file;
            this.bt_save_rtb_data.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_save_rtb_data.Font = new System.Drawing.Font("細明體", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_save_rtb_data.Location = new System.Drawing.Point(1248, 649);
            this.bt_save_rtb_data.Name = "bt_save_rtb_data";
            this.bt_save_rtb_data.Size = new System.Drawing.Size(45, 45);
            this.bt_save_rtb_data.TabIndex = 40;
            this.bt_save_rtb_data.UseVisualStyleBackColor = true;
            this.bt_save_rtb_data.Click += new System.EventHandler(this.bt_save_rtb_data_Click);
            // 
            // bt_search_pattern_python
            // 
            this.bt_search_pattern_python.BackgroundImage = global::vcs_DrAP.Properties.Resources.python;
            this.bt_search_pattern_python.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_search_pattern_python.Font = new System.Drawing.Font("細明體", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_search_pattern_python.Location = new System.Drawing.Point(1674, 59);
            this.bt_search_pattern_python.Name = "bt_search_pattern_python";
            this.bt_search_pattern_python.Size = new System.Drawing.Size(50, 50);
            this.bt_search_pattern_python.TabIndex = 39;
            this.bt_search_pattern_python.UseVisualStyleBackColor = true;
            this.bt_search_pattern_python.Click += new System.EventHandler(this.bt_search_pattern_python_Click);
            // 
            // bt_search_pattern_vcs
            // 
            this.bt_search_pattern_vcs.BackgroundImage = global::vcs_DrAP.Properties.Resources.vcs;
            this.bt_search_pattern_vcs.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_search_pattern_vcs.Font = new System.Drawing.Font("細明體", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_search_pattern_vcs.Location = new System.Drawing.Point(1674, 6);
            this.bt_search_pattern_vcs.Name = "bt_search_pattern_vcs";
            this.bt_search_pattern_vcs.Size = new System.Drawing.Size(50, 50);
            this.bt_search_pattern_vcs.TabIndex = 26;
            this.bt_search_pattern_vcs.UseVisualStyleBackColor = true;
            this.bt_search_pattern_vcs.Click += new System.EventHandler(this.bt_search_pattern_vcs_Click);
            // 
            // bt_delete_file
            // 
            this.bt_delete_file.BackgroundImage = global::vcs_DrAP.Properties.Resources.delete;
            this.bt_delete_file.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_delete_file.Font = new System.Drawing.Font("細明體", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_delete_file.Location = new System.Drawing.Point(940, 6);
            this.bt_delete_file.Name = "bt_delete_file";
            this.bt_delete_file.Size = new System.Drawing.Size(50, 50);
            this.bt_delete_file.TabIndex = 22;
            this.bt_delete_file.UseVisualStyleBackColor = true;
            this.bt_delete_file.Click += new System.EventHandler(this.bt_delete_file_Click);
            // 
            // bt_start_files
            // 
            this.bt_start_files.BackgroundImage = global::vcs_DrAP.Properties.Resources.potplayer;
            this.bt_start_files.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_start_files.Font = new System.Drawing.Font("細明體", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_start_files.Location = new System.Drawing.Point(420, 6);
            this.bt_start_files.Name = "bt_start_files";
            this.bt_start_files.Size = new System.Drawing.Size(50, 50);
            this.bt_start_files.TabIndex = 15;
            this.bt_start_files.UseVisualStyleBackColor = true;
            this.bt_start_files.Click += new System.EventHandler(this.bt_start_files_Click);
            // 
            // bt_open_dir
            // 
            this.bt_open_dir.BackgroundImage = global::vcs_DrAP.Properties.Resources.open_folder;
            this.bt_open_dir.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_open_dir.Font = new System.Drawing.Font("細明體", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_open_dir.Location = new System.Drawing.Point(252, 56);
            this.bt_open_dir.Name = "bt_open_dir";
            this.bt_open_dir.Size = new System.Drawing.Size(50, 50);
            this.bt_open_dir.TabIndex = 11;
            this.bt_open_dir.UseVisualStyleBackColor = true;
            this.bt_open_dir.Click += new System.EventHandler(this.bt_open_dir_Click);
            // 
            // bt_save_data
            // 
            this.bt_save_data.BackgroundImage = global::vcs_DrAP.Properties.Resources.save_file;
            this.bt_save_data.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_save_data.Font = new System.Drawing.Font("細明體", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_save_data.Location = new System.Drawing.Point(480, 6);
            this.bt_save_data.Name = "bt_save_data";
            this.bt_save_data.Size = new System.Drawing.Size(50, 50);
            this.bt_save_data.TabIndex = 7;
            this.bt_save_data.UseVisualStyleBackColor = true;
            this.bt_save_data.Click += new System.EventHandler(this.bt_save_data_Click);
            // 
            // bt_find_empty_folders
            // 
            this.bt_find_empty_folders.Font = new System.Drawing.Font("細明體", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_find_empty_folders.Location = new System.Drawing.Point(1363, 17);
            this.bt_find_empty_folders.Name = "bt_find_empty_folders";
            this.bt_find_empty_folders.Size = new System.Drawing.Size(144, 23);
            this.bt_find_empty_folders.TabIndex = 54;
            this.bt_find_empty_folders.Text = "找空資料夾";
            this.bt_find_empty_folders.UseVisualStyleBackColor = true;
            this.bt_find_empty_folders.Click += new System.EventHandler(this.bt_find_empty_folders_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1886, 1008);
            this.Controls.Add(this.bt_find_empty_folders);
            this.Controls.Add(this.bt_copy_rtb_data);
            this.Controls.Add(this.bt_setup);
            this.Controls.Add(this.checkBox8);
            this.Controls.Add(this.bt_search_pattern_matlab);
            this.Controls.Add(this.cb_file_size);
            this.Controls.Add(this.groupBox_file);
            this.Controls.Add(this.groupBox_video);
            this.Controls.Add(this.checkBox7);
            this.Controls.Add(this.cb_generate_text);
            this.Controls.Add(this.cb_video_only);
            this.Controls.Add(this.checkBox3);
            this.Controls.Add(this.bt_save_rtb_data);
            this.Controls.Add(this.bt_search_pattern_python);
            this.Controls.Add(this.bt_find_same_files2);
            this.Controls.Add(this.bt_clear2);
            this.Controls.Add(this.bt_clear1);
            this.Controls.Add(this.bt_test);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.textBox4);
            this.Controls.Add(this.bt_find_small_folders);
            this.Controls.Add(this.bt_clear_dir);
            this.Controls.Add(this.bt_remove_dir);
            this.Controls.Add(this.listBox1);
            this.Controls.Add(this.bt_add_dir);
            this.Controls.Add(this.bt_find_same_files);
            this.Controls.Add(this.bt_search_pattern_vcs);
            this.Controls.Add(this.textBox3);
            this.Controls.Add(this.bt_delete_file);
            this.Controls.Add(this.bt_find_big_files);
            this.Controls.Add(this.tb_search_text_pattern);
            this.Controls.Add(this.richTextBox2);
            this.Controls.Add(this.checkBox2);
            this.Controls.Add(this.bt_start_files);
            this.Controls.Add(this.listView1);
            this.Controls.Add(this.bt_open_dir);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.bt_help);
            this.Controls.Add(this.bt_save_data);
            this.Controls.Add(this.bt_copy_data);
            this.Controls.Add(this.bt_clear_data);
            this.Controls.Add(this.bt_search_one_layer_files);
            this.Controls.Add(this.bt_search_all_files);
            this.Controls.Add(this.comboBox1);
            this.Controls.Add(this.label1);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Name = "Form1";
            this.Text = "DrAP";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.Form1_FormClosing);
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox_video.ResumeLayout(false);
            this.groupBox_video.PerformLayout();
            this.groupBox_file.ResumeLayout(false);
            this.groupBox_file.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.ComboBox comboBox1;
        private System.Windows.Forms.Button bt_search_all_files;
        private System.Windows.Forms.Button bt_search_one_layer_files;
        private System.Windows.Forms.Button bt_clear_data;
        private System.Windows.Forms.Button bt_help;
        private System.Windows.Forms.Button bt_save_data;
        private System.Windows.Forms.Button bt_copy_data;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Button bt_open_dir;
        private System.Windows.Forms.FolderBrowserDialog folderBrowserDialog1;
        private System.Windows.Forms.SaveFileDialog saveFileDialog1;
        private System.Windows.Forms.ListView listView1;
        private System.Windows.Forms.Button bt_start_files;
        private System.Windows.Forms.CheckBox checkBox2;
        private System.Windows.Forms.TextBox tb_file_l;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.RichTextBox richTextBox2;
        private System.Windows.Forms.TextBox tb_search_text_pattern;
        private System.Windows.Forms.Button bt_find_big_files;
        private System.Windows.Forms.Button bt_delete_file;
        private System.Windows.Forms.TextBox textBox3;
        private System.Windows.Forms.Button bt_search_pattern_vcs;
        private System.Windows.Forms.Button bt_find_same_files;
        private System.Windows.Forms.Button bt_add_dir;
        private System.Windows.Forms.ListBox listBox1;
        private System.Windows.Forms.Button bt_remove_dir;
        private System.Windows.Forms.Button bt_clear_dir;
        private System.Windows.Forms.Button bt_find_small_folders;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.TextBox textBox4;
        private System.Windows.Forms.Button bt_test;
        private System.Windows.Forms.Button bt_clear1;
        private System.Windows.Forms.Button bt_clear2;
        private System.Windows.Forms.Button bt_find_same_files2;
        private System.Windows.Forms.Button bt_search_pattern_python;
        private System.Windows.Forms.Button bt_save_rtb_data;
        private System.Windows.Forms.CheckBox checkBox3;
        private System.Windows.Forms.CheckBox cb_video_only;
        private System.Windows.Forms.CheckBox cb_video_s;
        private System.Windows.Forms.CheckBox cb_generate_text;
        private System.Windows.Forms.CheckBox checkBox7;
        private System.Windows.Forms.GroupBox groupBox_video;
        private System.Windows.Forms.CheckBox cb_video_l;
        private System.Windows.Forms.CheckBox cb_video_m;
        private System.Windows.Forms.GroupBox groupBox_file;
        private System.Windows.Forms.CheckBox cb_file_l;
        private System.Windows.Forms.CheckBox cb_file_m;
        private System.Windows.Forms.CheckBox cb_file_s;
        private System.Windows.Forms.TextBox tb_file_s;
        private System.Windows.Forms.CheckBox cb_file_size;
        private System.Windows.Forms.Button bt_search_pattern_matlab;
        private System.Windows.Forms.CheckBox checkBox8;
        private System.Windows.Forms.Button bt_setup;
        private System.Windows.Forms.Button bt_copy_rtb_data;
        private System.Windows.Forms.Button bt_find_empty_folders;
    }
}

