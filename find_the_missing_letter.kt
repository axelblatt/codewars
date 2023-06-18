fun findMissingLetter(array: CharArray): Char {
    
    var str: ByteArray = String(array).toByteArray()
    
    for (i: Int in str.first()..str.last()) {
        if (i.toByte() !in str) {
            return i.toChar()
        }
    }
    
    return ' '
}