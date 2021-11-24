using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace vcs_Puzzle2
{
    public class Puzzle
    {
        public enum Diff         //遊戲難度
        {
            simple,//簡單
            ordinary,//普通
            difficulty//困難
        }
        private struct Node      //拼圖單元格結構體
        {
            public Image Img;
            public int Num;
        }
        private Image _img;      //拼圖圖片
        public int Width;       //拼圖邊長
        private Diff _gameDif;   //遊戲難度
        private Node[,] node;    //單元格數組
        public int N;           //單元格數組行列數

        /// <summary>
        /// 構造函數
        /// </summary>
        /// <param name="Img">拼圖大圖</param>
        /// <param name="GameDif">遊戲難度，該類下結構體Diff</param>
        public Puzzle(Image Img,int Width, Diff GameDif)
        {
            this._gameDif = GameDif;
            this._img = Img;
            this.Width = Width;
            switch(this._gameDif)
            {
                case Diff.simple:　　　　//簡單則單元格數組保存為3*3的二維數組
                    this.N = 3;
                    node=new Node[3,3];
                    break;
                case Diff.ordinary:　　  //一般則為5*5
                    this.N = 5;
                    node = new Node[5, 5];
                    break;
                case Diff.difficulty:　　//困難則為9*9
                    this.N = 9;
                    node = new Node[9, 9];
                    break;
            }
            
            //分割圖片形成各單元保存在數組中
            int Count = 0;
            for (int x = 0; x < this.N; x++)
            {
                for (int y = 0; y < this.N; y++)
                {

                    node[x, y].Img = CaptureImage(this._img, this.Width / this.N, this.Width / this.N, x * (this.Width / this.N), y * (this.Width / this.N));
                    node[x, y].Num = Count;
                    Count++;
                }
            }
            
            for (int x = 0; x < this.N; x++)
            {
                for (int y = 0; y < this.N; y++)
                {

                    Graphics newGra = Graphics.FromImage(node[x, y].Img);
                    newGra.DrawLine(new Pen(Color.White), new Point(0, 0), new Point(0, this.Width / this.N));
                    newGra.DrawLine(new Pen(Color.White), new Point(0, 0), new Point(this.Width / this.N, 0));
                    newGra.DrawLine(new Pen(Color.White), new Point(this.Width / this.N, this.Width / this.N), new Point(this.Width / this.N, 0));
                    newGra.DrawLine(new Pen(Color.White), new Point(this.Width / this.N, this.Width / this.N), new Point(0,this.Width / this.N));
                }
            }
            //(最後一項為空單獨處理)
            node[N - 1, N - 1].Img = Image.FromFile(@"../../img/end.PNG");
            Graphics newGra2 = Graphics.FromImage(node[N - 1, N - 1].Img);
            newGra2.DrawLine(new Pen(Color.Red), new Point(1, 1), new Point(1, this.Width / this.N - 1));
            newGra2.DrawLine(new Pen(Color.Red), new Point(1, 1), new Point(this.Width / this.N - 1, 1));
            newGra2.DrawLine(new Pen(Color.Red), new Point(this.Width / this.N - 1, this.Width / this.N - 1), new Point(this.Width / this.N - 1, 1));
            newGra2.DrawLine(new Pen(Color.Red), new Point(this.Width / this.N - 1, this.Width / this.N - 1), new Point( 1,this.Width / this.N - 1));
            //打亂拼圖
            this.Upset();

        }


        /// <summary>
        /// 由圖片fromImage中截圖並返回
        /// </summary>
        /// <param name="fromImage">原圖片</param>
        /// <param name="width">寬</param>
        /// <param name="height">高</param>
        /// <param name="spaceX">起始X坐標</param>
        /// <param name="spaceY">起始Y坐標</param>
        /// <returns></returns>
        public  Image CaptureImage(Image fromImage, int width, int height, int spaceX, int spaceY)
        {
            int x = 0;
            int y = 0;
            int sX = fromImage.Width - width;
            int sY = fromImage.Height - height;
            if (sX > 0)
            {
                x = sX > spaceX ? spaceX : sX;
            }
            else
            {
                width = fromImage.Width;
            }
            if (sY > 0)
            {
                y = sY > spaceY ? spaceY : sY;
            }
            else
            {
                height = fromImage.Height;
            }

            //創建新圖位圖   
            Bitmap bitmap = new Bitmap(width, height);
            //創建作圖區域   
            Graphics graphic = Graphics.FromImage(bitmap);
            //截取原圖相應區域寫入作圖區   
            graphic.DrawImage(fromImage, 0, 0, new Rectangle(x, y, width, height), GraphicsUnit.Pixel);
            //從作圖區生成新圖   
            Image saveImage = Image.FromHbitmap(bitmap.GetHbitmap());
            return saveImage;
        }
        /// <summary>
        /// 移動坐標（x,y）拼圖單元
        /// </summary>
        /// <param name="x">拼圖單元x坐標</param>
        /// <param name="y">拼圖單元y坐標</param>
        public bool Move(int x,int y)
        {
            //MessageBox.Show(" " + node[2, 2].Num);
            if (x + 1 != N && node[x + 1, y].Num ==  N * N - 1)
            {
                Swap(new Point(x + 1, y), new Point(x, y));
                return true;
            }
            if (y + 1 != N && node[x, y + 1].Num ==  N * N - 1)
            {
                Swap(new Point(x, y + 1), new Point(x, y));
                return true;
            }                
            if (x - 1 != -1 && node[x - 1, y].Num == N * N - 1)
            {
                Swap(new Point(x - 1, y), new Point(x, y));
                return true;
            }   
            if (y - 1 != -1 && node[x, y - 1].Num == N * N - 1)
            {
                Swap(new Point(x, y - 1), new Point(x, y));
                return true;
            }
            return false;
                
        }
        //交換兩個單元格
        private  void Swap(Point a, Point b)
        {
            Node temp = new Node();
            temp = this.node[a.X, a.Y];
            this.node[a.X, a.Y] = this.node[b.X, b.Y];
            this.node[b.X, b.Y] = temp;
        }
        public bool Judge()
        {
            int count=0;
            for (int x = 0; x < this.N; x++)
            {
                for (int y = 0; y < this.N; y++)
                {
                    if (this.node[x, y].Num != count)
                        return false;
                    count++;
                }
            }
            return true;
        }
        public Image Display()
        {
            Bitmap bitmap = new Bitmap(this.Width, this.Width);
            //創建作圖區域   
            Graphics newGra = Graphics.FromImage(bitmap);
            for (int x = 0; x < this.N; x++)
                for (int y = 0; y < this.N; y++)
                    newGra.DrawImage(node[x, y].Img, new Point(x * this.Width / this.N, y * this.Width / this.N));
            return bitmap;
        }
        /// <summary>
        /// 打亂拼圖
        /// </summary>
        public void Upset()
        {
            int sum = 100000;
            if (this._gameDif == Diff.simple) sum = 10000;
            //if (this._gameDif == Diff.ordinary) sum = 100000;
            Random ran = new Random();
            for (int i = 0, x = N - 1, y = N - 1; i < sum; i++)
            {
                long tick = DateTime.Now.Ticks;
                ran = new Random((int)(tick & 0xffffffffL) | (int)(tick >> 32)|ran.Next());
                switch (ran.Next(0, 4))
                {
                    case 0:
                        if (x + 1 != N)
                        {
                            Move(x + 1, y);
                            x = x + 1;
                        }
                            
                        break;
                    case 1:
                        if (y + 1 != N)
                        {
                            Move(x, y + 1);
                            y = y + 1;
                        } 
                        break;
                    case 2:
                        if (x - 1 != -1)
                        {
                            Move(x - 1, y);
                            x = x - 1;
                        }      
                        break;
                    case 3:
                        if (y - 1 != -1)
                        {
                            Move(x, y - 1);
                            y = y - 1;
                        }
                        break;
                }

            }
        }

        

    }
}
