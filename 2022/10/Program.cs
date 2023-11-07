using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;

namespace Day10
{
    class Program
    {
        static public readonly bool DebugLog = false;
        static readonly string inputPath = Directory.GetCurrentDirectory().Replace("Day10/bin/Debug/netcoreapp3.1", "") + "/Input.txt"; //The directory of your input text file, create an Input.txt at your "System.AppContext.BaseDirectory" folder
        static bool[,] CRT = new bool[40, 6];
        static void Main()
        {
            string Input = File.ReadAllText(inputPath);
            List<int> phase = new List<int> { };
            int currentValue = 1;
            int currentPhase = 0;
            string[] lines = Input.Split("\n");

            int i = -1;
            foreach (string line in lines)
            {
                if (DebugLog) Debug.Write("Function: \"" + line + "\"");

                if (line == "noop")
                {
                    i++;
                    currentPhase++;
                    phase.Add(currentValue);
                    if (DebugLog) Debug.WriteLine(" Val: " + currentValue + " Phase: " + currentPhase);
                    DrawAndSaveCurrentLine(currentValue, i);

                }
                if (line.Contains("addx"))
                {
                    i++;
                    currentPhase++;
                    phase.Add(currentValue);
                    if (DebugLog) Debug.WriteLine(" Val: " + currentValue + " Phase: " + currentPhase);
                    DrawAndSaveCurrentLine(currentValue, i);

                    i++;
                    currentPhase++;
                    phase.Add(currentValue);
                    //Debug.WriteLine("Val: " + currentValue + " Phase: " + currentPhase);
                    DrawAndSaveCurrentLine(currentValue, i);

                    int inBy = int.Parse(line.Split(" ")[1]);
                    currentValue += inBy;
                }
                //Debug.WriteLine("");

            }


            Console.WriteLine(
                "A: " +
                (
                phase[19] * 20 +
                phase[59] * 60 +
                phase[99] * 100 +
                phase[139] * 140 +
                phase[179] * 180 +
                phase[219] * 220
                )
            );


            Console.WriteLine("B:");

            //Draws the screen
            for (int y = 0; y < 6; y++)
            {
                ConsoleColor originalBackgroundColor = Console.BackgroundColor;
                ConsoleColor originalForegroundColor = Console.ForegroundColor;
                for (int x = 0; x < 40; x++)
                {
                    Console.BackgroundColor = ConsoleColor.Black;
                    Console.ForegroundColor = ConsoleColor.White;
                    if (CRT[x, y])
                    {
                        Console.Write('█');
                    }
                    else
                    {
                        Console.Write(' ');
                    }
                }
                Console.BackgroundColor = originalBackgroundColor;
                Console.ForegroundColor = originalForegroundColor;
                Console.WriteLine("");
            }


            //Debug.WriteLine(currentValue);
        }
        static void DrawAndSaveCurrentLine(int x, int CRTI)
        {
            int cX = CRTI % 40;
            int cY = CRTI / 40 % 6;
            if (DebugLog) Console.WriteLine(cX + "," + cY);
            if (Math.Abs(x - cX) <= 1)
            {
                CRT[cX, cY] = true;
            }
            else
            {
                CRT[cX, cY] = false;
            }

            if (DebugLog)
            {
                Debug.Write("CRT Line:     ");
                for (int a = 0; a < 40; a++)
                {
                    if (CRT[a, cY])
                    {
                        Debug.Write("X");
                    }
                    else
                    {
                        Debug.Write(".");
                    }
                }
                if (DebugLog) Debug.WriteLine("");
                Debug.Write("Current Line: ");
                for (int a = 0; a < 40; a++)
                {
                    if (Math.Abs(a - x) <= 1)
                    {
                        Debug.Write("X");
                    }
                    else
                    {
                        Debug.Write(".");
                    }
                }
                Debug.WriteLine("");
            }
        }
    }
}
