using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{  
    //Author: Alex Leo
    //Email: alexleo321@hotmail.com
    //Blog: http://www.cnblogs.com/conexpress/


    //更新日志
    //Date:2008-4-24; Author:Alex Leo;
    //Remark:将语法分析的单个方法进行重构，提出多个方法
    //Remark:对字符串的处理更灵活，可以接受单引号和双引号，和HTML一样，同时对于两个字符串标识符进行转义
    //Date:2009-5-21; Author:Alex Leo;
    //Remark:实现变量，将min和max的操作数修改为不限制个数（但必须大于1）
    //Remark:新增Sum和Avg方法
	
    /// <summary>
    /// 表达式分析计算类，功能入口
    /// </summary>
    /// <remarks>Author:Alex Leo</remarks>
    public class SyntaxAnalyse
	{
        /// <summary>
        /// 构造函数
        /// </summary>
        /// <remarks>Author:Alex Leo; Date:2007-8-2</remarks>
        public SyntaxAnalyse()
        { }

        internal static Dictionary<string, TokenValue> DicVariable = new Dictionary<string,TokenValue>();//变量字典（新增）

        /// <summary>
        /// 分析语句并返回记号记录对象
        /// </summary>
        /// <param name="Code">运算表达式</param>
        /// <returns>顶级TokenRecord对象</returns>
        public TokenRecord Analyse(string Code)
        {
            if (Code.Trim().Equals(string.Empty))
            {
                return new TokenValue(0,1);
            }

            List<TokenRecord> ListToken = new List<TokenRecord>();//TokenRecord列表

            int intIndex = 0;
            TokenFactory.LexicalAnalysis(ListToken, Code, ref intIndex);//词法分析，将代码转换为TokenRecord列表

            //语法树分析，将Token列表按优先级转换为树
            TokenRecord TokenTop = SyntaxTreeAnalyse.SyntaxTreeGetTopTokenAnalyse(ListToken, 0, ListToken.Count - 1);
            TokenTop.Execute();
            return TokenTop;
        }
   }
}