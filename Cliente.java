import java.io.IOException;
import java.net.Socket;
import java.net.UnknownHostException;
import java.io.PrintWriter;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Cliente {
	
	private static final String SERVER_ADDRESS = "localhost";
	private static final int SERVER_PORT = 5007;
	private Socket soc;
	PrintWriter sendServer;
	BufferedReader readServer;
	public Cliente(){
		soc = null;
		sendServer = null;
		readServer = null;
	}
	
	public void connect() throws IOException{
		//make connection
		soc = new Socket(SERVER_ADDRESS, SERVER_PORT);
		
		//start data I/O
		sendServer = new PrintWriter(soc.getOutputStream(),true);
		readServer = new BufferedReader(new InputStreamReader(soc.getInputStream()));
	}
	
	public void send(String str){
		sendServer.println(str);
	}
	
	public String receive() throws IOException{
		return readServer.readLine();
	}
	
	public void close() throws IOException{
		sendServer.close();
		readServer.close();
		soc.close();
	}
	
	public static void main(String[] args) throws IOException {
		Cliente c = new Cliente();
		c.connect();
		boolean loop = false;
		while(!loop){
			System.out.print("Enviar> ");
			InputStreamReader isr = new InputStreamReader(System.in);
			BufferedReader br = new BufferedReader (isr);
			String msg = br.readLine();
			c.send(msg);
			loop = msg.equals("quit()") ? true : false;
			if(loop){
				System.out.println("Conexion Terminada()");
				c.close();
			}
			else{
				System.out.println(c.receive());
			}
		}
	}
}