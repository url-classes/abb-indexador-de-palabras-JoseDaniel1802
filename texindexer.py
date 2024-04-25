from binary_search_tree import BinarySearchTree


class TextIndexer:
    def __init__(self):
        self.index = BinarySearchTree()

    def index_text(self, text: str, line_number: int = 1):
        words = text.split()
        for word in words:
            word = word.strip(',.:;?!')  # Limpiar la palabra de signos de puntuación
            self.insert_word(word.lower(), line_number)
        return

    def search_word(self, word: str):
        result = self.index.search((word.lower(),))  # Convertir la palabra a minúsculas para la búsqueda
        return result

    def display_search_results(self, word, result):
        if result:
            locations = ", ".join([f"(línea {location[1]})" for location in result])
            print(f"Ubicaciones de '{word}' en el texto: {locations}")
        else:
            print(f"'{word}' no encontrado en el índice.")
    def insert_word(self, word: str, line_number: int):
        self.index.insert((word.lower(), line_number))  # Convertir la palabra a minúsculas

    def delete_word(self, word: str):
        self.index.delete((word.lower(),))  # Convertir la palabra a minúsculas

    def display_index(self):
        return self.index.preorder()

    def save_index_to_file(self, file_path: str):
        with open(file_path, 'w') as f:
            f.write(self.display_index())

    def navigate_tree(self, word: str):
        # Convertir la palabra a minúsculas
        word_lower = word.lower()
        current_node = self.index.root  # Acceder al root del árbol

        # Recorrer el árbol para determinar la dirección (izquierda o derecha)
        while current_node is not None:
            current_word = current_node.data[0]
            # Comparar la palabra actual con la palabra ingresada
            if word_lower < current_word:
                current_node = current_node.left
                print("Go left")
            elif word_lower > current_word:
                current_node = current_node.right
                print("Go right")
            else:
                print("Word found in the index!")
                return

        print("Word not found in the index!")


def display_menu():
    print("\n=== Menú del Indexador de Texto ===")
    print("1. Indexar Texto")
    print("2. Buscar Palabra")
    print("3. Insertar Palabra")
    print("4. Eliminar Palabra")
    print("5. Mostrar Índice")
    print("6. Salir")


def main():
    indexer = TextIndexer()

    while True:
        display_menu()
        choice = input("Ingrese su opción: ")

        if choice == "1":
            text = input("Ingrese el texto a indexar: ")
            indexer.index_text(text)
            print("¡Texto indexado exitosamente!")
        elif choice == "2":
            if indexer.display_index() is None:
                print("Debe indexar el texto primero.")
            else:
                word = input("Ingrese una palabra para buscar: ")
                result = indexer.search_word(word)
                if result:
                    print(f"Ubicaciones de '{word}' en el texto:", result)
                else:
                    print(f"'{word}' no encontrado en el índice.")
        elif choice == "3":
            word = input("Ingrese la palabra a insertar: ")
            line_number = int(input("Ingrese el número de línea para la palabra: "))
            indexer.insert_word(word, line_number)
            print("Palabra insertada en el índice.")
        elif choice == "4":
            word = input("Ingrese la palabra a eliminar: ")
            indexer.delete_word(word)
            print("Palabra eliminada del índice.")
        elif choice == "5":
            print("Índice:")
            print(indexer.display_index())
        elif choice == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")


if __name__ == "__main__":
    main()

