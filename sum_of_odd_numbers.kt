fun rowSumOddNumbers(n: Int): Int {
    var x: Int = 1;
    var y: Int = 0;

    for (i: Int in 1..n) {
        for (j: Int in 1..i) {

            if (i == n) {
                y += x;
                println(x);
            }
            x += 2;

        }
    }

    return y;

}