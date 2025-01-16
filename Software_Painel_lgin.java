import javafx.application.Application;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.control.Button;
import javafx.scene.layout.VBox;
import javafx.geometry.Pos;
import javafx.event.EventHandler;
import javafx.event.ActionEvent;
    public class Main extends Application {
        @Override
        public void start(Stage primaryStage) {
            Label lblusuario= new Label("usuário: ");
            TextField txtusuario = new TextField();
            Label lblsenha = new Label("senha: ");
            TextField txtsenha = new TextField();
            Button btnentra = new Button("Entrar");
            btnentra.setOnAction(new EventHandler<ActionEvent>() {
                @Override
                public void handle(ActionEvent event) {
                }
            });
            VBox root = new VBox(10, lblusuario, txtusuario, lblsenha, txtsenha, btnentra);
            root.setAlignment(Pos.CENTER);
            Scene scene = new Scene(root, 300, 250);
            primaryStage.setTitle("painel de login");
            primaryStage.setScene(scene);
            primaryStage.show();
        }
        public static void main(String[] args) {
            launch(args);
        }
    }
