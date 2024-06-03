
import javax.swing.*;
import java.awt.*;
import java.security.*;
import java.awt.event.*;

public class AcquisizioneDati {
    public void visualizzaDatiDiAccesso() {
        JFrame frame = new JFrame("Accesso");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JPanel panel = new JPanel();
        panel.setLayout(new GridBagLayout());

        GridBagConstraints gbc = new GridBagConstraints();
        gbc.insets = new Insets(5, 5, 5, 5);

        gbc.gridx = 0;
        gbc.gridy = 0;
        gbc.anchor = GridBagConstraints.LINE_END;
        panel.add(new JLabel("Nome utente:"), gbc);

        gbc.gridx = 1;
        gbc.gridy = 0;
        gbc.fill = GridBagConstraints.HORIZONTAL;
        gbc.weightx = 1.0;
        JTextField campoNomeUtente = new JTextField(20);
        panel.add(campoNomeUtente, gbc);

        gbc.gridx = 0;
        gbc.gridy = 1;
        gbc.anchor = GridBagConstraints.LINE_END;
        panel.add(new JLabel("Password:"), gbc);

        gbc.gridx = 1;
        gbc.gridy = 1;
        gbc.fill = GridBagConstraints.HORIZONTAL;
        gbc.weightx = 1.0;
        JPasswordField campoPassword = new JPasswordField(20);
        panel.add(campoPassword, gbc);

        gbc.gridx = 0;
        gbc.gridy = 2;
        gbc.gridwidth = 2;
        gbc.anchor = GridBagConstraints.LINE_END;
        JButton pulsanteAccesso = new JButton("Accesso");
        pulsanteAccesso.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                String nomeUtente = campoNomeUtente.getText();
                char[] password = campoPassword.getPassword();

                String hashPassword = hashPassword(password);

                JOptionPane.showMessageDialog(frame, "Nome utente: " + nomeUtente + "\nHash password: " + hashPassword);
            }
        });
        panel.add(pulsanteAccesso, gbc);

        frame.getContentPane().add(panel);

        frame.pack();
        frame.setVisible(true);
    }

    private String hashPassword(char[] password) {
        try {
            MessageDigest md = MessageDigest.getInstance("SHA-256");
            md.update(String.valueOf(password).getBytes());
            byte[] hash = md.digest();
            StringBuilder sb = new StringBuilder();
            for (byte b : hash) {
                sb.append(String.format("%02x", b));
            }
            return sb.toString();
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
            return null;
        }
    }
}
