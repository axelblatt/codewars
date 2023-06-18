fun maxMultiple(d: Int, b: Int): Int {
    var x: Int = 1
    for (i: Int in d..b) {
        if (i % d == 0 && i >= x) {
            x = i
        }
    }
    return x
}