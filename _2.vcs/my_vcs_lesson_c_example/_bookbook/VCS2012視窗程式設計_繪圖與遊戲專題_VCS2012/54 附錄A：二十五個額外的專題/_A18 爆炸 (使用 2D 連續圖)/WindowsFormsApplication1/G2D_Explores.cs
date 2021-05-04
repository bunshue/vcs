using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Drawing;

namespace WindowsFormsApplication1
{
    class G2D_Explores
    {
        Image myImage;
        List<Point> ICON_List = new List<Point>(); // 紀錄小圖的位置
        Point ICON_Size = new Point();   // 小圖的寬高

        List<Point> myPosList = new List<Point>();     // 紀錄 爆炸的位置
        List<short> myCurrent_NoList = new List<short>();  // 紀錄 爆炸的圖形次序編號

        public G2D_Explores(Image myImage, int col, int row)
        {
            this.myImage = myImage;
            Point point = new Point();

            ICON_Size.X = myImage.Width / col;  // 每張小圖的寬
            ICON_Size.Y = myImage.Height / row;

            for (int i = 0; i < row; i++)  // i 往下走
                for (int j = 0; j < col; j++) // j 往右走
                {
                    point.X = j * ICON_Size.X;  // j 乘成上 小圖的寬
                    point.Y = i * ICON_Size.Y;  // i 乘成上 小圖的高
                    ICON_List.Add(point);
                }
        }

        public int Count  // 屬性 幾張小圖
        {
            get
            {
                return myPosList.Count;
            }
        }

        // 加入一個座標
        public void AddPos(Point pos)
        {
            myPosList.Add(pos);
            myCurrent_NoList.Add(0);
        }

        public void Update()
        {
            // TODO: Add your update code here
            //ElapsedTime += gameTime.ElapsedGameTime.TotalMilliseconds; // 兩個 Frame 間隔的千分秒
            //if (ElapsedTime > FrameSpeed)
            //{
            //    ElapsedTime = 0;

                for (int i = myCurrent_NoList.Count - 1; i >= 0; i--)
                {
                    myCurrent_NoList[i]++;
                    if (myCurrent_NoList[i] >= ICON_List.Count)
                    {
                        myCurrent_NoList.RemoveAt(i);
                        myPosList.RemoveAt(i);
                    }
                }
            //}
        }

        public void Draw(Graphics G)
        {
            for (int i = 0; i < myPosList.Count; i++)
            {
                Rectangle dest = new Rectangle();
                dest.Width = (int)(ICON_Size.X );
                dest.Height = (int)(ICON_Size.Y );
                dest.X = (int)myPosList[i].X - dest.Width / 2;
                dest.Y = (int)myPosList[i].Y - dest.Height / 2;

                Rectangle src = new Rectangle();
                src.Width = ICON_Size.X;
                src.Height = ICON_Size.Y;
                src.X = ICON_List[myCurrent_NoList[i]].X;
                src.Y = ICON_List[myCurrent_NoList[i]].Y;

                G.DrawImage(myImage,   // 2D Texture
                                 dest,   // 目的區的 矩形區塊
                                 src,   // 來源區的 矩形區塊，null就是 全圖
                                 GraphicsUnit.Pixel); 
            }

        }
    }
}
