# compile the problem code
javac Homework.java Task.java
# compile the test
javac -cp .:junit-4.13.2.jar:hamcrest-core-1.3.jar HomeworkTest.java
# run the test
java -cp .:junit-4.13.2.jar:hamcrest-core-1.3.jar org.junit.runner.JUnitCore HomeworkTest