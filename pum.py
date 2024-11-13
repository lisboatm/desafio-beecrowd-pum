def main():
    N = int(input())
    num = 1
    
    for _ in range(N):
        # Imprime os três números seguidos por "PUM"
        print(f"{num} {num + 1} {num + 2} PUM")
        # Incrementa o número para a próxima linha
        num += 4

if __name__ == "__main__":
    main()
