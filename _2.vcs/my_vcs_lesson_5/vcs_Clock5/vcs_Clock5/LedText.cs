using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.Drawing;

namespace vcs_Clock5
{
    class LedText
    {
        public float CellWidth, CellHeight, LedThickness, Gap;
        public Dictionary<char, bool[]> LetterLeds = null;

        public LedText(float cell_width, float cell_height,
            float led_thickness, float gap)
        {
            CellWidth = cell_width;
            CellHeight = cell_height;
            LedThickness = led_thickness;
            Gap = gap;

            // Define the functions that draw the LEDs.
            DefineLedFuncs();

            // Define the letters.
            DefineLetters();
        }

        // Define the LED methods used to draw letters.
        public void DefineLetters()
        {
            if (LetterLeds != null) return;
            LetterLeds = new Dictionary<char, bool[]>();

            LetterLeds.Add((char)0, StringToBool("11111111111111"));

            //LetterLeds.Add('0', StringToBool("11000100100011"));    // Without diagonal slashes.
            LetterLeds.Add('0', StringToBool("11001100110011"));    // With diagonal slashes.
            LetterLeds.Add('1', StringToBool("00001100000010"));
            LetterLeds.Add('2', StringToBool("10000111100001"));
            LetterLeds.Add('3', StringToBool("10000101000011"));
            LetterLeds.Add('4', StringToBool("01000111000010"));
            LetterLeds.Add('5', StringToBool("11000011000011"));
            LetterLeds.Add('6', StringToBool("11000011100011"));
            LetterLeds.Add('7', StringToBool("10000100000010"));
            LetterLeds.Add('8', StringToBool("11000111100011"));
            LetterLeds.Add('9', StringToBool("11000111000011"));
            LetterLeds.Add('A', StringToBool("11000111100010"));
            LetterLeds.Add('B', StringToBool("10010101001011"));
            LetterLeds.Add('C', StringToBool("11000000100001"));
            LetterLeds.Add('D', StringToBool("10010100001011"));
            LetterLeds.Add('E', StringToBool("11000010100001"));
            LetterLeds.Add('F', StringToBool("11000010100000"));
            LetterLeds.Add('G', StringToBool("11000001100011"));
            LetterLeds.Add('H', StringToBool("01000111100010"));
            LetterLeds.Add('I', StringToBool("10010000001001"));
            LetterLeds.Add('J', StringToBool("00000100100011"));
            LetterLeds.Add('K', StringToBool("01001010100100"));
            LetterLeds.Add('L', StringToBool("01000000100001"));
            LetterLeds.Add('M', StringToBool("01101100100010"));
            LetterLeds.Add('N', StringToBool("01100100100110"));
            LetterLeds.Add('O', StringToBool("11000100100011"));
            LetterLeds.Add('P', StringToBool("11000111100000"));
            LetterLeds.Add('Q', StringToBool("11000100100111"));
            LetterLeds.Add('R', StringToBool("11000111100100"));
            LetterLeds.Add('S', StringToBool("11000011000011"));
            LetterLeds.Add('T', StringToBool("10010000001000"));
            LetterLeds.Add('U', StringToBool("01000100100011"));
            LetterLeds.Add('V', StringToBool("01001000110000"));
            LetterLeds.Add('W', StringToBool("01000100110110"));
            LetterLeds.Add('X', StringToBool("00101000010100"));
            LetterLeds.Add('Y', StringToBool("00101000001000"));
            LetterLeds.Add('Z', StringToBool("10001000010001"));
            LetterLeds.Add('/', StringToBool("00001000010000"));
            LetterLeds.Add(' ', StringToBool("00000000000000"));
            //                                -|\|/|--|/|\|-
        }

        // Convert a string of the form 10100110...
        // into an array of bool.
        private bool[] StringToBool(string values)
        {
            bool[] result = new bool[values.Length];
            for (int i = 0; i < values.Length; i++)
                result[i] = (values[i] == '1');
            return result;
        }

        // Make an array to hold the LED-drawing functions.
        private delegate PointF[] LedFunc(PointF point);
        private LedFunc[] LedFuncs = null;

        private void DefineLedFuncs()
        {
            LedFuncs = new LedFunc[]
            {
                MakeLed0,
                MakeLed1,
                MakeLed2,
                MakeLed3,
                MakeLed4,
                MakeLed5,
                MakeLed6,
                MakeLed7,
                MakeLed8,
                MakeLed9,
                MakeLed10,
                MakeLed11,
                MakeLed12,
                MakeLed13,
            };
        }

#region Led polygon functions
        public PointF[] MakeLed0(PointF position)
        {
            PointF p1 = new PointF(
                position.X + LedThickness / 2f + Gap,
                position.Y + LedThickness / 2f);
            PointF p2 = new PointF(
                position.X + CellWidth - LedThickness / 2f - Gap,
                p1.Y);
            return MakeHLed(p1, p2);
        }
        public PointF[] MakeLed13(PointF position)
        {
            PointF p1 = new PointF(
                position.X + LedThickness / 2f + Gap,
                position.Y + CellHeight - LedThickness / 2f);
            PointF p2 = new PointF(
                position.X + CellWidth - LedThickness / 2f - Gap,
                p1.Y);
            return MakeHLed(p1, p2);
        }
        public PointF[] MakeLed6(PointF position)
        {
            PointF p1 = new PointF(
                position.X + LedThickness / 2f + Gap,
                position.Y + CellHeight / 2f);
            PointF p2 = new PointF(
                position.X + CellWidth / 2f - Gap,
                p1.Y);
            return MakeHLed(p1, p2);
        }
        public PointF[] MakeLed7(PointF position)
        {
            PointF p1 = new PointF(
                position.X + CellWidth / 2f + Gap,
                position.Y + CellHeight / 2f);
            PointF p2 = new PointF(
                position.X + CellWidth - LedThickness / 2f - Gap,
                p1.Y);
            return MakeHLed(p1, p2);
        }
        public PointF[] MakeHLed(PointF p1, PointF p2)
        {
            PointF[] points =
            {
                new PointF(p1.X, p1.Y),
                new PointF(p1.X + LedThickness / 2f, p1.Y + LedThickness / 2f),
                new PointF(p2.X - LedThickness / 2f, p2.Y + LedThickness / 2f),
                new PointF(p2.X, p2.Y),
                new PointF(p2.X - LedThickness / 2f, p2.Y - LedThickness / 2f),
                new PointF(p1.X + LedThickness / 2f, p1.Y - LedThickness / 2f),
            };
            return points;
        }

        public PointF[] MakeLed1(PointF position)
        {
            PointF p1 = new PointF(
                position.X + LedThickness / 2f,
                position.Y + LedThickness / 2f + Gap);
            PointF p2 = new PointF(
                p1.X,
                position.Y + CellHeight / 2f - Gap);
            return MakeVLed(p1, p2);
        }
        public PointF[] MakeLed8(PointF position)
        {
            PointF p1 = new PointF(
                position.X + LedThickness / 2f,
                position.Y + CellHeight / 2f + Gap);
            PointF p2 = new PointF(
                p1.X,
                position.Y + CellHeight - LedThickness / 2f - Gap);
            return MakeVLed(p1, p2);
        }
        public PointF[] MakeLed5(PointF position)
        {
            PointF p1 = new PointF(
                position.X + CellWidth - LedThickness / 2f,
                position.Y + LedThickness / 2f + Gap);
            PointF p2 = new PointF(
                p1.X,
                position.Y + CellHeight / 2f - Gap);
            return MakeVLed(p1, p2);
        }
        public PointF[] MakeLed12(PointF position)
        {
            PointF p1 = new PointF(
                position.X + CellWidth - LedThickness / 2f,
                position.Y + CellHeight / 2f + Gap);
            PointF p2 = new PointF(
                p1.X,
                position.Y + CellHeight - LedThickness / 2f - Gap);
            return MakeVLed(p1, p2);
        }
        public PointF[] MakeVLed(PointF p1, PointF p2)
        {
            PointF[] points =
            {
                new PointF(p1.X, p1.Y),
                new PointF(p1.X + LedThickness / 2f, p1.Y + LedThickness / 2f),
                new PointF(p2.X + LedThickness / 2f, p2.Y - LedThickness / 2f),
                new PointF(p2.X, p2.Y),
                new PointF(p2.X - LedThickness / 2f, p2.Y - LedThickness / 2f),
                new PointF(p1.X - LedThickness / 2f, p1.Y + LedThickness / 2f),
            };
            return points;
        }

        public PointF[] MakeLed3(PointF position)
        {
            PointF p1 = new PointF(
                position.X + CellWidth / 2f,
                position.Y + LedThickness + Gap);
            PointF p2 = new PointF(
                p1.X,
                position.Y + CellHeight / 2f - Gap);
            return MakeCtLed(p1, p2);
        }
        public PointF[] MakeCtLed(PointF p1, PointF p2)
        {
            PointF[] points =
            {
                new PointF(p1.X - LedThickness / 2f, p1.Y),
                new PointF(p1.X + LedThickness / 2f, p1.Y),
                new PointF(p2.X + LedThickness / 2f, p2.Y - LedThickness / 2f),
                new PointF(p2.X, p2.Y),
                new PointF(p1.X - LedThickness / 2f, p2.Y - LedThickness / 2f),
            };
            return points;
        }

        public PointF[] MakeLed10(PointF position)
        {
            PointF p1 = new PointF(
                position.X + CellWidth / 2f,
                position.Y + CellHeight / 2f + Gap);
            PointF p2 = new PointF(
                p1.X,
                position.Y + CellHeight - LedThickness - Gap);
            return MakeCbLed(p1, p2);
        }
        public PointF[] MakeCbLed(PointF p1, PointF p2)
        {
            PointF[] points =
            {
                new PointF(p1.X, p1.Y),
                new PointF(p1.X + LedThickness / 2f, p1.Y + LedThickness / 2f),
                new PointF(p2.X + LedThickness / 2f, p2.Y),
                new PointF(p2.X - LedThickness / 2f, p2.Y),
                new PointF(p1.X - LedThickness / 2f, p1.Y + LedThickness / 2f),
            };
            return points;
        }

        public PointF[] MakeLed2(PointF position)
        {
            float sqrt2 = (float)Math.Sqrt(2.0);
            float dx = LedThickness / sqrt2;
            float dy = dx;

            PointF u_diag_pt1 = new PointF(
                position.X + dx,
                position.Y);
            PointF u_diag_pt2 = new PointF(
                position.X + CellWidth,
                position.Y + CellHeight - dy);

            PointF l_diag_pt1 = new PointF(
                position.X,
                position.Y + dy);
            PointF l_diag_pt2 = new PointF(
                position.X + CellWidth - dx,
                position.Y + CellHeight);

            PointF u_horz_pt1 = new PointF(
                position.X,
                position.Y + LedThickness + Gap);
            PointF u_horz_pt2 = new PointF(
                position.X + CellWidth,
                position.Y + LedThickness + Gap);

            PointF l_horz_pt1 = new PointF(
                position.X,
                position.Y + CellHeight / 2f - LedThickness / 2f - Gap);
            PointF l_horz_pt2 = new PointF(
                position.X + CellWidth,
                position.Y + CellHeight / 2f - LedThickness / 2f - Gap);

            PointF l_vert_pt1 = new PointF(
                position.X + LedThickness + Gap,
                position.Y);
            PointF l_vert_pt2 = new PointF(
                position.X + LedThickness + Gap,
                position.Y + CellHeight);

            PointF r_vert_pt1 = new PointF(
                position.X + CellWidth / 2f - LedThickness / 2f - Gap,
                position.Y);
            PointF r_vert_pt2 = new PointF(
                position.X + CellWidth / 2f - LedThickness / 2f - Gap,
                position.Y + CellHeight);

            PointF[][] segs =
            {
                new PointF[] { l_vert_pt1, l_vert_pt2, u_horz_pt1, u_horz_pt2 },
                new PointF[] { u_horz_pt1, u_horz_pt2, u_diag_pt1, u_diag_pt2 },
                new PointF[] { u_diag_pt1, u_diag_pt2, r_vert_pt1, r_vert_pt2 },
                new PointF[] { r_vert_pt1, r_vert_pt2, l_horz_pt1, l_horz_pt2 },
                new PointF[] { l_horz_pt1, l_horz_pt2, l_diag_pt1, l_diag_pt2 },
                new PointF[] { l_diag_pt1, l_diag_pt2, l_vert_pt1, l_vert_pt2 },
            };
            return MakeIntersectionLed(segs);
        }
        public PointF[] MakeLed4(PointF position)
        {
            float sqrt2 = (float)Math.Sqrt(2.0);
            float dx = LedThickness / sqrt2;
            float dy = dx;

            PointF u_diag_pt1 = new PointF(
                position.X + CellWidth - dx,
                position.Y);
            PointF u_diag_pt2 = new PointF(
                position.X,
                position.Y + CellHeight - dy);

            PointF l_diag_pt1 = new PointF(
                position.X + CellWidth,
                position.Y + dy);
            PointF l_diag_pt2 = new PointF(
                position.X + dx,
                position.Y + CellHeight);

            PointF u_horz_pt1 = new PointF(
                position.X,
                position.Y + LedThickness + Gap);
            PointF u_horz_pt2 = new PointF(
                position.X + CellWidth,
                position.Y + LedThickness + Gap);

            PointF l_horz_pt1 = new PointF(
                position.X,
                position.Y + CellHeight / 2f - LedThickness / 2f - Gap);
            PointF l_horz_pt2 = new PointF(
                position.X + CellWidth,
                position.Y + CellHeight / 2f - LedThickness / 2f - Gap);

            PointF l_vert_pt1 = new PointF(
                position.X + CellWidth / 2f + LedThickness / 2f + Gap,
                position.Y);
            PointF l_vert_pt2 = new PointF(
                position.X + CellWidth / 2f + LedThickness / 2f + Gap,
                position.Y + CellHeight);

            PointF r_vert_pt1 = new PointF(
                position.X + CellWidth - LedThickness - Gap,
                position.Y);
            PointF r_vert_pt2 = new PointF(
                position.X + CellWidth - LedThickness - Gap,
                position.Y + CellHeight);

            PointF[][] segs =
            {
                new PointF[] { u_horz_pt1, u_horz_pt2, r_vert_pt1, r_vert_pt2 },
                new PointF[] { r_vert_pt1, r_vert_pt2, l_diag_pt1, l_diag_pt2 },
                new PointF[] { l_diag_pt1, l_diag_pt2, l_horz_pt1, l_horz_pt2 },
                new PointF[] { l_horz_pt1, l_horz_pt2, l_vert_pt1, l_vert_pt2 },
                new PointF[] { l_vert_pt1, l_vert_pt2, u_diag_pt1, u_diag_pt2 },
                new PointF[] { u_diag_pt1, u_diag_pt2, u_horz_pt1, u_horz_pt2 },
            };
            return MakeIntersectionLed(segs);
        }
        public PointF[] MakeLed9(PointF position)
        {
            float sqrt2 = (float)Math.Sqrt(2.0);
            float dx = LedThickness / sqrt2;
            float dy = dx;

            PointF u_diag_pt1 = new PointF(
                position.X,
                position.Y + CellHeight - dy);
            PointF u_diag_pt2 = new PointF(
                position.X + CellWidth - dx,
                position.Y);

            PointF l_diag_pt1 = new PointF(
                position.X + dx,
                position.Y + CellHeight);
            PointF l_diag_pt2 = new PointF(
                position.X + CellWidth,
                position.Y + dy);

            PointF u_horz_pt1 = new PointF(
                position.X,
                position.Y + CellHeight / 2f + LedThickness / 2f + Gap);
            PointF u_horz_pt2 = new PointF(
                position.X + CellWidth,
                position.Y + CellHeight / 2f + LedThickness / 2f + Gap);

            PointF l_horz_pt1 = new PointF(
                position.X,
                position.Y + CellHeight - LedThickness - Gap);
            PointF l_horz_pt2 = new PointF(
                position.X + CellWidth,
                position.Y + CellHeight - LedThickness - Gap);

            PointF l_vert_pt1 = new PointF(
                position.X + LedThickness + Gap,
                position.Y);
            PointF l_vert_pt2 = new PointF(
                position.X + LedThickness + Gap,
                position.Y + CellHeight);

            PointF r_vert_pt1 = new PointF(
                position.X + CellWidth / 2f - LedThickness / 2f - Gap,
                position.Y);
            PointF r_vert_pt2 = new PointF(
                position.X + CellWidth / 2f - LedThickness / 2f - Gap,
                position.Y + CellHeight);

            PointF[][] segs =
            {
                new PointF[] { u_horz_pt1, u_horz_pt2, r_vert_pt1, r_vert_pt2 },
                new PointF[] { r_vert_pt1, r_vert_pt2, l_diag_pt1, l_diag_pt2 },
                new PointF[] { l_diag_pt1, l_diag_pt2, l_horz_pt1, l_horz_pt2 },
                new PointF[] { l_horz_pt1, l_horz_pt2, l_vert_pt1, l_vert_pt2 },
                new PointF[] { l_vert_pt1, l_vert_pt2, u_diag_pt1, u_diag_pt2 },
                new PointF[] { u_diag_pt1, u_diag_pt2, u_horz_pt1, u_horz_pt2 },
            };
            return MakeIntersectionLed(segs);
        }
        public PointF[] MakeLed11(PointF position)
        {
            float sqrt2 = (float)Math.Sqrt(2.0);
            float dx = LedThickness / sqrt2;
            float dy = dx;

            PointF u_diag_pt1 = new PointF(
                position.X + dx,
                position.Y);
            PointF u_diag_pt2 = new PointF(
                position.X + CellWidth,
                position.Y + CellHeight - dy);

            PointF l_diag_pt1 = new PointF(
                position.X,
                position.Y + dy);
            PointF l_diag_pt2 = new PointF(
                position.X + CellWidth - dx,
                position.Y + CellHeight);

            PointF u_horz_pt1 = new PointF(
                position.X,
                position.Y + CellHeight / 2f + LedThickness / 2f + Gap);
            PointF u_horz_pt2 = new PointF(
                position.X + CellWidth,
                position.Y + CellHeight / 2f + LedThickness / 2f + Gap);

            PointF l_horz_pt1 = new PointF(
                position.X,
                position.Y + CellHeight - LedThickness - Gap);
            PointF l_horz_pt2 = new PointF(
                position.X + CellWidth,
                position.Y + CellHeight - LedThickness - Gap);

            PointF l_vert_pt1 = new PointF(
                position.X + CellWidth / 2f + LedThickness / 2f + Gap,
                position.Y);
            PointF l_vert_pt2 = new PointF(
                position.X + CellWidth / 2f + LedThickness / 2f + Gap,
                position.Y + CellHeight);

            PointF r_vert_pt1 = new PointF(
                position.X + CellWidth - LedThickness - Gap,
                position.Y);
            PointF r_vert_pt2 = new PointF(
                position.X + CellWidth - LedThickness - Gap,
                position.Y + CellHeight);

            PointF[][] segs =
            {
                new PointF[] { l_vert_pt1, l_vert_pt2, u_horz_pt1, u_horz_pt2 },
                new PointF[] { u_horz_pt1, u_horz_pt2, u_diag_pt1, u_diag_pt2 },
                new PointF[] { u_diag_pt1, u_diag_pt2, r_vert_pt1, r_vert_pt2 },
                new PointF[] { r_vert_pt1, r_vert_pt2, l_horz_pt1, l_horz_pt2 },
                new PointF[] { l_horz_pt1, l_horz_pt2, l_diag_pt1, l_diag_pt2 },
                new PointF[] { l_diag_pt1, l_diag_pt2, l_vert_pt1, l_vert_pt2 },
            };
            return MakeIntersectionLed(segs);
        }

        public PointF[] MakeIntersectionLed(PointF[][] segs)
        {
            List<PointF> points = new List<PointF>();

            foreach (PointF[] seg in segs)
            {
                PointF a1 = seg[0];
                PointF a2 = seg[1];
                PointF b1 = seg[2];
                PointF b2 = seg[3];
                bool lines_intersect, segs_intersect;
                PointF intersection, close_pt1, close_pt2;
                FindIntersection(a1, a2, b1, b2,
                    out lines_intersect, out segs_intersect,
                    out intersection, out close_pt1, out close_pt2);
                points.Add(intersection);
            }

            return points.ToArray();
        }

        // Draw a colon.
        public void DrawColon(Graphics gr,
            Brush bg_brush, Brush used_brush,
            Pen used_pen, Brush unused_brush,
            Pen unused_pen, PointF position)
        {
            // Clear the background.
            gr.FillRectangle(bg_brush,
                position.X, position.Y,
                LedThickness, CellHeight);

            float y1 = position.Y + CellHeight / 4f;
            float y2 = y1 + CellHeight / 2f;

            RectangleF rect1 = new RectangleF(
                position.X, y1 - LedThickness / 2f,
                LedThickness, LedThickness);
            gr.FillRectangle(used_brush, rect1);
            gr.DrawRectangle(used_pen, rect1);

            RectangleF rect2 = new RectangleF(
                position.X, y2 - LedThickness / 2f,
                LedThickness, LedThickness);
            gr.FillRectangle(used_brush, rect2);
            gr.DrawRectangle(used_pen, rect2);
        }

#endregion Led polygon functions

        // Make the polygons that represent a letter.
        public void MakeLetterPgons(char letter, PointF position,
            out List<PointF[]> used_pgons, out List<PointF[]> unused_pgons)
        {
            used_pgons = new List<PointF[]>();
            unused_pgons = new List<PointF[]>();

            bool[] used;
            if (LetterLeds.ContainsKey(letter)) used = LetterLeds[letter];
            else used = LetterLeds[(char)0];

            for (int i = 0; i < used.Length; i++)
            {
                if (used[i])
                    used_pgons.Add(LedFuncs[i](position));
                else
                    unused_pgons.Add(LedFuncs[i](position));
            }
        }

        // Draw a letter.
        public void DrawLetter(Graphics gr, Brush bg_brush,
            Brush used_brush, Pen used_pen,
            Brush unused_brush, Pen unused_pen,
            PointF position, char letter)
        {
            // Clear the background.
            gr.FillRectangle(bg_brush,
                position.X, position.Y,
                CellWidth, CellHeight);

            // Draw the polygons.
            List<PointF[]> used_pgons, unused_pgons;
            MakeLetterPgons(letter, position, out used_pgons, out unused_pgons);
            foreach (PointF[] pgon in unused_pgons)
            {
                gr.FillPolygon(unused_brush, pgon);
                gr.DrawPolygon(unused_pen, pgon);
            }
            foreach (PointF[] pgon in used_pgons)
            {
                gr.FillPolygon(used_brush, pgon);
                gr.DrawPolygon(used_pen, pgon);
            }
        }

        // Draw a sequence of letters.
        public void DrawText(Graphics gr, Brush bg_brush,
            Brush used_brush, Pen used_pen,
            Brush unused_brush, Pen unused_pen,
            PointF position, float h_spacing, string text)
        {
            float cell_space = CellWidth * (h_spacing - 1);
            foreach (char ch in text)
            {
                if (ch == ':')
                {
                    DrawColon(gr, bg_brush, used_brush, used_pen,
                        unused_brush, unused_pen, position);
                    position.X += LedThickness;
                }
                else
                {
                    DrawLetter(gr, bg_brush, used_brush, used_pen,
                        unused_brush, unused_pen, position, ch);
                    position.X += CellWidth;
                }
                position.X += cell_space;
            }
        }

        // Find the point of intersection between
        // the lines p1 --> p2 and p3 --> p4.
        private void FindIntersection(
            PointF p1, PointF p2, PointF p3, PointF p4,
            out bool lines_intersect, out bool segments_intersect,
            out PointF intersection,
            out PointF close_p1, out PointF close_p2)
        {
            // Get the segments' parameters.
            float dx12 = p2.X - p1.X;
            float dy12 = p2.Y - p1.Y;
            float dx34 = p4.X - p3.X;
            float dy34 = p4.Y - p3.Y;

            // Solve for t1 and t2
            float denominator = (dy12 * dx34 - dx12 * dy34);

            float t1 =
                ((p1.X - p3.X) * dy34 + (p3.Y - p1.Y) * dx34)
                    / denominator;
            if (float.IsInfinity(t1))
            {
                // The lines are parallel (or close enough to it).
                lines_intersect = false;
                segments_intersect = false;
                intersection = new PointF(float.NaN, float.NaN);
                close_p1 = new PointF(float.NaN, float.NaN);
                close_p2 = new PointF(float.NaN, float.NaN);
                return;
            }
            lines_intersect = true;

            float t2 =
                ((p3.X - p1.X) * dy12 + (p1.Y - p3.Y) * dx12)
                    / -denominator;

            // Find the point of intersection.
            intersection = new PointF(p1.X + dx12 * t1, p1.Y + dy12 * t1);

            // The segments intersect if t1 and t2 are between 0 and 1.
            segments_intersect =
                ((t1 >= 0) && (t1 <= 1) &&
                 (t2 >= 0) && (t2 <= 1));

            // Find the closest points on the segments.
            if (t1 < 0)
            {
                t1 = 0;
            }
            else if (t1 > 1)
            {
                t1 = 1;
            }

            if (t2 < 0)
            {
                t2 = 0;
            }
            else if (t2 > 1)
            {
                t2 = 1;
            }

            close_p1 = new PointF(p1.X + dx12 * t1, p1.Y + dy12 * t1);
            close_p2 = new PointF(p3.X + dx34 * t2, p3.Y + dy34 * t2);
        }
    }
}
