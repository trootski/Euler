object test {
  println("Welcome to the Scala worksheet")       //> Welcome to the Scala worksheet
  def isMutiple = (i:Int, op:Int) => (i % op) == 0//> isMutiple: => (Int, Int) => Boolean
  isMutiple(10, 5)                                //> res0: Boolean = true
  val l = ""                                      //> l  : String = ""
}