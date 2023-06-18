import java.math.BigInteger;
fun lastDigit(base: BigInteger, exponent: BigInteger): Int {
    val _0 = BigInteger("0")
    val _4 = BigInteger("4")
    val _10 = BigInteger("10")
    
    if (exponent == _0) return 1
    val md = exponent.mod(_4).toInt()
    val _1o = base.mod(_10).toInt()
    
    if (md == 1) return base.mod(_10).toInt()
    if (md == 2) return base.pow(2).mod(_10).toInt()
    if (md == 3) return base.pow(3).mod(_10).toInt()
    if (md == 0) {
        if (_1o == 5) return 5
        if (_1o == 6) return 6
        if (_1o == 0) return 0
        if (base.mod(BigInteger("2")).toInt() != 0) return 1
        else return 6
    }
    
    
    return 0
}