using System;
using System.Collections.Generic;
using System.Text;
using Microsoft.VisualBasic;

namespace ConExpress.Calculator
{
    public abstract class TokenCompare : TokenLogic
    {
        public TokenCompare(int Index, int Length)
            : base(Index, Length)
        {
        }

        public override void Execute()
        {
            base.Execute();
        }

        protected int Compare()
        {
            TokenRecord TokenFirst = this.ChildList[0];
            TokenRecord TokenSecond = this.ChildList[1];
            if (TokenFirst.TokenValueType != TokenSecond.TokenValueType)
            {
                if (Information.IsNumeric(TokenFirst.TokenValue) && Information.IsNumeric(TokenSecond.TokenValue))
                {
                    return TokenFirst.ChangeTokenToDouble("无法将当前值转换为数字").CompareTo(TokenSecond.ChangeTokenToDouble("无法将当前值转换为数字"));
                }
                else
                {
                    return TokenFirst.ChangeTokenToString().CompareTo(TokenSecond.ChangeTokenToString());
                }
            }
            else
            {
                if (TokenFirst.TokenValueType == typeof(bool))
                {
                    return TokenFirst.ChangeTokenToBoolean().CompareTo(TokenSecond.ChangeTokenToBoolean());
                }
                else if (TokenFirst.TokenValueType == typeof(double))
                {
                    return TokenFirst.ChangeTokenToDouble("无法将当前值转换为数字").CompareTo(TokenSecond.ChangeTokenToDouble("无法将当前值转换为数字"));
                }
                else
                {
                    return TokenFirst.ChangeTokenToString().CompareTo(TokenSecond.ChangeTokenToString());
                } 
            }

        }
    }
}
