using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_PID
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        float pid_max = 0;
        float pid_min = 0;

        private void button1_Click(object sender, EventArgs e)
        {
            int i;
            float kp = float.Parse(tb_kp.Text);
            float ki = float.Parse(tb_ki.Text);
            float kd = float.Parse(tb_kd.Text);
            int target_speed = int.Parse(tb_target.Text);
            int max_speed = int.Parse(tb_max_speed.Text);
            int min_speed = int.Parse(tb_min_speed.Text);
            int max_duty = int.Parse(tb_max_duty.Text);
            int min_duty = int.Parse(tb_min_duty.Text);
            int steps = int.Parse(cb_steps.Text);

            int[] real_speed_array = new int[200];
            int x_st = 0;
            int h_st = 0;
            int x_step = 0;
            int STEP = 0;

            //int STEP = (max_speed - min_speed) / (max_duty - min_duty);   //原本是這一行，改成以下16行。
            try
            {   //可能會產生錯誤的程式區段
                STEP = (max_speed - min_speed) / (max_duty - min_duty);
            }
            catch (Exception ex)
            {   //定義產生錯誤時的例外處理程式碼
                MessageBox.Show("參數錯誤：" + ex.Message);
                richTextBox1.Text += ex.Message + "\n";
                richTextBox1.Text += "max_duty = " + max_duty.ToString() + "\t";
                richTextBox1.Text += "min_duty = " + min_duty.ToString() + "\n";
            }
            finally
            {
                //一定會被執行的程式區段
                if (STEP > 0)
                    richTextBox1.Text += "STEP = " + STEP.ToString() + "\n";
                else
                    richTextBox1.Text += "FAIL STEP = " + STEP.ToString() + "\n";
            }

            label_STEP.Text = "STEP: " + STEP.ToString();

            int real_speed = 0;
            int error = 0;
            int pp = 0;
            int ii = 0;
            int dd = 0;
            int ii_old = 0;
            int error_old = 0;
            float pid = 0;
            int max_real_speed = 0;
            float ratio = 0;
            int draw_target_speed = 0;
            Point[] point_array0 = new Point[50];
            Point[] point_array1 = new Point[100];
            Point[] point_array2 = new Point[200];

            richTextBox1.Text += "kp = " + kp.ToString() + "\t";
            richTextBox1.Text += "ki = " + ki.ToString() + "\t";
            richTextBox1.Text += "kd = " + kd.ToString() + "\n";
            richTextBox1.Text += "target_speed = " + target_speed.ToString() + "\n";
            richTextBox1.Text += "max_speed = " + max_speed.ToString() + "\t";
            richTextBox1.Text += "min_speed = " + min_speed.ToString() + "\n";
            richTextBox1.Text += "max_duty = " + max_duty.ToString() + "\t";
            richTextBox1.Text += "min_duty = " + min_duty.ToString() + "\n";
            richTextBox1.Text += "steps = " + steps.ToString() + "\n";
            richTextBox1.Text += "STEP = " + STEP.ToString() + "\n";

            richTextBox1.Text += "step\ttgt\treal\terr\tpp\tii\tdd\tpid\n";
            for (i = 0; i < steps; i++)
            {
                error = target_speed - real_speed;
                pp = error;
                ii = error + ii_old;
                dd = error - error_old;
                pid = kp * pp + ki * ii + kd * dd;
                if (pid > pid_max)
                    pid_max = pid;
                else if (pid < pid_min)
                    pid_min = pid;

                real_speed_array[i] = real_speed;

                richTextBox1.Text += i.ToString() + "\t" + target_speed.ToString() + "\t" + real_speed.ToString() + "\t" + error.ToString() + "\t";
                richTextBox1.Text += pp.ToString() + "\t" + ii.ToString() + "\t" + dd.ToString() + "\t" + pid.ToString() + "\n";

                //richTextBox1.Text += "real_speed(" + (i + 1).ToString() + ")=" + real_speed.ToString() + ";";
                //richTextBox1.Text += "pid(" + (i + 1).ToString() + ")=" + pid.ToString() + ";";
                //richTextBox1.Text += "\n";

                if (pid > 50)
                    real_speed += STEP;
                else if (pid < -50)
                    real_speed -= STEP;

                error_old = error;
                ii_old = ii;
            }

            //畫圖
            richTextBox1.Text += "\n\nW = " + panel1.Width.ToString() + "\n";
            richTextBox1.Text += "H = " + panel1.Height.ToString() + "\n";

            max_real_speed = real_speed_array.Max();
            label_max_speed.Text = "Max: " + max_real_speed.ToString();
            label_pid_max.Text = "pid_max: " + pid_max.ToString();
            label_pid_min.Text = "pid_min: " + pid_min.ToString();

            max_real_speed = Math.Max(max_real_speed, target_speed);
            richTextBox1.Text += "real_speed_max = " + max_real_speed.ToString() + "\n";
            ratio = (float)max_real_speed / (float)(panel1.Height*90/100);
            richTextBox1.Text += "ratio = " + ratio.ToString() + "\n";

            for (i = 0; i < steps; i++)
            {
                real_speed_array[i] = (int)((float)real_speed_array[i] / ratio);
            }

            Graphics g = panel1.CreateGraphics();
            //g.Clear(Color.White);
            DrawXY();

            x_st = panel1.Width * 5 / 100;
            h_st = panel1.Height * 95 / 100;
            x_step = panel1.Width * 90 / 100 / (steps - 1);

            richTextBox1.Text += "x_st = " + x_st.ToString() + "\n";
            richTextBox1.Text += "h_st = " + h_st.ToString() + "\n";
            richTextBox1.Text += "x_step = " + x_step.ToString() + "\n";

            // Create pens.
            Pen redPen = new Pen(Color.Red, 3);
            // Create points that define curve.

            for (i = 0; i < steps; i++)
            {
                if (cb_steps.SelectedIndex == 0)
                {
                    point_array0[i].X = x_st + x_step * i;
                    point_array0[i].Y = h_st - real_speed_array[i];
                }
                else if (cb_steps.SelectedIndex == 1)
                {
                    point_array1[i].X = x_st + x_step * i;
                    point_array1[i].Y = h_st - real_speed_array[i];
                }
                else if (cb_steps.SelectedIndex == 2)
                {
                    point_array2[i].X = x_st + x_step * i;
                    point_array2[i].Y = h_st - real_speed_array[i];
                }
            }

            if (cb_steps.SelectedIndex == 0)
            {
                Point[] curvePoints = point_array0;
                // Draw lines between original points to screen.
                //g.DrawLines(redPen, curvePoints);   //畫直線

                // Draw curve to screen.
                g.DrawCurve(redPen, curvePoints); //畫曲線

                //畫X刻度
                DrawXTick(curvePoints);
            }
            else if (cb_steps.SelectedIndex == 1)
            {
                Point[] curvePoints = point_array1;
                // Draw lines between original points to screen.
                //g.DrawLines(redPen, curvePoints);   //畫直線

                // Draw curve to screen.
                g.DrawCurve(redPen, curvePoints); //畫曲線

                //畫X刻度
                DrawXTick(curvePoints);
            }
            else if (cb_steps.SelectedIndex == 2)
            {
                Point[] curvePoints = point_array2;
                // Draw lines between original points to screen.
                //g.DrawLines(redPen, curvePoints);   //畫直線

                // Draw curve to screen.
                g.DrawCurve(redPen, curvePoints); //畫曲線

                //畫X刻度
                DrawXTick(curvePoints);
            }

            //畫目標轉速
            draw_target_speed = (int)((float)target_speed / ratio);
            System.Drawing.Point px1 = new System.Drawing.Point(x_st, h_st - draw_target_speed);
            System.Drawing.Point px2 = new System.Drawing.Point(x_st + x_step * (steps-1), h_st - draw_target_speed);
            g.DrawLine(new Pen(Brushes.Blue, 2), px1, px2);

            // Create string to draw.
            String drawString = "目標轉速: " + target_speed.ToString() + " rpm";
            // Create font and brush.
            Font drawFont = new Font("Arial", 16);
            SolidBrush drawBrush = new SolidBrush(Color.Blue);
            // Create point for upper-left corner of drawing.
            PointF drawPoint = new PointF(x_st, h_st - draw_target_speed);
            // Draw string to screen.
            g.DrawString(drawString, drawFont, drawBrush, drawPoint);
            
            g.Dispose();
        }

        private void DrawXY()//画X轴Y轴
        {
            Graphics g = this.panel1.CreateGraphics();
            System.Drawing.Point px1 = new System.Drawing.Point(this.panel1.Width * 5 / 100, this.panel1.Height * 95 / 100);
            System.Drawing.Point px2 = new System.Drawing.Point(this.panel1.Width * 95 / 100, this.panel1.Height * 95 / 100);
            g.DrawLine(new Pen(Brushes.Black, 5), px1, px2);
            System.Drawing.Point py1 = new System.Drawing.Point(this.panel1.Width * 5 / 100, this.panel1.Height * 95 / 100);
            System.Drawing.Point py2 = new System.Drawing.Point(this.panel1.Width * 5 / 100, this.panel1.Height * 5 / 100);
            g.DrawLine(new Pen(Brushes.Black, 5), py1, py2);
            g.Dispose();
        }

        private void DrawXTick(Point[] curvePoints)//画X轴刻度
        {
            int x_pos = 0;
            int tick = 0;
            int major_tick = this.panel1.Height * 80 / 100;
            int minor_tick = this.panel1.Height * 85 / 100;
            int width = 0;
            Graphics g = this.panel1.CreateGraphics();
            for (int i = 0; i < curvePoints.Length; i++)
            {
                //richTextBox1.Text += "X = " + curvePoints[i].X.ToString() + "\n";
                x_pos = curvePoints[i].X;
                if ((i % 10) == 0)
                {
                    tick = major_tick;
                    width = 2;
                }
                else
                {
                    tick = minor_tick;
                    width = 1;
                }
                System.Drawing.Point px1 = new System.Drawing.Point(x_pos, tick);
                System.Drawing.Point px2 = new System.Drawing.Point(x_pos, this.panel1.Height * 95 / 100);
                g.DrawLine(new Pen(Brushes.Black, width), px1, px2);
            }
            g.Dispose();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            tb_kp.Text = "0.4";
            tb_ki.Text = "0.4";
            tb_kd.Text = "0";
            tb_target.Text = "1000";
            tb_max_speed.Text = "30000";
            tb_min_speed.Text = "0";
            tb_max_duty.Text = "100";
            tb_min_duty.Text = "0";
            tb_tolerance.Text = "80";
            label_STEP.Text = "STEP: ";
            label_max_speed.Text = "Max: ";
            cb_steps.SelectedIndex = 0;
            label_pid_max.Text = "pid_max:";
            label_pid_min.Text = "pid_min:";
        }

        private void button4_Click(object sender, EventArgs e)
        {
            Graphics g = panel1.CreateGraphics();
            g.Clear(Color.White);
            richTextBox1.Clear();
            label_STEP.Text = "STEP: ";
            label_max_speed.Text = "Max: ";
            label_pid_max.Text = "pid_max:";
            label_pid_min.Text = "pid_min:";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            int i;
            int target_speed = int.Parse(tb_target.Text);
            int max_speed = int.Parse(tb_max_speed.Text);
            int min_speed = int.Parse(tb_min_speed.Text);
            int max_duty = int.Parse(tb_max_duty.Text);
            int min_duty = int.Parse(tb_min_duty.Text);
            int steps = int.Parse(cb_steps.Text);
            int tolerance = int.Parse(tb_tolerance.Text);

            int[] real_speed_array = new int[200];
            int x_st = 0;
            int h_st = 0;
            int x_step = 0;
            int STEP = (max_speed - min_speed) / (max_duty - min_duty);
            label_STEP.Text = "STEP: " + STEP.ToString();

            int real_speed = 0;
            int max_real_speed = 0;
            float ratio = 0;
            int draw_target_speed = 0;
            Point[] point_array0 = new Point[50];
            Point[] point_array1 = new Point[100];
            Point[] point_array2 = new Point[200];

            richTextBox1.Text += "target_speed = " + target_speed.ToString() + "\n";
            richTextBox1.Text += "max_speed = " + max_speed.ToString() + "\t";
            richTextBox1.Text += "min_speed = " + min_speed.ToString() + "\n";
            richTextBox1.Text += "max_duty = " + max_duty.ToString() + "\t";
            richTextBox1.Text += "min_duty = " + min_duty.ToString() + "\n";
            richTextBox1.Text += "steps = " + steps.ToString() + "\n";
            richTextBox1.Text += "STEP = " + STEP.ToString() + "\n";

            richTextBox1.Text += "step\ttgt\treal\terr\n";
            for (i = 0; i < steps; i++)
            {

                real_speed_array[i] = real_speed;

                richTextBox1.Text += i.ToString() + "\t" + target_speed.ToString() + "\t" + real_speed.ToString() + "\n";

                if (real_speed < (target_speed - tolerance))
                    real_speed += STEP;
                else if (real_speed > (target_speed + tolerance))
                    real_speed -= STEP;

            }

            //畫圖
            richTextBox1.Text += "\n\nW = " + panel1.Width.ToString() + "\n";
            richTextBox1.Text += "H = " + panel1.Height.ToString() + "\n";

            max_real_speed = real_speed_array.Max();
            label_max_speed.Text = "Max: " + max_real_speed.ToString();

            max_real_speed = Math.Max(max_real_speed, target_speed);
            richTextBox1.Text += "real_speed_max = " + max_real_speed.ToString() + "\n";
            ratio = (float)max_real_speed / (float)(panel1.Height * 90 / 100);
            richTextBox1.Text += "ratio = " + ratio.ToString() + "\n";

            for (i = 0; i < steps; i++)
            {
                real_speed_array[i] = (int)((float)real_speed_array[i] / ratio);
            }

            Graphics g = panel1.CreateGraphics();
            //g.Clear(Color.White);
            DrawXY();

            x_st = panel1.Width * 5 / 100;
            h_st = panel1.Height * 95 / 100;
            x_step = panel1.Width * 90 / 100 / (steps - 1);

            richTextBox1.Text += "x_st = " + x_st.ToString() + "\n";
            richTextBox1.Text += "h_st = " + h_st.ToString() + "\n";
            richTextBox1.Text += "x_step = " + x_step.ToString() + "\n";

            for (i = 0; i < steps; i++)
            {
                if (cb_steps.SelectedIndex == 0)
                {
                    point_array0[i].X = x_st + x_step * i;
                    point_array0[i].Y = h_st - real_speed_array[i];
                }
                else if (cb_steps.SelectedIndex == 1)
                {
                    point_array1[i].X = x_st + x_step * i;
                    point_array1[i].Y = h_st - real_speed_array[i];
                }
                else if (cb_steps.SelectedIndex == 2)
                {
                    point_array2[i].X = x_st + x_step * i;
                    point_array2[i].Y = h_st - real_speed_array[i];
                }
            }

            // Create pens.
            Pen yellowPen = new Pen(Color.Yellow, 3);

            if (cb_steps.SelectedIndex == 0)
            {
                Point[] curvePoints = point_array0;
                // Draw lines between original points to screen.
                //g.DrawLines(yellowPen, curvePoints);   //畫直線

                // Draw curve to screen.
                g.DrawCurve(yellowPen, curvePoints); //畫曲線

                //畫X刻度
                DrawXTick(curvePoints);
            }
            else if (cb_steps.SelectedIndex == 1)
            {
                Point[] curvePoints = point_array1;
                // Draw lines between original points to screen.
                //g.DrawLines(yellowPen, curvePoints);   //畫直線

                // Draw curve to screen.
                g.DrawCurve(yellowPen, curvePoints); //畫曲線

                //畫X刻度
                DrawXTick(curvePoints);
            }
            else if (cb_steps.SelectedIndex == 2)
            {
                Point[] curvePoints = point_array2;
                // Draw lines between original points to screen.
                //g.DrawLines(yellowPen, curvePoints);   //畫直線

                // Draw curve to screen.
                g.DrawCurve(yellowPen, curvePoints); //畫曲線

                //畫X刻度
                DrawXTick(curvePoints);
            }

            //畫目標轉速
            draw_target_speed = (int)((float)target_speed / ratio);
            System.Drawing.Point px1 = new System.Drawing.Point(x_st, h_st - draw_target_speed);
            System.Drawing.Point px2 = new System.Drawing.Point(x_st + x_step * (steps - 1), h_st - draw_target_speed);
            g.DrawLine(new Pen(Brushes.Blue, 2), px1, px2);

            // Create string to draw.
            String drawString = "目標轉速: " + target_speed.ToString() + " rpm";
            // Create font and brush.
            Font drawFont = new Font("Arial", 16);
            SolidBrush drawBrush = new SolidBrush(Color.Blue);
            // Create point for upper-left corner of drawing.
            PointF drawPoint = new PointF(x_st, h_st - draw_target_speed);
            // Draw string to screen.
            g.DrawString(drawString, drawFont, drawBrush, drawPoint);
            
            g.Dispose();
            richTextBox1.Text += h_st.ToString() + "\n";
            richTextBox1.Text += draw_target_speed.ToString() + "\n";
            richTextBox1.Text += x_st.ToString() + "\t" + (h_st - draw_target_speed).ToString() + "\n";
            richTextBox1.Text += (x_st + x_step * (steps - 1)).ToString() + "\t" + (h_st - draw_target_speed).ToString() + "\n";
        }

        private void button5_Click(object sender, EventArgs e)
        {
            int i;
            float kp = float.Parse(tb_kp.Text);
            float ki = float.Parse(tb_ki.Text);
            float kd = float.Parse(tb_kd.Text);
            int target_speed = int.Parse(tb_target.Text);
            int max_speed = int.Parse(tb_max_speed.Text);
            int min_speed = int.Parse(tb_min_speed.Text);
            int max_duty = int.Parse(tb_max_duty.Text);
            int min_duty = int.Parse(tb_min_duty.Text);
            int steps = int.Parse(cb_steps.Text);
            int tolerance = int.Parse(tb_tolerance.Text);

            int[] real_speed_array = new int[200];
            int x_st = 0;
            int h_st = 0;
            int x_step = 0;
            int STEP = 0;
            int skip_pi = 0;

            //int STEP = (max_speed - min_speed) / (max_duty - min_duty);   //原本是這一行，改成以下16行。
            try
            {   //可能會產生錯誤的程式區段
                STEP = (max_speed - min_speed) / (max_duty - min_duty);
            }
            catch (Exception ex)
            {   //定義產生錯誤時的例外處理程式碼
                MessageBox.Show("參數錯誤：" + ex.Message);
                richTextBox1.Text += ex.Message + "\n";
                richTextBox1.Text += "max_duty = " + max_duty.ToString() + "\t";
                richTextBox1.Text += "min_duty = " + min_duty.ToString() + "\n";
            }
            finally
            {
                //一定會被執行的程式區段
                if (STEP > 0)
                    richTextBox1.Text += "STEP = " + STEP.ToString() + "\n";
                else
                    richTextBox1.Text += "FAIL STEP = " + STEP.ToString() + "\n";
            }

            label_STEP.Text = "STEP: " + STEP.ToString();

            int real_speed = 0;
            int error = 0;
            int pp = 0;
            int ii = 0;
            int dd = 0;
            int ii_old = 0;
            int error_old = 0;
            float pid = 0;
            int max_real_speed = 0;
            float ratio = 0;
            int draw_target_speed = 0;
            Point[] point_array0 = new Point[50];
            Point[] point_array1 = new Point[100];
            Point[] point_array2 = new Point[200];

            richTextBox1.Text += "kp = " + kp.ToString() + "\t";
            richTextBox1.Text += "ki = " + ki.ToString() + "\t";
            richTextBox1.Text += "kd = " + kd.ToString() + "\n";
            richTextBox1.Text += "target_speed = " + target_speed.ToString() + "\n";
            richTextBox1.Text += "max_speed = " + max_speed.ToString() + "\t";
            richTextBox1.Text += "min_speed = " + min_speed.ToString() + "\n";
            richTextBox1.Text += "max_duty = " + max_duty.ToString() + "\t";
            richTextBox1.Text += "min_duty = " + min_duty.ToString() + "\n";
            richTextBox1.Text += "steps = " + steps.ToString() + "\n";
            richTextBox1.Text += "STEP = " + STEP.ToString() + "\n";

            richTextBox1.Text += "step\ttgt\treal\terr\tpp\tii\tdd\tpid\n";
            for (i = 0; i < steps; i++)
            {
                if ((skip_pi == 0) && (real_speed >= target_speed))
                {
                    skip_pi = 1;
                    ii_old = 0;
                    error_old = 0;
                }

                error = target_speed - real_speed;
                pp = error;
                ii = error + ii_old;
                dd = error - error_old;
                pid = kp * pp + ki * ii + kd * dd;

                if (pid > pid_max)
                    pid_max = pid;
                else if (pid < pid_min)
                    pid_min = pid;

                real_speed_array[i] = real_speed;

                richTextBox1.Text += i.ToString() + "\t" + target_speed.ToString() + "\t" + real_speed.ToString() + "\t" + error.ToString() + "\t";
                richTextBox1.Text += pp.ToString() + "\t" + ii.ToString() + "\t" + dd.ToString() + "\t" + pid.ToString() + "\n";

                //richTextBox1.Text += "real_speed(" + (i + 1).ToString() + ")=" + real_speed.ToString() + ";";
                //richTextBox1.Text += "pid(" + (i + 1).ToString() + ")=" + pid.ToString() + ";";
                //richTextBox1.Text += "\n";

                if (pid > tolerance)
                    real_speed += STEP;
                else if (pid < -tolerance)
                    real_speed -= STEP;

                error_old = error;
                ii_old = ii;
            }

            //畫圖
            richTextBox1.Text += "\n\nW = " + panel1.Width.ToString() + "\n";
            richTextBox1.Text += "H = " + panel1.Height.ToString() + "\n";

            max_real_speed = real_speed_array.Max();
            label_max_speed.Text = "Max: " + max_real_speed.ToString();

            label_pid_max.Text = "pid_max: " + pid_max.ToString();
            label_pid_min.Text = "pid_min: " + pid_min.ToString();

            max_real_speed = Math.Max(max_real_speed, target_speed);
            richTextBox1.Text += "real_speed_max = " + max_real_speed.ToString() + "\n";
            ratio = (float)max_real_speed / (float)(panel1.Height * 90 / 100);
            richTextBox1.Text += "ratio = " + ratio.ToString() + "\n";

            for (i = 0; i < steps; i++)
            {
                real_speed_array[i] = (int)((float)real_speed_array[i] / ratio);
            }

            Graphics g = panel1.CreateGraphics();
            //g.Clear(Color.White);
            DrawXY();

            x_st = panel1.Width * 5 / 100;
            h_st = panel1.Height * 95 / 100;
            x_step = panel1.Width * 90 / 100 / (steps - 1);

            richTextBox1.Text += "x_st = " + x_st.ToString() + "\n";
            richTextBox1.Text += "h_st = " + h_st.ToString() + "\n";
            richTextBox1.Text += "x_step = " + x_step.ToString() + "\n";

            // Create pens.
            Pen greenPen = new Pen(Color.Green, 3);
            // Create points that define curve.

            for (i = 0; i < steps; i++)
            {
                if (cb_steps.SelectedIndex == 0)
                {
                    point_array0[i].X = x_st + x_step * i;
                    point_array0[i].Y = h_st - real_speed_array[i];
                }
                else if (cb_steps.SelectedIndex == 1)
                {
                    point_array1[i].X = x_st + x_step * i;
                    point_array1[i].Y = h_st - real_speed_array[i];
                }
                else if (cb_steps.SelectedIndex == 2)
                {
                    point_array2[i].X = x_st + x_step * i;
                    point_array2[i].Y = h_st - real_speed_array[i];
                }
            }

            if (cb_steps.SelectedIndex == 0)
            {
                Point[] curvePoints = point_array0;
                // Draw lines between original points to screen.
                //g.DrawLines(greenPen, curvePoints);   //畫直線

                // Draw curve to screen.
                g.DrawCurve(greenPen, curvePoints); //畫曲線

                //畫X刻度
                DrawXTick(curvePoints);
            }
            else if (cb_steps.SelectedIndex == 1)
            {
                Point[] curvePoints = point_array1;
                // Draw lines between original points to screen.
                //g.DrawLines(greenPen, curvePoints);   //畫直線

                // Draw curve to screen.
                g.DrawCurve(greenPen, curvePoints); //畫曲線

                //畫X刻度
                DrawXTick(curvePoints);
            }
            else if (cb_steps.SelectedIndex == 2)
            {
                Point[] curvePoints = point_array2;
                // Draw lines between original points to screen.
                //g.DrawLines(greenPen, curvePoints);   //畫直線

                // Draw curve to screen.
                g.DrawCurve(greenPen, curvePoints); //畫曲線

                //畫X刻度
                DrawXTick(curvePoints);
            }

            //畫目標轉速
            draw_target_speed = (int)((float)target_speed / ratio);
            System.Drawing.Point px1 = new System.Drawing.Point(x_st, h_st - draw_target_speed);
            System.Drawing.Point px2 = new System.Drawing.Point(x_st + x_step * (steps - 1), h_st - draw_target_speed);
            g.DrawLine(new Pen(Brushes.Blue, 2), px1, px2);

            // Create string to draw.
            String drawString = "目標轉速: " + target_speed.ToString() + " rpm";
            // Create font and brush.
            Font drawFont = new Font("Arial", 16);
            SolidBrush drawBrush = new SolidBrush(Color.Blue);
            // Create point for upper-left corner of drawing.
            PointF drawPoint = new PointF(x_st, h_st - draw_target_speed);
            // Draw string to screen.
            g.DrawString(drawString, drawFont, drawBrush, drawPoint);

            g.Dispose();

        }

        private void button6_Click(object sender, EventArgs e)
        {
            int i;
            float kp = float.Parse(tb_kp.Text);
            float ki = float.Parse(tb_ki.Text);
            float kd = float.Parse(tb_kd.Text);
            int target_speed = int.Parse(tb_target.Text);
            int max_speed = int.Parse(tb_max_speed.Text);
            int min_speed = int.Parse(tb_min_speed.Text);
            int max_duty = int.Parse(tb_max_duty.Text);
            int min_duty = int.Parse(tb_min_duty.Text);
            int steps = int.Parse(cb_steps.Text);
            int tolerance = int.Parse(tb_tolerance.Text);

            int[] real_speed_array = new int[200];
            int x_st = 0;
            int h_st = 0;
            int x_step = 0;
            int STEP = 0;
            int skip_pi = 0;

            //int STEP = (max_speed - min_speed) / (max_duty - min_duty);   //原本是這一行，改成以下16行。
            try
            {   //可能會產生錯誤的程式區段
                STEP = (max_speed - min_speed) / (max_duty - min_duty);
            }
            catch (Exception ex)
            {   //定義產生錯誤時的例外處理程式碼
                MessageBox.Show("參數錯誤：" + ex.Message);
                richTextBox1.Text += ex.Message + "\n";
                richTextBox1.Text += "max_duty = " + max_duty.ToString() + "\t";
                richTextBox1.Text += "min_duty = " + min_duty.ToString() + "\n";
            }
            finally
            {
                //一定會被執行的程式區段
                if (STEP > 0)
                    richTextBox1.Text += "STEP = " + STEP.ToString() + "\n";
                else
                    richTextBox1.Text += "FAIL STEP = " + STEP.ToString() + "\n";
            }

            label_STEP.Text = "STEP: " + STEP.ToString();

            int real_speed = 0;
            int error = 0;
            int pp = 0;
            int ii = 0;
            int dd = 0;
            int ii_old = 0;
            int error_old = 0;
            float pid = 0;
            int max_real_speed = 0;
            float ratio = 0;
            int draw_target_speed = 0;
            Point[] point_array0 = new Point[50];
            Point[] point_array1 = new Point[100];
            Point[] point_array2 = new Point[200];

            richTextBox1.Text += "kp = " + kp.ToString() + "\t";
            richTextBox1.Text += "ki = " + ki.ToString() + "\t";
            richTextBox1.Text += "kd = " + kd.ToString() + "\n";
            richTextBox1.Text += "target_speed = " + target_speed.ToString() + "\n";
            richTextBox1.Text += "max_speed = " + max_speed.ToString() + "\t";
            richTextBox1.Text += "min_speed = " + min_speed.ToString() + "\n";
            richTextBox1.Text += "max_duty = " + max_duty.ToString() + "\t";
            richTextBox1.Text += "min_duty = " + min_duty.ToString() + "\n";
            richTextBox1.Text += "steps = " + steps.ToString() + "\n";
            richTextBox1.Text += "STEP = " + STEP.ToString() + "\n";

            richTextBox1.Text += "step\ttgt\treal\terr\tpp\tii\tdd\tpid\n";
            for (i = 0; i < steps; i++)
            {
                if ((skip_pi == 0) && (real_speed >= target_speed))
                {
                    skip_pi = 1;
                    ii_old = 0;
                    error_old = 0;
                }

                error = target_speed - real_speed;
                pp = error;
                ii = error + ii_old;
                dd = error - error_old;
                pid = kp * pp + ki * ii + kd * dd;

                if (pid > pid_max)
                    pid_max = pid;
                else if (pid < pid_min)
                    pid_min = pid;

                real_speed_array[i] = real_speed;

                richTextBox1.Text += i.ToString() + "\t" + target_speed.ToString() + "\t" + real_speed.ToString() + "\t" + error.ToString() + "\t";
                richTextBox1.Text += pp.ToString() + "\t" + ii.ToString() + "\t" + dd.ToString() + "\t" + pid.ToString() + "\n";

                //richTextBox1.Text += "real_speed(" + (i + 1).ToString() + ")=" + real_speed.ToString() + ";";
                //richTextBox1.Text += "pid(" + (i + 1).ToString() + ")=" + pid.ToString() + ";";
                //richTextBox1.Text += "\n";

                if (pid > (tolerance*5))
                    real_speed += STEP;
                else if (pid < -(tolerance*5))
                    real_speed -= STEP;

                error_old = error;
                ii_old = ii;
            }

            //畫圖
            richTextBox1.Text += "\n\nW = " + panel1.Width.ToString() + "\n";
            richTextBox1.Text += "H = " + panel1.Height.ToString() + "\n";

            max_real_speed = real_speed_array.Max();
            label_max_speed.Text = "Max: " + max_real_speed.ToString();

            label_pid_max.Text = "pid_max: " + pid_max.ToString();
            label_pid_min.Text = "pid_min: " + pid_min.ToString();

            max_real_speed = Math.Max(max_real_speed, target_speed);
            richTextBox1.Text += "real_speed_max = " + max_real_speed.ToString() + "\n";
            ratio = (float)max_real_speed / (float)(panel1.Height * 90 / 100);
            richTextBox1.Text += "ratio = " + ratio.ToString() + "\n";

            for (i = 0; i < steps; i++)
            {
                real_speed_array[i] = (int)((float)real_speed_array[i] / ratio);
            }

            Graphics g = panel1.CreateGraphics();
            //g.Clear(Color.White);
            DrawXY();

            x_st = panel1.Width * 5 / 100;
            h_st = panel1.Height * 95 / 100;
            x_step = panel1.Width * 90 / 100 / (steps - 1);

            richTextBox1.Text += "x_st = " + x_st.ToString() + "\n";
            richTextBox1.Text += "h_st = " + h_st.ToString() + "\n";
            richTextBox1.Text += "x_step = " + x_step.ToString() + "\n";

            // Create pens.
            Pen bluePen = new Pen(Color.Blue, 3);
            // Create points that define curve.

            for (i = 0; i < steps; i++)
            {
                if (cb_steps.SelectedIndex == 0)
                {
                    point_array0[i].X = x_st + x_step * i;
                    point_array0[i].Y = h_st - real_speed_array[i];
                }
                else if (cb_steps.SelectedIndex == 1)
                {
                    point_array1[i].X = x_st + x_step * i;
                    point_array1[i].Y = h_st - real_speed_array[i];
                }
                else if (cb_steps.SelectedIndex == 2)
                {
                    point_array2[i].X = x_st + x_step * i;
                    point_array2[i].Y = h_st - real_speed_array[i];
                }
            }

            if (cb_steps.SelectedIndex == 0)
            {
                Point[] curvePoints = point_array0;
                // Draw lines between original points to screen.
                //g.DrawLines(bluePen, curvePoints);   //畫直線

                // Draw curve to screen.
                g.DrawCurve(bluePen, curvePoints); //畫曲線

                //畫X刻度
                DrawXTick(curvePoints);
            }
            else if (cb_steps.SelectedIndex == 1)
            {
                Point[] curvePoints = point_array1;
                // Draw lines between original points to screen.
                //g.DrawLines(bluePen, curvePoints);   //畫直線

                // Draw curve to screen.
                g.DrawCurve(bluePen, curvePoints); //畫曲線

                //畫X刻度
                DrawXTick(curvePoints);
            }
            else if (cb_steps.SelectedIndex == 2)
            {
                Point[] curvePoints = point_array2;
                // Draw lines between original points to screen.
                //g.DrawLines(bluePen, curvePoints);   //畫直線

                // Draw curve to screen.
                g.DrawCurve(bluePen, curvePoints); //畫曲線

                //畫X刻度
                DrawXTick(curvePoints);
            }

            //畫目標轉速
            draw_target_speed = (int)((float)target_speed / ratio);
            System.Drawing.Point px1 = new System.Drawing.Point(x_st, h_st - draw_target_speed);
            System.Drawing.Point px2 = new System.Drawing.Point(x_st + x_step * (steps - 1), h_st - draw_target_speed);
            g.DrawLine(new Pen(Brushes.Green, 2), px1, px2);

            // Create string to draw.
            String drawString = "目標轉速: " + target_speed.ToString() + " rpm";
            // Create font and brush.
            Font drawFont = new Font("Arial", 16);
            SolidBrush drawBrush = new SolidBrush(Color.Green);
            // Create point for upper-left corner of drawing.
            PointF drawPoint = new PointF(x_st, h_st - draw_target_speed);
            // Draw string to screen.
            g.DrawString(drawString, drawFont, drawBrush, drawPoint);

            g.Dispose();


        }

    }
}
