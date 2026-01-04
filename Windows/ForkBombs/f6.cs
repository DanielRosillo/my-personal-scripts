using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

namespace Rextester
{
    public class Program
    {
        public static void Main(string[] args)
        {
            fork();
        }
        public static void fork()
        {
            while(true){
                fork(); 
            }
        }
    }
}