using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        List<ClassBomb> bombList = new List<ClassBomb>();
        List<ClassBoom> boomList = new List<ClassBoom>();
        List<ClassRocket> rocketList = new List<ClassRocket>();
        ClassLandscape landscape = new ClassLandscape();
        Font fn = new Font("Times New Roman", 20);
        Random rd = new Random();

        int Gain = 0;

        public Form1()
        {
            InitializeComponent();
            landscape.Build(this.ClientSize.Width, this.ClientSize.Height);
        }

        private void Form1_MouseClick(object sender, MouseEventArgs e)
        {
            ClassRocket rocket = new ClassRocket(e.X, e.Y, this.ClientSize.Width / 2, this.ClientSize.Height);
            rocketList.Add(rocket);

            //ClassBoom boom = new ClassBoom(e.X, e.Y, 1, ClassBoom.status.active);
            //boomList.Add(boom);
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            landscape.Draw(e.Graphics);

            // 火箭和炸彈 的碰撞測試
            foreach (ClassRocket rocket in rocketList)
            {
                foreach (ClassBomb bomb in bombList)
                {
                    if (rocket.CheckCollision(bomb.X, bomb.Y, 10))
                    {
                        rocket.X = bomb.X;
                        rocket.Y = bomb.Y;

                        rocket.Shooting = false;
                        Gain++;
                    }
                }
            }

            // 火箭往上飛
            for (int i = rocketList.Count - 1; i >= 0; i--)
            {
                if (rocketList[i].Shooting == false) // 火箭 就定位 或 和炸彈碰撞
                {
                    ClassBoom boom = new ClassBoom(rocketList[i].X, rocketList[i].Y, 1, ClassBoom.status.active);
                    boomList.Add(boom);
                    rocketList.RemoveAt(i);
                }
            }

            foreach (ClassRocket b in rocketList)
            {
                b.Draw(e.Graphics);
            }

            // 爆炸
            for (int i = boomList.Count - 1; i >= 0; i--)
            {
                if (boomList[i].Current_Status == ClassBoom.status.die) boomList.RemoveAt(i);
            }

            foreach (ClassBoom b in boomList)
            {
                b.Draw(e.Graphics);
            }

            // 爆炸和炸彈 的碰撞測試
            foreach (ClassBoom boom in boomList)
            {
                foreach (ClassBomb bomb in bombList)
                {
                    if (boom.CheckCollision(bomb.X, bomb.Y))
                    {
                        bomb.Falling = false;
                        if (boom.boom_Type == ClassBoom.BoomType.active)
                            Gain++;
                    }
                }
            }

            // 炸彈往下掉
            for (int i = bombList.Count - 1; i >= 0; i--)
            {
                if (bombList[i].Falling == false)  // 到底了 或是 被爆炸或Rocket 碰到了
                {
                    ClassBoom boom = new ClassBoom(bombList[i].X, bombList[i].Y, 1, ClassBoom.status.active);
                    boom.boom_Type = ClassBoom.BoomType.passive;
                    boomList.Add(boom);

                    bombList.RemoveAt(i);
                }
            }
            foreach (ClassBomb b in bombList)
            {
                b.Draw(e.Graphics);
            }

            e.Graphics.DrawString("Gain : " + Gain.ToString(), fn, Brushes.White, 10, 30, StringFormat.GenericTypographic);
            e.Graphics.DrawString("Lose : " + ClassBomb.ToButtomCount.ToString(), fn, Brushes.White, 10, 60, StringFormat.GenericTypographic);
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            this.Invalidate();
        }

        private void timer2_Tick(object sender, EventArgs e)
        {
            if (rd.NextDouble() < 0.1)
            {
                ClassBomb bomb = new ClassBomb(this.ClientSize.Width,
                                            this.ClientSize.Height,
                                            rd.Next(this.ClientSize.Width),
                                            rd.Next(this.ClientSize.Width));

                bombList.Add(bomb);
            }
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            landscape.Build(this.ClientSize.Width, this.ClientSize.Height);
            bombList.Clear();
            boomList.Clear();
            rocketList.Clear();
            Gain = 0;
            ClassBomb.ToButtomCount = 0;
        }
    }
}