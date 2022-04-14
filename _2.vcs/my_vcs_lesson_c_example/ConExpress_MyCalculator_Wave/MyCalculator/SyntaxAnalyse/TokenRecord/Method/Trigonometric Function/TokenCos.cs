using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    /// <summary>
    /// 余弦记号类，对应关键字cos，不区分大小写，采用角度值，截取小数点后10位。
    /// </summary>
    /// <example>用法cos(45)，必须带括号。</example>
    public class TokenCos : TokenTrigonometricFunction
    {
        public TokenCos(int Index, int Length)
            : base(Index, Length)
        { }

        public override void Execute()
        {
            this.CheckChildCount("cos方法的运算元素数量不合法");

            TokenRecord TokenChild = this.ChildList[0];
            TokenChild.Execute();

            this.TokenValue = Math.Round(Math.Cos(TokenChild.ChangeTokenToDouble("cos方法的操作数不是数字") / 180 * Math.PI), 10);
        }
    }
}