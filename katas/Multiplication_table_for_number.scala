// Kata Multiplication table for number IRL:https://www.codewars.com/kata/5a2fd38b55519ed98f0000ce/scala

def multiTable(n: Int): String = {

  var tabla = ""
  for
    i <- 1 to 10
  do
    if i == 10 then
      tabla += s"$i * $n = " + i * n
    else
      tabla += s"$i * $n = " + i * n + "\n"
  return tabla
}