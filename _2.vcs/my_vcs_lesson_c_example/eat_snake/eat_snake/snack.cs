using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Drawing;


namespace eat_snake
{
    class snack
    {
        public int lenth=0;
        private List<int[]>Stack=new List<int[]>();
        private int[,]jiemian=new int[35,24];//1-->身体位置 2-->食物分值1

        public void push(int x,int y)
        {
            int[] temp = new int[2];
            temp[0] = x;
            temp[1] = y;
            Stack.Add(temp);
            jiemian[(x-11)/10,(y-28)/10] = 1;
            lenth++;
        }
        public bool Pop(ref int[] x)
        {
            if (Stack.Count > 0)
            {
                x = Stack[0];
                Stack.RemoveAt(0);
                jiemian[(x[0]-11)/10, (x[1]-28)/10]=0;
                lenth--;
                return true;
            }
            else return false;
        }

        public void restart()//清空数据
        {
            Stack.Clear();
            jiemian = null;
            jiemian = new int[35, 24];
        }
        public void modify(int x,int y,int socre=1)//x y坐标和应该的分数 默认等于1
        {
            jiemian[x, y] = socre + 1;
        }
        public int IsEat(int x,int y)//检测是否吃到食物或者迟到自身
        {
            return jiemian[x,y];
        }
    }
    class cube//一个矩形
    {
        private snack buffer=new snack();
        private int ox = 0;
        private int oy = 0;
        private int addlenth = 0;
        private Graphics p;
        public cube(int x,int y,Graphics g)
        {
            ox = x;
            oy = y;
            p = g;
            g.DrawRectangle(new Pen(Color.Black,2),x,y,5,5);
            g.FillRectangle(new SolidBrush(Color.Black),x,y,5,5);
            buffer.push(x, y);
        }
        private int check()//检测边界，得分，游戏结束  0-->无事件 1-->得分 2-->触碰到边界 3-->触碰到自己  next函数之后进行检测
        {
            if (ox < 11 || ox > 356 || oy < 28 || oy > 263)
            {
                return 2;
            }
            else if(buffer.IsEat((ox-11)/10,(oy-28)/10) == 0)
            {
                return 0;
            }
            else if(buffer.IsEat((ox-11)/10,(oy-28)/10) == 1)
            {
                return 3;
            }
            else
            {
                addlenth += buffer.IsEat((ox-11)/10,(oy-28)/10)-1;
                return 1;
            }
        }

        public bool Createfood(int x,int y,int socre=1)
        {
            if (buffer.IsEat((x-11)/10, (y-28)/10) == 1) return false;
            buffer.modify((x-11)/10,(y-28)/10,socre);
            Color t=new Color();
            //一分红  二分紫 三分黄
            switch(socre)
            {
                case 1: t = Color.Red; break;
                case 2: t = Color.Purple; break;
                case 3: t = Color.Gold; break;
            }
            p.DrawRectangle(new Pen(t, 2), x, y, 5, 5);
            p.FillRectangle(new SolidBrush(t), x, y, 5, 5);
            return true;
        }
        Random sx = new Random();
        Random sy = new Random();
        Random fenzhi = new Random();
        private int Get_Pos()
        {
            int[] pos = new int[2];
            int cube_x = 0;
            int cube_y = 0;
            int point = fenzhi.Next(1,4);
            while (true)
            {
                cube_x = sx.Next(0, 34);
                cube_y = sy.Next(0, 23);
                pos[0] = 11 + cube_x * 10;
                pos[1] = 28 + cube_y * 10;
                if (this.Createfood(pos[0], pos[1], point)) break;
            }
            return point;
        }
        public bool next(int direct,ref int point)//画下一个矩形 定义 0上1下2左3右
        {
            int dec = 0;
            point = 0;
            switch(direct)
            {
                case 0: oy += 10; break;
                case 1: oy -= 10; break;
                case 2: ox -= 10; break;
                case 3: ox += 10; break;
            }
            //这里进行检测
            dec=this.check();
            if(dec == 2)//碰到边界
            {
                return false;
            }
            else if (dec == 3)//碰到自己
            {
                p.DrawRectangle(new Pen(Color.Red, 2), ox, oy, 5, 5);
                p.FillRectangle(new SolidBrush(Color.Red), ox, oy, 5, 5);
                return false;
            }
            else
            {
                p.DrawRectangle(new Pen(Color.Black, 2), ox, oy, 5, 5);
                p.FillRectangle(new SolidBrush(Color.Black), ox, oy, 5, 5);
                buffer.push(ox, oy);
                if (dec == 1)
                {
                    point = addlenth;
                    Get_Pos();
                }
                return true;
            }
        }
        public void move()//消掉最后一个
        {
            if (addlenth == 0)
            {
                int[] temp = new int[2];
                buffer.Pop(ref temp);
                p.DrawRectangle(new Pen(Color.White, 2), temp[0], temp[1], 5, 5);
                p.FillRectangle(new SolidBrush(Color.White), temp[0], temp[1], 5, 5);
            }
            else addlenth--;
        }

        public void end()
        {
            buffer.restart();
        }
    }
}
