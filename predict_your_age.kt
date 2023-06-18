fun predictAge(age1: Int, age2: Int, age3: Int, age4: Int, age5: Int, age6: Int, age7: Int, age8: Int): Int {
  val m: List<Int> = listOf(age1, age2, age3, age4, age5, age6, age7, age8)
  var r: Double = 0.0
  for (i in m) r += Math.pow(i.toDouble(), 2.0)
  return (Math.sqrt(r) / 2.0).toInt()
}