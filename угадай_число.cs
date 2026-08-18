using System;
using System.ComponentModel.Design;
public class Animal
{
    private string token = "secret";
    protected string animal;

    public void An(string animalName)
    {
        animal = animalName;
    }
}
class Cat : Animal
{
    public void Meaw(string name = "нету", int age = 0, int speed = 0, int strong = 0)
    {
        Console.WriteLine(
            $"{animal} {name} ему {age}\n" +
            $"скорость: {speed}\n" +
            $"сила: {strong}"
        );
    }
}
public class pro
{
    public static void Main()
    {
        System.Random random = new System.Random();
        int number = random.Next(1, 10);
        int heath = 3;
        while (heath > 0)
        {
            try
            {
                Console.Write("угадай число:");
                int rnd = int.Parse(Console.ReadLine());
                if (rnd < 0 || rnd > 10)
                {
                    Console.WriteLine("только 1 до 10");
                    continue;
                }
                else if (rnd == number)
                {
                    Console.WriteLine("победа");
                    break;
                }
                else if (rnd > number)
                {
                    Console.WriteLine("меньше");
                }
                else
                {
                    Console.WriteLine("больше");
                }
                cat cat1 = new cat();
                cat1.meaw("багира", 3, 35, 12);
                heath -= 1;
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