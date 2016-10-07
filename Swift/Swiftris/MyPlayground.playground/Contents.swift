let numberSymbol = "Three"

var possibleIntegerValue: Int?

switch numberSymbol {
    case "1", "one":
    possibleIntegerValue = 1
    case "2", "two":
    possibleIntegerValue = 2
    case "3", "Three":
    possibleIntegerValue = 3
    case "4", "four":
    possibleIntegerValue = 4
default:
    break
}

if let integerValue = possibleIntegerValue {
    print("The integer value of \(numberSymbol) is \(integerValue).")
}