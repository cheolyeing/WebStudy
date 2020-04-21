import static org.junit.Assert.*;

import org.junit.Test;
import org.junit.*;

public class CalculatorTest {

	private Calculator cal;
		
		@Before
		public void setUp() throws Exception {
			cal = new Calculator();
			System.out.println("Set Up!");
		}
		
		@Test
		public void testAdd() throws Exception {
			int result = cal.add(1, 2);
			assertEquals(3, result);
		}
	
		@Test
		public void testSub() {
			int result = cal.sub(1, 2);
			assertEquals(-1, result);
		}
		
		@Test
		public void testMul() {
			int result = cal.mul(2, 3);
			assertEquals(6, result);
		}
		
		@Test
		public void testDiv() {
			int result = cal.div(6, 2);
			assertEquals(3, result);
		}
		
		@After
		public void teardown() {
			System.out.println("teardown");
		}
}