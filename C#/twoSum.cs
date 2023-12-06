using System;

class Program
{
    static void Main()
    {
        // Exemplo de uso da função twoSum
        int[] nums = { 2, 7, 11, 15 };
        int target = 18;

        // Chama a função e armazena o resultado em uma variável
        int[] result = TwoSum(nums, target);

        // Exibe o resultado no console
        Console.WriteLine($"[{result[0]}, {result[1]}]");
    }

    static int[] TwoSum(int[] nums, int target)
    {
        int size = nums.Length;
        bool found = false;
        int x1 = 0;
        int x2 = 0;

        for (int i = 0; i < size; i++)
        {
            for (int j = i + 1; j < size; j++)
            {
                if (nums[i] + nums[j] == target)
                {
                    x1 = i;
                    x2 = j;
                    found = true;
                }
                if (found)
                {
                    break;
                }
            }
            if (found)
            {
                break;
            }
        }

        return new int[] { x1, x2 };
    }
}
