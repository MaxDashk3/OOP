using static System.Math;

namespace Lab_1
{
    internal class Vector
    {
        // ----------- static variable ---------
        static int count = 0;

        // ------------ variable -------------
        float[] vector;

        // --------- encapsulation ------------
        float[] start;
        public float[] Start
        {
            get => start;
            set
            {
                Check(end, value);
                start = value;
                UpdateVector();
            }
        }

        float[] end;
        public float[] End
        {
            get => start;
            set
            {
                Check(start, value);
                end = value;
                UpdateVector();
            }
        }

        //---------- static methods -----------
        static bool Check(float[] start, float[] end)
        {
            if (start[0] == end[0] && start[1] == end[1])
                throw new ArgumentException("Vector's length can't be 0");
            return true;
        }

        static public int GetCount() => count;

        //----------- operator methods ----------
        public static float operator *(Vector v1, Vector v2)
        {
            var a = v1.vector;
            var b = v2.vector;
            return a[0] * b[0] + a[1] * b[1];
        }
        public static Vector operator +(Vector v1, Vector v2)
        {
            var a = v1.end[0] + v2.vector[0];
            var b = v1.end[1] + v2.vector[1];
            float[] end = [a, b];
            return new Vector(v1.start, end);
        }
        public static Vector operator -(Vector v1, Vector v2)
        {
            var a = v1.end[0] - v2.vector[0];
            var b = v1.end[1] - v2.vector[1];
            float[] end = [a, b];
            return new Vector(v1.start, end);
        }


        //---------- other methods ----------
        void UpdateVector()
        {
            float a = end[0] - start[0];
            float b = end[1] - start[1];
            vector = [a, b];            
        }

        public float[] GetVector() => vector;
        public Vector MultiplyByNumber(float num)
        {
            float[] vector_by_num = [vector[0] * num, vector[1] * num];
            float a = start[0] + vector_by_num[0];
            float b = start[1] + vector_by_num[1];
            return new Vector(start, [a, b]);
        }

        public float GetLength()
        {
            return (float) Sqrt(Pow(vector[0], 2) + Pow(vector[1],2));
        }
        
        // ----------- constructor --------------
        public Vector(float[] start, float[] end)
        {
            Check(start, end);
            this.start = start;
            this.end = end;
            UpdateVector();
            count++;
        }
        // ---------- destructor ---------------
        ~Vector()
        {
            count-=1;
        }

        // ------------ to string -------------
        public override string? ToString()
        {
            return $"->[({start[0]}; {start[1]}), ({end[0]}; {end[1]})]";
        }
    }
}
