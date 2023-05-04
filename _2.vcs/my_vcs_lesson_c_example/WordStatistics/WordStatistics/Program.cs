using System;
using System.Collections;
using System.Collections.Concurrent;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading;
using System.Threading.Tasks;
using System.Threading.Tasks.Dataflow;

namespace WordStatistics
{
    class Program
    {
        static void Main(string[] args)
        {
            DateTime dt = DateTime.Now;

            var buffer = new BufferBlock<WordStream>();

            //创建工作BufferBlock
            WordProcessBufferBlock wb = new WordProcessBufferBlock(8, buffer);
            wb.StartWord();

            //创建读取文件,发送的BufferBlock
            FileBufferBlock fb = new FileBufferBlock(buffer, @"C:\______test_files1\__RW\_txt\english_text.txt");
            fb.ReadFile();

            Dictionary<string,int> dic = new Dictionary<string,int>();

            //等待工作完成汇总结果
            wb.WaitAll(p =>
                {
                    foreach (var row in p)
                    {
                        if (!dic.ContainsKey(row.Key))
                            dic.Add(row.Key, row.Value);
                        else
                        {
                            dic[row.Key] += row.Value;
                        }
                    }
                }
                );

            var myList = dic.ToList();
            myList.Sort((p, v) => v.Value.CompareTo(p.Value));
            foreach (var row in myList.Take(10))
            {
                Console.WriteLine(row);
            }

            
            Console.WriteLine(DateTime.Now - dt);

            Console.Write("Press any key to continue"); //無換行
            Console.Write("Press any key to continue");//無換行
            Console.WriteLine("Press any key");//有換行
            Console.WriteLine("Press any key");//有換行
            Console.ReadLine();
            Console.ReadKey();
            Console.Read();


        }
    }

}
