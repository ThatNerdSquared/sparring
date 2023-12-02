import 'dart:io';

void main() {
  final inputFile = File('./day1.input');
  final rawInput = inputFile.readAsLinesSync();
  final numRegex = RegExp(r'[0-9]');
  final newInput = rawInput.map((line) => int.parse(
        numRegex.firstMatch(line)![0].toString() +
            numRegex.allMatches(line).last[0].toString(),
      ));
  print(newInput.fold<int>(
    0,
    (previousValue, element) {
      return previousValue + element;
    },
  ));
}
