// given problem code
public class Task {
    private String courseName;
    private int hours;

    public Task(String className, int neededHours) {
        courseName = className;
        hours = neededHours;
    }

    public int getHours() {
        return hours;
    }
}