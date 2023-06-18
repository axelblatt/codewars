fun evaporator(content: Double, evap_per_day: Double, threshold: Double): Int { 
    val m: Double = content * threshold / 100
    var d = 0
    var content_ = content
    while (content_ > m) {
        content_ -= content_ * evap_per_day / 100
        d += 1
    }
    
    return d
}