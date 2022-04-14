using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    public class TokenEqual : TokenCompare
    {
        public TokenEqual(int Index, int Length)
            : base(Index, Length)
        {
        }

        protected override void SetChildCountError()
        {
            this.m_ChildCountErrorInformation = "等于运算的元素数量不合法";
        }

        public override void Execute()
        {
            base.Execute();
            this.TokenValue = (base.Compare() == 0);
        }
    }

    /// <summary>
    /// 赋值运算符
    /// </summary>
    /// <remarks>对应=号</remarks>
    public class TokenEvaluate : TokenCompare
    {
        public TokenEvaluate(int Index, int Length)
            : base(Index, Length)
        { 
        }

        protected override void SetChildCountError()
        {
            this.m_ChildCountErrorInformation = "赋值运算的元素数量不合法";
        }

        public override void Execute()
        {
            //base.Execute();
            this.CheckChildCount(this.m_ChildCountErrorInformation);

            TokenRecord TokenFirst = this.ChildList[0];
            TokenRecord TokenSecond = this.ChildList[1];
            TokenSecond.Execute();

            if (TokenFirst is TokenValue && SyntaxAnalyse.DicVariable.ContainsValue(TokenFirst as TokenValue))
            {
                TokenFirst.TokenValueType = TokenSecond.TokenValueType;
                TokenFirst.TokenValue = TokenSecond.TokenValue;
                this.TokenValue = TokenSecond.TokenValue;
                this.TokenValueType = TokenSecond.TokenValueType;
            }
            else
            {
                //错误
                throw new SyntaxException(this.Index, this.Length, "赋值运算的赋值对象不是变量");
            }
        }
    }
}
