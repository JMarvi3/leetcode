SELECT MAX(penult.salary) AS SecondHighestSalary FROM Employee AS penult JOIN Employee AS ultimate ON penult.salary < ultimate.salary;