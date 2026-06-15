using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;  // for FileStream
using System.Drawing.Imaging;  // for PropertyItem

//方案總管/加入/現有項目/選取ExifStuff.cs, 把 namespace 改成 vcs_Exif

//EXIF : Exchangeable Image File
/*
目前大部分數碼相機都將所拍照的圖像保存成JPG格式，
而像拍照日期這樣的 信息統稱為EXIF信息。
EXIF是英文ExchangeableImageFile(可交換圖像文件)的 縮寫
*/

namespace vcs_Exif
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //------------------------------------------------------------  # 60個

            CheckForIllegalCrossThreadCalls = false;

            label3.Text = "取得圖片內的方向值,\n自動轉換圖片方向";

            string filename = @"D:\_git\vcs\_1.data\______test_files1\orient1.jpg";

            // Open the file.
            using (Bitmap bm = new Bitmap(filename))
            {
                // Display the original image.
                Bitmap original_bm = new Bitmap(bm);
                pictureBox1.Image = original_bm;

                // Display the image property oriented.
                // Note: If you use new Bitmap(bm) to make the copy,
                //       then the EXIF properties are lost. Clone instead.
                Bitmap oriented_bm = (Bitmap)bm.Clone();
                ExifStuff.OrientImage(oriented_bm);
                pictureBox2.Image = oriented_bm;
            }
        }

        void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;
            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);

            listView1.Size = new Size(500, 400);
            listView1.Location = new Point(x_st + dx * 5, y_st + dy * 0);
            richTextBox1.Size = new Size(500, 320);
            richTextBox1.Location = new Point(x_st + dx * 5, y_st + dy * 6);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1620, 800);
            this.Text = "vcs_Exif";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        PropertyItem[] pi;
        string TakePicDateTime;
        int SpaceLocation;
        string pdt;
        string ptm;
        Bitmap bitmap1;
        Graphics g;

        private void button0_Click(object sender, EventArgs e)
        {
            //印上拍照日期

            richTextBox1.Text += "印上拍照日期\n";
            richTextBox1.Text += "开始添加数码相片拍摄日期\n";

            Font normalContentFont = new Font("宋体", 36, FontStyle.Bold);
            Color normalContentColor = Color.Red;

            string filename = @"D:\_git\vcs\_1.data\______test_files1\p3.jpg";

            richTextBox1.Text += filename + "\n";

            return;

            pi = GetExif(filename);
            //获取元数据中的拍照日期时间，以字符串形式保存
            TakePicDateTime = GetDateTime(pi);
            richTextBox1.Text += "1取得相片的拍攝時間 : " + TakePicDateTime + "\n";

            //分析字符串分别保存拍照日期和时间的标准格式
            SpaceLocation = TakePicDateTime.IndexOf(" ");
            pdt = TakePicDateTime.Substring(0, SpaceLocation);
            pdt = pdt.Replace(":", "-");
            ptm = TakePicDateTime.Substring(SpaceLocation + 1, TakePicDateTime.Length - SpaceLocation - 2);
            TakePicDateTime = pdt + " " + ptm;
            //由列表中的文件创建内存位图对象
            bitmap1 = new Bitmap(filename);
            //由位图对象创建Graphics对象的实例
            g = Graphics.FromImage(bitmap1);

            //绘制数码照片的日期/时间
            richTextBox1.Text += "\n2取得相片的拍攝時間 : " + TakePicDateTime + "\n";

            g.DrawString(TakePicDateTime, normalContentFont, new SolidBrush(normalContentColor), 10, bitmap1.Height - 40);
            g.DrawString("西江月製作", normalContentFont, new SolidBrush(normalContentColor), 10, bitmap1.Height - 80);

            //将添加日期/时间戳后的图像进行保存

            string filename2 = Application.StartupPath + "\\" + Path.GetFileName(filename);
            bitmap1.Save(filename2);
            richTextBox1.Text += "已存檔 : " + filename2 + "\n";

            //释放内存位图对象
            bitmap1.Dispose();

            //System.Threading.Thread.Sleep(3500);
            //Application.DoEvents();

            richTextBox1.Text += "全部数码相片拍摄日期添加成功\n";
        }

        // 获取数码相片的拍摄日期
        // 获取图像文件的所有元数据属性，保存倒PropertyItem数组
        public static PropertyItem[] GetExif(string filename)
        {
            FileStream Mystream = new FileStream(filename, FileMode.Open, FileAccess.Read);
            //通过指定的数据流来创建Image
            Image image = Image.FromStream(Mystream, true, false);
            return image.PropertyItems;
        }

        //遍历所有元数据，获取拍照日期/时间
        private string GetDateTime(PropertyItem[] parr)
        {
            Encoding ascii = Encoding.ASCII;
            //遍历图像文件元数据，检索所有属性
            foreach (PropertyItem pp in parr)
            {
                //如果是PropertyTagDateTime，则返回该属性所对应的值
                if (pp.Id == 0x0132)
                {
                    return ascii.GetString(pp.Value);
                }
            }
            //若没有相关的EXIF信息则返回N/A
            return "N/A";
        }

        //------------------------------------------------------------  # 60個

        private void button1_Click(object sender, EventArgs e)
        {
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__pic\_icon\IMG_20180228_215525.jpg";

            richTextBox1.Text += "讀取檔案:\t" + filename + "\n";

            using (Bitmap bm = new Bitmap(filename))
            {
                richTextBox1.Text += "Property\t\t\tID\t\t\tData Type\t\t\tDataLength\t\t\tValue\n";
                // Get EXIF property data.
                List<ExifStuff.ExifPropertyData> property_data = ExifStuff.GetExifProperties(bm);

                // Display the property information.
                List<string> results = new List<string>();
                foreach (ExifStuff.ExifPropertyData data in property_data)
                {
                    ListViewItem item = listView1.Items.Add(data.PropertyType.ToString());
                    item.SubItems.Add(data.Id.ToString());
                    item.SubItems.Add(data.DataType.ToString());
                    item.SubItems.Add(data.DataLength.ToString());
                    item.SubItems.Add(data.DataString);

                    richTextBox1.Text += data.PropertyType.ToString() + "\t\t\t";
                    richTextBox1.Text += data.Id.ToString() + "\t\t\t";
                    richTextBox1.Text += data.DataType.ToString() + "\t\t\t";
                    richTextBox1.Text += data.DataLength.ToString() + "\t\t\t";
                    if (data.DataLength < 32)
                    {
                        richTextBox1.Text += data.DataString + "\n";
                    }
                    else
                    {
                        richTextBox1.Text += "\n";
                    }
                }
            }
            Bitmap bitmap1 = new Bitmap(filename);
            pictureBox1.Image = bitmap1;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__pic\_icon\IMG_20180228_215525.jpg";

            richTextBox1.Text += "相片檔案:\t" + filename + "\n";

            PropertyItem[] pi;
            pi = GetExif(filename);
            string TakePicDateTime = GetDateTime(pi);

            richTextBox1.Text += "取得相片拍攝時間:\t" + TakePicDateTime + "\n";
        }

        //------------------------------------------------------------  # 60個

        private void button3_Click(object sender, EventArgs e)
        {
            string filename = @"D:\_git\vcs\_1.data\______test_files1\p3.jpg";

            PropertyItem[] pi;
            pi = GetExif2(filename);
            //获取元数据中的拍照日期时间，以字符串形式保存
            string TakePicDateTime = GetDateTime2(pi);
            richTextBox1.Text += "1取得相片的拍攝時間 : " + TakePicDateTime + "\n";

            GetInfo(pi);
        }

        //获取图像文件的所有元数据属性，保存倒PropertyItem数组
        public static PropertyItem[] GetExif2(string fileName)
        {
            FileStream Mystream = new FileStream(fileName, FileMode.Open, FileAccess.Read);
            //通过指定的数据流来创建Image
            Image image = Image.FromStream(Mystream, true, false);
            return image.PropertyItems;
        }

        //遍历所有元数据，获取拍照日期/时间
        private string GetDateTime2(PropertyItem[] parr)
        {
            Encoding ascii = Encoding.ASCII;
            //遍历图像文件元数据，检索所有属性
            foreach (PropertyItem pp in parr)
            {
                //如果是PropertyTagDateTime，则返回该属性所对应的值
                if (pp.Id == 0x0132)
                {
                    return ascii.GetString(pp.Value);
                }
            }
            //若没有相关的EXIF信息则返回N/A
            return "N/A";
        }

        private void GetInfo(PropertyItem[] parr)
        {
            Encoding ascii = Encoding.ASCII;
            foreach (PropertyItem pp in parr)
            {
                richTextBox1.Text += "\nID = " + pp.Id.ToString() + "\t" + ascii.GetString(pp.Value) + "\n";
            }
            return;
        }

        //------------------------------------------------------------  # 60個

        private void button4_Click(object sender, EventArgs e)
        {
            //取得拍照時間
            string filename = @"D:\_git\vcs\_1.data\______test_files1\orient1.jpg";
            string TakePicDateTime = GetTakePicDateTime(GetExifPropertIEs(filename));
            richTextBox1.Text += TakePicDateTime + "\n\n\n";

            //分析字符串分別保存拍照日期和時間的標准格式
            int SpaceLocation = TakePicDateTime.IndexOf(" ");
            string dt = TakePicDateTime.Substring(0, SpaceLocation);
            dt = dt.Replace(":", "-");
            string tm = TakePicDateTime.Substring(SpaceLocation + 1, TakePicDateTime.Length - SpaceLocation - 2);
            TakePicDateTime = dt + " " + tm;

            richTextBox1.Text += "\n\n\nTakePicDateTime = " + TakePicDateTime + "\n";

            //ex: 2019:11:16 20:07:23 => 2019-11-16 20:07:23




        }

        //獲取圖像文件的所有元數據屬性，以PropertyItem數組的格式保存
        public static PropertyItem[] GetExifPropertIEs(string fileName)
        {
            FileStream stream = new FileStream(fileName, FileMode.Open, FileAccess.Read);
            //通過指定的數據流來創建Image
            System.Drawing.Image image = System.Drawing.Image.FromStream(stream, true, false);
            return image.PropertyItems;
        }

        //遍歷所有元數據，獲取拍照日期/時間
        private string GetTakePicDateTime(PropertyItem[] parr)
        {
            Encoding ascii = Encoding.ASCII;
            //遍歷圖像文件元數據，檢索所有屬性
            foreach (PropertyItem p in parr)
            {
                //如果是PropertyTagDateTime，則返回該屬性所對應的值
                if (p.Id == 0x0132)
                {
                    return ascii.GetString(p.Value);
                }
            }
            //若沒有相關的EXIF信息則返回N/A
            return "N/A";
        }

        private void button5_Click(object sender, EventArgs e)
        {
            string filename = @"D:\_git\vcs\_1.data\______test_files1\orient1.jpg";

            Picturexif em = new Picturexif();

            string filePath = filename;

            Picturexif.Metadata m = em.GetEXIFMetaData(filePath);//这里就是调用，传图片绝对路径 

            string exif = m.Ver.DisplayValue;

            string camera = m.CameraModel.DisplayValue;

            string model = m.CameraModel.DisplayValue;

            string aperture = m.Aperture.DisplayValue;

            string shutter = m.ShutterSpeed.DisplayValue;

            string sensitive = m.ExposureIndex.DisplayValue;

            richTextBox1.Text += "aaaaa : " + exif + "\n\n";
            richTextBox1.Text += "aaaaa : " + camera + "\n\n";
            richTextBox1.Text += "aaaaa : " + model + "\n\n";
            richTextBox1.Text += "aaaaa : " + aperture + "\n\n";
            richTextBox1.Text += "aaaaa : " + shutter + "\n\n";
            richTextBox1.Text += "aaaaa : " + sensitive + "\n\n";
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //檢查圖片的方向
            string filename = @"D:\_git\vcs\_1.data\______test_files1\orient1.jpg";

            // Open the file.
            Bitmap bm = new Bitmap(filename);
            picOriginal.Image = bm;

            // Get the PropertyItems property from image.
            ExifStuff.ExifOrientations orientation = ExifStuff.ImageOrientation(bm);
            lblOrientation.Text = orientation.ToString();
            richTextBox1.Text += orientation.ToString() + "\n";
            picOrientation.Image = ExifStuff.OrientationImage(orientation);
        }
    }

    //------------------------------------------------------------  # 60個

    public class Picturexif
    {
        //#region 构造函数
        /// <summary> 
        /// 构造函数 
        /// </summary> 
        public Picturexif()
        {
        }
        //#endregion

        //#region 数据转换结构
        /// <summary> 
        /// 转换数据结构 
        /// </summary> 
        public struct MetadataDetail
        {
            public string Hex;//十六进制字符串 
            public string RawValueAsString;//原始值串 
            public string DisplayValue;//显示值串 
        }
        //#endregion

        //#region EXIF元素结构
        /// <summary> 
        /// 结构：存储EXIF元素信息 
        /// </summary> 
        public struct Metadata
        {
            public MetadataDetail EquipmentMake;
            public MetadataDetail CameraModel;
            public MetadataDetail ExposureTime;//曝光时间 
            public MetadataDetail Fstop;
            public MetadataDetail DatePictureTaken;
            public MetadataDetail ShutterSpeed;// 快门速度 
            public MetadataDetail MeteringMode;//曝光模式 
            public MetadataDetail Flash;//闪光灯 
            public MetadataDetail XResolution;
            public MetadataDetail YResolution;
            public MetadataDetail ImageWidth;//照片宽度 
            public MetadataDetail ImageHeight;//照片高度 

            public MetadataDetail FNumber;// added f值，光圈数 
            public MetadataDetail ExposureProg;// added 曝光程序 
            public MetadataDetail SpectralSense;// added  
            public MetadataDetail ISOSpeed;// added ISO感光度 
            public MetadataDetail OECF;// added  
            public MetadataDetail Ver;// added EXIF版本 
            public MetadataDetail CompConfig;// added 色彩设置 
            public MetadataDetail CompBPP;// added 压缩比率 
            public MetadataDetail Aperture;// added 光圈值 
            public MetadataDetail Brightness;// added 亮度值Ev 
            public MetadataDetail ExposureBias;// added 曝光补偿 
            public MetadataDetail MaxAperture;// added 最大光圈值 

            public MetadataDetail SubjectDist;// added主体距离 
            public MetadataDetail LightSource;// added 白平衡 
            public MetadataDetail FocalLength;// added 焦距 
            public MetadataDetail FPXVer;// added FlashPix版本 
            public MetadataDetail ColorSpace;// added 色彩空间 
            public MetadataDetail Interop;// added  
            public MetadataDetail FlashEnergy;// added  
            public MetadataDetail SpatialFR;// added  
            public MetadataDetail FocalXRes;// added  
            public MetadataDetail FocalYRes;// added  
            public MetadataDetail FocalResUnit;// added  
            public MetadataDetail ExposureIndex;// added 曝光指数 
            public MetadataDetail SensingMethod;// added 感应方式 
            public MetadataDetail SceneType;// added  
            public MetadataDetail CfaPattern;// added  
        }
        //#endregion

        //#region 查找EXIF元素值
        public string LookupEXIFValue(string Description, string Value)
        {
            string DescriptionValue = null;

            switch (Description)
            {
                case "MeteringMode":

                    //#region  MeteringMode
                    {
                        switch (Value)
                        {
                            case "0":
                                DescriptionValue = "Unknown"; break;
                            case "1":
                                DescriptionValue = "Average"; break;
                            case "2":
                                DescriptionValue = "Center Weighted Average"; break;
                            case "3":
                                DescriptionValue = "Spot"; break;
                            case "4":
                                DescriptionValue = "Multi-spot"; break;
                            case "5":
                                DescriptionValue = "Multi-segment"; break;
                            case "6":
                                DescriptionValue = "Partial"; break;
                            case "255":
                                DescriptionValue = "Other"; break;
                        }
                    }
                    //#endregion

                    break;
                case "ResolutionUnit":

                    //#region ResolutionUnit
                    {
                        switch (Value)
                        {
                            case "1":
                                DescriptionValue = "No Units"; break;
                            case "2":
                                DescriptionValue = "Inch"; break;
                            case "3":
                                DescriptionValue = "Centimeter"; break;
                        }
                    }

                    //#endregion

                    break;
                case "Flash":

                    //#region Flash
                    {
                        switch (Value)
                        {
                            case "0":
                                DescriptionValue = "未使用"; break;
                            case "1":
                                DescriptionValue = "闪光"; break;
                            case "5":
                                DescriptionValue = "Flash fired but strobe return light not detected"; break;
                            case "7":
                                DescriptionValue = "Flash fired and strobe return light detected"; break;
                        }
                    }
                    //#endregion

                    break;
                case "ExposureProg":

                    //#region ExposureProg
                    {
                        switch (Value)
                        {
                            case "0":
                                DescriptionValue = "没有定义"; break;
                            case "1":
                                DescriptionValue = "手动控制"; break;
                            case "2":
                                DescriptionValue = "程序控制"; break;
                            case "3":
                                DescriptionValue = "光圈优先"; break;
                            case "4":
                                DescriptionValue = "快门优先"; break;
                            case "5":
                                DescriptionValue = "夜景模式"; break;
                            case "6":
                                DescriptionValue = "运动模式"; break;
                            case "7":
                                DescriptionValue = "肖像模式"; break;
                            case "8":
                                DescriptionValue = "风景模式"; break;
                            case "9":
                                DescriptionValue = "保留的"; break;
                        }
                    }

                    //#endregion

                    break;
                case "CompConfig":

                    //#region CompConfig
                    {
                        switch (Value)
                        {

                            case "513":
                                DescriptionValue = "YCbCr"; break;
                        }
                    }
                    //#endregion

                    break;
                case "Aperture":

                    //#region Aperture
                    DescriptionValue = Value;
                    //#endregion

                    break;
                case "LightSource":

                    //#region LightSource
                    {
                        switch (Value)
                        {
                            case "0":
                                DescriptionValue = "未知"; break;
                            case "1":
                                DescriptionValue = "日光"; break;
                            case "2":
                                DescriptionValue = "荧光灯"; break;
                            case "3":
                                DescriptionValue = "白炽灯"; break;
                            case "10":
                                DescriptionValue = "闪光灯"; break;
                            case "17":
                                DescriptionValue = "标准光A"; break;
                            case "18":
                                DescriptionValue = "标准光B"; break;
                            case "19":
                                DescriptionValue = "标准光C"; break;
                            case "20":
                                DescriptionValue = "标准光D55"; break;
                            case "21":
                                DescriptionValue = "标准光D65"; break;
                            case "22":
                                DescriptionValue = "标准光D75"; break;
                            case "255":
                                DescriptionValue = "其它"; break;
                        }
                    }


                    //#endregion
                    break;

            }
            return DescriptionValue;
        }
        //#endregion

        //#region 取得图片的EXIF信息
        public Metadata GetEXIFMetaData(string PhotoName)
        {
            // 创建一个图片的实例 
            System.Drawing.Image MyImage = System.Drawing.Image.FromFile(PhotoName);
            // 创建一个整型数组来存储图像中属性数组的ID 
            int[] MyPropertyIdList = MyImage.PropertyIdList;
            //创建一个封闭图像属性数组的实例 
            PropertyItem[] MyPropertyItemList = new PropertyItem[MyPropertyIdList.Length];
            //创建一个图像EXIT信息的实例结构对象，并且赋初值 

            //#region 创建一个图像EXIT信息的实例结构对象，并且赋初值
            Metadata MyMetadata = new Metadata();
            MyMetadata.EquipmentMake.Hex = "10f";
            MyMetadata.CameraModel.Hex = "110";
            MyMetadata.DatePictureTaken.Hex = "9003";
            MyMetadata.ExposureTime.Hex = "829a";
            MyMetadata.Fstop.Hex = "829d";
            MyMetadata.ShutterSpeed.Hex = "9201";
            MyMetadata.MeteringMode.Hex = "9207";
            MyMetadata.Flash.Hex = "9209";
            MyMetadata.FNumber.Hex = "829d"; //added  
            MyMetadata.ExposureProg.Hex = ""; //added  
            MyMetadata.SpectralSense.Hex = "8824"; //added  
            MyMetadata.ISOSpeed.Hex = "8827"; //added  
            MyMetadata.OECF.Hex = "8828"; //added  
            MyMetadata.Ver.Hex = "9000"; //added  
            MyMetadata.CompConfig.Hex = "9101"; //added  
            MyMetadata.CompBPP.Hex = "9102"; //added  
            MyMetadata.Aperture.Hex = "9202"; //added  
            MyMetadata.Brightness.Hex = "9203"; //added  
            MyMetadata.ExposureBias.Hex = "9204"; //added  
            MyMetadata.MaxAperture.Hex = "9205"; //added  
            MyMetadata.SubjectDist.Hex = "9206"; //added  
            MyMetadata.LightSource.Hex = "9208"; //added  
            MyMetadata.FocalLength.Hex = "920a"; //added  
            MyMetadata.FPXVer.Hex = "a000"; //added  
            MyMetadata.ColorSpace.Hex = "a001"; //added  
            MyMetadata.FocalXRes.Hex = "a20e"; //added  
            MyMetadata.FocalYRes.Hex = "a20f"; //added  
            MyMetadata.FocalResUnit.Hex = "a210"; //added  
            MyMetadata.ExposureIndex.Hex = "a215"; //added  
            MyMetadata.SensingMethod.Hex = "a217"; //added  
            MyMetadata.SceneType.Hex = "a301";
            MyMetadata.CfaPattern.Hex = "a302";
            //#endregion

            // ASCII编码 
            System.Text.ASCIIEncoding Value = new System.Text.ASCIIEncoding();

            int index = 0;
            int MyPropertyIdListCount = MyPropertyIdList.Length;
            if (MyPropertyIdListCount != 0)
            {
                foreach (int MyPropertyId in MyPropertyIdList)
                {
                    string hexVal = "";
                    MyPropertyItemList[index] = MyImage.GetPropertyItem(MyPropertyId);

                    //#region 初始化各属性值
                    string myPropertyIdString = MyImage.GetPropertyItem(MyPropertyId).Id.ToString("x");
                    switch (myPropertyIdString)
                    {
                        case "10f":
                            {
                                MyMetadata.EquipmentMake.RawValueAsString = BitConverter.ToString(MyImage.GetPropertyItem(MyPropertyId).Value);
                                MyMetadata.EquipmentMake.DisplayValue = Value.GetString(MyPropertyItemList[index].Value);
                                break;
                            }

                        case "110":
                            {
                                MyMetadata.CameraModel.RawValueAsString = BitConverter.ToString(MyImage.GetPropertyItem(MyPropertyId).Value);
                                MyMetadata.CameraModel.DisplayValue = Value.GetString(MyPropertyItemList[index].Value);
                                break;

                            }

                        case "9003":
                            {
                                MyMetadata.DatePictureTaken.RawValueAsString = BitConverter.ToString(MyImage.GetPropertyItem(MyPropertyId).Value);
                                MyMetadata.DatePictureTaken.DisplayValue = Value.GetString(MyPropertyItemList[index].Value);
                                break;
                            }

                        case "9207":
                            {
                                MyMetadata.MeteringMode.RawValueAsString = BitConverter.ToString(MyImage.GetPropertyItem(MyPropertyId).Value);
                                MyMetadata.MeteringMode.DisplayValue = LookupEXIFValue("MeteringMode", BitConverter.ToInt16(MyImage.GetPropertyItem(MyPropertyId).Value, 0).ToString());
                                break;
                            }

                        case "9209":
                            {
                                MyMetadata.Flash.RawValueAsString = BitConverter.ToString(MyImage.GetPropertyItem(MyPropertyId).Value);
                                MyMetadata.Flash.DisplayValue = LookupEXIFValue("Flash", BitConverter.ToInt16(MyImage.GetPropertyItem(MyPropertyId).Value, 0).ToString());
                                break;
                            }

                        case "829a":
                            {
                                MyMetadata.ExposureTime.RawValueAsString = BitConverter.ToString(MyImage.GetPropertyItem(MyPropertyId).Value);
                                string StringValue = "";
                                for (int Offset = 0; Offset < MyImage.GetPropertyItem(MyPropertyId).Len; Offset = Offset + 4)
                                {
                                    StringValue += BitConverter.ToInt32(MyImage.GetPropertyItem(MyPropertyId).Value, Offset).ToString() + "/";
                                }
                                MyMetadata.ExposureTime.DisplayValue = StringValue.Substring(0, StringValue.Length - 1);
                                break;
                            }
                        case "829d":
                            {
                                MyMetadata.Fstop.RawValueAsString = BitConverter.ToString(MyImage.GetPropertyItem(MyPropertyId).Value);
                                int int1;
                                int int2;
                                int1 = BitConverter.ToInt32(MyImage.GetPropertyItem(MyPropertyId).Value, 0);
                                int2 = BitConverter.ToInt32(MyImage.GetPropertyItem(MyPropertyId).Value, 4);
                                MyMetadata.Fstop.DisplayValue = "F/" + (int1 / int2);

                                MyMetadata.FNumber.RawValueAsString = BitConverter.ToString(MyImage.GetPropertyItem(MyPropertyId).Value);
                                MyMetadata.FNumber.DisplayValue = BitConverter.ToInt16(MyImage.GetPropertyItem(MyPropertyId).Value, 0).ToString();

                                break;
                            }
                        case "9201":
                            {
                                MyMetadata.ShutterSpeed.RawValueAsString = BitConverter.ToString(MyImage.GetPropertyItem(MyPropertyId).Value);
                                string StringValue = BitConverter.ToInt32(MyImage.GetPropertyItem(MyPropertyId).Value, 0).ToString();
                                MyMetadata.ShutterSpeed.DisplayValue = "1/" + StringValue;
                                break;
                            }

                        case "8822":
                            {
                                MyMetadata.ExposureProg.RawValueAsString = BitConverter.ToString(MyImage.GetPropertyItem(MyPropertyId).Value);
                                MyMetadata.ExposureProg.DisplayValue = LookupEXIFValue("ExposureProg", BitConverter.ToInt16(MyImage.GetPropertyItem(MyPropertyId).Value, 0).ToString());
                                break;
                            }

                        case "8824":
                            {
                                MyMetadata.SpectralSense.RawValueAsString = BitConverter.ToString(MyImage.GetPropertyItem(MyPropertyId).Value);
                                MyMetadata.SpectralSense.DisplayValue = Value.GetString(MyPropertyItemList[index].Value);
                                break;
                            }
                        case "8827":
                            {
                                hexVal = "";
                                MyMetadata.ISOSpeed.RawValueAsString = BitConverter.ToString(MyImage.GetPropertyItem(MyPropertyId).Value);
                                hexVal = BitConverter.ToString(MyImage.GetPropertyItem(MyPropertyId).Value).Substring(0, 2);
                                MyMetadata.ISOSpeed.DisplayValue = Convert.ToInt32(hexVal, 16).ToString();//Value.GetString(MyPropertyItemList[index].Value); 
                                break;
                            }

                        case "8828":
                            {
                                MyMetadata.OECF.RawValueAsString = BitConverter.ToString(MyImage.GetPropertyItem(MyPropertyId).Value);
                                MyMetadata.OECF.DisplayValue = Value.GetString(MyPropertyItemList[index].Value);
                                break;
                            }

                        case "9000":
                            {
                                MyMetadata.Ver.RawValueAsString = BitConverter.ToString(MyImage.GetPropertyItem(MyPropertyId).Value);
                                MyMetadata.Ver.DisplayValue = Value.GetString(MyPropertyItemList[index].Value).Substring(1, 1) + "." + Value.GetString(MyPropertyItemList[index].Value).Substring(2, 2);
                                break;
                            }

                        case "9101":
                            {
                                MyMetadata.CompConfig.RawValueAsString = BitConverter.ToString(MyImage.GetPropertyItem(MyPropertyId).Value);
                                MyMetadata.CompConfig.DisplayValue = LookupEXIFValue("CompConfig", BitConverter.ToInt16(MyImage.GetPropertyItem(MyPropertyId).Value, 0).ToString());
                                break;
                            }

                        case "9102":
                            {
                                MyMetadata.CompBPP.RawValueAsString = BitConverter.ToString(MyImage.GetPropertyItem(MyPropertyId).Value);
                                MyMetadata.CompBPP.DisplayValue = BitConverter.ToInt16(MyImage.GetPropertyItem(MyPropertyId).Value, 0).ToString();
                                break;
                            }

                        case "9202":
                            {
                                hexVal = "";
                                MyMetadata.Aperture.RawValueAsString = BitConverter.ToString(MyImage.GetPropertyItem(MyPropertyId).Value);
                                hexVal = BitConverter.ToString(MyImage.GetPropertyItem(MyPropertyId).Value).Substring(0, 2);
                                hexVal = Convert.ToInt32(hexVal, 16).ToString();
                                hexVal = hexVal + "00";
                                MyMetadata.Aperture.DisplayValue = hexVal.Substring(0, 1) + "." + hexVal.Substring(1, 2);
                                break;
                            }

                        case "9203":
                            {
                                hexVal = "";
                                MyMetadata.Brightness.RawValueAsString = BitConverter.ToString(MyImage.GetPropertyItem(MyPropertyId).Value);
                                hexVal = BitConverter.ToString(MyImage.GetPropertyItem(MyPropertyId).Value).Substring(0, 2);
                                hexVal = Convert.ToInt32(hexVal, 16).ToString();
                                hexVal = hexVal + "00";
                                MyMetadata.Brightness.DisplayValue = hexVal.Substring(0, 1) + "." + hexVal.Substring(1, 2);
                                break;
                            }

                        case "9204":
                            {
                                MyMetadata.ExposureBias.RawValueAsString = BitConverter.ToString(MyImage.GetPropertyItem(MyPropertyId).Value);
                                MyMetadata.ExposureBias.DisplayValue = BitConverter.ToInt16(MyImage.GetPropertyItem(MyPropertyId).Value, 0).ToString();
                                break;
                            }

                        case "9205":
                            {
                                hexVal = "";
                                MyMetadata.MaxAperture.RawValueAsString = BitConverter.ToString(MyImage.GetPropertyItem(MyPropertyId).Value);
                                hexVal = BitConverter.ToString(MyImage.GetPropertyItem(MyPropertyId).Value).Substring(0, 2);
                                hexVal = Convert.ToInt32(hexVal, 16).ToString();
                                hexVal = hexVal + "00";
                                MyMetadata.MaxAperture.DisplayValue = hexVal.Substring(0, 1) + "." + hexVal.Substring(1, 2);
                                break;
                            }

                        case "9206":
                            {
                                MyMetadata.SubjectDist.RawValueAsString = BitConverter.ToString(MyImage.GetPropertyItem(MyPropertyId).Value);
                                MyMetadata.SubjectDist.DisplayValue = Value.GetString(MyPropertyItemList[index].Value);
                                break;
                            }

                        case "9208":
                            {
                                MyMetadata.LightSource.RawValueAsString = BitConverter.ToString(MyImage.GetPropertyItem(MyPropertyId).Value);
                                MyMetadata.LightSource.DisplayValue = LookupEXIFValue("LightSource", BitConverter.ToInt16(MyImage.GetPropertyItem(MyPropertyId).Value, 0).ToString());
                                break;
                            }

                        case "920a":
                            {
                                hexVal = "";
                                MyMetadata.FocalLength.RawValueAsString = BitConverter.ToString(MyImage.GetPropertyItem(MyPropertyId).Value);
                                hexVal = BitConverter.ToString(MyImage.GetPropertyItem(MyPropertyId).Value).Substring(0, 2);
                                hexVal = Convert.ToInt32(hexVal, 16).ToString();
                                hexVal = hexVal + "00";
                                MyMetadata.FocalLength.DisplayValue = hexVal.Substring(0, 1) + "." + hexVal.Substring(1, 2);
                                break;
                            }

                        case "a000":
                            {
                                MyMetadata.FPXVer.RawValueAsString = BitConverter.ToString(MyImage.GetPropertyItem(MyPropertyId).Value);
                                MyMetadata.FPXVer.DisplayValue = Value.GetString(MyPropertyItemList[index].Value).Substring(1, 1) + "." + Value.GetString(MyPropertyItemList[index].Value).Substring(2, 2);
                                break;
                            }

                        case "a001":
                            {
                                MyMetadata.ColorSpace.RawValueAsString = BitConverter.ToString(MyImage.GetPropertyItem(MyPropertyId).Value);
                                if (BitConverter.ToInt16(MyImage.GetPropertyItem(MyPropertyId).Value, 0).ToString() == "1")
                                    MyMetadata.ColorSpace.DisplayValue = "RGB";
                                if (BitConverter.ToInt16(MyImage.GetPropertyItem(MyPropertyId).Value, 0).ToString() == "65535")
                                    MyMetadata.ColorSpace.DisplayValue = "Uncalibrated";
                                break;
                            }

                        case "a20e":
                            {
                                MyMetadata.FocalXRes.RawValueAsString = BitConverter.ToString(MyImage.GetPropertyItem(MyPropertyId).Value);
                                MyMetadata.FocalXRes.DisplayValue = BitConverter.ToInt16(MyImage.GetPropertyItem(MyPropertyId).Value, 0).ToString();
                                break;
                            }

                        case "a20f":
                            {
                                MyMetadata.FocalYRes.RawValueAsString = BitConverter.ToString(MyImage.GetPropertyItem(MyPropertyId).Value);
                                MyMetadata.FocalYRes.DisplayValue = BitConverter.ToInt16(MyImage.GetPropertyItem(MyPropertyId).Value, 0).ToString();
                                break;
                            }

                        case "a210":
                            {
                                string aa;
                                MyMetadata.FocalResUnit.RawValueAsString = BitConverter.ToString(MyImage.GetPropertyItem(MyPropertyId).Value);
                                aa = BitConverter.ToInt16(MyImage.GetPropertyItem(MyPropertyId).Value, 0).ToString(); ;
                                if (aa == "1") MyMetadata.FocalResUnit.DisplayValue = "没有单位";
                                if (aa == "2") MyMetadata.FocalResUnit.DisplayValue = "英尺";
                                if (aa == "3") MyMetadata.FocalResUnit.DisplayValue = "厘米";
                                break;
                            }

                        case "a215":
                            {
                                MyMetadata.ExposureIndex.RawValueAsString = BitConverter.ToString(MyImage.GetPropertyItem(MyPropertyId).Value);
                                MyMetadata.ExposureIndex.DisplayValue = Value.GetString(MyPropertyItemList[index].Value);
                                break;
                            }

                        case "a217":
                            {
                                string aa;
                                aa = BitConverter.ToInt16(MyImage.GetPropertyItem(MyPropertyId).Value, 0).ToString();
                                MyMetadata.SensingMethod.RawValueAsString = BitConverter.ToString(MyImage.GetPropertyItem(MyPropertyId).Value);
                                if (aa == "2") MyMetadata.SensingMethod.DisplayValue = "1 chip color area sensor";
                                break;
                            }

                        case "a301":
                            {
                                MyMetadata.SceneType.RawValueAsString = BitConverter.ToString(MyImage.GetPropertyItem(MyPropertyId).Value);
                                MyMetadata.SceneType.DisplayValue = BitConverter.ToString(MyImage.GetPropertyItem(MyPropertyId).Value);
                                break;
                            }

                        case "a302":
                            {
                                MyMetadata.CfaPattern.RawValueAsString = BitConverter.ToString(MyImage.GetPropertyItem(MyPropertyId).Value);
                                MyMetadata.CfaPattern.DisplayValue = BitConverter.ToString(MyImage.GetPropertyItem(MyPropertyId).Value);
                                break;
                            }



                    }
                    //#endregion

                    index++;
                }
            }

            MyMetadata.XResolution.DisplayValue = MyImage.HorizontalResolution.ToString();
            MyMetadata.YResolution.DisplayValue = MyImage.VerticalResolution.ToString();
            MyMetadata.ImageHeight.DisplayValue = MyImage.Height.ToString();
            MyMetadata.ImageWidth.DisplayValue = MyImage.Width.ToString();
            MyImage.Dispose();
            return MyMetadata;
        }
        //#endregion
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

/*  可搬出

*/

