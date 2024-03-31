#WAP to calculate the mean, variance and std. deviation of given list of numbers
import statistics

my_list = [10, 20, 30, 40, 50]

mean = statistics.mean(my_list)
variance = statistics.variance(my_list)
std_dev = statistics.stdev(my_list)

print("Mean:", mean)
print("Variance:", variance)
print("Standard Deviation:", std_dev)