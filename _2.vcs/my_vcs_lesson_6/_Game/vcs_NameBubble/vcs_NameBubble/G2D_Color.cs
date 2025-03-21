﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Drawing;

namespace vcs_NameBubble
{
    class G2D_Color  // 方便取得顏色的類別
    {
        static Color[] Colors = new Color[] {
            Color.AliceBlue, Color.AntiqueWhite, Color.Aqua, Color.Aquamarine, 
            Color.Azure, Color.Beige, Color.Bisque, Color.Black, Color.BlanchedAlmond, 
            Color.Blue, Color.BlueViolet, Color.Brown, Color.BurlyWood, Color.CadetBlue, 
            Color.Chartreuse, Color.Chocolate, Color.Coral, Color.CornflowerBlue, 
            Color.Cornsilk, Color.Crimson, Color.Cyan, Color.DarkBlue, Color.DarkCyan, 
            Color.DarkGoldenrod, Color.DarkGray, Color.DarkGreen, Color.DarkKhaki, 
            Color.DarkMagenta, Color.DarkOliveGreen, Color.DarkOrange, Color.DarkOrchid, 
            Color.DarkRed, Color.DarkSalmon, Color.DarkSeaGreen, Color.DarkSlateBlue, 
            Color.DarkSlateGray, Color.DarkTurquoise, Color.DarkViolet, Color.DeepPink, 
            Color.DeepSkyBlue, Color.DimGray, Color.DodgerBlue, Color.Firebrick, 
            Color.FloralWhite, Color.ForestGreen, Color.Fuchsia, Color.Gainsboro, 
            Color.GhostWhite, Color.Gold, Color.Goldenrod, Color.Gray, Color.Green, 
            Color.GreenYellow, Color.Honeydew, Color.HotPink, Color.IndianRed, Color.Indigo, 
            Color.Ivory, Color.Khaki, Color.Lavender, Color.LavenderBlush, Color.LawnGreen, 
            Color.LemonChiffon, Color.LightBlue, Color.LightCoral, Color.LightCyan, 
            Color.LightGoldenrodYellow, Color.LightGray, Color.LightGreen, Color.LightPink, 
            Color.LightSalmon, Color.LightSeaGreen, Color.LightSkyBlue, Color.LightSlateGray, 
            Color.LightSteelBlue, Color.LightYellow, Color.Lime, Color.LimeGreen, Color.Linen, 
            Color.Magenta, Color.Maroon, Color.MediumAquamarine, Color.MediumBlue, 
            Color.MediumOrchid, Color.MediumPurple, Color.MediumSeaGreen, Color.MediumSlateBlue, 
            Color.MediumSpringGreen, Color.MediumTurquoise, Color.MediumVioletRed, 
            Color.MidnightBlue, Color.MintCream, Color.MistyRose, Color.Moccasin, 
            Color.NavajoWhite, Color.Navy, Color.OldLace, Color.Olive, Color.OliveDrab, 
            Color.Orange, Color.OrangeRed, Color.Orchid, Color.PaleGoldenrod, Color.PaleGreen, 
            Color.PaleTurquoise, Color.PaleVioletRed, Color.PapayaWhip, Color.PeachPuff, 
            Color.Peru, Color.Pink, Color.Plum, Color.PowderBlue, Color.Purple, Color.Red, 
            Color.RosyBrown, Color.RoyalBlue, Color.SaddleBrown, Color.Salmon, Color.SandyBrown,
            Color.SeaGreen, Color.SeaShell, Color.Sienna, Color.Silver, Color.SkyBlue,
            Color.SlateBlue, Color.SlateGray, Color.Snow, Color.SpringGreen, Color.SteelBlue, 
            Color.Tan, Color.Teal, Color.Thistle, Color.Tomato, Color.Turquoise, Color.Violet, 
            Color.Wheat, Color.White, Color.WhiteSmoke, Color.Yellow, Color.YellowGreen};
        static Random rd = new Random();

        static public Color GetColor() // 取得一個預設的顏色
        {
            int k = rd.Next(Colors.Length);
            return Colors[k];  // 取出顏色
        }

        static public Color GetRandomColor() // 隨機取得一個顏色
        {
            byte r = (byte)rd.Next(256); // 紅 red
            byte g = (byte)rd.Next(256); // 綠 green
            byte b = (byte)rd.Next(256); // 藍 blue

            return Color.FromArgb(r, g, b);  // 紅綠藍 配方
        }

        static public Color GetWebSafeColor()  // 隨機取得一個網頁安全色
        {
            byte r = (byte)(rd.Next(6) * 51); // 每次間格 33 (16 進位) = 51
            byte g = (byte)(rd.Next(6) * 51);
            byte b = (byte)(rd.Next(6) * 51);
            return Color.FromArgb(r, g, b);  // 紅綠藍 配方
        }
    }
}
