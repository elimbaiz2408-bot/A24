using System;
class Programing
{
    static void Main()
    {
        Dictionary<string, int> math = new Dictionary<string, int>();
        math["2+4="] = 6;
        math["5*8="] = 40;
        math["20*34="] = 748;
        math["54*13="] = 702;
        while (true)
        {
            try
            {
                Console.Write("Салам как тебя зовут: ");
                string name = Console.ReadLine();
                if (string.IsNullOrEmpty(name))
                {
                    Console.WriteLine("пусто");
                    continue;
                }
                Console.WriteLine($"тебя зовут {name}");
            }

            catch (Exception)
            {
                Console.WriteLine("только буквы");
                continue;
            }

            try
            {
                Console.Write("Сколько тебе лет: ");
                int age = int.Parse(Console.ReadLine());
                Console.WriteLine($"тебе {age}");
            }

            catch (Exception)
            {
                Console.WriteLine("только цифры");
                continue;
            }
            try
            {
                foreach (var item in math)
                {
                    Console.Write(item.Key);
                    int user_op = int.Parse(Console.ReadLine());
                    if (user_op == item.Value)
                    {
                        Console.WriteLine("Правильно");
                    }
                    else
                    {
                        Console.WriteLine("Неверно");
                    }
                }
            }
            catch (Exception)
            {
                Console.WriteLine("Ошибка");
            }
        }
    }
}