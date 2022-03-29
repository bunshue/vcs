#region 版权
/*
 * 版权归Lawson所有
 * QQ：313769823
 * Email:lawson.ls@hotmail.com
 * Blog:lawson.cnblogs.com
 */
#endregion

using System;
using System.Collections.Generic;
using System.Text;

namespace Main
{
    public class FlakeList<T> where T : IImage
    {
        private IList<T> flyPlakeList = null;
        private T flyFlake = default(T);

        /// <summary>
        /// 构造函数
        /// </summary>
        /// <param name="t">定义类型</param>
        public FlakeList(T t)
        {
            flyFlake = t;
            flyPlakeList = new List<T>();
        }

        public void BuildImage(T method)
        {
            //flyFlake = new List<flake>();
            flyFlake = method;
            flyPlakeList = new List<T>();
        }

        public void Add(T t)
        {
            flyPlakeList.Add(t);
        }
    }
}
