// not sure if these imports are correct, but they
// did say to assume that everything required has been
// imported so....
import java.util.*;
import static org.junit.Assert.assertEquals;
import org.junit.Test;


public class HomeworkTest {

    // problem #1: test workOnTasks when no tasks have been added
    @Test
    public void testWorkOnTasksWhenNoTasksAdded() {
        Homework hw = new Homework();
        List<String> item = hw.workOnTasks(43);
        assertEquals(item.isEmpty(), true);
        /*
        could also be `assertTrue(item.isEmpty())`
        could also be `assertEquals(new ArrayList<String>(), item)
        could also be `assertEquals(0, item.size())`

        we could also check for:
        assertEquals(0, h.hoursToGo())
        assertEquals(0, h.numTasksRemaining())
        */
    }

    // problem #2: test workOnTasks when 3 tasks has been added, after
    // working one task should be complete, one partial, one not worked on
    // TODO: complete this
    @Test
    public void checkCorrectThreeTaskConfig() {
        Homework hw = new Homework();
        hw.addTask(new String("shouldBeComplete"), 42);
        // assertEquals(item.)
    }
}