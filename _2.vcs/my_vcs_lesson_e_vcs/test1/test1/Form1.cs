using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Xml;

using System.Text.RegularExpressions;

using System.Management;

using System.IO;

using Shell32;

/*
XmlDocument 用來存放XML文件的類別

XmlElement 存取節點屬性的類別

XmlNode 選取節點的類別


使用XmlDocument.CreateElement 方法建立節點
*/




namespace test1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            XmlDocument doc = new XmlDocument();
            //建立根節點
            XmlElement company = doc.CreateElement("Company");
            doc.AppendChild(company);
            //建立子節點
            XmlElement department = doc.CreateElement("Department");
            department.SetAttribute("部門名稱", "技術部");//設定屬性
            department.SetAttribute("部門負責人", "余小章");//設定屬性
            //加入至company節點底下
            company.AppendChild(department);

            XmlElement members = doc.CreateElement("Members");//建立節點
            //加入至department節點底下
            department.AppendChild(members);

            XmlElement info = doc.CreateElement("Information");
            info.SetAttribute("名字", "余小章");
            info.SetAttribute("電話", "0806449");
            //加入至members節點底下
            members.AppendChild(info);
            info = doc.CreateElement("Information");
            info.SetAttribute("名字", "王大明");
            info.SetAttribute("電話", "080644978");
            //加入至members節點底下
            members.AppendChild(info);
            doc.Save("Test.xml");

        }

        private void button2_Click(object sender, EventArgs e)
        {
            //xml write add data



            //插入節點
            XmlDocument doc = new XmlDocument();
            doc.Load("Test.xml");
            XmlNode node = doc.SelectSingleNode("Company/Department");//選擇節點
            if (node == null)
                return;
            XmlElement main = doc.CreateElement("newPerson"); //添加person節點
            main.SetAttribute("name", "小明");
            main.SetAttribute("sex", "女");
            main.SetAttribute("age", "25");
            node.AppendChild(main);
            XmlElement sub1 = doc.CreateElement("phone");
            sub1.InnerText = "123456778";
            main.AppendChild(sub1);
            XmlElement sub2 = doc.CreateElement("address");
            sub2.InnerText = "高雄";
            main.AppendChild(sub2);
            doc.Save("Test.xml");
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //修改資料
            //取得根節點內的子節點
            XmlDocument doc = new XmlDocument();
            doc.Load("Test.xml");
            //選擇節點
            XmlNode main = doc.SelectSingleNode("Company/Department");
            if (main == null)
                return;
            //取得節點內的欄位
            XmlElement element = (XmlElement)main;
            //取得節點內的"部門名稱"內容
            string data = element.GetAttribute("部門名稱");
            //取得節點內的"部門名稱"的屬性
            XmlAttribute attribute = element.GetAttributeNode("部門名稱");
            //列舉節點內的屬性
            XmlAttributeCollection attributes = element.Attributes;
            string content = "";
            foreach (XmlAttribute item in attributes)
            {
                content += item.Name + "," + item.Value + Environment.NewLine;
                if (item.Name == "部門名稱")
                    item.Value = "胎哥部門";
                if (item.Name == "部門負責人")
                    item.Value = "胎哥郎";
            }
            doc.Save("Test.xml");
            Console.WriteLine(content);
            richTextBox1.Text += content + "\n";
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //remove data

            XmlDocument doc = new XmlDocument();
            doc.Load("Test.xml");
            //選擇節點
            XmlNode main = doc.SelectSingleNode("Company/Department");
            if (main == null)
                return;
            //取得節點內的欄位
            XmlElement element = (XmlElement)main;
            //刪除節點內的屬性
            element.RemoveAttribute("部門名稱");
            //刪除節點內所有的內容
            //element.RemoveAll();
            doc.Save("Test.xml");
        }

        //C#兩種方法判斷字符是否為漢字

        //一、用漢字的 UNICODE 編碼范圍判斷

        //漢字的 UNICODE 編碼范圍是4e00-9fbb，


        private void button5_Click(object sender, EventArgs e)
        {
            string text = "判斷是不是漢字，ABC,keleyi.com";
            char[] c = text.ToCharArray();

            for (int i = 0; i < c.Length; i++)
            {
                richTextBox1.Text += c[i] + "\t";
                if (c[i] >= 0x4e00 && c[i] <= 0x9fbb)
                {
                    Console.WriteLine("是漢字");
                    richTextBox1.Text += "是漢字\n";
                }
                else
                {
                    Console.WriteLine("不是漢字");
                    richTextBox1.Text += "不是漢字\n";
                }
            }

        }

        private void button6_Click(object sender, EventArgs e)
        {
            //獲取本機電腦名稱,IP,MAC地址,硬碟ID

            string CpuID;
            string MacAddress;
            string DiskID;
            string IpAddress;
            string LoginUserName;
            string ComputerName;
            string SystemType;
            string TotalPhysicalMemory; //單位：M

            CpuID = GetCpuID();
            MacAddress = GetMacAddress();
            DiskID = GetDiskID();
            IpAddress = GetIPAddress();
            LoginUserName = GetUserName();
            SystemType = GetSystemType();
            TotalPhysicalMemory = GetTotalPhysicalMemory();
            ComputerName = GetComputerName();

            richTextBox1.Text += "CpuID\t" + CpuID + "\n";
            richTextBox1.Text += "MacAddress\t" + MacAddress + "\n";
            richTextBox1.Text += "DiskID\t" + DiskID + "\n";
            richTextBox1.Text += "IpAddress\t" + IpAddress + "\n";
            richTextBox1.Text += "LoginUserName\t" + LoginUserName + "\n";
            richTextBox1.Text += "SystemType\t" + SystemType + "\n";
            richTextBox1.Text += "TotalPhysicalMemory\t" + TotalPhysicalMemory + "\n";
            richTextBox1.Text += "ComputerName\t" + ComputerName + "\n";


        }



        //獲取CPU序列號
        public string GetCpuID()
        {
            try
            {
                string cpuInfo = "";
                ManagementClass mc = new ManagementClass("Win32_Processor");
                ManagementObjectCollection moc = mc.GetInstances();
                foreach (ManagementObject mo in moc)
                {
                    cpuInfo = mo.Properties["ProcessorId"].Value.ToString();
                }
                moc = null;
                mc = null;
                return cpuInfo;
            }
            catch
            {
                return "unknow";
            }
            finally
            {
            }
        }

        //獲取網卡硬件地址
        public string GetMacAddress()
        {
            try
            {
                string mac = "";
                ManagementClass mc = new ManagementClass("Win32_NetworkAdapterConfiguration");
                ManagementObjectCollection moc = mc.GetInstances();
                foreach (ManagementObject mo in moc)
                {
                    if ((bool)mo["IPEnabled"] == true)
                    {
                        mac = mo["MacAddress"].ToString();
                        break;
                    }
                }
                moc = null;
                mc = null;
                return mac;
            }
            catch
            {
                return "unknow";
            }
            finally
            {
            }
        }

        //獲取IP地址
        public string GetIPAddress()
        {
            try
            {
                string st = "";
                ManagementClass mc = new ManagementClass("Win32_NetworkAdapterConfiguration");
                ManagementObjectCollection moc = mc.GetInstances();
                foreach (ManagementObject mo in moc)
                {
                    if ((bool)mo["IPEnabled"] == true)
                    {
                        //st=mo["IpAddress"].ToString();
                        System.Array ar;
                        ar = (System.Array)(mo.Properties["IpAddress"].Value);
                        st = ar.GetValue(0).ToString();
                        break;
                    }
                }
                moc = null;
                mc = null;
                return st;
            }
            catch
            {
                return "unknow";
            }
            finally
            {
            }
        }

        //獲取硬盤ID
        public string GetDiskID()
        {
            try
            {
                String HDid = "";
                ManagementClass mc = new ManagementClass("Win32_DiskDrive");
                ManagementObjectCollection moc = mc.GetInstances();
                foreach (ManagementObject mo in moc)
                {
                    HDid = (string)mo.Properties["Model"].Value;
                }
                moc = null;
                mc = null;
                return HDid;
            }
            catch
            {
                return "unknow";
            }
            finally
            {
            }
        }

        //操作系統的登錄用戶名
        public string GetUserName()
        {
            try
            {
                string st = "";
                ManagementClass mc = new ManagementClass("Win32_ComputerSystem");
                ManagementObjectCollection moc = mc.GetInstances();
                foreach (ManagementObject mo in moc)
                {

                    st = mo["UserName"].ToString();

                }
                moc = null;
                mc = null;
                return st;
            }
            catch
            {
                return "unknow";
            }
            finally
            {
            }
        }

        //PC類型
        public string GetSystemType()
        {
            try
            {
                string st = "";
                ManagementClass mc = new ManagementClass("Win32_ComputerSystem");
                ManagementObjectCollection moc = mc.GetInstances();
                foreach (ManagementObject mo in moc)
                {
                    st = mo["SystemType"].ToString();
                }
                moc = null;
                mc = null;
                return st;
            }
            catch
            {
                return "unknow";
            }
            finally
            {
            }
        }

        //物理內存
        public string GetTotalPhysicalMemory()
        {
            try
            {
                string st = "";
                ManagementClass mc = new ManagementClass("Win32_ComputerSystem");
                ManagementObjectCollection moc = mc.GetInstances();
                foreach (ManagementObject mo in moc)
                {
                    st = mo["TotalPhysicalMemory"].ToString();
                }
                moc = null;
                mc = null;
                return st;
            }
            catch
            {
                return "unknow";
            }
            finally
            {
            }
        }

        //電腦名稱
        public string GetComputerName()
        {
            try
            {
                return System.Environment.GetEnvironmentVariable("ComputerName");
            }
            catch
            {
                return "unknow";
            }
            finally
            {
            }
        }

        //數字大寫顯示 ST
        private void button7_Click(object sender, EventArgs e)
        {
            int money = 123456;
            string result = MoneyToChinese(money.ToString());
            richTextBox1.Text += result + "\n";
        }

        public static string MoneyToChinese(string strAmount)
        {
            string functionReturnValue = null;
            bool IsNegative = false; // 是否是負數
            if (strAmount.Trim().Substring(0, 1) == "-")
            {
                // 是負數則先轉為正數
                strAmount = strAmount.Trim().Remove(0, 1);
                IsNegative = true;
            }
            string strLower = null;
            string strUpart = null;
            string strUpper = null;
            int iTemp = 0;
            // 保留兩位小數123.489→123.49　　123.4→123.4
            strAmount = Math.Round(double.Parse(strAmount), 2).ToString();
            if (strAmount.IndexOf(".") > 0)
            {
                if (strAmount.IndexOf(".") == strAmount.Length - 2)
                {
                    strAmount = strAmount + "0";
                }
            }
            else
            {
                strAmount = strAmount + ".00";
            }

            strLower = strAmount;
            iTemp = 1;
            strUpper = "";
            while (iTemp <= strLower.Length)
            {
                switch (strLower.Substring(strLower.Length - iTemp, 1))
                {
                    case ".":
                        strUpart = "圓";
                        break;
                    case "0":
                        strUpart = "零";
                        break;
                    case "1":
                        strUpart = "壹";
                        break;
                    case "2":
                        strUpart = "貳";
                        break;
                    case "3":
                        strUpart = "三";
                        break;
                    case "4":
                        strUpart = "肆";
                        break;
                    case "5":
                        strUpart = "伍";
                        break;
                    case "6":
                        strUpart = "陸";
                        break;
                    case "7":
                        strUpart = "柒";
                        break;
                    case "8":
                        strUpart = "捌";
                        break;
                    case "9":
                        strUpart = "玖";
                        break;
                }

                switch (iTemp)
                {
                    case 1:
                        strUpart = strUpart + "分";
                        break;
                    case 2:
                        strUpart = strUpart + "角";
                        break;
                    case 3:
                        strUpart = strUpart + "";
                        break;
                    case 4:
                        strUpart = strUpart + "";
                        break;
                    case 5:
                        strUpart = strUpart + "拾";
                        break;
                    case 6:
                        strUpart = strUpart + "佰";
                        break;
                    case 7:
                        strUpart = strUpart + "仟";
                        break;
                    case 8:
                        strUpart = strUpart + "萬";
                        break;
                    case 9:
                        strUpart = strUpart + "拾";
                        break;
                    case 10:
                        strUpart = strUpart + "佰";
                        break;
                    case 11:
                        strUpart = strUpart + "仟";
                        break;
                    case 12:
                        strUpart = strUpart + "億";
                        break;
                    case 13:
                        strUpart = strUpart + "拾";
                        break;
                    case 14:
                        strUpart = strUpart + "佰";
                        break;
                    case 15:
                        strUpart = strUpart + "仟";
                        break;
                    case 16:
                        strUpart = strUpart + "萬";
                        break;
                    default:
                        strUpart = strUpart + "";
                        break;
                }
                strUpper = strUpart + strUpper;
                iTemp = iTemp + 1;
            }

            strUpper = strUpper.Replace("零拾", "零");
            strUpper = strUpper.Replace("零佰", "零");
            strUpper = strUpper.Replace("零仟", "零");
            strUpper = strUpper.Replace("零零零", "零");
            strUpper = strUpper.Replace("零零", "零");
            strUpper = strUpper.Replace("零角零分", "整");
            strUpper = strUpper.Replace("零分", "整");
            strUpper = strUpper.Replace("零角", "零");
            strUpper = strUpper.Replace("零億零萬零圓", "億圓");
            strUpper = strUpper.Replace("億零萬零圓", "億圓");
            strUpper = strUpper.Replace("零億零萬", "億");
            strUpper = strUpper.Replace("零萬零圓", "萬圓");
            strUpper = strUpper.Replace("零億", "億");
            strUpper = strUpper.Replace("零萬", "萬");
            strUpper = strUpper.Replace("零圓", "圓");
            strUpper = strUpper.Replace("零零", "零");

            // 對壹圓以下的金額的處理

            if (strUpper.Substring(0, 1) == "圓")
            {
                strUpper = strUpper.Substring(1, strUpper.Length - 1);
            }

            if (strUpper.Substring(0, 1) == "零")
            {
                strUpper = strUpper.Substring(1, strUpper.Length - 1);
            }

            if (strUpper.Substring(0, 1) == "角")
            {
                strUpper = strUpper.Substring(1, strUpper.Length - 1);
            }

            if (strUpper.Substring(0, 1) == "分")
            {
                strUpper = strUpper.Substring(1, strUpper.Length - 1);
            }

            if (strUpper.Substring(0, 1) == "整")
            {
                strUpper = "零圓整";
            }

            functionReturnValue = strUpper;

            if (IsNegative == true)
            {
                return "負" + functionReturnValue;
            }
            else
            {
                return functionReturnValue;
            }
        }

        //數字大寫顯示 SP


        //由日期找出星座 ST
        private void button8_Click(object sender, EventArgs e)
        {
            //由日期找出星座
            int month = 3;
            int day = 11;
            string result = getAstro(month, day);
            richTextBox1.Text += result + "\n";
        }

        private static String getAstro(int month, int day)
        {
            String[] starArr = { "魔羯座", "水瓶座", "雙魚座", "牡羊座", "金牛座", "雙子座", "巨蟹座", "獅子座", "處女座", "天秤座", "天蠍座", "射手座" };
            int[] DayArr = { 22, 20, 19, 21, 21, 21, 22, 23, 23, 23, 23, 22 };  // 兩個星座分割日
            int index = month;
            // 所查詢日期在分割日之前，索引-1，否則不變
            if (day < DayArr[month - 1])
            {
                index = index - 1;
            }
            index = index % 12;
            // 返回索引指向的星座string
            return starArr[index];
        }

        //由日期找出星座 SP

        //根據文件頭判斷上傳的文件類型 ST
        private void button9_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\doraemon.jpg";
            string result = getFileType(filename);
            richTextBox1.Text += "File Type : " + result + "\n";

        }

        /// <summary>
        /// 根據文件頭判斷上傳的文件類型
        /// </summary>
        /// <param name="filePath">filePath是文件的完整路徑 </param>
        /// <returns>返回true或false</returns>
        public string getFileType(string filePath)
        {
            try
            {
                FileStream fs = new FileStream(filePath, FileMode.Open, FileAccess.Read);
                BinaryReader reader = new BinaryReader(fs);
                string fileClass;
                byte buffer;
                buffer = reader.ReadByte();
                fileClass = buffer.ToString();
                buffer = reader.ReadByte();
                fileClass += buffer.ToString();
                reader.Close();
                fs.Close();

                //richTextBox1.Text += "fileClass == " + fileClass + "\t";

                if (fileClass == "255216")
                    return "jpg";
                else if (fileClass == "7173")
                    return "gif";
                else if (fileClass == "13780")
                    return "png";
                else if (fileClass == "6677")
                    return "bmp";
                else if (fileClass == "80114")
                    return "csv";
                else if (fileClass == "6063")
                    return "xml";
                else if (fileClass == "3780")
                    return "pdf";
                else if (fileClass == "4948")
                    return "txt";
                else if (fileClass == "8075")
                    return "zip";
                else if (fileClass == "XXXX")
                    return "XXXX";
                else if (fileClass == "XXXX")
                    return "XXXX";
                else if (fileClass == "XXXX")
                    return "XXXX";
                else if (fileClass == "XXXX")
                    return "XXXX";
                else
                {
                    return fileClass + "\tunknown";

                }
                //;7173是gif;,13780是PNG;7790是exe,8297是rar 
            }
            catch
            {
                return "unknown";
            }
        }

        //C#實現小小的日歷 ST
        private void button10_Click(object sender, EventArgs e)
        {

            int year = 2021;

            int month = 10;

            int day = 0;

            int sum = 0;



            for (int i = 1900; i < year; i++)
            {

                if (i % 4 == 0 && i % 100 != 0 || i % 400 == 0)
                {

                    sum += 366;

                }

                else
                {

                    sum += 365;

                }

            }



            switch (month)
            {

                case 12:

                    day = 31;

                    break;

                case 11:

                    day = 30;

                    break;

                case 10:

                    day = 31;

                    break;

                case 9:

                    day = 30;

                    break;

                case 8:

                    day = 31;

                    break;

                case 7:

                    day = 31;

                    break;

                case 6:

                    day = 30;

                    break;

                case 5:

                    day = 31;

                    break;

                case 4:

                    day = 30;

                    break;

                case 3:

                    day = 31;

                    break;

                case 2:

                    if (year % 4 == 0 && year % 100 != 0 || year % 400 == 0)

                        day = 29;

                    else

                        day = 28;

                    break;

                case 1:

                    day = 31;

                    break;

            }

            int leap;

            /*先計算某月以前月份的總天數*/

            switch (month)
            {

                case 1: sum += 0; break;

                case 2: sum += 31; break;

                case 3: sum += 59; break;

                case 4: sum += 90; break;

                case 5: sum += 120; break;

                case 6: sum += 151; break;

                case 7: sum += 181; break;

                case 8: sum += 212; break;

                case 9: sum += 243; break;

                case 10: sum += 273; break;

                case 11: sum += 304; break;

                case 12: sum += 334; break;

            }

            /*判斷是不是閏年*/

            if (year % 400 == 0 || (year % 4 == 0 && year % 100 != 0))

                leap = 1;

            else

                leap = 0;

            /*如果是閏年且月份大於2,總天數應該加一天*/

            if (leap == 1 && month > 2)

                sum++;



            int space = (sum + 1) % 7;



            Console.WriteLine("日\t一\t二\t三\t四\t五\t六\t");
            richTextBox1.Text += "日\t一\t二\t三\t四\t五\t六\t";



            for (int i = 1; i <= space + day; i++)
            {

                if (i <= space)
                {

                    //Console.Write("\t");
                    richTextBox1.Text += "\t";
                }
                else
                {
                    //Console.Write(i - space + "\t");
                    richTextBox1.Text += i - space + "\t";
                }


                if (i % 7 == 0)
                {

                    //Console.WriteLine();
                    richTextBox1.Text += "\n";
                }

            }

            //Console.WriteLine();
            richTextBox1.Text += "\n";


        }

        //C#實現小小的日歷 SP


        private void button11_Click(object sender, EventArgs e)
        {
        }
    }
}

