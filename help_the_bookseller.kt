package solution

object StockList {
    fun stockSummary(lstOfArt: Array<String>, lstOfCat: Array<String>): String {
        var res: String = ""
        var temp: Int
        if (lstOfArt.size == 0) return ""
        for (i: String in lstOfCat) {
            
        	temp = 0
            for (j: String in lstOfArt)
                if (j[0] == i[0]) {
                    for (k: Int in 0..j.length - 1) if (j[k] == ' ')
                    temp += j.takeLast(j.length - k - 1).toInt() 
                }
            res += "(" + i + " : " + temp.toString() + ") - "
        }
        
        return res.dropLast(3)
    }
}