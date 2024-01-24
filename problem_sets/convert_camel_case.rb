# Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"

# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"

# "The_Stealth-Warrior" gets converted to "TheStealthWarrior"

def to_camel_case(str)
  words = str.split(/[-_]/)
  words.map do |word|
    if word == words[0]
      word
    else
      word.capitalize
    end
  end.join("")
end

puts to_camel_case("the-stealth-warrior")
to_camel_case("The_Stealth_Warrior")
to_camel_case("The_Stealth-Warrior")
