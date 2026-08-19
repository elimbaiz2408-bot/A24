using System;
using System.ComponentModel.Design;
class programming
{
    public static void Main()
    {
        System.Random random = new System.Random();
        int heath = 3;
        int number = random.Next(1, 10);
        string op = null;
        Console.WriteLine("|Легкий|Средний|Сложный|");
        while (true)
        {
            try
            {
                Console.Write("Выбор:");
                op = Console.ReadLine().ToLower();
                if (op == "легкий")
                {
                }
                else if (op == "средний")
                {

                    number = random.Next(1, 40);
                }
                else if (op == "сложный")
                {
                    number = random.Next(1, 100);
                }
                else
                {
                    Console.WriteLine("только:\n|Легкий|Средний|Сложный|");
                    continue;
                }
            }
            catch (Exception)
            {
                Console.WriteLine("только буквы");
                continue;
            }
            break;
        }
        while (heath > 0)
        {
            try
            {
                Console.Write("угадай число:");
                int rnd = int.Parse(Console.ReadLine());
                if (op == "легко")
                {
                    if (rnd < 0 || rnd > 10)
                    {
                        Console.WriteLine("только 1 до 10");
                        continue;
                    }
                }
                else if (op == "средний")
                {
                    if (rnd < 0 || rnd > 40)
                    {
                        Console.WriteLine("только 1 до 10");
                        continue;
                    }
                }
                else
                {
                    if (rnd < 0 || rnd > 100)
                    {
                        Console.WriteLine("только 1 до 10");
                        continue;
                    }
                }
                if (rnd == number)
                {
                    Console.WriteLine("--- победа ---");
                    break;
                }
                else if (rnd > number)
                {
                    Console.WriteLine("--- меньше ---");
                }
                else
                {
                    Console.WriteLine("--- больше ---");
                }
                heath -= 1;
                if (heath <= 2)
                {
                    Console.WriteLine($"Осталось попыток: {heath}");
                }
                continue;
            }
            catch (Exception)
            {
                Console.WriteLine("только цифры");
                continue;
            }
        }
    }
}