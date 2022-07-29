import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import br.com.empresa.pessoa.*;

// public static void limparTela() {
//     try {
//         new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
//     } catch (Exception e) {
//         System.out.println(e.getMessage());
//     }
// }



public class Teste {
    public static void main(String[] args) throws Exception {
        criarArquivoSerializado();
        lerArquivoSerializado();
    }
    
    private static void criarArquivoSerializado() {
        Pessoa p1 = new Pessoa(1, "Fulano", 4000);
        FileOutputStream fos = null;
        ObjectOutputStream oos = null;
        try {
            fos = new FileOutputStream("arquivo.bin");
            oos = new ObjectOutputStream(fos);
            oos.writeObject(p1);
        } catch (FileNotFoundException e) {
            System.out.println("Arquivo não encontrado.");
        } catch (IOException e) {
            System.out.println("Erro ao criar aquivo.");
        } finally {
            if (oos != null) {
                try {
                    oos.close();
                } catch (IOException e) {
                    System.out.println("Erro ao fechar o arquivo");
                }
            }
        }
    } 
    
    private static void lerArquivoSerializado() {
        Pessoa p1 = null;
        FileInputStream fis = null;
        ObjectInputStream ois = null;
        try {
            fis = new FileInputStream("arquivo.bin");
            ois = new ObjectInputStream(fis);
            p1 = (Pessoa)ois.readObject();
            System.out.printf("Id: %2d\nNome: %s\nSalário: %.2f", p1.getIdPessoa(), p1.getNome(), p1.getSalario());
        } catch (ClassNotFoundException e) {
            System.out.println("Classe não encontrado.");
        } catch (IOException e) {
            System.out.println("Erro ao criar aquivo.");
        } finally {
            if (ois != null) {
                try {
                    ois.close();
                } catch (IOException e) {
                    System.out.println("Erro ao fechar o arquivo");
                }
            }
        }
    }
}

