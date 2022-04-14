using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    /// <summary>
    /// If记号类，对应关键字if，不区分大小写
    /// </summary>
    /// <example>用法：if(Condition, TrueValue, FalseValue)，如果Condition为true，则返回TrueValue，否则返回FalseValue</example>
    public class TokenIf : TokenMethod
    {
        public TokenIf(int Index, int Length)
            : base(Index, Length)
        {
        }

        protected override void SetChildCount()
        {
            this.m_ChildCount = 3;
        }

        public override void Execute()
        {
            this.CheckChildCount("if语句运算元素数量不合法");

            TokenRecord TokenCondition = this.ChildList[0];
            TokenRecord TokenTrue = this.ChildList[1];
            TokenRecord TokenFalse = this.ChildList[2];

            //execute child token
            TokenCondition.Execute();
            //根据条件短路执行
            if (TokenCondition.ChangeTokenToBoolean())
            {
                TokenTrue.Execute();
                this.TokenValueType = TokenTrue.TokenValueType;
                this.TokenValue = TokenTrue.TokenValue;
            }
            else
            {
                TokenFalse.Execute();
                this.TokenValueType = TokenFalse.TokenValueType;
                this.TokenValue = TokenFalse.TokenValue;
            }

            ////if TokenTrue's type is not equal TokenFalse's type, convert them to string
            //if (TokenTrue.TokenValueType != TokenFalse.TokenValueType)
            //{
            //    //Error or set token type as string
            //    TokenTrue.ChangeTokenToString();
            //    TokenFalse.ChangeTokenToString();
            //}

            //this.TokenValueType = TokenTrue.TokenValueType;
            //this.TokenValue = TokenCondition.ChangeTokenToBoolean() ? TokenTrue.TokenValue : TokenFalse.TokenValue;
        }
    }
}