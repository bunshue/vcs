using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    /// <summary>
    /// 左括号记号类，对应字符(
    /// </summary>
    public class TokenLeftBracket : TokenCompart
    {
        public TokenLeftBracket(int Index, int Length)
            : base(Index, Length)
        {
        }

        protected override void SetPriority()
        {
            this.m_Priority = 10;//括号的优先级最高，可以任意设置最大的数
        }

        public override void Execute()
        {
            this.CheckChildCount("括号内运算结果不唯一");

            TokenRecord TokenInner = this.ChildList[0];
            TokenInner.Execute();
            this.TokenValueType = TokenInner.TokenValueType;
            this.TokenValue = TokenInner.TokenValue;
            //if (TokenInner.TokenValueType == TokenValueTypeEnum.String)
            //{
            //    this.TokenString = TokenInner.TokenString;
            //}
            //else
            //{
            //    this.TokenNumber = TokenInner.TokenNumber;
            //}
        }
    }
}