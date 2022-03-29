using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Text;
using System.Threading;
using System.Windows.Forms;

namespace Main
{
    public partial class MainForm : Form
    {
        private List<Flakes> flyFlakeList = new List<Flakes>();
        private static Random random = new Random();

        //���������߳̿��ƣ����������Timer������Ҳ�ѵø���
        private delegate void refreshHandler();

        public MainForm()
        {
            InitializeComponent();

            SetStyle(ControlStyles.UserPaint | ControlStyles.AllPaintingInWmPaint | ControlStyles.DoubleBuffer, true);
            //��ȡ���泤�ȺͿ��
            //Width = Screen.PrimaryScreen.Bounds.Width;
            //Height = Screen.PrimaryScreen.Bounds.Height;
        }

        private void MainForm_Load(object sender, EventArgs e)
        {
            System.Windows.Forms.Timer timer = new System.Windows.Forms.Timer();
            timer.Interval =  100;
            timer.Tick += ManageFlake;
            timer.Start();
        }

        /// <summary>
        /// ���������Fly
        /// </summary>
        private void ManageFlake(object o, EventArgs e)//object o, EventArgs e
        {
            Thread.Sleep(100);
            addFlake();
            operateFlake();
            this.Invoke((refreshHandler)refreshForm);
        }

        /// <summary>
        /// ���Fly
        /// </summary>
        private void addFlake()
        {
            if (random.NextDouble() < 0.2)
            {
                IImage gdiImage = new GDIPlusImage();        
                IImage fileImage = new FileImage();
                //�������Fly
                ProxyImage.AddImage(gdiImage);
                ProxyImage.AddImage(fileImage);
                Flakes flake = new Flakes(random.Next(-50, Width + 50), random.Next(-20, -7), (float)(random.NextDouble() - 0.5f) * 2f,
                    (float)(random.NextDouble() * 3) + 2f, random.Next(0, 359), random.Next(-3, 3) * 2, (float)(random.NextDouble() / 2) + 0.75f, ProxyImage.GetImage());

                if (flake.RotationRate == 0)
                {
                    flake.RotationRate = 3f;
                }
                flyFlakeList.Add(flake);
                //Refresh();
            } 
        }

        /// <summary>
        /// �޸�Fly����
        /// </summary>
        private void operateFlake()
        {
            List<Flakes> del = new List<Flakes>();
            foreach (Flakes s in flyFlakeList)
            {
                s.X += s.XRate;
                s.Y += s.YRate;
                s.Rotation += s.RotationRate;
                s.XRate += ((float)random.NextDouble() - 0.5f) * 0.7f;
                s.XRate = Math.Max(s.XRate, -2f);
                s.XRate = Math.Min(s.XRate, +2f);

                if (s.Y > Height + 10)
                {
                    del.Add(s);
                }
            }
            foreach (Flakes s in del)
            {
                flyFlakeList.Remove(s);
            } 
        }

        /// <summary>
        /// ˢ��
        /// </summary>
        private void refreshForm()
        {
            this.Refresh();
        }

        /// <summary>
        /// ��д�ػ��ƽ���
        /// </summary>
        /// <param name="e">�ػ��¼�</param>
        protected override void OnPaint(PaintEventArgs e)
        {
            SetStyle(ControlStyles.UserPaint | ControlStyles.AllPaintingInWmPaint | ControlStyles.DoubleBuffer, true);
            Graphics g = e.Graphics;
            g.SmoothingMode = SmoothingMode.HighQuality;

            foreach (Flakes s in flyFlakeList)
            {
                g.ResetTransform();
                //g.TranslateTransform(-16, -16, MatrixOrder.Append);
                g.ScaleTransform(s.Scale, s.Scale, MatrixOrder.Append);
                g.RotateTransform(s.Rotation, MatrixOrder.Append);
                g.TranslateTransform(s.X, s.Y, MatrixOrder.Append);

                g.DrawImage(s.ShowImage, 0, 0);
            }
            //base.OnPaint(e);
        }

        /// <summary>
        /// ˫�����˳�
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void notifyIcon1_MouseDoubleClick(object sender, MouseEventArgs e)
        {
            notifyIcon1.Visible = false;
            Application.Exit();
        }

        /// <summary>
        /// �����ô���
        /// </summary>
        private void openAbout()
        {
            aboutForm childForm = new aboutForm();
            childForm.Show();
        }

        /// <summary>
        /// �˳�����
        /// </summary>
        /// <param name="sender">object</param>
        /// <param name="e">�¼�</param>
        private void tsmiExit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void tsmiAbout_Click(object sender, EventArgs e)
        {
            openAbout();
        }
    }
}