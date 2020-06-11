import java.io.IOException;

import java.util.*;
import org.jsoup.*;
import org.jsoup.nodes.*;

public class Crawling {
	
	// counting 하게 될 키워드 입니다.
	private final static String keyWord = "사랑";
	
	// 지니의 곡 상세정보 페이지는 아래 lyricsUrl과 같고, 마지막 부분 songInfo?xgnm= 뒤에 해당 곡의 ID가 들어가게 됩니다.
	private final static String lyricsUrl = "https://www.genie.co.kr/detail/songInfo?xgnm=";
	
	// 아래 ArrayList songId는 곡들의 ID를 담아올 자료구조입니다.
	static String[] songId = {"90351399", "90351400", "90351401", "90313511", "90178428", "90329116", "90021550", "90250302", "90155964", "90278892", "90155965", "89520901", "90182881", "90341412", "90001474", "89943155", "89320910", "90208247", "90341709", "89815269", "89776757", "89671631", "90069478", "90161044", "89374289", "90253075", "89290354", "90271276", "89613039", "90109509", "87928158", "90031687", "89558702", "89492238", "90173969", "90257120", "89952547", "90259405", "90098776", "90341734", "89058209", "89744994", "89830405", "90077755", "90367852", "89859975", "89883242", "89382909", "88773173", "89671935"};
	 
	// 아래 ArrayList lyrics에는 각 곡들의 가사가 들어가게 됩니다.
	public static ArrayList<String> lyrics = new ArrayList<String>();
	
	// 아래 Integer Array에는 각 페이지마다의 키워드 출력 횟수가 저장됩니다.
	static int[] numOfKeyWord = new int[40];
	
	public static void main(String[] args) throws IOException {
		System.out.println("<크롤링 시작>");
		multiThreading();
		System.out.println("<크롤링 완료>");
		countKeyWord();
	}
	
	static void multiThreading() {
		for(int i=0; i<5; i++) Threading(i);		
	}
	
	static void Threading(int idx) {
		Task t = new Task(idx);
		t.start();
		synchronized(t) {
			try {
				t.wait();
			} catch(Exception e) {
				e.printStackTrace();
			}
		}
	}
	
	// 아래 collectLyrics 메소드는 곡의 ID를 기준으로 해당 곡의 상세페이지에서 곡의 가사를 크롤링합니다.	
	public static void collectLyrics(int idx) throws IOException {
		
		// 아래 과정은 0 ~ 39번의 songId를 가지고 각 곡의 가사를 가져오는 과정입니다.
		for(int i=idx*8; i<(idx+1)*8; i++) {			
			String URL = lyricsUrl+songId[i];
			Document doc = Jsoup.connect(URL).get();
			Element pLyrics = doc.getElementById("pLyrics");
			String lyric = pLyrics.toString().split("p>")[1];
			lyric = lyric.substring(0, lyric.length()-2);
			lyrics.add(lyric);
		}
	}
	
	static synchronized void countKeyWord() {
		System.out.println("<'"+keyWord+"'단어 갯수>");
		int sum=0;
		for(int i=0; i<40; i++) {
			String lyric = lyrics.get(i);
			String[] word = lyric.split(" ");
			for(int j=0; j<word.length; j++) {
				if(word[j].contains(keyWord)) numOfKeyWord[i]++; 
			}
			sum += numOfKeyWord[i];
			String out = lyricsUrl+songId[i] + " : " + numOfKeyWord[i]+"개";
			System.out.println(out);
		}
		System.out.println("총 개수 : "+sum);
	}
}

class Task extends Thread {
	public int index;
	public ArrayList<String> lyrics;
	public Task(int index) {
		this.index = index; this.lyrics = new ArrayList<String>();
	}
	@Override
	public void run() {
		// TODO Auto-generated method stub
		Crawling c = new Crawling();
		try {
			c.collectLyrics(index);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		this.lyrics = c.lyrics;
	}	
}
