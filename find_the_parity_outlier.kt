fun find(integers: Array<Int>): Int {
    var c = 0
    for (i: Int in integers) if (i % 2 == 0) c += 1
    if (c > 1) for (i: Int in integers) if (i % 2 != 0) return i
    for (i: Int in integers) if (i % 2 == 0) return i
    return 0
}