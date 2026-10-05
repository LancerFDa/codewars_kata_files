// Kata Create Phone Number IRL: https://www.codewars.com/kata/525f50e3b73515a6db000b83/scala

def createPhoneNumber(n: Seq[Int]): String = { 
    var phoneNumber = ""
    var firstDigits = n.slice(0, 3).mkString("")
    var secondDigits = n.slice(3, 6).mkString("")
    var thirdDigits = n.slice(6, 10).mkString("")
    phoneNumber = s"(${firstDigits}) ${secondDigits}-${thirdDigits}"
    return phoneNumber
  }

// slice es usado para tomar un rango de elementos de una lista
// mkString("") es usado comunmente para pasar listas a strings