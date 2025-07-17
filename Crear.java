/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class Crear {

    public static void main(String[] args) {
        // Ruta donde se creará el archivo
        String ruta = "nuevo.txt";
        Scanner sc = new Scanner(System.in);

        // Crear el objeto File usando la sintaxis solicitada
        File archivo = new File(ruta);

        try {
            if (archivo.createNewFile()) {
                System.out.println("Archivo creado exitosamente: " + archivo.getAbsolutePath());
            } else {
                System.out.println("El archivo ya existe en: " + archivo.getAbsolutePath());
            }

            // Abrir el archivo para escritura (modo agregar)
            FileWriter writer = new FileWriter(archivo, true);

            System.out.println("Ingrese texto para guardar en el archivo. Escriba '0' para salir:");

            while (true) {
                String entrada = sc.nextLine();
                if (entrada.equals("0")) {
                    break; // Finaliza el bucle si se escribe 0
                }
                writer.write(entrada + "\n");
            }

            writer.close();
            System.out.println("Datos guardados correctamente en el archivo.");

        } catch (IOException e) {
            System.out.println("No se pudo crear o escribir el archivo. Verifica la ruta o los permisos.");
        } finally {
            sc.close();
        }
    }
}
