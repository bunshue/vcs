using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    public class TokenMinus : TokenArithmeticSymbol
    {
        public TokenMinus(int Index, int Length)
            : base(Index, Length)
        {
        }

        protected override void SetPriority()
        {
            this.m_Priority = 2;
        }

        /// <summary>
        /// 检查下级数量
        /// </summary>
        /// <returns></returns>
        protected new void CheckChildCount(string ErrorInformation)
        {
            if (!(this.ChildList.Count == 1 || this.ChildList.Count == 2))
            {
                //throw new ArgumentException(string.Format("语法错误，列{0}，{1}。", this.Index.ToString(), ErrorInformation));
                throw new SyntaxException(this.Index, this.Length, ErrorInformation);
            }
        }


        public override void Execute()
        {
            this.CheckChildCount("减法的运算元素数量不合法");

            TokenRecord TokenFirst;
            TokenRecord TokenSecond;
            if (this.ChildList.Count == 1)
            {
                TokenFirst = TokenNumberFactory.ProduceToken("0", this.Index);
                TokenSecond = this.ChildList[0];
            }
            else
            {
                TokenFirst = this.ChildList[0];
                TokenSecond = this.ChildList[1];
            }

            TokenFirst.Execute();
            TokenSecond.Execute();

            this.TokenValue = TokenFirst.ChangeTokenToDouble("减法的运算元素不是数值") - TokenSecond.ChangeTokenToDouble("减法的运算元素不是数值");
        }

    }
}
