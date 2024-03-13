/*
string[] fraudulentOrderIds = new string[3];

fraudulentOrderIds[0] = "A123";
fraudulentOrderIds[1] = "B345";
fraudulentOrderIds[2] = "C222";
//fraudulentOrderIds[3] = "D678";
*/

string[] fraudulentOrderIds = { "A123", "B345", "C222" };

Console.WriteLine($"First: {fraudulentOrderIds[0]}");
Console.WriteLine($"Second: {fraudulentOrderIds[1]}");
Console.WriteLine($"Third: {fraudulentOrderIds[2]}");

fraudulentOrderIds[0] = "F000";

Console.WriteLine($"Reassigned First: {fraudulentOrderIds[0]}");

Console.WriteLine($"There are {fraudulentOrderIds.Length} fraudulent cards to process.");