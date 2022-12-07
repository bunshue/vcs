using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace IMSCap2
{
    public partial class Form1 : Form
    {
        private const int S_OK = 0;     //system return OK
        private const int S_FALSE = 1;     //system return FALSE
        private const int LAYER0_WIDTH = 1920;
        private const int LAYER0_HEIGHT = 1080;
        private const int LAYER1_WIDTH = 1216;
        private const int LAYER1_HEIGHT = 912;
        private const int LAYER2_WIDTH = 640;
        private const int LAYER2_HEIGHT = 480;
        //private const int LAYER3_WIDTH = 1920;
        //private const int LAYER3_HEIGHT = 1080;
        private const int LAYER1_START_X = (LAYER0_WIDTH - LAYER1_WIDTH - BORDER_X);
        private const int LAYER1_START_Y = BORDER_Y;
        private const int LAYER2_START_X = BORDER_X;
        private const int LAYER2_START_Y = (LAYER0_HEIGHT - LAYER2_HEIGHT - BORDER_Y);
        private const int BORDER_X = 16;
        private const int BORDER_Y = 16;
        private const int OFFSET_X = 70;
        private const int WIDTH1 = 150;
        private const int WIDTH2 = 370;
        private const int THICK1 = 40;
        private const int CAMERA_INFO_POS_X1 = 670;
        private const int CAMERA_INFO_POS_X2 = CAMERA_INFO_POS_X1 + 550;
        private const int CAMERA_INFO_POS_X3 = CAMERA_INFO_POS_X1 + 740;
        private const int CAMERA_INFO_POS_Y1 = 950 - 11;
        private const int CAMERA_INFO_POS_Y2 = 950 - 11 + 34;
        private const int CAMERA_INFO_POS_Y3 = 950 - 11 + 68;
        private const int ICON_LINEWDITH = 5; //設定按鈕畫線線寬
        private const int ICON_W = 50; //設定按鈕大小 W
        private const int ICON_H = 50; //設定按鈕大小 H

        //第一群Label, 指示用Label
        Label lb_1_id = new Label();
        Label lb_1_name = new Label();
        Label lb_1_sex = new Label();
        Label lb_1_birthday = new Label();
        Label lb_1_age = new Label();

        //第二群Label, 顯示結果用Label
        Label lb_2_id = new Label();
        Label lb_2_name = new Label();
        Label lb_2_sex = new Label();
        Label lb_2_birthday = new Label();
        Label lb_2_age = new Label();
        Label lb_2_id2 = new Label();
        Label lb_2_name2 = new Label();
        Label lb_2_sex2 = new Label();
        Label lb_2_birthday2 = new Label();
        Label lb_2_age2 = new Label();
        Label lb_2_endoscope2 = new Label();

        TextBox tb_id = new TextBox();
        TextBox tb_name = new TextBox();
        TextBox tb_sex = new TextBox();
        TextBox tb_birthday = new TextBox();
        TextBox tb_age = new TextBox();

        Button bt_id = new Button();
        Button bt_name = new Button();
        Button bt_sex = new Button();
        Button bt_birthday = new Button();
        Button bt_age = new Button();
        Button bt_endoscope = new Button();
        Button bt_record = new Button();
        Button bt_capture = new Button();
        Button bt_setup = new Button();

        Label lb_1_date = new Label();
        Label lb_1_time = new Label();
        Label lb_serial = new Label();
        Label lb_version = new Label();     //可能沒有用了

        Color background_color = Color.White;
        Font font = new Font("新細明體", 20.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(136)));

        //Font font = new Font("Times New Roman", 18, FontStyle.Bold));
        //((Label)c).Font = new Font("Courier New", 18, FontStyle.Bold);  //建立字體對象
        //((Label)c).Font = new Font("Arial", 18, FontStyle.Bold);  //建立字體對象
        //((Label)c).Font = new Font("Times New Roman", 18, FontStyle.Bold);  //建立字體對象
        //this.lb_ims2.Font = new System.Drawing.Font("新細明體", 20.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(136)));

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        void setup_controls()
        {
            //this.BackColor = Color.Black;
            int w = 160;
            int h = 40;
            int dx = w + 5;
            int dy = h + 5;

            lb_1_id.Name = "lb_1_id";
            lb_1_name.Name = "lb_1_name";
            lb_1_sex.Name = "lb_1_sex";
            lb_1_birthday.Name = "lb_1_birthday";
            lb_1_age.Name = "lb_1_age";
            lb_1_date.Name = "lb_1_date";
            lb_1_time.Name = "lb_1_time";
            lb_serial.Name = "lb_serial";

            lb_1_id.Text = "ID NO:";
            lb_1_name.Text = "NAME:";
            lb_1_sex.Text = "SEX:";
            lb_1_birthday.Text = "Birthday:";
            lb_1_age.Text = "Age:";
            lb_1_date.Text = "12/05/2022 Mon";
            lb_1_time.Text = "13:53:55";
            lb_serial.Text = "EGD NO:  N2201001A0001";

            this.Controls.Add(lb_1_id);
            this.Controls.Add(lb_1_name);
            this.Controls.Add(lb_1_sex);
            this.Controls.Add(lb_1_birthday);
            this.Controls.Add(lb_1_age);
            this.Controls.Add(lb_1_date);
            this.Controls.Add(lb_1_time);
            this.Controls.Add(lb_serial);

            lb_2_id.Name = "lb_2_id";
            lb_2_name.Name = "lb_2_name";
            lb_2_sex.Name = "lb_2_sex";
            lb_2_birthday.Name = "lb_2_birthday";
            lb_2_age.Name = "lb_2_age";

            lb_2_id2.Name = "lb_2_id";
            lb_2_name2.Name = "lb_2_name";
            lb_2_sex2.Name = "lb_2_sex";
            lb_2_birthday2.Name = "lb_2_birthday";
            lb_2_age2.Name = "lb_2_age";
            lb_2_endoscope2.Name = "lb_2_endoscope2";

            this.Controls.Add(lb_2_id);
            this.Controls.Add(lb_2_name);
            this.Controls.Add(lb_2_sex);
            this.Controls.Add(lb_2_birthday);
            this.Controls.Add(lb_2_age);
            this.Controls.Add(lb_2_id2);
            this.Controls.Add(lb_2_name2);
            this.Controls.Add(lb_2_sex2);
            this.Controls.Add(lb_2_birthday2);
            this.Controls.Add(lb_2_age2);
            this.Controls.Add(lb_2_endoscope2);

            tb_id.Name = "tb_id";
            tb_name.Name = "tb_name";
            tb_sex.Name = "tb_sex";
            tb_birthday.Name = "tb_birthday";
            tb_age.Name = "tb_age";

            this.Controls.Add(tb_id);
            this.Controls.Add(tb_name);
            this.Controls.Add(tb_sex);
            this.Controls.Add(tb_birthday);
            this.Controls.Add(tb_age);

            bt_id.Name = "bt_id";
            bt_name.Name = "bt_name";
            bt_sex.Name = "bt_sex";
            bt_birthday.Name = "bt_birthday";
            bt_age.Name = "bt_age";
            bt_endoscope.Name = "bt_endoscope";
            bt_record.Name = "bt_record";
            bt_capture.Name = "bt_capture";
            bt_setup.Name = "bt_setup";

            /*
            bt_id.Text = "ID NO:";
            bt_name.Text = "NAME:";
            bt_sex.Text = "SEX:";
            bt_birthday.Text = "Birthday:";
            bt_age.Text = "Age:";
            bt_endoscope.Text ="EGD No.";
            bt_record.Text = Record";
            bt_capture.Text ="Capture";
            bt_setup.Text = "Setup";
            */

            this.Controls.Add(bt_id);
            this.Controls.Add(bt_name);
            this.Controls.Add(bt_sex);
            this.Controls.Add(bt_birthday);
            this.Controls.Add(bt_age);
            this.Controls.Add(bt_endoscope);
            this.Controls.Add(bt_record);
            this.Controls.Add(bt_capture);
            this.Controls.Add(bt_setup);

            bt_id.BackgroundImage = Properties.Resources.image_id;
            bt_name.BackgroundImage = Properties.Resources.image_name;
            bt_sex.BackgroundImage = Properties.Resources.image_sex_male;
            bt_birthday.BackgroundImage = Properties.Resources.image_birthday;
            bt_age.BackgroundImage = Properties.Resources.image_age;
            bt_endoscope.BackgroundImage = Properties.Resources.image_endoscope;
            bt_record.BackgroundImage = Properties.Resources.image_record;
            bt_capture.BackgroundImage = Properties.Resources.image_capture;
            bt_setup.BackgroundImage = Properties.Resources.image_setup1;

            bt_id.BackgroundImageLayout = ImageLayout.Zoom;
            bt_name.BackgroundImageLayout = ImageLayout.Zoom;
            bt_sex.BackgroundImageLayout = ImageLayout.Zoom;
            bt_birthday.BackgroundImageLayout = ImageLayout.Zoom;
            bt_age.BackgroundImageLayout = ImageLayout.Zoom;
            bt_endoscope.BackgroundImageLayout = ImageLayout.Zoom;
            bt_record.BackgroundImageLayout = ImageLayout.Zoom;
            bt_capture.BackgroundImageLayout = ImageLayout.Zoom;
            bt_setup.BackgroundImageLayout = ImageLayout.Zoom;

            //控件的共通設定

            foreach (Control c in this.Controls)  //撈出所有控件
            {
                //richTextBox1.Text += c.GetType().Name;

                if (c.GetType().Name == "Label")   //判斷是否為 Label 控件
                {
                    if (((Label)c).Name[3] == '1')
                    {
                        w = 120;
                        h = 35;

                        ((Label)c).Size = new Size(w, h);  //設定大小
                        ((Label)c).Font = font;
                        ((Label)c).TextAlign = ContentAlignment.MiddleLeft;
                        ((Label)c).ForeColor = Color.White;
                    }
                    else if (((Label)c).Name[3] == '2')
                    {
                        w = 180;
                        h = 35;

                        ((Label)c).Size = new Size(w, h);  //設定大小
                        ((Label)c).Font = font;
                        ((Label)c).TextAlign = ContentAlignment.MiddleLeft;
                        ((Label)c).ForeColor = Color.White;
                        //((Label)c).BackColor = Color.Pink;
                    }
                    else if (((Label)c).Name == "lb_serial")
                    {
                        w = 350;
                        h = 35;

                        ((Label)c).Size = new Size(w, h);  //設定大小
                        ((Label)c).Font = font;
                        ((Label)c).TextAlign = ContentAlignment.MiddleLeft;
                        ((Label)c).ForeColor = Color.White;
                    }
                }
                else if (c.GetType().Name == "TextBox")   //判斷是否為 TextBox 控件
                {
                    w = 230;
                    h = 35;

                    ((TextBox)c).Size = new Size(w, h);  //設定大小
                    ((TextBox)c).BackColor = background_color;
                    ((TextBox)c).Font = font;
                    ((TextBox)c).TextAlign = HorizontalAlignment.Left;
                }
                else if (c.GetType().Name == "Button")   //判斷是否為 Button 控件
                {
                    w = 64;
                    h = 64;

                    ((Button)c).Size = new Size(w, h);  //設定大小
                    ((Button)c).BackColor = background_color;
                    //((TextBox)c).Font = font;
                    //((Button)c).TextAlign = ContentAlignment.MiddleLeft;
                }
            }

            int x;
            int y;
            int THICK1 = 40;
            //int OFFSET = WIDTH1;    //useless

            x = BORDER_X;
            y = BORDER_Y + THICK1 * 0;
            x = OFFSET_X + BORDER_X;
            lb_1_id.Location = new Point(x, y);
            x += 150;
            //tb_id.Size = new Size(300, 30);
            tb_id.Location = new Point(x + 200, y);
            lb_2_id.Location = new Point(x, y);

            x = BORDER_X;
            y = BORDER_Y + THICK1 * 1;
            x = OFFSET_X + BORDER_X;
            y = BORDER_Y + THICK1 * 1;
            lb_1_name.Location = new Point(x, y);
            x += 150;
            //tb_name.Size = new Size(300, 30);
            tb_name.Location = new Point(x + 200, y);
            lb_2_name.Location = new Point(x, y);

            x = BORDER_X;
            y = BORDER_Y + THICK1 * 3;
            x = OFFSET_X + BORDER_X;
            y = BORDER_Y + THICK1 * 3;
            lb_1_sex.Location = new Point(x, y);
            x += 150;
            //tb_sex.Size = new Size(300, 30);
            tb_sex.Location = new Point(x + 200, y);
            lb_2_sex.Location = new Point(x, y);

            x = BORDER_X;
            y = BORDER_Y + THICK1 * 4;
            x = OFFSET_X + BORDER_X;
            y = BORDER_Y + THICK1 * 4;
            lb_1_birthday.Location = new Point(x, y);
            x += 150;
            //tb_birthday.Size = new Size(300, 30);
            tb_birthday.Location = new Point(x + 200, y);
            lb_2_birthday.Location = new Point(x, y);

            x = OFFSET_X + BORDER_X;
            y = BORDER_Y + THICK1 * 5;
            lb_1_age.Location = new Point(x, y);
            x += 150;
            //tb_age.Size = new Size(300, 30);
            tb_age.Location = new Point(x + 200, y);
            lb_2_age.Location = new Point(x, y);

            string[] Day = new string[] { "Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat" };
            string weekday = Day[Convert.ToInt32(DateTime.Now.DayOfWeek.ToString("d"))].ToString();

            string current_date = DateTime.Now.ToString("MM/dd/yyyy ") + weekday;
            //richTextBox1.Text += current_date + "\n";
            string current_time = DateTime.Now.ToString("HH:mm:ss");
            //richTextBox1.Text += current_time + "\n";

            x = BORDER_X;
            y = BORDER_Y + THICK1 * 7;
            lb_1_date.Location = new Point(x, y);
            lb_1_date.Text = current_date;

            x = BORDER_X;
            y = BORDER_Y + THICK1 * 8;
            lb_1_time.Location = new Point(x, y);
            lb_1_time.Text = current_time;

            x = BORDER_X;
            y = BORDER_Y + THICK1 * 9;
            lb_serial.Location = new Point(x, y);

            /*
            x = BORDER_X;
            y = BORDER_Y + THICK1 * 10;
            lb_main_mesg1.Location = new Point(x, y);
            lb_main_mesg1.Text = "";
            */

            x = BORDER_X + 350;
            y = BORDER_Y + THICK1 * 13;
            lb_ims1.Location = new Point(x, y);

            x = 1920 - BORDER_X * 1 - 200;
            y = 1080 - BORDER_Y * 2 - 5;
            lb_ims2.Location = new Point(x, y);

            /*
            textBox0.Visible = false;
            textBox1.Visible = false;
            textBox3.Visible = false;
            label0_data.Text = "";
            label1_data.Text = "";
            label2_data.Text = "";
            label3_data.Text = "";
            label4_data.Text = "";
            label0_data.Visible = false;
            label1_data.Visible = false;
            label2_data.Visible = false;
            label3_data.Visible = false;
            label4_data.Visible = false;
            */

            int x_st = BORDER_X;
            int y_st = 20;

            x_st = BORDER_X; ;
            y_st = BORDER_Y + THICK1 * 15;
            w = 64;
            h = 64;
            dx = w + 10;
            dy = h + 10;
            bt_id.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            bt_name.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            bt_sex.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            bt_birthday.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            bt_age.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            bt_endoscope.Location = new Point(x_st + dx * 0, y_st + dy * 5);

            lb_2_id2.Location = new Point(x_st + dx * 0 + 80, y_st + dy * 0);
            lb_2_name2.Location = new Point(x_st + dx * 0 + 80, y_st + dy * 1);
            lb_2_sex2.Location = new Point(x_st + dx * 0 + 80, y_st + dy * 2);
            lb_2_birthday2.Location = new Point(x_st + dx * 0 + 80, y_st + dy * 3);
            lb_2_age2.Location = new Point(x_st + dx * 0 + 80, y_st + dy * 4);
            lb_2_endoscope2.Location = new Point(x_st + dx * 0 + 80, y_st + dy * 5);

            bt_record.Location = new Point(x_st + dx * 7, y_st + dy * 0);
            bt_capture.Location = new Point(x_st + dx * 7, y_st + dy * 1);
            bt_setup.Location = new Point(x_st + dx * 7, y_st + dy * 2);

            lb_2_id.Text = "D021120903";
            lb_2_name.Text = "哆啦A夢";
            lb_2_sex.Text = "男";
            lb_2_birthday.Text = "9/3/2112";
            lb_2_age.Text = "-90";
            lb_2_id2.Text = "D021120903";
            lb_2_name2.Text = "哆啦A夢";
            lb_2_sex2.Text = "男";
            lb_2_birthday2.Text = "9/3/2112";
            lb_2_age2.Text = "-90";

            lb_2_endoscope2.Size = new Size(340, 35);
            lb_2_endoscope2.Text = "EGD NO: N2201001A0001";

            tb_id.Text = "D021141202";
            tb_name.Text = "哆啦美";
            tb_sex.Text = "女";
            tb_birthday.Text = "12/2/2114";
            tb_age.Text = "-92";
        }

        void show_item_location()
        {
            int W = LAYER0_WIDTH;
            int H = LAYER0_HEIGHT;

            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;  // 設定表單最大化
            this.BackColor = Color.Black;
            this.Size = new Size(W, H);

            int w = 640 * 19 / 10;
            int h = 480 * 19 / 10;

            pictureBox1.Size = new Size(w, h);
            pictureBox1.BackColor = Color.Gray;
            pictureBox1.Location = new Point(LAYER1_START_X, LAYER1_START_Y);
            pictureBox1.BackgroundImageLayout = ImageLayout.Zoom;
            pictureBox1.BackgroundImage = Properties.Resources.image_ims;

            pictureBox2.Size = new Size(LAYER2_WIDTH, LAYER2_HEIGHT);
            pictureBox2.BackColor = Color.Gray;
            pictureBox2.Location = new Point(LAYER2_START_X, LAYER2_START_Y);
            pictureBox2.Visible = false;


            pictureBox3.Size = new Size(261, 75);
            //pictureBox3.BackColor = Color.Gray;
            Image ims_small = Properties.Resources.image_ims_small;
            pictureBox3.Image = ims_small;
            pictureBox3.Location = new Point(LAYER0_WIDTH - ims_small.Width - BORDER_X * 1, LAYER0_HEIGHT - ims_small.Height - BORDER_Y * 2 - 15);
            pictureBox3.Visible = true;

            /*
                            richTextBox1.Visible = false;
                            bt_clear.Visible = false;
                            lb_fps.Visible = false;
                            lb_main_mesg1.Visible = false;
                            groupBox1.Visible = false;
            */

            setup_controls();
        }

        void Update_Clock()
        {
            string[] Day = new string[] { "Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat" };
            string weekday = Day[Convert.ToInt32(DateTime.Now.DayOfWeek.ToString("d"))].ToString();

            string current_date = DateTime.Now.ToString("MM/dd/yyyy ") + weekday;
            //richTextBox1.Text += current_date + "\n";
            string current_time = DateTime.Now.ToString("HH:mm:ss");
            //richTextBox1.Text += current_time + "\n";

            lb_1_date.Text = current_date;
            lb_1_time.Text = current_time;
            /*
            label5.Text = current_date;
            label6.Text = current_time;
            label5b.Text = current_date;
            label6b.Text = current_time;
            */
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            Update_Clock();
        }
    }
}
