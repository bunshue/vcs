 
C# 使用Bitmap類進行圖片裁剪
 
 在Mapwin（手機游戲地圖編輯器）生成的地圖txt文件中添加自己需要處理的數據後轉換成可在手機（Ophone）開發環境中使用的字節流地圖文件的小工具，其中就涉及到圖片的裁剪和生成了。有以下幾種方式。
 
方法一：拷貝像素。
 
當然這種方法是最笨的，效率也就低了些。
在Bitmap類中我們可以看到這樣兩個方法：GetPixel（int x, int y）和SetPixel（int x, int y, Color color）方法。從字面的含以上就知道前者是獲取圖像某點像素值，是用Color對象返回的；後者是將已知像素描畫到制定的位置。
下面就來做個實例檢驗下：
1.首先創建一個Windows Form窗體程序，往該窗體上拖放7個PictureBox控件，第一個用於放置並顯示原始的大圖片，其後6個用於放置並顯示裁剪後新生成的6個小圖；
2.放置原始大圖的PictureBox控件name屬性命名為pictureBoxBmpRes，其後pictureBox1到pictureBox6依次命名，並放置在合適的位置；
3.雙擊Form窗體，然後在Form1_Load事件中加入下面的代碼即可。
//導入圖像資源
            Bitmap bmpRes = null;
            String strPath = Application.ExecutablePath;
            try{
                int nEndIndex = strPath.LastIndexOf('//');
                strPath = strPath.Substring(0,nEndIndex) + "//Bmp//BmpResMM.bmp";
                bmpRes = new Bitmap(strPath);
 
                //窗體上顯示加載圖片
                pictureBoxBmpRes.Width = bmpRes.Width;
                pictureBoxBmpRes.Height = bmpRes.Height;
                pictureBoxBmpRes.Image = bmpRes;
            }
            catch(Exception ex)
            {
               System.Windows.Forms.MessageBox.Show("圖片資源加載失敗！/r/n" + ex.ToString());
            }
 
            //裁剪圖片(裁成2行3列的6張圖片)
            int nYClipNum = 2, nXClipNum = 3;
            Bitmap[] bmpaClipBmpArr = new Bitmap[nYClipNum * nXClipNum];            
            for (int nYClipNumIndex = 0; nYClipNumIndex < nYClipNum; nYClipNumIndex++)
            {
                for (int nXClipNumIndex = 0; nXClipNumIndex < nXClipNum; nXClipNumIndex++)
                {
                    int nClipWidth = bmpRes.Width / nXClipNum;
                    int nClipHight = bmpRes.Height / nYClipNum;
                    int nBmpIndex = nXClipNumIndex + nYClipNumIndex * nYClipNum + (nYClipNumIndex > 0?1:0);
                    bmpaClipBmpArr[nBmpIndex] = new Bitmap(nClipWidth, nClipHight);
 
                    for(int nY = 0; nY < nClipHight; nY++)
                    {
                        for(int nX = 0; nX < nClipWidth; nX++)
                        {
                            int nClipX = nX + nClipWidth * nXClipNumIndex;
                            int nClipY = nY + nClipHight * nYClipNumIndex;
                            Color cClipPixel = bmpRes.GetPixel(nClipX, nClipY);
                            bmpaClipBmpArr[nBmpIndex].SetPixel(nX, nY, cClipPixel);
                        }
                    }                   
                }
            }
            PictureBox[] picbShow = new PictureBox[nYClipNum * nXClipNum];
            picbShow[0] = pictureBox1;
            picbShow[1] = pictureBox2;
            picbShow[2] = pictureBox3;
            picbShow[3] = pictureBox4;
            picbShow[4] = pictureBox5;
            picbShow[5] = pictureBox6;
            for (int nLoop = 0; nLoop < nYClipNum * nXClipNum; nLoop++)
            {
                picbShow[nLoop].Width = bmpRes.Width / nXClipNum;
                picbShow[nLoop].Height = bmpRes.Height / nYClipNum;
                picbShow[nLoop].Image = bmpaClipBmpArr[nLoop];               
            }
            
            
 現在看看那些地方需要注意的了。其中
int nBmpIndex =
nXClipNumIndex + nYClipNumIndex * nYClipNum + (nYClipNumIndex > 0?1:0);
 這句定義了存儲裁剪圖片對象在數組中的索引，需要注意的就是後面的(nYClipNumIndex > 0?1:0)——因為只有當裁剪的對象處於第一行以外的行時需要將索引加1；
另外，因為這種方法的效率不高，程序運行起來還是頓了下。如果有興趣的話，可以將以上的代碼放到一個按鈕Click事件函數中，當單擊該按鈕時就可以感覺到了。
 
 方法二：運用Clone函數局部復制。
 
同樣在Bitmap中可以找到Clone（）方法，該方法有三個重載方法。Clone（），Clone（Rectangle， PixelFormat）和Clone（RectangleF， PixelFormat）。第一個方法將創建並返回一個精確的實例對象，後兩個就是我們這裡需要用的局部裁剪了（其實後兩個方法本人覺得用法上差不多）。
將上面的程序稍稍改進下——將裁剪的處理放到一個按鈕事件函數中，然後再托一個按鈕好窗體上，最後將下面的代碼復制到該按鈕的事件函數中。
for (int nYClipNumIndex = 0; nYClipNumIndex < nYClipNum; nYClipNumIndex++)
{
       for (int nXClipNumIndex = 0; nXClipNumIndex < nXClipNum; nXClipNumIndex++)
         {
              int nClipWidth = bmpRes.Width / nXClipNum;
                      int nClipHight = bmpRes.Height / nYClipNum;
                int nBmpIndex =
nXClipNumIndex + nYClipNumIndex * nYClipNum + (nYClipNumIndex > 0 ? 1 : 0);
             
        Rectangle rClipRect = new Rectangle(nClipWidth * nXClipNumIndex,
                                                            nClipHight * nYClipNumIndex,
                                                            nClipWidth,
                                                            nClipHight);
             
                bmpaClipBmpArr[nBmpIndex] = bmpRes.Clone(rClipRect, bmpRes.PixelFormat);
            }
}
 
 運行程序，單擊按鈕檢驗下，發現速度明顯快可很多。
其實這種方法較第一中方法不同的地方僅只是變換了for循環中的拷貝部分的處理，
Rectangle rClipRect = new Rectangle(nClipWidth * nXClipNumIndex,
                                                            nClipHight * nYClipNumIndex,
                                                            nClipWidth,
                                                            nClipHight);
 
bmpaClipBmpArr[nBmpIndex] = bmpRes.Clone(rClipRect, bmpRes.PixelFormat);
 





GrayBitmapData


 
 
C# colorMatrix 對圖片的處理 : 亮度調整 翻轉 隨鼠標畫矩形
 
1.圖片亮度處理
 
        private void btn_Grap_Click(object sender, EventArgs e)
        {
            //亮度百分比
            int percent = 50;
            Single v = 0.006F * percent;    
            Single[][] matrix = {         
                new Single[] { 1, 0, 0, 0, 0 },         
                new Single[] { 0, 1, 0, 0, 0 },          
                new Single[] { 0, 0, 1, 0, 0 },         
                new Single[] { 0, 0, 0, 1, 0 },         
                new Single[] { v, v, v, 0, 1 }     
            };    
            System.Drawing.Imaging.ColorMatrix cm = new System.Drawing.Imaging.ColorMatrix(matrix);
            System.Drawing.Imaging.ImageAttributes attr = new System.Drawing.Imaging.ImageAttributes();    
            attr.SetColorMatrix(cm);    
            //Image tmp 
            Image tmp = Image.FromFile("1.png");
 
            this.pictureBox_Src.Image = Image.FromFile("1.png");
 
            Graphics g = Graphics.FromImage(tmp);  
            try  
            {
                Rectangle destRect = new Rectangle(0, 0, tmp.Width, tmp.Height);        
                g.DrawImage(tmp, destRect, 0, 0, tmp.Width, tmp.Height, GraphicsUnit.Pixel, attr);    
            }    
            finally    
            {        
                g.Dispose();    
            }
 
            this.pictureBox_Dest.Image = (Image)tmp.Clone();
        }
 
 
3.翻轉
 
        private void btn_RotateFlip_Click(object sender, EventArgs e)
        {
            this.pictureBox_Src.Image = Image.FromFile("1.png");
 
            Image tmp = Image.FromFile("1.png");
 
            tmp.RotateFlip(RotateFlipType.Rotate90FlipNone);
            this.pictureBox_Dest.Image = tmp;
        }


4.跟隨鼠標在 pictureBox的圖片上畫矩形

        private int intStartX = 0;
        private int intStartY = 0;
        private bool isMouseDraw = false;
 
        private void pictureBox_Src_MouseDown(object sender, MouseEventArgs e)
        {
            isMouseDraw = true;
 
            intStartX = e.X;
            intStartY = e.Y;
        }
 
        private void pictureBox_Src_MouseMove(object sender, MouseEventArgs e)
        {
            if (isMouseDraw)
            {
                try
                {
                    //Image tmp = Image.FromFile("1.png");
                    Graphics g = this.pictureBox_Src.CreateGraphics();
                    //清空上次畫下的痕跡
                    g.Clear(this.pictureBox_Src.BackColor);
                    Brush brush = new SolidBrush(Color.Red);
                    Pen pen = new Pen(brush, 1);
                    pen.DashStyle = DashStyle.Solid;
                    g.DrawRectangle(pen, new Rectangle(intStartX > e.X ? e.X : intStartX, intStartY > e.Y ? e.Y : intStartY, Math.Abs(e.X - intStartX), Math.Abs(e.Y - intStartY)));
                    g.Dispose();
                    //this.pictureBox_Src.Image = tmp;
                }
                catch (Exception ex)
                {
                    ex.ToString();
                }
            }
        }
 
        private void pictureBox_Src_MouseUp(object sender, MouseEventArgs e)
        {
            isMouseDraw = false;
 
            intStartX = 0;
            intStartY = 0;
        }
　


