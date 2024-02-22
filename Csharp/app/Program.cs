using System;

class Kalkulator
{
    static void Main()
    {
        Console.WriteLine("Enkel Kalkulator");

        // Input av to heltall
        Console.Write("Skriv inn det første heltallet: ");
        int num1 = Convert.ToInt32(Console.ReadLine());

        Console.Write("Skriv inn det andre heltallet: ");
        int num2 = Convert.ToInt32(Console.ReadLine());

        // Meny for matematiske operasjoner
        Console.WriteLine("\nVelg en operasjon:");
        Console.WriteLine("1. Addisjon");
        Console.WriteLine("2. Subtraksjon");
        Console.WriteLine("3. Multiplikasjon");
        Console.WriteLine("4. Divisjon");

        Console.Write("\nSkriv inn nummeret for ønsket operasjon: ");
        int valg = Convert.ToInt32(Console.ReadLine());

        // Utfør valgt operasjon
        switch (valg)
        {
            case 1:
                Console.WriteLine($"{num1} + {num2} = {num1 + num2}");
                break;
            case 2:
                Console.WriteLine($"{num1} - {num2} = {num1 - num2}");
                break;
            case 3:
                Console.WriteLine($"{num1} * {num2} = {num1 * num2}");
                break;
            case 4:
                if (num2 != 0)
                    Console.WriteLine($"{num1} / {num2} = {num1 / (double)num2}");
                else
                    Console.WriteLine("Kan ikke dele på 0.");
                break;
            default:
                Console.WriteLine("Ugyldig valg av operasjon.");
                break;
        }

        Console.ReadLine();
    }
}
