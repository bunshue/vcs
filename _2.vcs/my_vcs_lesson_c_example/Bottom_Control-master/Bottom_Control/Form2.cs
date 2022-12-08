using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

using Bottom_Control.PLC通讯协议;
using Bottom_Control.基本控件;
using Bottom_Control.按钮__TO__PLC方法;
using CCWin.SkinClass;

namespace Bottom_Control
{
    public partial class Form2 : Form
    {
        private const int S_OK = 0;     //system return OK
        private const int S_FALSE = 1;     //system return FALSE

        public Form2()
        {
            InitializeComponent();
        }

        private void Form2_Load(object sender, EventArgs e)
        {
            this.plC_Open_Time1.Enabled = true;
            this.plC_Open_Time1.Start();

            show_item_location();
        }

        void show_item_location()
        {
            lb_main_mesg1.Visible = true;
            lb_main_mesg1.Text = "";
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
            bt_copy_to_clipboard.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width * 2, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
            bt_copy_to_clipboard.BackgroundImage = Properties.Resources.clipboard;
            bt_copy_to_clipboard.BackgroundImageLayout = ImageLayout.Zoom;
            cb_random.Checked = true;

            lb_plc_mesg.Location = new Point(groupBox_plc_status.Location.X + 200, groupBox_plc_status.Location.Y + 155);

            int x_st = 10;
            int y_st = 15;
            int dx = 400;
            int dy = 30;
            int w = 30;
            int h = 30;
            pbx_m10000.Size = new Size(w, h);
            pbx_m10001.Size = new Size(w, h);
            pbx_m10002.Size = new Size(w, h);
            pbx_m12000.Size = new Size(w, h);
            pbx_m12001.Size = new Size(w, h);
            pbx_m12002.Size = new Size(w, h);
            pbx_m10000.Location = new Point(x_st + dx * 0, y_st + dy * 0 - 5);
            pbx_m10001.Location = new Point(x_st + dx * 0, y_st + dy * 1 - 5);
            pbx_m10002.Location = new Point(x_st + dx * 0, y_st + dy * 2 - 5);
            pbx_m12000.Location = new Point(x_st + dx * 1, y_st + dy * 0 - 5);
            pbx_m12001.Location = new Point(x_st + dx * 1, y_st + dy * 1 - 5);
            pbx_m12002.Location = new Point(x_st + dx * 1, y_st + dy * 2 - 5);
            pbx_m10000.BackgroundImageLayout = ImageLayout.Zoom;
            pbx_m10001.BackgroundImageLayout = ImageLayout.Zoom;
            pbx_m10002.BackgroundImageLayout = ImageLayout.Zoom;
            pbx_m12000.BackgroundImageLayout = ImageLayout.Zoom;
            pbx_m12001.BackgroundImageLayout = ImageLayout.Zoom;
            pbx_m12002.BackgroundImageLayout = ImageLayout.Zoom;
            pbx_m10000.BackgroundImage = Properties.Resources.ball_gray;
            pbx_m10001.BackgroundImage = Properties.Resources.ball_gray;
            pbx_m10002.BackgroundImage = Properties.Resources.ball_gray;
            pbx_m12000.BackgroundImage = Properties.Resources.ball_gray;
            pbx_m12001.BackgroundImage = Properties.Resources.ball_gray;
            pbx_m12002.BackgroundImage = Properties.Resources.ball_gray;

            pbx_plc_status.Size = new Size(w*3, h*3);
            pbx_plc_status.Location = new Point(x_st + dx * 2-90, y_st + dy * 3 - 30);
            pbx_plc_status.BackgroundImageLayout = ImageLayout.Zoom;
            pbx_plc_status.BackgroundImage = Properties.Resources.ball_green;

            x_st = 40;
            lb_plc_pc0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            lb_plc_pc1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            lb_plc_pc2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            lb_plc_pc3a.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            lb_plc_pc4a.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            lb_plc_pc3b.Location = new Point(x_st + dx * 0 + 160, y_st + dy * 3);
            lb_plc_pc4b.Location = new Point(x_st + dx * 0 + 160, y_st + dy * 4);
            lb_pc_plc0.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            lb_pc_plc1.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            lb_pc_plc2.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            lb_pc_plc3a.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            lb_pc_plc4a.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            lb_pc_plc3b.Location = new Point(x_st + dx * 1 + 160, y_st + dy * 3);
            lb_pc_plc4b.Location = new Point(x_st + dx * 1 + 160, y_st + dy * 4);

            lb_plc_pc0.Text = "M10000 PLC -> PC 動作要求";
            lb_plc_pc1.Text = "M10001 PLC -> PC 確認完成";
            lb_plc_pc2.Text = "M10002 PLC -> PC 收到動作完成";
            lb_pc_plc0.Text = "M12000 PC -> PLC 收到動作要求";
            lb_pc_plc1.Text = "M12001 PC -> PLC 確認開始";
            lb_pc_plc2.Text = "M12002 PC -> PLC 動作完成";
            lb_plc_pc3a.Text = "ID資料    D2000";
            lb_plc_pc4a.Text = "收到結果D2010";
            lb_plc_pc3b.Text = "";
            lb_plc_pc4b.Text = "";
            lb_pc_plc3a.Text = "ID資料    D8000";
            lb_pc_plc4a.Text = "檢測結果D8010";
            lb_pc_plc3b.Text = "";
            lb_pc_plc4b.Text = "";
            lb_plc_mesg.Text = "";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            show_main_message1("讀取 D2000", S_OK, 30);
            string contact_point = "D";
            string contact_address = "2000";
            string data_read = read_data_from_plc_d_register(contact_point, contact_address);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            show_main_message1("寫入 D8000", S_OK, 30);
            string contact_point = "D";
            string contact_address = "8000";
            string write_data = tb_data_to_write.Text;
            tb_data_to_write.Text = "";

            write_data_to_plc_d_register(contact_point, contact_address, write_data);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            show_main_message1("讀取 D8000", S_OK, 30);
            string contact_point = "D";
            string contact_address = "8000";
            string data_read = read_data_from_plc_d_register(contact_point, contact_address);
        }

        private void bt_generate_Click(object sender, EventArgs e)
        {
            if (cb_random.Checked == true)
            {
                make_random_data();
            }
            else
            {
                string finalString1 = "A1234567B1234";
                richTextBox1.Text += "相機序號：" + finalString1 + "\n";
                tb_data_to_write.Text = finalString1;
            }
        }

        void make_random_data()
        {
            //[C#] 產生一組亂數
            //最後產生的finalString就是我們要的亂數,至於亂數長度,你可以調整第二行中8這個數字,如果沒改就是長度8的亂數.
            var chars1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
            var chars2 = "0123456789";
            var stringChars1 = new char[13];
            var random = new Random();
            for (int i = 0; i < stringChars1.Length; i++)
            {
                if ((i == 0) || (i == 8))
                {
                    stringChars1[i] = chars1[random.Next(chars1.Length)];
                }
                else
                {
                    stringChars1[i] = chars2[random.Next(chars2.Length)];
                }
            }
            var finalString1 = new String(stringChars1);
            richTextBox1.Text += "相機序號：" + finalString1 + "\n";
            tb_data_to_write.Text = finalString1;
            return;
        }

        private void button4_Click(object sender, EventArgs e)
        {
        }

        private void button5_Click(object sender, EventArgs e)
        {
        }

        string read_data_from_plc_d_register(string contact_point, string contact_address)
        {
            string data_read = "";
            IPLC_interface mitsubishi = new Mitsubishi_realize();//实例化接口--实现三菱在线访问
            if (mitsubishi.PLC_ready)//PLC是否准备完成
            {
                //richTextBox1.Text += "三菱PLC ready 1\n";

                //richTextBox1.Text += "\n觸點 : " + contact_point + "\t位址 : " + contact_address + "\n";
                tb_contact_address.Text = "觸點 : " + contact_point + "\t位址 : " + contact_address;

                List<bool> data = mitsubishi.PLC_read_M_bit(contact_point, contact_address);    //讀取狀態
                //richTextBox1.Text += "len = " + data.Count.ToString() + ", data = " + data[0].ToString() + "\n";

                if (data[0] == true)
                {
                    string dddd = mitsubishi.PLC_read_D_register(contact_point, contact_address, numerical_format.String_32_Bit);
                    tb_data_read.Text = dddd;
                    tb_data_d.Text = dddd;
                    data_read = dddd;
                    //richTextBox1.Text += "b len = " + dddd.Length.ToString() + "\t";
                    //richTextBox1.Text += "data : " + dddd + "\n";
                }
                else
                {
                    tb_data_read.Text = "無資料";
                    tb_data_d.Text = "無資料";

                }
            }
            else
            {
                //richTextBox1.Text += "三菱PLC 不 ready\n";
            }
            return data_read;
        }
        void write_data_to_plc_d_register(string contact_point, string contact_address, string write_data)
        {
            if (write_data.Length == 0)
            {
                tb_data_read.Text = "無寫入資料";
                tb_data_d.Text = "無寫入資料";
                return;
            }

            IPLC_interface mitsubishi = new Mitsubishi_realize();//实例化接口--实现三菱在线访问
            if (mitsubishi.PLC_ready)//PLC是否准备完成
            {
                //richTextBox1.Text += "三菱PLC ready 2\n";

                richTextBox1.Text += "\n觸點 : " + contact_point + "\t位址 : " + contact_address + "\n";
                tb_contact_address.Text = "觸點 : " + contact_point + "\t位址 : " + contact_address;

                string dddd = mitsubishi.PLC_write_D_register(contact_point, contact_address, write_data, numerical_format.String_32_Bit);

                richTextBox1.Text += "cccc len = " + dddd.Length.ToString() + "\t";
                richTextBox1.Text += "data : " + dddd + "\n";
                richTextBox1.Text += "\n";
            }
            else
            {
                //richTextBox1.Text += "三菱PLC 不 ready\n";
            }
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            bool plc_power_status = check_plc_power_status();
            //bool plc_power_status = true;

            if (plc_power_status == false)
            {
                lb_plc_pc3b.Text = "";
                lb_plc_pc4b.Text = "";
                lb_pc_plc3b.Text = "";
                lb_pc_plc4b.Text = "";
                pbx_m10000.BackgroundImage = Properties.Resources.ball_gray;
                pbx_m10001.BackgroundImage = Properties.Resources.ball_gray;
                pbx_m10002.BackgroundImage = Properties.Resources.ball_gray;
                pbx_m12000.BackgroundImage = Properties.Resources.ball_gray;
                pbx_m12001.BackgroundImage = Properties.Resources.ball_gray;
                pbx_m12002.BackgroundImage = Properties.Resources.ball_gray;
                lb_plc_mesg.Text = "三菱PLC 不 Ready";
                lb_plc_mesg.Visible = true;
                groupBox_plc_status.Enabled = false;
                pictureBox1.Enabled = false;
                return;
            }
            else
            {
                lb_plc_mesg.Text = "";
                lb_plc_mesg.Visible = false;
                groupBox_plc_status.Enabled = true;
                pictureBox1.Enabled = true;
            }

            update_plc_data_status_data();
            draw_status();
        }

        private const int N = 16;
        int m10000_value = 0;
        int m10001_value = 0;
        int m10002_value = 0;
        int m12000_value = 0;
        int m12001_value = 0;
        int m12002_value = 0;

        int[] m10000_data = new int[N];
        int[] m10001_data = new int[N];
        int[] m10002_data = new int[N];
        int[] m12000_data = new int[N];
        int[] m12001_data = new int[N];
        int[] m12002_data = new int[N];

        bool check_plc_power_status()
        {
            bool plc_power_status = false;
            //讀取 PLC狀態
            IPLC_interface mitsubishi = new Mitsubishi_realize();//实例化接口--实现三菱在线访问
            if (mitsubishi.PLC_ready == true)   //PLC是否准备完成
            {
                plc_power_status = true;
                /* 目前無法判斷 PLC_read_M_bit 是讀不到資料 還是資料為True/False
                richTextBox1.Text += "check_plc_power_status\n";
                //richTextBox1.Text += "三菱PLC ready 3\n";
                List<bool> data = mitsubishi.PLC_read_M_bit("M", "10000");//读取状态
                richTextBox1.Text += "aaaa len = " + data.Count.ToString() + ", data = " + data[0].ToString() + "\n";

                if (data[0] == true)
                {
                    plc_power_status = true;
                }
                else
                {
                    plc_power_status = false;
                }
                */
            }
            else
            {
                plc_power_status = false;
            }
            return plc_power_status;
        }

        void update_plc_data_status_data()
        {
            int i;
            int rrrr;
            Random r = new Random();
            bool status;

            //M10000
            status = get_plc_data_status(10000);
            if (status == true)
            {
                m10000_value = 1;
            }
            else
            {
                m10000_value = 0;
            }

            if (cb_debug.Checked == true)
            {
                rrrr = r.Next(0, 2);
                m10000_value = rrrr;
            }

            for (i = 0; i < (N - 1); i++)
            {
                m10000_data[i] = m10000_data[i + 1];
            }
            m10000_data[N - 1] = m10000_value;

            if (m10000_value == 1)
            {
                pbx_m10000.BackgroundImage = Properties.Resources.ball_green;
            }
            else
            {
                pbx_m10000.BackgroundImage = Properties.Resources.ball_gray;
            }

            //M10001
            status = get_plc_data_status(10001);
            if (status == true)
            {
                m10001_value = 1;
            }
            else
            {
                m10001_value = 0;
            }

            if (cb_debug.Checked == true)
            {
                rrrr = r.Next(0, 2);
                m10001_value = rrrr;
            }

            for (i = 0; i < (N - 1); i++)
            {
                m10001_data[i] = m10001_data[i + 1];
            }
            m10001_data[N - 1] = m10001_value;

            if (m10001_value == 1)
            {
                pbx_m10001.BackgroundImage = Properties.Resources.ball_green;
            }
            else
            {
                pbx_m10001.BackgroundImage = Properties.Resources.ball_gray;
            }

            //M10002
            status = get_plc_data_status(10002);
            if (status == true)
            {
                m10002_value = 1;
            }
            else
            {
                m10002_value = 0;
            }

            if (cb_debug.Checked == true)
            {
                rrrr = r.Next(0, 2);
                m10002_value = rrrr;
            }

            for (i = 0; i < (N - 1); i++)
            {
                m10002_data[i] = m10002_data[i + 1];
            }
            m10002_data[N - 1] = m10002_value;

            if (m10002_value == 1)
            {
                pbx_m10002.BackgroundImage = Properties.Resources.ball_green;
            }
            else
            {
                pbx_m10002.BackgroundImage = Properties.Resources.ball_gray;
            }

            //M12000
            status = get_plc_data_status(12000);
            if (status == true)
            {
                m12000_value = 1;
            }
            else
            {
                m12000_value = 0;
            }

            if (cb_debug.Checked == true)
            {
                rrrr = r.Next(0, 2);
                m12000_value = rrrr;
            }

            for (i = 0; i < (N - 1); i++)
            {
                m12000_data[i] = m12000_data[i + 1];
            }
            m12000_data[N - 1] = m12000_value;

            if (m12000_value == 1)
            {
                pbx_m12000.BackgroundImage = Properties.Resources.ball_green;
            }
            else
            {
                pbx_m12000.BackgroundImage = Properties.Resources.ball_gray;
            }

            //M12001
            status = get_plc_data_status(12001);
            if (status == true)
            {
                m12001_value = 1;
            }
            else
            {
                m12001_value = 0;
            }

            if (cb_debug.Checked == true)
            {
                rrrr = r.Next(0, 2);
                m12001_value = rrrr;
            }

            for (i = 0; i < (N - 1); i++)
            {
                m12001_data[i] = m12001_data[i + 1];
            }
            m12001_data[N - 1] = m12001_value;

            if (m12001_value == 1)
            {
                pbx_m12001.BackgroundImage = Properties.Resources.ball_green;
            }
            else
            {
                pbx_m12001.BackgroundImage = Properties.Resources.ball_gray;
            }

            //M12002
            status = get_plc_data_status(12002);
            if (status == true)
            {
                m12002_value = 1;
            }
            else
            {
                m12002_value = 0;
            }

            if (cb_debug.Checked == true)
            {
                rrrr = r.Next(0, 2);
                m12002_value = rrrr;
            }

            for (i = 0; i < (N - 1); i++)
            {
                m12002_data[i] = m12002_data[i + 1];
            }
            m12002_data[N - 1] = m12002_value;

            if (m12002_value == 1)
            {
                pbx_m12002.BackgroundImage = Properties.Resources.ball_green;
            }
            else
            {
                pbx_m12002.BackgroundImage = Properties.Resources.ball_gray;
            }

            string contact_point = "D";
            string contact_address = "2000";
            show_main_message1("讀取: " + contact_point + contact_address, S_OK, 30);
            string data_read = read_data_from_plc_d_register(contact_point, contact_address);
            //richTextBox1.Text += "\nD2000 len = " + data_read.Length.ToString() + "\n";
            //richTextBox1.Text += "data : |" + data_read + "|\n";
            lb_plc_pc3b.Text = data_read;

            contact_point = "D";
            contact_address = "2010";
            show_main_message1("讀取: " + contact_point + contact_address, S_OK, 30);
            data_read = read_data_from_plc_d_register(contact_point, contact_address);
            //richTextBox1.Text += "\nD8000 len = " + data_read.Length.ToString() + "\n";
            //richTextBox1.Text += "data : |" + data_read + "|\n";
            lb_plc_pc4b.Text = data_read;

            contact_point = "D";
            contact_address = "8000";
            show_main_message1("讀取: " + contact_point + contact_address, S_OK, 30);
            data_read = read_data_from_plc_d_register(contact_point, contact_address);
            //richTextBox1.Text += "\nD8000 len = " + data_read.Length.ToString() + "\n";
            //richTextBox1.Text += "data : |" + data_read + "|\n";
            lb_pc_plc3b.Text = data_read;

            contact_point = "D";
            contact_address = "8010";
            show_main_message1("讀取: " + contact_point + contact_address, S_OK, 30);
            data_read = read_data_from_plc_d_register(contact_point, contact_address);
            //richTextBox1.Text += "\nD8000 len = " + data_read.Length.ToString() + "\n";
            //richTextBox1.Text += "data : |" + data_read + "|\n";
            lb_pc_plc4b.Text = data_read;
        }

        void draw_status()
        {
            int W = pictureBox1.Width;
            int H = pictureBox1.Height;

            Bitmap bitmap1 = new Bitmap(W, H);
            Graphics g = Graphics.FromImage(bitmap1);
            g.Clear(Color.White);

            //畫X軸 Y軸
            Point px1 = new Point(W * 10 / 100, H * 90 / 100);
            Point px2 = new Point(W * 90 / 100, H * 90 / 100);
            g.DrawLine(new Pen(Brushes.Black, 5), px1, px2);
            Point py1 = new Point(W * 10 / 100, H * 90 / 100);
            Point py2 = new Point(W * 10 / 100, H * 10 / 100);
            g.DrawLine(new Pen(Brushes.Black, 5), py1, py2);

            int x_st = W * 10 / 100;
            int x_sp = W * 90 / 100;
            int y_st = H * 10 / 100;
            int y_sp = H * 90 / 100;
            int w = x_sp - x_st;
            int h = y_sp - y_st;
            int step = w / (N - 1);

            //richTextBox1.Text += "step  = " + step.ToString() + " ";

            // Create pens.
            Pen redPen = new Pen(Color.Red, 3);
            Pen grayPen = new Pen(Color.Gray, 5);
            Point[] curvePoints = new Point[N];    //一維陣列內有 N 個Point

            int i;
            int dd = 8;
            //畫M10000
            for (i = 0; i < N; i++)
            {
                curvePoints[i].X = x_st + step * i;
                curvePoints[i].Y = H - y_st - (h / 7) * m10000_data[i] - 5 - (h / 7) * 5 - dd * 5;
            }
            g.DrawLines(grayPen, curvePoints);   //畫直線
            g.DrawString("M10000", new Font("標楷體", 15), new SolidBrush(Color.Green), new PointF(x_st - 70, H - y_st - (h / 7) * 1 - 5 - (h / 7) * 5 - dd * 5));

            //畫M10001
            for (i = 0; i < N; i++)
            {
                curvePoints[i].X = x_st + step * i;
                curvePoints[i].Y = H - y_st - (h / 7) * m10001_data[i] - 5 - (h / 7) * 4 - dd * 4;
            }
            g.DrawLines(redPen, curvePoints);   //畫直線
            g.DrawString("M10001", new Font("標楷體", 15), new SolidBrush(Color.Green), new PointF(x_st - 70, H - y_st - (h / 7) * 1 - 5 - (h / 7) * 4 - dd * 4));

            //畫M10002
            for (i = 0; i < N; i++)
            {
                curvePoints[i].X = x_st + step * i;
                curvePoints[i].Y = H - y_st - (h / 7) * m10002_data[i] - 5 - (h / 7) * 3 - dd * 3;
            }
            g.DrawLines(redPen, curvePoints);   //畫直線
            g.DrawString("M10002", new Font("標楷體", 15), new SolidBrush(Color.Green), new PointF(x_st - 70, H - y_st - (h / 7) * 1 - 5 - (h / 7) * 3 - dd * 3));

            //畫M12000
            for (i = 0; i < N; i++)
            {
                curvePoints[i].X = x_st + step * i;
                curvePoints[i].Y = H - y_st - (h / 7) * m12000_data[i] - 5 - (h / 7) * 2 - dd * 2;
            }
            g.DrawLines(redPen, curvePoints);   //畫直線
            g.DrawString("M12000", new Font("標楷體", 15), new SolidBrush(Color.Green), new PointF(x_st - 70, H - y_st - (h / 7) * 1 - 5 - (h / 7) * 2 - dd * 2));

            //畫M12001
            for (i = 0; i < N; i++)
            {
                curvePoints[i].X = x_st + step * i;
                curvePoints[i].Y = H - y_st - (h / 7) * m12001_data[i] - 5 - (h / 7) * 1 - dd * 1;
            }
            g.DrawLines(redPen, curvePoints);   //畫直線
            g.DrawString("M12001", new Font("標楷體", 15), new SolidBrush(Color.Green), new PointF(x_st - 70, H - y_st - (h / 7) * 1 - 5 - (h / 7) * 1 - dd * 1));

            //畫M12002
            for (i = 0; i < N; i++)
            {
                curvePoints[i].X = x_st + step * i;
                curvePoints[i].Y = H - y_st - (h / 7) * m12002_data[i] - 5 - (h / 7) * 0 - dd * 0;
            }
            g.DrawLines(redPen, curvePoints);   //畫直線
            g.DrawString("M12002", new Font("標楷體", 15), new SolidBrush(Color.Green), new PointF(x_st - 70, H - y_st - (h / 7) * 1 - 5 - (h / 7) * 0 - dd * 0));




            pictureBox1.Image = bitmap1;

            g.Dispose();
        }

        bool get_plc_data_status(int address)
        {
            //讀取 M10000 看資料是否 Ready
            IPLC_interface mitsubishi = new Mitsubishi_realize();//实例化接口--实现三菱在线访问
            if (mitsubishi.PLC_ready)//PLC是否准备完成
            {
                //richTextBox1.Text += "三菱PLC ready 4\n";
                List<bool> data = mitsubishi.PLC_read_M_bit("M", address.ToString());//读取状态
                //richTextBox1.Text += "len = " + data.Count.ToString() + ", data = " + data[0].ToString() + "\n";

                if (data[0] == true)
                {
                    return true;

                }
                else
                {
                    return false;
                }

                /*
                //string dddd = mitsubishi.PLC_read_D_register(button_base.PLC_Contact, button_base.PLC_Address, numerical_format.Hex_16_Bit);
                //string dddd = mitsubishi.PLC_read_D_register("M", "10000", numerical_format.Signed_16_Bit);

                string contact_point = "Y";
                string contact_address = "20";
                richTextBox1.Text += "\n觸點 : " + contact_point + "\t位址 : " + contact_address + "\n";
                tb_contact_address.Text = "觸點 : " + contact_point + "\t位址 : " + contact_address;

                string dddd = mitsubishi.PLC_read_D_register(contact_point, contact_address, numerical_format.Signed_16_Bit);
                richTextBox1.Text += "len = " + dddd.Length.ToString() + "\t";
                richTextBox1.Text += "data : " + dddd[0] + "\n";
                */
            }
            else
            {
                //richTextBox1.Text += "三菱PLC 不 ready\n";
                return false;
            }
        }

        int timer_display_show_main_mesg_count = 0;
        int timer_display_show_main_mesg_count_target = 0;

        void show_main_message1(string mesg, int number, int timeout)
        {
            lb_main_mesg1.Text = mesg;
            //playSound(number);

            timer_display_show_main_mesg_count = 0;
            timer_display_show_main_mesg_count_target = timeout;   //timeout in 0.1 sec
            timer_display.Enabled = true;
        }

        private void timer_display_Tick(object sender, EventArgs e)
        {
            if (timer_display_show_main_mesg_count < timer_display_show_main_mesg_count_target)      //display main message timeout
            {
                timer_display_show_main_mesg_count++;
                if (timer_display_show_main_mesg_count >= timer_display_show_main_mesg_count_target)
                {
                    lb_main_mesg1.Text = "";
                }
                /*
                if (timer_display_show_main_mesg_count >= (timer_display_show_main_mesg_count_target * 2))
                {
                    //lb_main_mesg.Text = "";
                    lb_main_mesg2.Text = "";
                }
                */
            }

        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void bt_copy_to_clipboard_Click(object sender, EventArgs e)
        {
            //C# – 複製資料到剪貼簿
            //Clipboard.SetData(DataFormats.Text, richTextBox1.Text + "\n");
            Clipboard.SetDataObject(richTextBox1.Text + "\n");      //建議用此
            richTextBox1.Text += "已複製資料到系統剪貼簿\n";
        }

        private void bt_erase_d_Click(object sender, EventArgs e)
        {
            tb_data_d.Text = "";
        }

        private void bt_read_d_Click(object sender, EventArgs e)
        {
            string contact_point = tb_contact_point_d.Text;
            string contact_address = tb_contact_address_d.Text;

            if (contact_point.Length <= 0)
            {
                show_main_message1("無觸點", S_OK, 30);
                return;
            }
            if (contact_address.Length <= 0)
            {
                show_main_message1("無位址", S_OK, 30);
                return;
            }

            show_main_message1("讀取: " + contact_point + contact_address, S_OK, 30);

            string data_read = read_data_from_plc_d_register(contact_point, contact_address);
        }

        private void bt_write_d_Click(object sender, EventArgs e)
        {
            string contact_point = tb_contact_point_d.Text;
            string contact_address = tb_contact_address_d.Text;
            string write_data = tb_data_d.Text;
            tb_data_d.Text = "";

            if (contact_point.Length <= 0)
            {
                show_main_message1("無觸點", S_OK, 30);
                return;
            }
            if (contact_address.Length <= 0)
            {
                show_main_message1("無位址", S_OK, 30);
                return;
            }
            if (write_data.Length <= 0)
            {
                show_main_message1("無資料", S_OK, 30);
                return;
            }
            if (write_data == "無資料")
            {
                show_main_message1("無資料", S_OK, 30);
                return;
            }
            if (write_data == "無寫入資料")
            {
                show_main_message1("無資料", S_OK, 30);
                return;
            }

            show_main_message1("寫入: " + contact_point + contact_address + ", 資料: " + write_data, S_OK, 30);

            write_data_to_plc_d_register(contact_point, contact_address, write_data);
        }

        private void bt_erase_m_Click(object sender, EventArgs e)
        {
            tb_data_m.Text = "";
            tb_data_m.BackColor = Color.White;
        }

        private void bt_read_m_Click(object sender, EventArgs e)
        {
            string contact_point = tb_contact_point_m.Text;
            string contact_address = tb_contact_address_m.Text;

            if (contact_point.Length <= 0)
            {
                show_main_message1("無觸點", S_OK, 30);
                return;
            }
            if (contact_address.Length <= 0)
            {
                show_main_message1("無位址", S_OK, 30);
                return;
            }

            show_main_message1("讀取: " + contact_point + contact_address, S_OK, 30);

            bool ret = read_data_from_plc_m_bit(contact_point, contact_address);
            if (ret == true)
            {
                tb_data_m.BackColor = Color.Lime;
                tb_data_m.Text = "High";
            }
            else
            {
                tb_data_m.BackColor = Color.Gray;
                tb_data_m.Text = "Low";
            }

        }

        private void bt_write_m_Click(object sender, EventArgs e)
        {
            string contact_point = tb_contact_point_m.Text;
            string contact_address = tb_contact_address_m.Text;

            Button_state button_State;
            if (rb_high.Checked == true)
            {
                button_State = Button_state.ON;
            }
            else
            {
                button_State = Button_state.Off;
            }

            tb_data_m.Text = "";
            tb_data_m.BackColor = Color.White;

            if (contact_point.Length <= 0)
            {
                show_main_message1("無觸點", S_OK, 30);
                return;
            }
            if (contact_address.Length <= 0)
            {
                show_main_message1("無位址", S_OK, 30);
                return;
            }

            show_main_message1("寫入: " + contact_point + contact_address + ", 資料: " + button_State, S_OK, 30);

            write_data_to_plc_m_bit(contact_point, contact_address, button_State);
        }

        bool read_data_from_plc_m_bit(string contact_point, string contact_address)
        {
            bool ret = false;
            IPLC_interface mitsubishi = new Mitsubishi_realize();//实例化接口--实现三菱在线访问
            if (mitsubishi.PLC_ready)//PLC是否准备完成
            {
                //richTextBox1.Text += "三菱PLC ready 5\n";

                //richTextBox1.Text += "\n觸點 : " + contact_point + "\t位址 : " + contact_address + "\n";
                tb_contact_address.Text = "觸點 : " + contact_point + "\t位址 : " + contact_address;

                List<bool> data = mitsubishi.PLC_read_M_bit(contact_point, contact_address);    //讀取狀態
                //richTextBox1.Text += "len = " + data.Count.ToString() + ", data = " + data[0].ToString() + "\n";

                if (data[0] == true)
                {
                    tb_data_read.Text = "True";
                    tb_data_m.Text = "True";
                    ret = true;
                }
                else
                {
                    tb_data_read.Text = "False";
                    tb_data_m.Text = "False";
                    ret = false;
                }
            }
            else
            {
                //richTextBox1.Text += "三菱PLC 不 ready\n";
                ret = false;
            }
            return ret;
        }
        void write_data_to_plc_m_bit(string contact_point, string contact_address, Button_state write_data)
        {
            IPLC_interface mitsubishi = new Mitsubishi_realize();//实例化接口--实现三菱在线访问
            if (mitsubishi.PLC_ready)//PLC是否准备完成
            {
                //richTextBox1.Text += "三菱PLC ready 6\n";

                richTextBox1.Text += "\n觸點 : " + contact_point + "\t位址 : " + contact_address + "\n";
                tb_contact_address.Text = "觸點 : " + contact_point + "\t位址 : " + contact_address;

                //List<bool>                   PLC_write_M_bit(string Name,   string id, Button_state button_State);//写入--位
                List<bool> data = mitsubishi.PLC_write_M_bit(contact_point, contact_address, write_data);



            }
            else
            {
                //richTextBox1.Text += "三菱PLC 不 ready\n";
            }
        }

        //delay 10000 約 10秒
        //C# 不lag的延遲時間
        private void delay(int delay_milliseconds)
        {
            delay_milliseconds *= 2;
            DateTime time_before = DateTime.Now;
            while (((TimeSpan)(DateTime.Now - time_before)).TotalMilliseconds < delay_milliseconds)
            {
                Application.DoEvents();
            }
        }

        bool flag_plc_test = false;
        private void button6_Click(object sender, EventArgs e)
        {
            int i;
            string contact_point = String.Empty;
            string contact_address = String.Empty;
            bool ret = false;

            richTextBox1.Text += "測試PLC作業流程\n";

            flag_plc_test = true;

            richTextBox1.Text += "(1) PLC 把資料放在 D2000\n";
            richTextBox1.Text += "(2a) PLC 拉高 M10000, 供PC讀取, 通知條碼內容已備便\n";
            richTextBox1.Text += "(2b) PC 讀取 M10000 狀態\n";
            contact_point = "M";
            contact_address = "10000";
            ret = false;
            for (i = 0; i < 1000; i++)
            {
                ret = read_data_from_plc_m_bit(contact_point, contact_address);

                //richTextBox1.Text += "測試PLC作業流程\t" + i.ToString() + "\t" + DateTime.Now.ToString() + "\n";
                //richTextBox1.Text += ret.ToString() + "\n";

                if (ret == false)
                {
                    //richTextBox1.Text += "取得 M10000 為 OFF  ";
                    richTextBox1.Text += "OFF  ";
                    delay(500);
                }
                else
                {
                    richTextBox1.Text += "\n取得 M10000 為 ON\n";

                    richTextBox1.Text += "(3a) PC 讀取 D2000 資料\n";

                    show_main_message1("讀取 D2000", S_OK, 30);
                    contact_point = "D";
                    contact_address = "2000";
                    string data_read = read_data_from_plc_d_register(contact_point, contact_address);
                    if (data_read.Length > 0)
                    {
                        richTextBox1.Text += "取得 D2000 資料 : " + data_read + "\n";

                        delay(500);

                        richTextBox1.Text += "\nlen = " + data_read.Length.ToString() + "\n";

                        richTextBox1.Text += "(3b) PC 將 從 D2000 取得的資料 寫到 D8000\n";

                        string data_to_write = data_read.Substring(0, 16);

                        richTextBox1.Text += "欲寫入 D8000 資料 : " + data_to_write + ", len = " + data_to_write.Length.ToString() + "\n";

                        show_main_message1("寫入 D8000", S_OK, 30);
                        contact_point = "D";
                        contact_address = "8000";
                        //write_data = tb_data_to_write.Text;
                        //tb_data_to_write.Text = "";

                        write_data_to_plc_d_register(contact_point, contact_address, data_to_write);

                        delay(500);

                        richTextBox1.Text += "(4) PC 拉高 M12000, 供PLC讀取\n";

                        contact_point = "M";
                        contact_address = "12000";

                        Button_state button_State;
                        button_State = Button_state.ON;

                        tb_data_m.Text = "";
                        tb_data_m.BackColor = Color.White;

                        show_main_message1("寫入: " + contact_point + contact_address + ", 資料: " + button_State, S_OK, 30);

                        write_data_to_plc_m_bit(contact_point, contact_address, button_State);

                        delay(500);

                        richTextBox1.Text += "(5a) PLC 拉高 M10001, 供PC讀取, 通知開始做色調\n";
                        richTextBox1.Text += "(5b) PC 讀取 M10001 狀態\n";
                        contact_point = "M";
                        contact_address = "10001";
                        ret = false;
                        for (i = 0; i < 1000; i++)
                        {
                            ret = read_data_from_plc_m_bit(contact_point, contact_address);

                            if (ret == false)
                            {
                                richTextBox1.Text += "取得 M10001 為 OFF  ";
                                richTextBox1.Text += "OFF  ";
                                delay(500);
                            }
                            else
                            {
                                delay(500);

                                richTextBox1.Text += "\n取得 M10001 為 ON\n";

                                richTextBox1.Text += "(6) PC 拉高 M12001, 供PLC讀取, 通知PC已開始做色調\n";

                                contact_point = "M";
                                contact_address = "12001";

                                button_State = Button_state.ON;

                                tb_data_m.Text = "";
                                tb_data_m.BackColor = Color.White;

                                show_main_message1("寫入: " + contact_point + contact_address + ", 資料: " + button_State, S_OK, 30);
                                write_data_to_plc_m_bit(contact_point, contact_address, button_State);

                                richTextBox1.Text += "\n\n\nPC開始做色調........\n\n\n\n";
                                delay(500);
                                delay(500);
                                delay(500);

                                richTextBox1.Text += "(7) PC 做完色調, 將結果碼寫在 D8010\n";

                                Random r = new Random();
                                int color_result = r.Next(0, 20);
                                richTextBox1.Text += "色調結果: 0x" + color_result.ToString("X2") + " = " + color_result.ToString() + "\n";
                                contact_point = "D";
                                contact_address = "8010";
                                string write_data = color_result.ToString();
                                show_main_message1("寫入: " + contact_point + contact_address + ", 資料: " + write_data, S_OK, 30);
                                write_data_to_plc_d_register(contact_point, contact_address, write_data);

                                richTextBox1.Text += "(8) PC 拉高 M12002, 供PLC讀取, 通知PC已做完色調\n";

                                delay(500);

                                contact_point = "M";
                                contact_address = "12002";

                                button_State = Button_state.ON;

                                tb_data_m.Text = "";
                                tb_data_m.BackColor = Color.White;

                                show_main_message1("寫入: " + contact_point + contact_address + ", 資料: " + button_State, S_OK, 30);
                                write_data_to_plc_m_bit(contact_point, contact_address, button_State);


                                richTextBox1.Text += "測試PLC作業流程完成\n";

                                break;
                            }
                        }

                        richTextBox1.Text += "AAAAAAAAAAAAAAAAAAA\n";







                    }
                    else
                    {
                        richTextBox1.Text += "未取得 D2000 資料\n";
                    }




                    break;



                }

                if (flag_plc_test == false)
                {
                    richTextBox1.Text += "測試PLC作業流程 中斷\n";
                    break;
                }
            }
        }

        private void button7_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "設定 中斷\n";
            flag_plc_test = false;
        }

        private void button7_MouseDown(object sender, MouseEventArgs e)
        {
            richTextBox1.Text += "設定 中斷\n";
            flag_plc_test = false;
        }

        private void bt_pause_Click(object sender, EventArgs e)
        {
            if (bt_pause.Text == "暫停")
            {
                bt_pause.Text = "繼續";
                timer1.Enabled = false;
            }
            else
            {
                bt_pause.Text = "暫停";
                timer1.Enabled = true;
            }
        }
    }
}
