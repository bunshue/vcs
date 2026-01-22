using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.IO;    //for Directory, File

namespace vcs_Console_1
{
    class Program
    {
        static void Main(string[] args)
        {
            string path = "C:\\Windows\\System32\\com";  //預設開啟的路徑

            // Specify the starting folder on the command line, or in 
            // Visual Studio in the Project > Properties > Debug pane.
            TraverseTree(path);

            if (File.Exists(path))
            {
                // This path is a file
                ProcessFile(path);
            }
            else if (Directory.Exists(path))
            {
                // This path is a directory
                ProcessDirectory(path);
            }
            else
            {
                Console.WriteLine("{0} is not a valid file or directory.", path);
            }

            //C# 二進位轉十進位
            Console.WriteLine(Convert.ToInt32("1111", 2).ToString("D"));//Binary To Decimal
            //> Output: 15

            //C# 二進位轉十六進位
            Console.WriteLine(Convert.ToInt32("1111", 2).ToString("X"));//Binary To Hexadecimal
            //> Output: F

            //C# 十進位轉二進位
            Console.WriteLine(Convert.ToString(15, 2));//Decimal To Binary
            //> Output: 1111

            //C# 十進位轉十六進位
            Console.WriteLine(Convert.ToString(15, 16));//Decimal To Hexadecimal
            //> Output: f

            Console.WriteLine("目前時間 : " + DateTime.Now.ToString());

            Console.WriteLine("顯示Console支援的字體效果");
            ShowColor();

            Console.WriteLine("控制台程序設置字體顏色");

            Console.BackgroundColor = ConsoleColor.Blue; //設置背景色
            Console.ForegroundColor = ConsoleColor.White; //設置前景色，即字體顏色
            Console.WriteLine("第一行白藍.");

            Console.ResetColor(); //將控制台的前景色和背景色設為默認值
            Console.BackgroundColor = ConsoleColor.Green;
            Console.ForegroundColor = ConsoleColor.DarkGreen;
            string value = "第三行 綠暗綠";
            Console.WriteLine(value.PadRight(Console.WindowWidth - value.Length)); //設置一整行的背景色

            Console.Write("Press any key to continue");//無換行
            Console.WriteLine("Press any key");//有換行

            //以下都是讓畫面等一下, Hold住畫面
            Console.ReadLine();
            //Console.ReadKey();
            //Console.Read();
        }

        public static void TraverseTree(string root)
        {
            // Data structure to hold names of subfolders to be
            // examined for files.
            Stack<string> dirs = new Stack<string>(20);

            if (!System.IO.Directory.Exists(root))
            {
                throw new ArgumentException();
            }
            dirs.Push(root);

            while (dirs.Count > 0)
            {
                string currentDir = dirs.Pop();
                string[] subDirs;
                try
                {
                    subDirs = System.IO.Directory.GetDirectories(currentDir);
                }
                // An UnauthorizedAccessException exception will be thrown if we do not have
                // discovery permission on a folder or file. It may or may not be acceptable 
                // to ignore the exception and continue enumerating the remaining files and 
                // folders. It is also possible (but unlikely) that a DirectoryNotFound exception 
                // will be raised. This will happen if currentDir has been deleted by
                // another application or thread after our call to Directory.Exists. The 
                // choice of which exceptions to catch depends entirely on the specific task 
                // you are intending to perform and also on how much you know with certainty 
                // about the systems on which this code will run.
                catch (UnauthorizedAccessException e)
                {
                    Console.WriteLine(e.Message);
                    continue;
                }
                catch (System.IO.DirectoryNotFoundException e)
                {
                    Console.WriteLine(e.Message);
                    continue;
                }

                string[] files = null;
                try
                {
                    files = System.IO.Directory.GetFiles(currentDir);
                }

                catch (UnauthorizedAccessException e)
                {

                    Console.WriteLine(e.Message);
                    continue;
                }

                catch (System.IO.DirectoryNotFoundException e)
                {
                    Console.WriteLine(e.Message);
                    continue;
                }
                // Perform the required action on each file here.
                // Modify this block to perform your required task.
                foreach (string file in files)
                {
                    try
                    {
                        // Perform whatever action is required in your scenario.
                        System.IO.FileInfo fi = new System.IO.FileInfo(file);
                        Console.WriteLine("{0}: {1}, {2}", fi.Name, fi.Length, fi.CreationTime);
                    }
                    catch (System.IO.FileNotFoundException e)
                    {
                        // If file was deleted by a separate application
                        //  or thread since the call to TraverseTree()
                        // then just continue.
                        Console.WriteLine(e.Message);
                        continue;
                    }
                }

                // Push the subdirectories onto the stack for traversal.
                // This could also be done before handing the files.
                foreach (string str in subDirs)
                {
                    dirs.Push(str);
                }
            }
        }

        // Process all files in the directory passed in, recurse on any directories 
        // that are found, and process the files they contain.
        public static void ProcessDirectory(string targetDirectory)
        {
            // Process the list of files found in the directory.
            try
            {
                string[] fileEntries = Directory.GetFiles(targetDirectory);
                foreach (string fileName in fileEntries)
                {
                    ProcessFile(fileName);
                }

                // Recurse into subdirectories of this directory.
                string[] subdirectoryEntries = Directory.GetDirectories(targetDirectory);
                foreach (string subdirectory in subdirectoryEntries)
                    ProcessDirectory(subdirectory);
            }
            catch (UnauthorizedAccessException e)
            {
                Console.WriteLine(e.Message);
            }
        }

        // Insert logic for processing found files here.
        public static void ProcessFile(string path)
        {
            Console.WriteLine("Processed file '{0}'.", path);
        }

        static void ShowColor()
        {
            Type type = typeof(ConsoleColor);
            Console.ForegroundColor = ConsoleColor.White;
            foreach (var name in Enum.GetNames(type))
            {
                Console.BackgroundColor = (ConsoleColor)Enum.Parse(type, name);
                Console.WriteLine(name);
            }
            Console.BackgroundColor = ConsoleColor.Black;
            foreach (var name in Enum.GetNames(type))
            {
                Console.ForegroundColor = (ConsoleColor)Enum.Parse(type, name);
                Console.WriteLine(name);
            }
        }
    }
}
