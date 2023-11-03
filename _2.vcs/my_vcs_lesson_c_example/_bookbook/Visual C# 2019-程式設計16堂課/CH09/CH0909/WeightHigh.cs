using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CH0909
{
    class WeightHigh : Exception
    {
        //呼叫Exception預設建構函式
        public WeightHigh() : base() { }

        //呼叫Exception含有錯誤訊息的建構函式
        public WeightHigh(string String) : base(String) { }

        //定義成員方法以throw敘述擲出例外狀況的訊息
        public string testWeight(int weight, int high)
        {
            if (weight > 250)
            {
                throw new WeightHigh("有那麼重的體重嗎");
            }
            else if (weight < 40)
            {
                throw new WeightHigh("有那麼輕的體重嗎");
            }
            else if (high > 300)
            {
                throw new WeightHigh("有那麼高的嗎");
            }
            else if (high < 50)
            {
                throw new WeightHigh("有那麼矮的嗎");
            }

            double diff = weight - ((high - 80) * 0.7);

            //使用雙重條件運算子 ? :
            string result = (diff > 10) ? "太重囉."
                : ((diff < -10) ? "太輕噢" : "很正常，保持下去");
            return result;
        }
    }
}
