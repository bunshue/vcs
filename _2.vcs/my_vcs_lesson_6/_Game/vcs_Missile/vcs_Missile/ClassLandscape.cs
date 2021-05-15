using System;
using System.Collections.Generic;
using System.Text;
using System.Drawing; // for Brush class

namespace vcs_Missile
{
    class ClassLandscape
    {
        struct Building // 每個建築物 有一個矩形區域 和 塗刷索引
        {
            public Rectangle rect;
            public int brushIndex;
        }

        List<Building> BuildingList = new List<Building>(); // 代表建築物 的動態陣列

        Random rd = new Random();
        Brush[] myBrush = new Brush[]  // 四種顏色的塗刷
			{
				Brushes.WhiteSmoke,
				Brushes.Gold,
				Brushes.Magenta, // Orange,
				Brushes.Red // Crimson
			};
        int W, H; // 視窗客戶區的寬高

        public void Build(int W, int H)
        {
            BuildingList.Clear();
            this.W = W;
            this.H = H;

            Building building = new Building();
            for (int i = 0; i < W; i = i + 20) // 每隔 20 個像素 產生一棟 建築物
            {
                int w = rd.Next(10, 30); // 建築物 的寬 
                int h = rd.Next(10, 50); // 建築物 的高

                building.rect = new Rectangle();
                building.rect.X = i;
                building.rect.Y = H - h;
                building.rect.Width = w;
                building.rect.Height = h;

                building.brushIndex = rd.Next(4); // 建築物 的塗刷索引

                BuildingList.Add(building); // 加入到 動態陣列
            }
        }

        public void Draw(Graphics G)
        {
            // 繪出 建築物
            for (int i = 0; i < BuildingList.Count - 1; i++)
                G.FillRectangle(myBrush[BuildingList[i].brushIndex], BuildingList[i].rect);

            // 繪出 中心基地 飛彈發射處
            G.FillRectangle(Brushes.Black, W / 2 - 50, H - 50, 100, 50); //基地背景
            G.FillRectangle(Brushes.Brown, W / 2 - 25, H - 20, 50, 20);  //基地前景
        }
    }
}
