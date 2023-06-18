fun duplicateCount(text: String): Int {
    var t = text.lowercase()
    var c = 0
   	var co: Int
    for (i in t.split("").distinct()) {
        co = t.length
    	t = t.replace(i, "")
        if (co - t.length > 1) c += 1
    }
    return c
}