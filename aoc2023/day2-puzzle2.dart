import 'dart:io';

void main() {
  final inputFile = File('./day2.input');
  final rawInput = inputFile.readAsLinesSync();
  final List<int> setPowers = [];
  for (final game in rawInput) {
    final parts = game.split(':');
    final subsets = parts.last.trim().split('; ');
    final mins = {
      'red': 0,
      'green': 0,
      'blue': 0,
    };
    for (final subset in subsets) {
      final colourSets = subset.split(', ');
      for (final colourSet in colourSets) {
        final csParts = colourSet.split(' ');
        if (mins[csParts.last]! < int.parse(csParts.first)) {
          mins[csParts.last] = int.parse(csParts.first);
        }
      }
    }
    setPowers.add(mins.values.reduce((value, element) => value * element));
  }
  print(setPowers.fold<int>(
    0,
    (previousValue, element) {
      return previousValue + element;
    },
  ));
}
