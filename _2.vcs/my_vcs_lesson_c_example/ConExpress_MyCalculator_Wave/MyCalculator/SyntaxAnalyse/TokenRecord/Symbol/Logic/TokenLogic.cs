using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    public abstract class TokenLogic : TokenSymbol
    {
        public TokenLogic(int Index, int Length)
            : base(Index, Length)
        {
            this.SetChildCountError();
            this.TokenValueType = typeof(bool);
        }

        protected override void SetPriority()
        {
            this.m_Priority = 1;
        }

        protected string m_ChildCountErrorInformation;
        /// <summary>
        /// 设置下级数量错误信息，当下级数量不符时显示
        /// </summary>
        protected abstract void SetChildCountError();

        //public abstract override void Execute();
        public override void Execute()
        {
            this.CheckChildCount(m_ChildCountErrorInformation);

            for (int intIndex = 0; intIndex < this.m_ChildCount; intIndex++)
            {
                TokenRecord Token = this.ChildList[intIndex];
                Token.Execute();
            }
        }
    }
}