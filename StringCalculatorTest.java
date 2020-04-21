import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class StringCalculatorTest {

	@Test
	public void testadd() throws Exception {
		StringCalculator scal = new StringCalculator();
		int res = scal.add("//;\n1;2;3");
		assertEquals(6, res);
	}
}
