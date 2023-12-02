import 'dart:io';

const BAGVALS = {
  'red': 12,
  'green': 13,
  'blue': 14,
};

void main() {
  final inputFile = File('./day2.input');
  final rawInput = inputFile.readAsLinesSync();
  final List<int> validIDs = [];
  gameloop:
  for (final game in rawInput) {
    final parts = game.split(':');
    final id = int.parse(parts.first.split(' ').last);
    final subsets = parts.last.trim().split('; ');
    for (final subset in subsets) {
      final colourSets = subset.split(', ');
      for (final colourSet in colourSets) {
        final csParts = colourSet.split(' ');
        if (!(BAGVALS[csParts.last]! >= int.parse(csParts.first))) {
          continue gameloop;
        }
      }
    }
    validIDs.add(id);
  }
  print(validIDs.fold<int>(
    0,
    (previousValue, element) {
      return previousValue + element;
    },
  ));
}
