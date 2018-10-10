object problem_2 {
  def main(args:Array[String]) {
    def isDivisibleBy = (v: Int) => ((v % 3) == 0 || (v % 5) == 0)
    println((1 to 999).filter(isDivisibleBy).reduceLeft(_+_))
  }
}
