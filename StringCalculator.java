public class StringCalculator {
	
	static char separator = ',';
	static char customSep = ';';
	
	int add(String s) throws Exception {
		
		int res = 0;
		int start = 0, finish = s.length();
		boolean custom = false;
		String tmp = "";
		
		if(s.charAt(0)=='/') {
			customSep = s.charAt(2);
			start = 4;
			custom = true;
		}
		
		for(int i=start; i<finish; i++) {
			if(isNumber(s.charAt(i))) {
				tmp = tmp + s.charAt(i);
			} else {
				if(isSeparator(s.charAt(i), custom)) {
					res += Integer.parseInt(tmp);
					tmp = "";
				} else {
					if(s.charAt(i)=='-') System.out.println("Runtime Exception");
					else System.out.println("Separator ERROR");
				}
			}
		}
		res += Integer.parseInt(tmp);
		
		return res;
	}
	
	boolean isNumber(char c) {
		return '0'<=c && c<='9';
	}
	
	boolean isSeparator(char c, boolean custom) {
		if(custom) return c==customSep;
		else return (c==separator || c== customSep);
	}
}