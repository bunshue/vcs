using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    public class TokenMid : TokenStringMethod
    {
        public TokenMid(int Index, int Length)
            : base(Index, Length)
        { }

        /// <summary>
        /// 检查下级数量
        /// </summary>
        /// <returns></returns>
        public new void CheckChildCount(string ErrorInformation)
        {
            if (!(this.ChildList.Count == 2 || this.ChildList.Count == 3))
            {
                //throw new ArgumentException(string.Format("语法错误，列{0}，{1}。", this.Index.ToString(), ErrorInformation));
                throw new SyntaxException(this.Index, this.Length, ErrorInformation);
            }
        }

        public override void Execute()
        {
            this.CheckChildCount("mid的运算元素数量不合法");//check child token

            TokenRecord TokenSource = this.ChildList[0];
            TokenSource.Execute();
            string strSource = TokenSource.ChangeTokenToString();

            TokenRecord TokenStartIndex = this.ChildList[1];
            TokenStartIndex.Execute();
            int intStartIndex = Convert.ToInt32(TokenStartIndex.ChangeTokenToDouble("mid的起始序号不是合法数字"));

            //检查起始序号的合法性，有没有越过范围
            if(intStartIndex < 0)
                throw new SyntaxException(this.Index, this.Length, "mid的起始序号小于0");
            if(intStartIndex > strSource.Length)
                throw new SyntaxException(this.Index, this.Length, "mid的起始序号大于字符串长度");

            if (this.ChildList.Count == 2)
            {
                this.TokenValue = strSource.Substring(intStartIndex);
            }
            else
            {
                TokenRecord TokenLength = this.ChildList[2];
                TokenLength.Execute();
                int intLength = Convert.ToInt32(TokenLength.ChangeTokenToDouble("mid的结束序号不是合法数字"));

                //检查结束序号的合法性，有没有越过范围
                if (intLength < 0)
                    throw new SyntaxException(this.Index, this.Length, "mid的截取长度小于0");
                if(intLength > strSource.Length - intStartIndex)
                    throw new SyntaxException(this.Index, this.Length, "mid的截取长度超出范围");

                this.TokenValue = strSource.Substring(intStartIndex, intLength);
            }
        }
    }
}
