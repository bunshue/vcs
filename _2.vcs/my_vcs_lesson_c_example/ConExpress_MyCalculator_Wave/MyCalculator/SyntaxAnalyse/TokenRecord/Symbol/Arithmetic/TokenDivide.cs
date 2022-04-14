using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    public class TokenDivide : TokenArithmeticSymbol 
    {
        public TokenDivide(int Index, int Length)
            : base(Index, Length)
        {
        }

        protected override void SetPriority()
        {
            this.m_Priority = 3;
        }

        public override void Execute()
        {
            this.CheckChildCount("除法的运算元素数量不合法");

            TokenRecord TokenFirst = this.ChildList[0];
            TokenRecord TokenSecond = this.ChildList[1];
            TokenFirst.Execute();
            TokenSecond.Execute();

            //检查除数不能为0
            if (TokenSecond.ChangeTokenToDouble("除法的运算元素不是数值") == 0)
            {
                //throw new DivideByZeroException(string.Format("算术运算错误，列{0}，除数不能为零。",this.Index.ToString()));
                throw new SyntaxException(this.Index, this.Length, "算术运算错误，除数不能为零");
            }

            this.TokenValue = TokenFirst.ChangeTokenToDouble("除法的运算元素不是数值") / TokenSecond.ChangeTokenToDouble("除法的运算元素不是数值");
        }
    }
}
