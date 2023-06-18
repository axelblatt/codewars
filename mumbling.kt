package accum

fun accum(s:String):String {
    var res: String = ""
    
    for (i: Int in 0..s.length - 1) {
        for (j: Int in 0..i) {
            if (j == 0) res += s[i].uppercase()
            else res += s[i].lowercase()
        }
        res += "-"
    }
    
    return res.dropLast(1)
}