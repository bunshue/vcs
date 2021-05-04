using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace WindowsApplication1
{
    public partial class Form1 : Form
    {
        Image[] image = new Image[9];
        Panel[] panel = new Panel[9];
        Random rd = new Random();
        int FromPanelNo, ToPanelNo, FromPaneTag;
        Point MovingLocation = new Point();
        Point MovingDirection = new Point();

        //  0  1  2
        //  3  4  5
        //  6  7  8
        Point[] LegalMove = new Point[]  // 合法移動的方式 Point(從, 到)
            {
                new Point(0,1), new Point(0,3),
                new Point(1,0), new Point(1,4), new Point(1,2),
                new Point(2,1), new Point(2,5),
                new Point(3,0), new Point(3,4), new Point(3,6),
                new Point(4,1), new Point(4,3), new Point(4,7), new Point(4,5),
                new Point(5,2), new Point(5,4), new Point(5,8),
                new Point(6,3), new Point(6,7),
                new Point(7,4), new Point(7,6), new Point(7,8),
                new Point(8,5), new Point(8,7)
            };

        int Count = 0; // 用了幾步
        int MovingSpeed = 20; // 動畫移動的速度參數

        public Form1()
        {
            InitializeComponent();
            image[0] = null;
            image[1] = new Bitmap(Properties.Resources.A002);
            image[2] = new Bitmap(Properties.Resources.A003);
            image[3] = new Bitmap(Properties.Resources.A004);
            image[4] = new Bitmap(Properties.Resources.A005);
            image[5] = new Bitmap(Properties.Resources.A006);
            image[6] = new Bitmap(Properties.Resources.A007);
            image[7] = new Bitmap(Properties.Resources.A008);
            image[8] = new Bitmap(Properties.Resources.A009);

            panel[0] = panel0;
            panel[1] = panel1;
            panel[2] = panel2;
            panel[3] = panel3;
            panel[4] = panel4;
            panel[5] = panel5;
            panel[6] = panel6;
            panel[7] = panel7;
            panel[8] = panel8;

            button1_Click(this, null);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            for (int i = 0; i <= 8; i++)
                panel[i].Tag = i;

            int k1, k2, t;
            for (int i = 0; i <= 20; i++)
            {
                k1 = rd.Next(9);
                k2 = rd.Next(9);
                t = (int)panel[k1].Tag;
                panel[k1].Tag = panel[k2].Tag;
                panel[k2].Tag = t;
            }

            for (int i = 0; i <= 8; i++)
                panel[i].BackgroundImage = image[(int)panel[i].Tag];

            Count = 0;
            label1.Text = Count.ToString();

            for (int i = 0; i <= 8; i++)
                panel[i].Enabled = true; 
        }

        private void panel0_Click(object sender, EventArgs e)
        {
            if (timer1.Enabled == true) return;

            Panel x = (Panel)sender;
            
            // 找出 是哪一個 Panel 被點到
            int SelectedPanelNo = 0;
            for (int i = 0; i <= 8; i++)
            {
                if (panel[i] == x)
                {
                    SelectedPanelNo = i;
                    break;
                }
            }

            // 找出 哪一個 Panel 是空的
            int EmptyPanelNo = 0;
            for (int i = 0; i <= 8; i++)
            {
                if ((int)panel[i].Tag == 0)
                {
                    EmptyPanelNo = i;
                    break;
                }
            }

            int k;
            for (int i = 0; i < 24; i++)
            {
                if (LegalMove[i].X == SelectedPanelNo &&
                    LegalMove[i].Y == EmptyPanelNo)
                {
                    Count++;
                    label1.Text = Count.ToString();

                    FromPanelNo = SelectedPanelNo;
                    ToPanelNo = EmptyPanelNo;
                    FromPaneTag = (int)panel[SelectedPanelNo].Tag;
                    panelMoving.BackgroundImage = panel[FromPanelNo].BackgroundImage;
                    MovingLocation = panel[FromPanelNo].Location;
                    if (MovingLocation.X > panel[ToPanelNo].Location.X)
                        MovingDirection.X = -MovingSpeed;
                    else if (MovingLocation.X < panel[ToPanelNo].Location.X)
                        MovingDirection.X = MovingSpeed;
                    else MovingDirection.X = 0;

                    if (MovingLocation.Y > panel[ToPanelNo].Location.Y)
                        MovingDirection.Y = -MovingSpeed;
                    else if (MovingLocation.Y < panel[ToPanelNo].Location.Y)
                        MovingDirection.Y = MovingSpeed;
                    else MovingDirection.Y = 0;

                    panelMoving.Location = new Point(MovingLocation.X, MovingLocation.Y);
                    panelMoving.Visible = true;

                    panel[SelectedPanelNo].BackgroundImage = null;
                    timer1.Enabled = true;

                    //k = (int) panel[SelectedPanelNo].Tag;
                    //panel[SelectedPanelNo].Tag = panel[EmptyPanelNo].Tag;
                    //panel[EmptyPanelNo].Tag = k;

                    //panel[SelectedPanelNo].BackgroundImage = image[(int)panel[SelectedPanelNo].Tag];
                    //panel[EmptyPanelNo].BackgroundImage = image[(int)panel[EmptyPanelNo].Tag];
                    break;
                }
            }
        }

        void CheckFinished()
        {
            // 檢查是否正確
            if ((int)panel[0].Tag == 1 && (int)panel[1].Tag == 2 && (int)panel[2].Tag == 3 &&
                (int)panel[3].Tag == 8 && (int)panel[4].Tag == 0 && (int)panel[5].Tag == 4 &&
                (int)panel[6].Tag == 7 && (int)panel[7].Tag == 6 && (int)panel[8].Tag == 5)
            {
                for (int i = 0; i <= 8; i++)
                    panel[i].Enabled = false;
                MessageBox.Show("完成了！");
            }
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            MovingLocation.X += MovingDirection.X;
            MovingLocation.Y += MovingDirection.Y;

            if ((MovingDirection.X < 0 && MovingLocation.X <= panel[ToPanelNo].Location.X) ||
                (MovingDirection.X > 0 && MovingLocation.X >= panel[ToPanelNo].Location.X))
            {
                MovingLocation.X = panel[ToPanelNo].Location.X;
                MovingDirection.X = 0;
            }

            if ((MovingDirection.Y < 0 && MovingLocation.Y <= panel[ToPanelNo].Location.Y) ||
                (MovingDirection.Y > 0 && MovingLocation.Y >= panel[ToPanelNo].Location.Y))
            {
                MovingLocation.Y = panel[ToPanelNo].Location.Y;
                MovingDirection.Y = 0;
            }

            panelMoving.Location = new Point(MovingLocation.X, MovingLocation.Y);


            if (MovingDirection.X == 0 && MovingDirection.Y == 0)
            {
                timer1.Enabled = false;
                panelMoving.Visible = false;
                panel[FromPanelNo].BackgroundImage = null;
                panel[ToPanelNo].BackgroundImage = panelMoving.BackgroundImage;

                panel[FromPanelNo].Tag = 0;
                panel[ToPanelNo].Tag = FromPaneTag;
                CheckFinished();
            }
        }
    }
}