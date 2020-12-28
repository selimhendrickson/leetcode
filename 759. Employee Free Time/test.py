
import unittest
from employee_free_time import Solution, Interval

class TestDriver(unittest.TestCase):

    def build_interval_list(self, input):
        interval_list = []

        for sublist in input:
            interval_sub_list = []
            for val in sublist:
                interval_sub_list.append(Interval(val[0], val[1]))
            interval_list.append(interval_sub_list)        

        return interval_list

    def build_output_list(self, output_interval_list):
        output = []

        for interval in output_interval_list:
            output.append([interval.start, interval.end])
        
        return output
        
    def test_sample_1(self):
        input = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
        expected = [[3,4]]

        input_interval_list = self.build_interval_list(input)
        output_interval_list = Solution().employeeFreeTime(input_interval_list)
        output = self.build_output_list(output_interval_list)

        self.assertEqual(output, expected)

    def test_sample_22(self):
        input = [[[7,24],[29,33],[45,57],[66,69],[94,99]],[[6,24],[43,49],[56,59],[61,75],[80,81]],[[5,16],[18,26],[33,36],[39,57],[65,74]],[[9,16],[27,35],[40,55],[68,71],[78,81]],[[0,25],[29,31],[40,47],[57,87],[91,94]]]
        expected = [[26,27],[36,39],[87,91]]

        input_interval_list = self.build_interval_list(input)
        output_interval_list = Solution().employeeFreeTime(input_interval_list)
        output = self.build_output_list(output_interval_list)

        self.assertEqual(output, expected)

if __name__ == "__main__":
    unittest.main()