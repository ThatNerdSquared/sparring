import java.util.*;

// given problem code
public class Homework {
    private List<Task> tasks;

    public Homework() {
    }

    public List<String> workOnTasks(int hours) {
        return null; //stub
    }

    public int hoursToGo() {
        /*
        return 0; //stub
        */

        // problem #3: implement this method
        int result = 0;
        for (Task t: tasks) {
            result += t.getHours();
        }
        return result;
    }

    public void addTask(String className, int neededHours) {
        // problem #3: implement this method
        tasks.add(new Task(className, neededHours));
    }
}