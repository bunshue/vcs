using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace xCh11_2_21
{
    class Program
    {
        static void Main(string[] args)
        {
            // Step 01. 資料來源
            string[] words = {
                                "blueberry", 
                                "chimpanzee", 
                                "abacus", 
                                "banana", 
                                "apple", 
                                "cheese", 
                                "elephant", 
                                "umbrella", 
                                "anteater" 
                             };

            // Step 02. 查詢運算式
            var wordGroups =
                from w in words
                group w by w[0] into grps
                where (grps.Key == 'a' ||
                            grps.Key == 'e' ||
                            grps.Key == 'i'  ||
                            grps.Key == 'o' ||
                            grps.Key == 'u')
                select grps;

            //Step 03. 執行查詢
            foreach (var wordGroup in wordGroups)
            {
                Console.WriteLine("以母音: {0} 開頭的群組", wordGroup.Key);
                foreach (var word in wordGroup)
                {
                    Console.WriteLine("   {0}", word);
                }
            }
        }
    }
}


