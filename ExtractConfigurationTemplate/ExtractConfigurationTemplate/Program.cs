using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ExtractConfigurationTemplate
{
    class Program
    {
        static void Main(string[] args)
        {
            string sourceDrawFilename = "DrawDev.py";

            if (args.Length > 0)
            {
                sourceDrawFilename = args[0];
            }

            if (!File.Exists(sourceDrawFilename))
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine(sourceDrawFilename + " not found. If the filename is different, pass it as argument.");
                Console.ResetColor();
                Console.ReadKey();
                return;
            }

            string[] lines = File.ReadAllLines(sourceDrawFilename);

            string startIndicator = "# Result logic START";
            string endIndicator = "# Result logic END";

            string result = "\"";

            bool startIndicatorNotFound = true;
            bool endIndicatorNotFound = true;

            int prefixCharCount = 0;

            bool isItFirstInterestingLine = true;

            foreach (var line in lines)
            {
                // Following sequence of logic is important

                if (line.Trim() == endIndicator)
                    endIndicatorNotFound = false;

                if (!startIndicatorNotFound && endIndicatorNotFound)
                {
                    if (isItFirstInterestingLine)
                    {
                        isItFirstInterestingLine = false;
                    }
                    else
                    {
                        result += "\\\\n";
                    }
                    result += line.Substring(prefixCharCount).Replace("\"", "\\\"");
                }

                if (line.Trim() == startIndicator)
                {
                    startIndicatorNotFound = false;
                    prefixCharCount = line.IndexOf(startIndicator);
                }
            }
            result += "\"";

            Console.ForegroundColor = ConsoleColor.Red;
            if (startIndicatorNotFound)
                Console.WriteLine("\"" + startIndicator + "\" was not found. It's needed to recognize start");

            if (endIndicatorNotFound)
                Console.WriteLine("\"" + endIndicator + "\" was not found. It's needed to recognize end");
            Console.ResetColor();

            if (!startIndicatorNotFound && !endIndicatorNotFound)
            {
                Console.WriteLine(result);
            }

            Console.ReadKey();
        }
    }
}
