using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    /// <summary>
    /// Left记号类，字符串操作，对应关键字left，不区分大小写
    /// </summary>
    /// <example>用法left("hello world",5)，返回hello。</example>
    /// <remarks>如果截取长度小于1，则默认为1；如果截取长度大于字符串长度，则默认为字符串长度。</remarks>
    public class TokenLeft : TokenStringMethod
    {
        public TokenLeft(int Index, int Length)
            : base(Index, Length)
        {
            this.TokenValueType = typeof(string);
        }

        public override void Execute()
        {
            this.CheckChildCount("left语句的运算元素数量不合法");//check child token

            string strMid = string.Empty;
            TokenRecord TokenSource = this.ChildList[0];
            TokenSource.Execute();
            string strSource = TokenSource.ChangeTokenToString();

            TokenRecord TokenLength = this.ChildList[1];
            TokenLength.Execute();
            int intLength = Convert.ToInt32(TokenLength.ChangeTokenToDouble("left语句的截取数量不是合法数字"));

            //检查长度的合法性，有没有越过范围
            intLength = Convert.ToInt32(intLength) < 1 ? 1 : intLength;
            intLength = Convert.ToInt32(intLength) > strSource.Length ? strSource.Length : intLength;

            this.TokenValue = strSource.Substring(0, intLength);
        }
    }
}
