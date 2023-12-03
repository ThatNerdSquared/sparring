import 'dart:io';
import 'dart:math';

void main() {
  final inputFile = File('./day3.input');
  final rawInput = inputFile.readAsLinesSync();
  final List<int> partNumbers = [];
  for (final entry in rawInput.asMap().entries) {
    final index = entry.key;
    final line = entry.value.trim();

    final numberMatcher = RegExp(r'[0-9]*');
    final matches = numberMatcher
        .allMatches(line)
        .where((e) => e[0]!.trim().isNotEmpty)
        .map((e) => (int.parse(e[0]!), e.start, e.end));
    for (final match in matches) {
      checkSurroundings((match.$2, match.$3), index, rawInput)
          ? partNumbers.add(match.$1)
          : null;
    }
  }
  print(partNumbers.fold<int>(
    0,
    (previousValue, element) {
      return previousValue + element;
    },
  ));
}

bool checkSurroundings((int, int) match, int lineNum, List<String> input) {
  final matchStart = match.$1;
  final matchEnd = match.$2;
  final currentLine = input[lineNum];
  const dot = '.';
  final notDot = RegExp(r'[^.]');
  return (falseIfRangeErr(() => currentLine[matchStart - 1] != dot) ||
      falseIfRangeErr(() => currentLine[matchEnd] != dot) ||
      falseIfRangeErr(() => notDot
          .allMatches(input[lineNum - 1].substring(
            max(matchStart - 1, 0),
            min(matchEnd + 1, currentLine.length),
          ))
          .isNotEmpty) ||
      falseIfRangeErr(() => notDot
          .allMatches(input[lineNum + 1].substring(
            max(matchStart - 1, 0),
            min(matchEnd + 1, currentLine.length),
          ))
          .isNotEmpty));
}

bool falseIfRangeErr(bool Function() op) {
  try {
    return op();
  } on RangeError {
    return false;
  }
}
