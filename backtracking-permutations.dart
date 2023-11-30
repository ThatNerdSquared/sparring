const List<int> allnums = [1, 2, 3];

List<int> allPossibleNums(List<int> current) {
  return allnums.where((element) => !current.contains(element)).toList();
}

List<int> fnForList(List<int> nums, List<int> res) {
  if (nums.isEmpty) {
    return res;
  } else {
    return fnForInt(nums.first, res);
  }
}

List<int> fnForInt(int num, List<int> res) {
  res.add(num);
  return fnForList(allPossibleNums(res), res);
}

List<List<int>> gen_permutes(List<int> allnums) {
  if (allnums.isEmpty) {
    return [];
  } else {
    return [
      fnForInt(allnums.first, []),
      ...gen_permutes(allnums.sublist(1)),
    ];
  }
}

void main() {
  print(gen_permutes(allnums));
}
