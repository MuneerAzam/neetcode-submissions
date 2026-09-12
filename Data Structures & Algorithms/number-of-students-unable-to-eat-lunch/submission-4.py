class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        ones = students.count(1)
        zeros = students.count(0)
        for sandwich in sandwiches:
            if sandwich == 1:
                if ones == 0:
                    return zeros
                ones -= 1
            else:
                if zeros == 0:
                    return ones
                zeros -= 1
        return 0