import 'dart:io';

final numsAsWords = {
  'one': '1',
  'two': '2',
  'three': '3',
  'four': '4',
  'five': '5',
  'six': '6',
  'seven': '7',
  'eight': '8',
  'nine': '9',
};

void main() {
  final inputFile = File('./day1.input');
  final rawInput = inputFile.readAsLinesSync();
  final newInput = rawInput.map(parseCalibrationFromLine);
  print(newInput.fold<int>(
    0,
    (previousValue, element) {
      return previousValue + element;
    },
  ));
}

int parseCalibrationFromLine(String line) {
  final detectedDigits = [];
  for (var i = 0; i < line.length; i++) {
    if (int.tryParse(line[i]) != null) {
      detectedDigits.add(line[i]);
      continue;
    }
    for (var word in numsAsWords.keys) {
      try {
        if (line.substring(i, i + word.length) == word) {
          detectedDigits.add(numsAsWords[word]);
          continue;
        }
      } on RangeError {
        continue;
      }
    }
  }
  return int.parse(detectedDigits.first + detectedDigits.last);
}
