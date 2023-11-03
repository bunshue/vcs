using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
using static System.Console;

namespace CH1506
{
    class Program
    {
        static void Main(string[] args)
        {
            BinaryReader readBit;
            FileStream objStream;
            //設定欲讀取檔案的路徑
            string path = @"D:\C#Lab\CH15\CH1506\005.jpg";
            //讀取範例CH1507寫入的二進位檔 Demo03.txt
            //string path = @"D:\C#Lab\Demo03.txt";
            int count = 0;
            try
            {
                objStream = new FileStream(
                   path, FileMode.Open, FileAccess.Read);

                //使用using陳述詞，確保資源的釋放
                using (readBit = new BinaryReader(objStream))
                {
                    do
                    {
                        //以位元組為單位讀取檔案內容，16進位方式顯示
                        Write($"{readBit.ReadByte(),2:X}");
                        count += 1;
                        //'** 換行
                        if (count == 10)
                        {
                            WriteLine();
                            count = 0;
                        }
                    } while (true);
                }
            }
            catch (IndexOutOfRangeException e)
            {
                WriteLine("沒有指定檔案");
            }

            catch (EndOfStreamException e)
            {
                WriteLine("\n檔案讀取完畢");
            }

            catch (Exception e)
            {
                WriteLine(e.Message);
            }
            ReadKey();
        }
    }
}
