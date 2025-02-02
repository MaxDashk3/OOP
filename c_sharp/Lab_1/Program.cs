namespace Lab_1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            var v1 = new Vector([1, 2], [10, 3]);
            var v2 = new Vector([1, 0], [1, 16]);
            var v3 = v1 + v2;
            Console.WriteLine(v1.GetLength()+v2.GetLength());
            Console.WriteLine(v3.GetLength());

        }
    }
}
